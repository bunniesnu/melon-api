import json
from datetime import datetime, timezone
from pathlib import Path

from melon import MelonClient

OUTPUT_DIR = Path("data")


def save_json(data: dict, filename: str) -> Path:
    OUTPUT_DIR.mkdir(exist_ok=True)
    path = OUTPUT_DIR / filename
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    return path


def main():
    timestamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")

    with MelonClient() as client:
        print("=== Realtime Chart (Top 10) ===")
        realtime = client.get_realtime_chart(page_size=10)
        for song in realtime.songs:
            artist_names = ", ".join(a.name for a in song.artists)
            print(f"{song.current_rank}. {song.title} - {artist_names}")

        realtime_path = save_json(
            realtime.model_dump(mode="json", by_alias=True),
            f"realtime_chart_{timestamp}.json",
        )
        print(f"Saved to {realtime_path}")

        print()
        print("=== Top100 Chart (Top 10) ===")
        top100 = client.get_top100_chart()
        for song in top100.songs[:10]:
            artist_names = ", ".join(a.name for a in song.artists)
            trend = "UP" if song.is_rising else song.rank_type
            print(f"{song.current_rank}. {song.title} - {artist_names} [{trend}]")

        top100_path = save_json(
            top100.model_dump(mode="json", by_alias=True),
            f"top100_chart_{timestamp}.json",
        )
        print(f"Saved to {top100_path}")

        print()
        print("=== Chart Report for Current #1 (Realtime) ===")
        top_song_id = realtime.songs[0].song_id
        report = client.get_chart_report(song_id=top_song_id)
        print(f"Song: {report.song_info.title}")
        print(f"Current Rank: {report.song_info.current_rank}")
        print(f"Past Rank: {report.song_info.past_rank}")
        print(f"Listeners: {report.listener_chart.title.value}")

        report_path = save_json(
            report.model_dump(mode="json", by_alias=True),
            f"chart_report_{top_song_id}_{timestamp}.json",
        )
        print(f"Saved to {report_path}")


if __name__ == "__main__":
    main()

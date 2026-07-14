from melon.chart import MelonClient


def main():
    with MelonClient() as client:
        print("=== Hourly Chart (Top 10) ===")
        songs = client.get_hourly_chart(page_size=10)
        for song in songs:
            artist_names = ", ".join(a.name for a in song.artists)
            print(f"{song.current_rank}. {song.title} - {artist_names}")

        print()
        print("=== Chart Report for LOVE ATTACK (37928381) ===")
        report = client.get_chart_report(song_id="37928381")
        print(f"Song: {report.song_info.title}")
        print(f"Current Rank: {report.song_info.current_rank}")
        print(f"Past Rank: {report.song_info.past_rank}")


if __name__ == "__main__":
    main()

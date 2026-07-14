from melon.chart import MelonClient


def main():
    with MelonClient() as client:
        print("=== Hourly Chart (Top 10) ===")
        chart = client.get_hourly_chart(page_size=10)
        for song in chart.songs:
            artist_names = ", ".join(a.name for a in song.artists)
            print(f"{song.current_rank}. {song.title} - {artist_names}")

        print()
        print("=== Chart Report for Current #1 ===")
        top_song_id = chart.songs[0].song_id
        report = client.get_chart_report(song_id=top_song_id)
        print(f"Song: {report.song_info.title}")
        print(f"Current Rank: {report.song_info.current_rank}")
        print(f"Past Rank: {report.song_info.past_rank}")


if __name__ == "__main__":
    main()

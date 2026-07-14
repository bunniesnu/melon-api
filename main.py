from melon.chart import MelonClient


def main():
    with MelonClient() as client:
        print("=== Hourly Chart (Top 10) ===")
        chart_data = client.get_hourly_chart(page_size=10)
        songs = chart_data["response"]["CHARTLIST"]
        for song in songs:
            artist_names = ", ".join(a["ARTISTNAME"] for a in song["ARTISTLIST"])
            print(f"{song['CURRANK']}. {song['SONGNAME']} - {artist_names}")

        print()
        print("=== Chart Report for LOVE ATTACK (37928381) ===")
        report_data = client.get_chart_report(song_id="37928381")
        info = report_data["response"]["SONGINFO"]
        print(f"Song: {info['SONGNAME']}")
        print(f"Current Rank: {info['CURRANK']}")
        print(f"Past Rank: {info['PASTRANK']}")


if __name__ == "__main__":
    main()

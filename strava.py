from functions import get_dates, write_csv_header, write_csv_by_div

CLUBS = [
    ["Replicant Fitness", "https://www.strava.com/clubs/1159003"]
]


def main():
    last_monday, this_monday = get_dates()
    filename_this = f"Leaderboard_{this_monday}.csv"
    filename_last = f"Leaderboard_{last_monday}.csv"
    write_csv_header(filename_this)
    write_csv_header(filename_last)

    for club_name, club_url in CLUBS:
        write_csv_by_div(filename_last,
                         filename_this,
                         club_name,
                         club_url)


if __name__ == "__main__":
    main()

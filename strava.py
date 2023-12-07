import selenium

from functions import get_dates, write_csv_header, write_csv_by_div

CLUBS = [
    ["Beast Mode Crew 🐻", "https://www.strava.com/clubs/1160959"],
    ["Big Steppers", "https://www.strava.com/clubs/1160980"],
    ["Gadi’s Gains Gang", "https://www.strava.com/clubs/1160978"],
    ["Couch Potatoes", "https://www.strava.com/clubs/couchpotatoes"],
    ["Escalate to athlete", "https://www.strava.com/clubs/escalate-to-athlete"],
    ["Department of Fitness Machines", "https://www.strava.com/clubs/dofm"],
    ["The Brain is a Muscle, Right?", "https://www.strava.com/clubs/brainmuscles"],
    ["Gloss Floss, MATTE Finish", "https://www.strava.com/clubs/MATTEfinish"],
    ["Cirque Du Sore Legs", "https://www.strava.com/clubs/sore-legs"],
    ["Holy Walkamolies 🥑", "https://www.strava.com/clubs/Holy-Walkamolies"],
    ["Slow Down For <break time=\“100ms\“/>` what?", "https://www.strava.com/clubs/slowDownForWhat"],
    ["The Mighty Blade Runners ⚡", "https://www.strava.com/clubs/mightyblades"],
    ["Red Hot Chili Steppers", "https://www.strava.com/clubs/redhot-chili-steppers"],
]


def main():
    last_monday, this_monday = get_dates()
    filename_this = f"Leaderboard_{this_monday}.csv"
    filename_last = f"Leaderboard_{last_monday}.csv"
    write_csv_header(filename_this)
    write_csv_header(filename_last)

    for club_name, club_url in CLUBS:
        try:
            driver = write_csv_by_div(filename_last,
                                      filename_this,
                                      club_name,
                                      club_url)
        except selenium.common.exceptions.NoSuchElementException:
            print(f'Unable to fetch club {club_name} at {club_url}')

    driver.close()


if __name__ == "__main__":
    main()

# replifitness keyboard macro
# (fset 'replifitness
#    (kmacro-lambda-form [?\[ ?\" ?\C-s tab left ?\" ?, ?\C-  ?\C-s ?h backspace ?\C-w backspace ?h return left ?\C-w ?  ?\" ?\C-e ?\" ?\] ?, down ?\C-a] 0 "%d"))

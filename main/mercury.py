import gspread
from oauth2client.service_account import ServiceAccountCredentials

from main.important_files.ExcelTopics import Topics
from main.utils import av_of_list

sheet = None
teams_and_row_numbers = {}
values_from_sheet = []
teams_and_calculations = {}


def open_and_read_sheet():
    global sheet

    scope = ['https://www.googleapis.com/auth/spreadsheets', "https://www.googleapis.com/auth/drive.file",
             "https://www.googleapis.com/auth/drive"]

    creds = ServiceAccountCredentials.from_json_keyfile_name(r'important_files/client_secret.json', scope)

    client = gspread.authorize(creds)
    sheet = client.open("test spreadsheet").sheet1


def first_analyse():
    global teams_and_row_numbers
    global values_from_sheet

    values_from_sheet = sheet.get_all_records()
    counter = 0
    for i in values_from_sheet:
        teamNumber = i.get(Topics.Team_Number.value)
        # print(teamNumber)
        if teams_and_row_numbers.get(teamNumber) is None:
            teams_and_row_numbers[teamNumber] = [counter]
            # print(teams_and_row_numbers.get(teamNumber))
        else:
            teams_and_row_numbers.get(teamNumber).append(counter)
        counter += 1


def calculations():
    global teams_and_calculations

    topics = [i.value for i in Topics][3:]
    for team in teams_and_row_numbers.keys():
        teams_and_calculations[team] = {}
        for topic in topics:
            scores = []
            for game_number in teams_and_row_numbers.get(team):
                game = values_from_sheet[game_number]
                score = game.get(topic)
                if teams_and_calculations.get(team).get("average " + topic) is None:
                    teams_and_calculations.get(team)["average " + topic] = score
                    scores.append(score)
                else:
                    scores.append(score)
            teams_and_calculations.get(team)["average " + topic] = av_of_list(scores)
            print("team: " + str(team) + " topic: " + topic)
            print(scores)
            print(teams_and_calculations.get(team).get("average " + topic))


def main():
    open_and_read_sheet()
    first_analyse()
    calculations()
    print(teams_and_calculations)
    # print(values_from_sheet[0])


if __name__ == '__main__':
    main()

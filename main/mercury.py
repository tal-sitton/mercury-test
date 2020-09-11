import gspread
from oauth2client.service_account import ServiceAccountCredentials

from main.important_files.ExcelTopics import topics as excel_topics
from main.important_files.ExcelTopics import same_topic as same_excel_topics
from main.important_files.ExcelTopics import positive_word, negative_word
from main.utils import average_of_list

sheet = None
comment_default = "תכתבו משהו, plz"
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
    for i in values_from_sheet[0].keys():
        excel_topics[i] = i
    counter = 0
    for i in values_from_sheet:
        teamNumber = i.get(excel_topics["Team Number"])
        if teams_and_row_numbers.get(teamNumber) is None:
            teams_and_row_numbers[teamNumber] = [counter]
        else:
            teams_and_row_numbers.get(teamNumber).append(counter)
        counter += 1
    print(excel_topics)


def average_calculations():
    global teams_and_calculations

    topics = excel_topics
    topics.pop('Scouter Name', None)
    topics.pop('Team Number', None)
    topics.pop('Match Number (pr02/q01/p04)', None)
    print(topics.keys())
    for team in teams_and_row_numbers.keys():
        teams_and_calculations[team] = {}
        for topic in topics.keys():
            scores = []
            for game_number in teams_and_row_numbers.get(team):
                game = values_from_sheet[game_number]
                score = game.get(topic)
                scores.append(score)
            if topic == "Comments":
                if scores.count(comment_default) > 0:
                    scores.remove(comment_default)
                if scores.count('') > 0:
                    scores.remove('')
                teams_and_calculations.get(team)[topic] = scores
            else:
                teams_and_calculations.get(team)["average " + topic] = average_of_list(scores)
                teams_and_calculations.get(team)[topic + " scores"] = scores
            print("team: " + str(team) + " topic: " + topic)
            print(scores)


def percentage_calculation():
    global teams_and_calculations
    for team in teams_and_row_numbers.keys():
        for upper_topic in same_excel_topics.keys():
            count = 0
            success = 0
            top = ""
            for topic in same_excel_topics[upper_topic]:
                # print("team: {}; topic {}".format(team, topic))
                # print(teams_and_calculations[team][topic + " scores"])
                if positive_word in topic:
                    success += teams_and_calculations[team]["average " + topic]
                else:
                    top = topic
                count += teams_and_calculations[team]["average " + topic]
                teams_and_calculations[team].pop(topic + " scores", None)
            if count != 0:
                if team == 1574:
                    print(f"team {team} top {top} success {success} count {count} percentage {success / count}")
                teams_and_calculations[team][top.replace(" " + negative_word, "") + " percentage"] = success / count
            else:
                teams_and_calculations[team][top.replace(" " + negative_word, "") + " percentage"] = 0

        topics_to_delete = []
        for topic in teams_and_calculations[team].keys():
            if "scores" in topic:
                topics_to_delete.append(topic)

        for del_topic in topics_to_delete:
            teams_and_calculations[team].pop(del_topic, None)


def main():
    open_and_read_sheet()
    first_analyse()
    average_calculations()
    percentage_calculation()
    print(teams_and_calculations)
    print(teams_and_calculations[1574])
    # print(values_from_sheet[0])


if __name__ == '__main__':
    main()

# Write your solution here
import json

class NHL:
    def __init__(self) -> None:
        pass

    def options(self):
        print("\ncommands:")
        print("0 quit")
        print("1 search for player")
        print("2 teams")
        print("3 countries")
        print("4 players in team")
        print("5 players from country")
        print("6 most points")
        print("7 most goals\n")

    def print_details(self, player):
        name = player["name"]
        team = player["team"]
        goals = int(player["goals"])
        assists = int(player["assists"])
        print(f"{name:<21}{team:<5}{goals:>2} + {assists:>2} = {goals + assists:>3}")

    def team_abbreviations(self, player_list):
        unique_teams = []
        for player in player_list:
            team = player["team"]
            if team not in unique_teams:
                unique_teams.append(team)
        for team in sorted(unique_teams):
            print(team)
        print()

    def country_abbreviations(self, player_list):
        unique_countries = []
        for player in player_list:
            country = player["nationality"]
            if country not in unique_countries:
                unique_countries.append(country)
        for country in sorted(unique_countries):
            print(country)
        print()

    def team_by_points(self, player_list):
        team_players = []
        team = input("team: ")
        for player in player_list:
            if team == player["team"]:
                team_players.append(player)
        team_players.sort(key=self.sort_by_points, reverse=True)
        print()
        for player in team_players:
            self.print_details(player)
        print()

    def country_by_points(self, player_list):
        country_players = []
        country = input("country: ")
        for player in player_list:
            if country == player["nationality"]:
                country_players.append(player)
        country_players.sort(key=self.sort_by_points, reverse=True)
        print()
        for player in country_players:
            self.print_details(player)
        print()
    
    def most_points(self, player_list: list, amount):
        player_list.sort(key=self.sort_by_points, reverse=True)
        for i in range(0, amount):
            self.print_details(player_list[i])
        print()

    def most_goals(self, player_list: list, amount):
        player_list.sort(key=self.sort_by_goals, reverse=True)
        for i in range(0, amount):
            self.print_details(player_list[i])
        print()

    def sort_by_points(self, player):
        return player["goals"] + player["assists"]

    def sort_by_goals(self, player):
        return [player["goals"], player["games"] * -1]
    
    def start(self):
        filename = input("file name: ")
        with open("src/" + filename) as file:
            data = file.read()
        player_list = json.loads(data)
        print(f"read the data of {len(player_list)} players")
        self.options()
        while True:
            command_no = int(input("command: "))
            if command_no == 0:
                break
            elif command_no == 1:
                player_name = input("name: ")
                for player in player_list:
                    if player["name"] == player_name:
                        self.print_details(player)
                print()
            elif command_no == 2:
                self.team_abbreviations(player_list)
            elif command_no == 3:
                self.country_abbreviations(player_list)
            elif command_no == 4:
                self.team_by_points(player_list)
            elif command_no == 5:
                self.country_by_points(player_list)
            elif command_no == 6:
                amount = int(input("how many: "))
                self.most_points(player_list, amount)
            elif command_no == 7:
                amount = int(input("how many: "))
                self.most_goals(player_list, amount)

#if __name__ == "__main__":
nhl_stats = NHL()
nhl_stats.start()
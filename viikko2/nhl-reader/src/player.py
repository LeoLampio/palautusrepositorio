import requests

class Player:
    def __init__(self, dict):
        self.name = dict['name']
        self.team = dict['team']
        self.goals = dict["goals"]
        self.assists = dict["assists"]
        self.nat = dict["nationality"]
    
    def __str__(self):
        return f"{self.name:25}{self.team:15}{self.goals:<2} + {self.assists:<2} = {self.goals + self.assists}"

class PlayerReader:
    def __init__(self, url):
        response = requests.get(url).json()

        self.players = []

        for player_dict in response:
            player = Player(player_dict)
            self.players.append(player)

class PlayerStats:
    def __init__(self, reader : PlayerReader):
        self.reader = reader

    def top_scorers_by_nationality(self, nat):
        players_of_nat = [p for p in self.reader.players if p.nat == nat]
        return sorted(players_of_nat, key=lambda p: -(p.goals + p.assists))
class Player:
    def __init__(self, dict):
        self.name = dict['name']
        self.nationality = dict['nationality']
        self.assists = dict['assists']
        self.goals = dict['goals']
        self.team = dict['team']
        self.games = dict['games']
        self.id = dict['id']
    
    def __str__(self):
        return f"{self.name.ljust(25)} {str(self.team).ljust(25)} {str(self.goals).ljust(2)} + {str(self.assists).ljust(2)} = {self.goals + self.assists}"

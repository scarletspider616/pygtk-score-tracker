from abc import abstractproperty

class Score:
    _home_team = None
    _away_team = None
    _home_score = None
    _away_score = None
    def __init__(self, home_team, away_team, home_score, away_score):
        self._home_team = home_team
        self._away_team = away_team
        self._home_score = home_score
        self._away_score = away_score
    
    @property
    def home_team(self):
        return self._home_team
    
    @property
    def away_team(self):
        return self._away_team
    
    @property
    def home_score(self):
        return self._home_score

    @property
    def away_score(self):
        return self._away_score

    @property
    def winning(self):
        if self._home_score > self._away_score:
            return self._home_team
        elif self._away_score > self._home_score:
            return self._away_team
        else:
            return None

    @abstractproperty
    def time_left(self):
        # override me!
        pass
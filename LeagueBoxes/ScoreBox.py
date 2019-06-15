import Gtk

class ScoreBox(Gtk.Box):
    _score = None
    def __init__(self, score):
        self._score = score
        self._pack_box()

    def _pack_box(self):
        header = Gtk.Label(self._score.home_team + " - " + self._score.away_team)
        self.push_back(header, expand=True, fill=True, padding=10)
        scoreline = Gtk.Label(str(self._score.home_score) + " - " + str(self._score.away_score))
        self.push_back(scoreline, expand=True, fill=True, padding=10)
        
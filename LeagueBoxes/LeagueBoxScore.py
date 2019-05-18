'''
Class for each individual league box to inherit from
'''

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

# pathing
import sys
import os

sys.path.append(os.getcwd() + "/assets/")
import StringDefs


class LeagueBoxScore(Gtk.Box):
    _league_label = StringDefs.GENERIC_LEAGUE_LABEL
    def __init__(self):
        Gtk.Box.__init__(self)

    @property
    def league_label(self):
        return self._league_label
    
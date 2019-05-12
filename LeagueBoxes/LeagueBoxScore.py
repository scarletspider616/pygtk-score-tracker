'''
Class for each individual league box to inherit from
'''

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

# TODO move labels into their own file
LEAGUE_LABEL = "LEAGUE LABEL"

class LeagueBoxScore(Gtk.Box):
    def __init__(self):
        Gtk.Box.__init__(self)
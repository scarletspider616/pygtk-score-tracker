import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

# TODO move labels into their own file
WELCOME_LABEL = "Welcome Page"

class WelcomeBox(Gtk.Box):
    def __init__(self):
        Gtk.Box.__init__(self)
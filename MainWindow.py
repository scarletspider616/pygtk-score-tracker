import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

# project 
from WelcomeBox import WelcomeBox
from LeagueBoxes.LeagueBoxScore import *

class MainWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Main Window Wrapper")
        self.set_border_width(3)

        self.notebook = Gtk.Notebook()
        self.add(self.notebook)

        self.welcome_page = WelcomeBox()
        self.notebook.append_page(self.welcome_page, Gtk.Label('Welcome Page'))


win = MainWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
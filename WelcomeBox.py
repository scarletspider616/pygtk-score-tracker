import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class WelcomeBox(Gtk.Box):
    def __init__(self, spacing=10):
        Gtk.Box.__init__(self, spacing)
        self.set_homogeneous(False)
    
        
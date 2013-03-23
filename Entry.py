#!/usr/bin/env python
# Python 3
from tkinter import ttk

class ConstrainedEntry(ttk.Entry):
    def __init__(self, *args, **kwargs):
        ttk.Entry.__init__(self, *args, **kwargs)

        vcmd = (self.register(self.on_validate),"%P")
        self.configure(validate="key", validatecommand=vcmd)

    def disallow(self):
        self.bell()

    def on_validate(self, new_value):
        try:
            if new_value.strip() == "": return True
            value = int(new_value)
            if value < 0 or value > 9999:
                self.disallow()
                return False
        except ValueError:
            self.disallow()
            return False

        return True

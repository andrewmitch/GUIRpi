#!/usr/bin/env python
# Python 3

# Class used to validate code being entered into entry widget, to ensure the value entered is a four digit interger, will not allow any other data type.
from tkinter import ttk
import re

class ConstrainedEntry(ttk.Entry):
    def __init__(self, *args, **kwargs):
        ttk.Entry.__init__(self, *args, **kwargs)

        vcmd = (self.register(self.on_validate),"%P")
        self.configure(validate="key", validatecommand=vcmd)

    def disallow(self):
        self.bell()

    def on_validate(self, new_value):
        value = re.match(r'^(\d{1,4})?$', new_value)
        if value is None:
            self.disallow()
            return False
        else:
            return True

import sys

try:
    import wx
    import wx.lib.inspection
except ModuleNotFoundError:
    print("ERROR: App cannot proceed, because wx is missing!")
    sys.exit(1)

from .l1 import Action
from . import m1
from . import m2

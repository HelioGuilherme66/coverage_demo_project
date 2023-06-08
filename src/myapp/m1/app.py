#!/bin/env python
import sys
import wx

class Application(wx.App):

    def __init__(self, path=None, updatecheck=True, *args):
        self._updatecheck = updatecheck
        self.workspace_path = path
        self.args = args
        wx.App.__init__(self, redirect=False)

    def OnInit(self):
        style = wx.OK|wx.ICON_INFORMATION
        parent = wx.Frame(None, size=(100, 200))
        dlg = wx.MessageDialog(parent, message=f"This is App\nArgs: {self.args}\n", caption="Test App", style=style)
        dlg.ShowModal()
        return True


def main(*args):
    if args and args[0] == 'error':
    	sys.exit(1)
    
    app = Application(None, False, args)


if __name__ == '__main__':
    main(*sys.argv[1:])


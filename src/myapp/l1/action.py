#!/bin/env python
import wx

def Action(data):
    info = f"Data:{data}"
    result = { 'version': wx.VERSION, 'info': info }
    return result


#!/bin/env python

import sys
import wx


def app(*args):
    print(f"This is Main using wx version= {wx.VERSION}\n")


if __name__ == '__main__':
    app(*sys.argv[1:])

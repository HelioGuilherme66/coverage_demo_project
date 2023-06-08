import unittest
import pytest 
from pytest import MonkeyPatch


def test_version():
    from myapp.m2 import VERSION
    assert VERSION == '2.0'

def test_app(capsys):
    import wx
    from wx import VERSION
    from myapp.m2 import main
    main.app()
    out, err = capsys.readouterr()
    assert out.startswith(f"This is Main using wx version= {VERSION}\n")


def test_main_call(capsys):
    def my_main():
        print("Called my_main")

    with MonkeyPatch().context() as m:
        from myapp.m2 import main
        m.setattr(main, 'app', my_main)
        m.setattr(main, '__name__', '__main__')
        assert main.__name__ == '__main__'
        main.app()
        out, err = capsys.readouterr()
        assert out.startswith("Called my_main")


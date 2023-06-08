import unittest
import pytest
from pytest import MonkeyPatch
import builtins

real_import = builtins.__import__


def myimport(name, globals, locals, fromlist, level):
    # DEBUG print(f"DEBUG: called myimport! name={name}")
    if name == 'wx.lib.inspection':
        raise ModuleNotFoundError  # real_import('wx_error', globals, locals, fromlist, level)
        # raise ImportError
    return real_import(name, globals, locals, fromlist, level)


class TestModule(unittest.TestCase):

    def tearDown(self):
        builtins.__import__ = real_import

    def test_missing_wx(self):
        with MonkeyPatch().context() as m:
            with pytest.raises((ModuleNotFoundError, SystemExit)):
                builtins.__import__ = myimport
                import myapp
                
                print(myapp.m1.VERSION)
                print(dir(myapp.m1))


class TestMain(unittest.TestCase):

    def tearDown(self):
        builtins.__import__ = real_import

    def test_main_call_with_error(self):
        with pytest.raises(SystemExit):
            import myapp
            myapp.m1.main('error')

    def test_version(self):
        from myapp.m1 import VERSION
        assert VERSION == '1.0'

    def test_app(self):
        from myapp.m1 import main as app
        app


def test_main_call():
    def my_show(*args):
        print("Called my_main")

    with MonkeyPatch().context() as m:
        import myapp
        from wx import MessageDialog
        m.setattr(MessageDialog, 'ShowModal', my_show)
        myapp.m1.main('all OK')


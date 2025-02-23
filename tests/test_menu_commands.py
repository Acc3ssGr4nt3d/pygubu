# encoding: utf8
import support
import pygubu
import os
import sys
import unittest
try:
    import tkinter as tk
    import tkinter.ttk as ttk
except:
    import Tkinter as tk
    import ttk


pygubu_basedir = os.path.abspath(os.path.dirname(
    os.path.dirname(os.path.realpath(sys.argv[0]))))
if pygubu_basedir not in sys.path:
    sys.path.insert(0, pygubu_basedir)


class TestMenu(unittest.TestCase):

    def setUp(self):
        self.root = support.get_tk_root()
        support.root_deiconify()
        xmldata = 'test_menu_commands.ui'
        self.builder = builder = pygubu.Builder()
        filepath = os.path.dirname(os.path.realpath(__file__))
        builder.add_resource_path(filepath)
        builder.add_from_file(xmldata)
        self.widget = builder.get_object('mainmenu')
        self.menu1 = builder.get_object('menu1')
        self.root['menu'] = self.widget

    def tearDown(self):
        support.root_withdraw()
        self.root['menu'] = None

    def test_tearoff_command(self):
        success = []

        class AnObject:
            def on_menu_tearoff(self, menu, tearoff):
                success.append(1)

            def on_menu_post(self):
                pass

            def button1_cb(self):
                pass

            def chkbutton_cb(self, widget_id):
                pass

        cbobj = AnObject()
        self.builder.connect_callbacks(cbobj)
        # Simulate user clicking on tearoff menu
        self.menu1.invoke(0)
        self.widget.update()
        # validate test
        self.assertTrue(success)
        self.widget.destroy()

    def test_post_command(self):
        success = []

        class AnObject:
            def on_menu_tearoff(self, menu, tearoff):
                pass

            def on_menu_post(self):
                success.append(1)

            def button1_cb(self):
                pass

            def chkbutton_cb(self, widget_id):
                pass

        cbobj = AnObject()
        self.builder.connect_callbacks(cbobj)
        # Simulate user clicking on menu
        self.menu1.post(0, 0)
        self.widget.update()
        # validate test
        self.assertTrue(success)
        self.widget.destroy()

    def test_button_command(self):
        success = []

        class AnObject:
            def on_menu_tearoff(self, menu, tearoff):
                pass

            def on_menu_post(self):
                pass

            def button1_cb(self):
                success.append(1)

            def chkbutton_cb(self, widget_id):
                pass

        cbobj = AnObject()
        self.builder.connect_callbacks(cbobj)
        # Simulate user clicking on menu item
        self.menu1.invoke(1)
        self.widget.update()
        # validate test
        self.assertTrue(success)
        self.widget.destroy()

    def test_button_command_with_widget_id(self):
        success = []

        class AnObject:
            def on_menu_tearoff(self, menu, tearoff):
                pass

            def on_menu_post(self):
                pass

            def button1_cb(self):
                pass

            def chkbutton_cb(self, widget_id):
                success.append(widget_id)

        cbobj = AnObject()
        self.builder.connect_callbacks(cbobj)
        # Simulate user clicking on menu item
        self.menu1.invoke(2)
        self.widget.update()
        # validate test
        self.assertTrue(success)
        wid = success[0]
        self.assertEqual(wid, 'mchb1')
        self.widget.destroy()

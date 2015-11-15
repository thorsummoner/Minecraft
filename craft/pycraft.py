"""
    Main pyCraft entry point.
"""
import pyglet

import craft
import craft.window


def main():
    """
        Main Entry Point
    """
    try:
        window = craft.window.Window(width=800, height=600, caption=craft.NAME, resizable=True)
        # Hide the mouse cursor and prevent the mouse from leaving the window.
        window.set_exclusive_mouse(True)
        craft.window.setup()
        pyglet.app.run()

    except KeyboardInterrupt:
        print 'User Exit'

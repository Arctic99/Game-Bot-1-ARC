"""
This file contains the game control logic.

Author: Arda Mavi
"""
import pyautogui

from pynput.mouse import Controller as Mouse
from pynput.keyboard import Key


# For encoding keyboard keys:
def get_keys():
    """
    Returns a list of all the keys that can be pressed.
    :return: The list of keys.
    """
    return ["w", "a", "s", "d", "r", "f", "g", "c", "Key.space", "Key.shift"]


def get_key(key_id):
    """
    Returns the key that corresponds to the given key id.
    :param key_id: Set the key id.
    :return: the key that corresponds to the given key id.
    """
    return get_keys()[key_id]


def get_id(key):
    """
    Returns the id of the given key.
    :param key: The key.
    :return: The id of the given key.
    """
    try:
        print("Key Pressed:", key.char, sep="")
        return get_keys().index(key.char)
    except:
        if (str(key) + "") not in get_keys():
            print((str(key) + ""), " is not in list")
            return 1000
    print("Key Pressed:", (str(key) + ""), sep="")
    return get_keys().index((str(key) + ""))


mouse = Mouse()


# Mouse:
def move(x, y):
    """
    Moves the mouse to the given coordinates.
    :param x: x coordinate.
    :param y: y coordinate.
    :return: None
    """
    pyautogui.moveTo(x, y)


def scroll(x, y):
    """
    Scrolls the mouse to the given coordinates.
    :param x: The horizontal scroll.
    :param y: The vertical scroll.
    :TODO: Change the scroll function to scroll with pyautogui.
    """
    mouse.scroll(x, y)


def click(x, y):
    """
    Clicks the mouse at the given coordinates.
    :param x: The x coordinate.
    :param y: The y coordinate.
    """
    move(x, y)
    pyautogui.click()


# Keyboard:
def press(key):
    """
    Presses the given key.
    :param key: The key.
    """
    if key in ["Key.shift", "shift"]:
        pyautogui.keyDown("shift")
    elif key in ["Key.space", "space"]:
        pyautogui.keyDown("space")
    else:
        pyautogui.keyDown(key)


def release(key):
    """
    Releases the given key.
    :param key: the key.
    """
    if key in ["Key.shift", "shift"]:
        pyautogui.keyUp(Key.shift)
    elif key in ["Key.space", "space"]:
        pyautogui.keyUp(Key.space)
    else:
        pyautogui.keyUp(key)

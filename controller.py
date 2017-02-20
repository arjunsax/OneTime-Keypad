''' import module here '''

import pythoncom, pyHook
from pykeyboard import PyKeyboard

import setting
import auto_complete

app = auto_complete.LIST_GUI()

# global pad
# pad = GUI.APP_GUI(tkinter.Tk())

''' functions '''


def monitor():
    '''
    Input: None
    Functionality: Monitor the signal from keypad. Hold the signal once received.
    Return: input event
    '''
    print(setting.PAGES)
    # create a hook manager
    hm = pyHook.HookManager()
    # call interpret when keydown
    hm.KeyDown = KeyDownEvent
    hm.KeyUp = KeyUpEvent
    # set the hook
    hm.HookKeyboard()
    # wait forever
    pythoncom.PumpMessages()


def caps(msg):
    if setting.CAPS is 1 and msg.isalpha():
        return msg.upper()
    elif msg.isalpha():
        return msg.lower()


def KeyDownEvent(event):
    '''
    Input: the keyboard event received by monitor.
    Functionality:interpret the signal, simulate key press of the signal.
    Return: the mapping symbol to both frontground app and GUI
    '''
    # create a keyboard object
    k = PyKeyboard()
    msg = str(event.Key)

    if event.Key in setting.keys_poss or \
        event.Key in setting.keys_poss2:
        msg = setting.PAGES[setting.SWITCH][event.Key]
        if msg is 'Switch':
            setting.SWITCH = (setting.SWITCH + 1) % len(setting.PAGES)
        elif msg is 'CapsLock':
            setting.CAPS = (setting.CAPS + 1) % 2
        elif msg is 'Tab':
            k.type_string('\t')
        else:
            msg = caps(msg)
            k.type_string(msg)
        app.auto_complete(msg)
        del k
        return False
    elif event.Key == "Space" or \
                    event.Key == "Return" or event.Key == "Back":
        app.auto_complete(msg)
        del k
        return True
    else:
        del k
        return True


def KeyUpEvent(event):
    '''
    Input: the keyboard event received by monitor.

    Functionality:interpret the signal, simulate key release of the signal.

    Return: the mapping symbol to both frontground app and GUI
    '''
    k = PyKeyboard()
    if event.Key in setting.keys_poss or event.Key in setting.keys_poss2:
        msg = setting.PAGES[setting.SWITCH][event.Key]
        # if msg is not 'switch_map' and not 'switch_cap' and not 'tab':
        #	k.release_key(msg)
        del k
        return False
    del k
    return True

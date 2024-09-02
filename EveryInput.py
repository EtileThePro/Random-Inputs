# EVERYTHING IS AUTOMATICALLY SET TO 0% CHANCE AND 0.1 DURATION
# AND KEYBOARD AND MOUSE FUNCTIONS ARE SET TO FALSE CHANGE FALSE TO TRUE TO ENABLE THEM
# MAKE SURE TO READ THE DOWNLOAD REQUIREMENTS
import pyautogui
import keyboard
import time
import random
import threading

all_keys = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
    '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
    'up', 'down', 'left', 'right', 'enter', 'space', 'backspace',
    'tab', 'escape', 'shift', 'ctrl', 'alt', 'capslock', 'numlock',
    'scrolllock', 'pause', 'insert', 'delete', 'home', 'end', 'pageup',
    'pagedown', 'printscreen', 'f1', 'f2', 'f3', 'f4', 'f5', 'f6', 'f7',
    'f8', 'f9', 'f10', 'f11', 'f12'
]

mouse_buttons = ['left', 'right', 'middle']

chance_to_press = 200
press_duration = 1

mouse_actions_enabled = False

def random_key_press():
    if random.randint(1, 1) <= chance_to_press:
        key = random.choice(all_keys)
        print(f"Pressing key: {key}")
        pyautogui.keyDown(key)
        time.sleep(press_duration)
        pyautogui.keyUp(key)

def random_mouse_action():
    global mouse_actions_enabled
    if mouse_actions_enabled and random.randint(1, 1) <= chance_to_press:
        action = random.choice(['move', 'click'])
        if action == 'move':
            x = random.randint(0, pyautogui.size().width)
            y = random.randint(0, pyautogui.size().height)
            print(f"Moving mouse to: ({x}, {y})")
            pyautogui.moveTo(x, y, duration=0.005)
        elif action == 'click':
            button = random.choice(mouse_buttons)
            print(f"Clicking mouse button: {button}")
            pyautogui.click(button=button)

def listen_for_stop(stop_event, hotkey='esc'):
    print(f"Press '{hotkey}' to stop the key and mouse actions.")
    keyboard.wait(hotkey)
    stop_event.set()

def toggle_mouse_actions():
    global mouse_actions_enabled
    while True:
        keyboard.wait('m')
        mouse_actions_enabled = not mouse_actions_enabled
        status = "enabled" if mouse_actions_enabled else "disabled"
        print(f"Mouse actions {status}.")

def main():
    stop_event = threading.Event()
    stop_thread = threading.Thread(target=listen_for_stop, args=(stop_event,))
    toggle_thread = threading.Thread(target=toggle_mouse_actions)

    stop_thread.start()
    toggle_thread.start()

    print("Starting random key and mouse actions. Press the stop hotkey to terminate.")
    print("Press 'm' to toggle mouse actions on or off.")
    try:
        while not stop_event.is_set():
            random_key_press()
            random_mouse_action()
    except KeyboardInterrupt:
        pass
    print("Key and mouse actions stopped.")

if __name__ == "__main__":
    main()
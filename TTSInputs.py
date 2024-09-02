# EVERYTHING IS AUTOMATICALLY SET TO 0% CHANCE AND 0.1 DURATION
# AND KEYBOARD AND MOUSE FUNCTIONS ARE SET TO FALSE CHANGE FALSE TO TRUE TO ENABLE THEM
# MAKE SURE TO READ THE DOWNLOAD REQUIREMENTS
import pyautogui
import keyboard
import time
import random
import threading
from tts_helper import play_tts

key_chances = {
    'up': {'chance': 0, 'duration': 0.1},
    'down': {'chance': 0, 'duration': 0.1},
    'left': {'chance': 0, 'duration': 0.1},
    'right': {'chance': 0, 'duration': 0.1},
    'a': {'chance': 0, 'duration': 0.1},
    'b': {'chance': 0, 'duration': 0.1},
    'c': {'chance': 0, 'duration': 0.1},
    'd': {'chance': 0, 'duration': 0.1},
    'e': {'chance': 0, 'duration': 0.1},
    'f': {'chance': 0, 'duration': 0.1},
    'g': {'chance': 0, 'duration': 0.1},
    'h': {'chance': 0, 'duration': 0.1},
    'i': {'chance': 0, 'duration': 0.1},
    'j': {'chance': 0, 'duration': 0.1},
    'k': {'chance': 0, 'duration': 0.1},
    'l': {'chance': 0, 'duration': 0.1},
    'm': {'chance': 0, 'duration': 0.1},
    'n': {'chance': 0, 'duration': 0.1},
    'o': {'chance': 0, 'duration': 0.1},
    'p': {'chance': 0, 'duration': 0.1},
    'q': {'chance': 0, 'duration': 0.1},
    'r': {'chance': 0, 'duration': 0.1},
    's': {'chance': 0, 'duration': 0.1},
    't': {'chance': 0, 'duration': 0.1},
    'u': {'chance': 0, 'duration': 0.1},
    'v': {'chance': 0, 'duration': 0.1},
    'w': {'chance': 0, 'duration': 0.1},
    'x': {'chance': 0, 'duration': 0.1},
    'y': {'chance': 0, 'duration': 0.1},
    'z': {'chance': 0, 'duration': 0.1},
    'enter': {'chance': 0, 'duration': 0.1},
    'backspace': {'chance': 0, 'duration': 0.1},
    'space': {'chance': 0, 'duration': 0.1},
}

mouse_chances = {
    'left': {'chance': 0, 'duration': 0.1},
    'right': {'chance': 0, 'duration': 0.1},
    'middle': {'chance': 0, 'duration': 0.1},
}

enable_mouse_actions = False
enable_keyboard_actions = False
def get_random_key():
    total_chance = sum(value['chance'] for value in key_chances.values())
    rand_val = random.randint(1, total_chance)
    cumulative_chance = 0
    for key, data in key_chances.items():
        cumulative_chance += data['chance']
        if rand_val <= cumulative_chance:
            return key, data['duration']

def get_random_mouse_action():
    total_chance = sum(value['chance'] for value in mouse_chances.values())
    rand_val = random.randint(1, total_chance)
    cumulative_chance = 0
    for button, data in mouse_chances.items():
        cumulative_chance += data['chance']
        if rand_val <= cumulative_chance:
            return button, data['duration']

def perform_mouse_action(action, duration):
    play_tts(f"Performing {action} mouse click")
    if action == 'left':
        pyautogui.mouseDown(button='left')
        time.sleep(duration)
        pyautogui.mouseUp(button='left')
    elif action == 'right':
        pyautogui.mouseDown(button='right')
        time.sleep(duration)
        pyautogui.mouseUp(button='right')
    elif action == 'middle':
        pyautogui.mouseDown(button='middle')
        time.sleep(duration)
        pyautogui.mouseUp(button='middle')

def move_mouse():
    screen_width, screen_height = pyautogui.size()
    x, y = random.randint(0, screen_width), random.randint(0, screen_height)
    play_tts(f"Moving mouse to position {x}, {y}")
    pyautogui.moveTo(x, y, duration=0.5)

def listen_for_stop(stop_event, hotkey='esc'):
    print(f"Press '{hotkey}' to stop the key spamming.")
    keyboard.wait(hotkey)
    stop_event.set()

def main():
    stop_event = threading.Event()
    stop_thread = threading.Thread(target=listen_for_stop, args=(stop_event,))
    stop_thread.start()

    print("Starting key and mouse spamming. Press the stop hotkey to terminate.")
    try:
        while not stop_event.is_set():
            if enable_mouse_actions:
                mouse_action, mouse_duration = get_random_mouse_action()
                perform_mouse_action(mouse_action, mouse_duration)
                time.sleep(0.1)
                move_mouse()

            if enable_keyboard_actions:
                key, duration = get_random_key()
                play_tts(f"Pressing {key} button")
                pyautogui.keyDown(key)
                time.sleep(duration)
                pyautogui.keyUp(key)
                time.sleep(0.1)
    except KeyboardInterrupt:
        pass
    print("Key and mouse spamming stopped.")

if __name__ == "__main__":
    main()
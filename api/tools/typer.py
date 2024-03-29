import pyautogui
import time
import keyboard
from Constants import Constants


class Typer:
    typing_continues = True
    pause = False

    def type_text_fast(text, wpm):
        try:
            space = False
            words = text.split()
            seconds_per_word = 60 / wpm

            for word in words:
                for char in word:
                    if not Typer.typing_continues:
                        return
                    if Typer.pause:
                        while Typer.pause:
                            time.sleep(1)
                    if char == "`":
                        space = False
                        pyautogui.typewrite(" ")
                        if word == "`":
                            pyautogui.press("backspace")
                        pyautogui.press("enter")
                        continue
                    else:
                        space = True
                    pyautogui.typewrite(char)
                    time.sleep(seconds_per_word / len(word))
                if space:
                    pyautogui.press("space")

            print("Typing finished")
        except Exception as e:
            print(f"An error occurred: {str(e)}")

    def stop_program():
        Typer.pause = False
        Typer.typing_continues = False

        print("Typing stopped")

    def pause_typing():
        if Typer.typing_continues:
            Typer.pause = True
            print("Typing paused")

    def resume_typing():
        if Typer.typing_continues:
            Typer.pause = False
            print("Typing resumed")

    def start_typing():
        try:
            Typer.typing_continues = True
            pyautogui.FAILSAFE = False

            keyboard.add_hotkey("esc", lambda: Typer.stop_program(), suppress=True)
            keyboard.add_hotkey("alt+[", lambda: Typer.pause_typing(), suppress=True)
            keyboard.add_hotkey("alt+]", lambda: Typer.resume_typing(), suppress=True)

            with open("temp/typer.txt", "r") as text_file:
                text_to_type = text_file.read()

            formatted_text_to_type = text_to_type.replace("\n", "`\n")

            time.sleep(2)

            Typer.type_text_fast(formatted_text_to_type, Constants.TYPING_SPEED)

        except Exception as e:
            print(f"An error occurred: {str(e)}")

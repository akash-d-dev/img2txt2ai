import pyautogui
import time
import keyboard


class Typer:
    typing_continues = True

    def type_text_fast(text, wpm):
        try:
            words = text.split()
            seconds_per_word = 60 / wpm

            for word in words:
                for char in word:
                    if not Typer.typing_continues:
                        return
                    if char == "`":
                        pyautogui.press("enter")
                        continue
                    pyautogui.typewrite(char)
                    time.sleep(seconds_per_word / len(word) / 10)
                pyautogui.press("space")
        except Exception as e:
            print(f"An error occurred: {str(e)}")

    def stop_program():
        Typer.typing_continues = False
        print("Typing stopped")

    def start_typing(typing_speed_wpm):
        try:
            Typer.typing_continues = True
            keyboard.add_hotkey("esc", lambda: Typer.stop_program(), suppress=True)

            with open("temp/typer.txt", "r") as text_file:
                text_to_type = text_file.read()

            time.sleep(2)

            Typer.type_text_fast(text_to_type, typing_speed_wpm)

        except Exception as e:
            print(f"An error occurred: {str(e)}")

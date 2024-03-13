import pyautogui
import time
import keyboard


class Typer:
    typing_continues = True
    pause = False

    def type_text_fast(text, wpm):
        try:
            space = False
            words = text.split()
            seconds_per_word = 60 / wpm

            for i, word in enumerate(words):

                current_line_empty = i > 0 and len(words[i - 1]) == 1
                next_line_empty = i < len(words) - 1 and len(words[i + 1]) == 1

                for char in word:
                    if not Typer.typing_continues:
                        return
                    if Typer.pause:
                        while Typer.pause:
                            time.sleep(1)
                    if char == "`":
                        space = False
                        if not current_line_empty or not next_line_empty:
                            pyautogui.typewrite(" ")
                            if current_line_empty:
                                pyautogui.press("backspace")
                        # pyautogui.press("enter")
                        pyautogui.typewrite("\n")

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

    def start_typing(typing_speed_wpm):
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

            Typer.type_text_fast(formatted_text_to_type, typing_speed_wpm)

        except Exception as e:
            print(f"An error occurred: {str(e)}")

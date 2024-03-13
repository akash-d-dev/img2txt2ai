import pyautogui
import time
import keyboard


class Typer:
    typing_continues = True

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
                    if char == "`":
                        space = False
                        if not current_line_empty or not next_line_empty:
                            pyautogui.typewrite(" ")
                            if current_line_empty:
                                pyautogui.press("backspace")
                        pyautogui.press("enter")
                        # pyautogui.typewrite("/n")

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

    def start_typing(typing_speed_wpm):
        try:
            Typer.typing_continues = True
            keyboard.add_hotkey("esc", lambda: Typer.stop_program(), suppress=True)

            with open("temp/typer.txt", "r") as text_file:
                text_to_type = text_file.read()

            formatted_text_to_type = text_to_type.replace("\n", "` \n")

            time.sleep(2)

            Typer.type_text_fast(formatted_text_to_type, typing_speed_wpm)

        except Exception as e:
            print(f"An error occurred: {str(e)}")

    # def type_text_fast(text, wpm):
    #     try:
    #         words = text.split()
    #         seconds_per_word = 60 / wpm

    #         for word in words:
    #             for char in word:
    #                 if not Typer.typing_continues:
    #                     return
    #                 if char == "`":
    #                     pyautogui.press("enter")
    #                     continue
    #                 pyautogui.typewrite(char)
    #                 time.sleep(seconds_per_word / len(word) / 10)
    #             pyautogui.press("space")
    #     except Exception as e:
    #         print(f"An error occurred: {str(e)}")

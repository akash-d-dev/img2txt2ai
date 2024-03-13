from tools.process_txt import TxtScreenshot
from tools.process_txt_file import TxtFile
from tools.typer import Typer


class Typer_handler:
    def createTyperHandler():
        print("Started Typer Text Generating")
        text = TxtScreenshot.getTxtFromClipboard()
        TxtFile.add_t_to_file_typer(text)
        print("Typer text created")

    def startTyperHandler():
        print("Typer started")
        Typer.start_typing(typing_speed_wpm=500)

    def clearTyperHandler():
        with open("temp/typer.txt", "w") as file:
            file.write("")
            print("Typer text cleared")

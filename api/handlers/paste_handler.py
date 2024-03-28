from tools.process_txt import TxtScreenshot
from tools.process_txt_file import TxtFile


class Paste_handler:
    def createPasteHandler():
        text = TxtScreenshot.getTxtFromClipboard()
        formatted_text = TxtScreenshot.formatTxt(text, makePrompt=False)
        TxtFile.add_t_to_file_paste(formatted_text)
        print("Paste created")

    def clearPasteHandler():
        with open("temp/paste.txt", "w") as file:
            file.write("")
            print("Paste cleared")

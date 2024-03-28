from tools.process_txt import TxtScreenshot
from tools.process_txt_file import TxtFile


class Qna_handler:
    def createQnaHandler():
        text = TxtScreenshot.getTxtFromClipboard()
        formatted_text = TxtScreenshot.formatTxt(text)
        TxtFile.add_q_to_file_qna(formatted_text)
        print("QnA created")

    def clearQnaHandler():
        with open("temp/qna.txt", "w") as file:
            file.write("")
            print("QnA cleared")

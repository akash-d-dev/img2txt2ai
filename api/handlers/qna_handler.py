from tools.process_txt import TxtScreenshot
from tools.process_txt_file import TxtFile


class Qna_handler:
    def createQnaHandler():
        text = TxtScreenshot.getTxtFromClipboard()
        formatted_text = TxtScreenshot.formatTxt(text)
        status = TxtFile.add_q_to_file_qna(formatted_text)
        if status:
            print("QnA created")
        else:
            print("QnA not created")

    def clearQnaHandler():
        with open("temp/qna.txt", "w") as file:
            file.write("")
            print("QnA cleared")

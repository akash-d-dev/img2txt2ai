import pyperclip


class TxtScreenshot:
    def getTxtFromClipboard():
        return pyperclip.paste()

    def pasteTxtToClipboard(text):
        pyperclip.copy(text)
        print("Text copied to clipboard: ", text)
        return True

    def formatTxt(qna):
        text = " - Ques with options:"
        text += "\n\n"
        text += "<b>"
        text += qna
        text += "</b>"
        text += "\n\n\n"
        text += "Your reply should have this queston and correct option listed ONLY. If options are missing then you should reply with the question and whatever you think is the correct answer. Make sure to solve the question."
        text += "\n\n\n"
        text += "Fill Answer here :"
        text += "\n\n\n"

        return text

    def formatTxtErorr(qna):
        text = qna.strip() + " -An error occured-" + "\n\n\n"

        return text

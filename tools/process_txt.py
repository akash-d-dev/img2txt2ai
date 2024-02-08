import pyperclip


class TxtScreenshot:
    def getTxtFromClipboard():
        return pyperclip.paste()

    def formatTxt(qna):
        text = " - Ques with options:"
        text += "\n\n"
        text += qna
        text += "\n\n\n"
        text += "You reply should have this queston listed with all the options"
        text += "\n\n\n"
        text += "Fill Answer here :"
        text += "\n\n\n"

        return text

    def formatTxtErorr(qna):
        text = qna.strip() + " -An error occured-" + "\n\n\n"

        return text

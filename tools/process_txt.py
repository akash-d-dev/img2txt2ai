import pyperclip


class TxtScreenshot:
    def getTxtFromClipboard():
        return pyperclip.paste()

    def formatTxt(qna):
        text = "Question with options:"
        text += "\n\n"
        text += qna
        text += "\n\n"
        text += "Pick the correct option only and add it below where you have been asked, no explanation needed- "
        text += "\n\n"
        text += "Fill Answer here :"
        text += "\n\n"

        return text

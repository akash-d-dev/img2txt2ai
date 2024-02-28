import pyperclip


class TxtScreenshot:
    def getTxtFromClipboard():
        return pyperclip.paste()

    def pasteTxtToClipboard(text):
        pyperclip.copy(text)
        print("Text copied to clipboard: ", text)
        return True

    def formatTxt(qna):
        text = " - Question you need to answer:"
        text += "\n\n\n"
        text += qna
        text += "\n\n\n"
        text += "Fill Answer here :"
        text += "\n\n\n"
        text += "Your reply should have this queston and correct option listed ONLY WITH SERIAL NUMBER. If options are missing then reply with the question and whatever you think is the correct answer. Make sure to solve the question."
        text += "\n\n\n"

        return text

    def formatTxtErorr(qna):
        text = qna.strip() + " -An error occured-" + "\n\n\n"

        return text

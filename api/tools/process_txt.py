import pyperclip


class TxtScreenshot:
    def getTxtFromClipboard():
        return pyperclip.paste()

    def pasteTxtToClipboard(text):
        pyperclip.copy(text)
        print("Text copied to clipboard: ", text)
        return True

    def formatTxt(qna, makePrompt=True):
        text = ""
        if makePrompt:
            text += " - Question you need to answer:"
            text += "\n\n\n"
            text += qna
            text += "\n\n"
            text += "PICK ONE CORRECT OPTION"
            text += "\n\n"
            text += "Your reply should have this question and correct option listed ONLY along WITH SERIAL NUMBER, if you think the question is very long hen use ... . If options are missing then reply with the question and whatever you think is the correct answer."
        else:
            text += qna
        return text

    def formatTxtErorr(qna):
        text = " -An error occured-" + qna.strip() + " -An error occured-" + "\n\n\n"

        return text

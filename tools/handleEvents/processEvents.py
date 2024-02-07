import keyboard
from handleAi.callAi import CallAi
from handleTxtFile.process_txt_file import TxtFile


class Events:
    def listen():
        Events.startApp()
        Events.stopApp()
        Events.clearQna()
        Events.createAns()

    def startApp():
        while True:
            print("Starting app")
            break

    def stopApp():
        print("Stopping app")

    def clearQna():
        keyboard.add_hotkey("right ctrl+0", Events.clearQnaHandler)

    def clearQnaHandler():
        with open("temp/qna.txt", "w") as file:
            file.write("")
            print("QnA cleared")

    def createAns():
        keyboard.add_hotkey("right ctrl+1", Events.createAnsHandler)

    def createAnsHandler():
        qna_doc = CallAi.openAi
        TxtFile.add_a_to_file(qna_doc)

    # def clearAns():
    #     keyboard.add_hotkey("right ctrl+9", Events.clearAnsHandler)

    # def clearAnsHandler():
    #     with open("temp/ans.txt", "w") as file:
    #         file.write("")
    #         print("Ans cleared")

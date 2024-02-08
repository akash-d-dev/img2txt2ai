from tools.process_image import Screenshot
from tools.process_txt import TxtScreenshot
from tools.process_txt_file import TxtFile
from tools.processAiReq import CallAi

# from tools.processEvents import Events

from fastapi import FastAPI, HTTPException
import keyboard
import pyperclip
import os
import uvicorn
import openai


# def main():
#     # stopApp()
#     createQna()
#     clearQna()
#     createAns()
#     clearAns()

#     def startApp():
#         while True:
#             print("Starting app")
#             break

#     def stopApp():
#         print("Stopping app")

#     def createQna():
#         keyboard.add_hotkey("right ctrl+0", createQnaHandler)

#     def createQnaHandler():
#         text = TxtScreenshot.getTxtFromClipboard()
#         formatted_text = TxtScreenshot.formatTxt(text)
#         TxtFile.add_q_to_file(formatted_text)

#     def clearQna():
#         keyboard.add_hotkey("right ctrl+9", clearQnaHandler)

#     def clearQnaHandler():
#         with open("temp/qna.txt", "w") as file:
#             file.write("")
#             print("QnA cleared")

#     def createAns():
#         keyboard.add_hotkey("right ctrl+1", createAnsHandler)

#     def createAnsHandler():
#         qna_doc = CallAi.openAi
#         TxtFile.add_a_to_file(qna_doc)

#     def clearAns():
#         keyboard.add_hotkey("right ctrl+8", clearAnsHandler)

#     def clearAnsHandler():
#         with open("temp/ans.txt", "w") as file:
#             file.write("")
#             print("Ans cleared")

# def main():
#     # stopApp()
#     createQna()
#     clearQna()
#     createAns()
#     clearAns()


def startApp():
    while True:
        print("Starting app")
        break


def stopApp():
    print("Stopping app")


def createQna():
    keyboard.add_hotkey("right ctrl+0", createQnaHandler)


def createQnaHandler():
    text = TxtScreenshot.getTxtFromClipboard()
    formatted_text = TxtScreenshot.formatTxt(text)
    TxtFile.add_q_to_file(formatted_text)


def clearQna():
    keyboard.add_hotkey("right ctrl+9", clearQnaHandler)


def clearQnaHandler():
    with open("temp/qna.txt", "w") as file:
        file.write("")
        print("QnA cleared")


def createAns():
    keyboard.add_hotkey("right ctrl+1", createAnsHandler)


async def createAnsHandler():
    qna_doc = await CallAi.openAi()
    TxtFile.add_a_to_file(qna_doc)


def clearAns():
    keyboard.add_hotkey("right ctrl+8", clearAnsHandler)


def clearAnsHandler():
    with open("temp/ans.txt", "w") as file:
        file.write("")
        print("Ans cleared")


app = FastAPI()

try:
    createQna()
    clearQna()
    createAns()
    clearAns()
except Exception as e:
    print(f"An error occurred: {str(e)}")


@app.get("/")
def read_root():
    qna_content = ""
    ans_content = ""
    with open("temp/qna.txt", "r") as file:
        qna_content = file.read()
        if not qna_content:
            qna_content = "-empty-"

    with open("temp/ans.txt", "r") as file:
        ans_content = file.read()
        if not ans_content:
            ans_content = "-empty-"

    return {"qna_content": qna_content, "ans_content": ans_content}


if __name__ == "__main__":
    uvicorn.run(app=app, host="localhost", port=5000)

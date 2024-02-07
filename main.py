from tools.handleSS.process_image import Screenshot
from tools.handleTxtSS.process_txt import TxtScreenshot
from tools.handleTxtFile.process_txt_file import TxtFile
from tools.handleEvents.processEvents import Events

from fastapi import FastAPI, HTTPException
import keyboard
import pyperclip
import os
import uvicorn
import openai


def main():
    FastAPI()
    Events.listen()
    # filename = Screenshot.process_image()
    # print(f"Screenshot saved as {filename}")
    # if filename:
    #     text = Screenshot.extract_text(filename)
    # print(text)
    text = TxtScreenshot.getTxtFromClipboard()
    formatted_text = TxtScreenshot.formatTxt(text)
    print(formatted_text)

    TxtFile.add_q_to_file(formatted_text)

    # text = TxtScreenshot.getTxtFromClipboard()
    # formatted_text = TxtScreenshot.formatTxt(text)
    # print(formatted_text)

    # TxtFile.add_txt_to_file(formatted_text, "qna.txt")


# # if __name__ == "__main__":
# #     main()

app = FastAPI()

main()


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

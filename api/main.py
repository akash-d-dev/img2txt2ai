from tools.process_txt import TxtScreenshot
from tools.process_txt_file import TxtFile
from tools.processAiReq import CallAi
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, Request
import keyboard
import uvicorn


def startApp():
    while True:
        print("Starting app")
        break


def stopApp():
    print("Stopping app")


def createQna():
    keyboard.add_hotkey("alt+0", createQnaHandler)


def createQnaHandler():
    text = TxtScreenshot.getTxtFromClipboard()
    formatted_text = TxtScreenshot.formatTxt(text)
    TxtFile.add_q_to_file(formatted_text)
    print("QnA created")


def clearQna():
    keyboard.add_hotkey("alt+9", clearQnaHandler)


def clearQnaHandler():
    with open("temp/qna.txt", "w") as file:
        file.write("")
        print("QnA cleared")


############################################################################
# OpenAI
############################################################################


# Create
def createAnsOpenAI():
    keyboard.add_hotkey("alt+1", createAnsHandlerOpenAI)


def createAnsHandlerOpenAI():
    print("Started Ans Generating: OpenAI ")
    error_message, qna_content = CallAi.openAi()
    print(qna_content)
    if error_message is not None:
        if qna_content is not None:
            qna_doc = TxtScreenshot.formatTxtErorr(qna_content)
        else:
            qna_doc = TxtScreenshot.formatTxtErorr("-No Question Present-")
    else:
        qna_doc = qna_content
    TxtFile.add_a_to_file_openai(qna_doc)
    print("Ans created using OpenAI")


# Clear
def clearAnsOpenAI():
    keyboard.add_hotkey("alt+8", clearAnsHandlerOpenAI)


def clearAnsHandlerOpenAI():
    with open("temp/ans.txt", "w") as file:
        file.write("")
        print("GPT Ans cleared")


############################################################################
# Gemini
############################################################################


# Create
def createAnsGemini():
    keyboard.add_hotkey("alt+2", createAnsHandlerGemini)


def createAnsHandlerGemini():
    print("Started Ans Generating: Gemini ")
    error_message, qna_content = CallAi.gemini()
    print(qna_content)
    if error_message is not None:
        if qna_content is not None:
            qna_doc = TxtScreenshot.formatTxtErorr(qna_content)
        else:
            qna_doc = TxtScreenshot.formatTxtErorr("-No Question Present-")
    else:
        qna_doc = qna_content
    TxtFile.add_a_to_file_gemini(qna_doc)
    print("Ans created using Gemini")


# Clear
def clearAnsGemini():
    keyboard.add_hotkey("alt+7", clearAnsHandlerGemini)


def clearAnsHandlerGemini():
    with open("temp/ans_gemini.txt", "w") as file:
        file.write("")
        print("Gemini Ans cleared")


############################################################################
# Gemini Img
############################################################################


# Create
def createAnsGeminiImg():
    keyboard.add_hotkey("alt+3", createAnsHandlerGeminiImg)


def createAnsHandlerGeminiImg():
    print("Started Img Ans Generating: Gemini ")
    # error_message, qna_content = CallAi.gemini_img()
    error_message, qna_content = CallAi.gemini_img()
    print(qna_content)
    if error_message is not None:
        if qna_content is not None:
            qna_doc = TxtScreenshot.formatTxtErorr(qna_content)
        else:
            qna_doc = TxtScreenshot.formatTxtErorr("-No Question Present-")
    else:
        qna_doc = qna_content
    TxtFile.add_a_to_file_gemini_img(qna_doc)
    print("Ans created using Gemini")


# Clear
def clearAnsGeminiImg():
    keyboard.add_hotkey("alt+6", clearAnsHandlerGeminiImg)


def clearAnsHandlerGeminiImg():
    with open("temp/ans_gemini_img.txt", "w") as file:
        file.write("")
        print("Gemini Img Ans cleared")


app = FastAPI()
##################################################################
# Setup CORS
##################################################################
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

try:
    createQna()
    clearQna()

    createAnsOpenAI()
    clearAnsOpenAI()

    createAnsGemini()
    clearAnsGemini()

    createAnsGeminiImg()
    clearAnsGeminiImg()

    print("Hotkeys created")
except Exception as e:
    print(f"An error occurred: {str(e)}")


@app.get("/")
def read_root():
    qna_content = ""
    ans_content_gpt = ""
    ans_content_gemini = ""
    ans_content_gemini_img = ""

    with open("temp/qna.txt", "r") as file:
        qna_content = file.read().replace("\n", "<br>")
        if not qna_content:
            qna_content = "-empty-"

    with open("temp/ans.txt", "r") as file:
        ans_content_gpt = file.read().replace("\n", "<br>")
        if not ans_content_gpt:
            ans_content_gpt = "-empty-"

    with open("temp/ans_gemini.txt", "r") as file:
        ans_content_gemini = file.read().replace("\n", "<br>")
        if not ans_content_gemini:
            ans_content_gemini = "-empty-"

    with open("temp/ans_gemini_img.txt", "r") as file:
        ans_content_gemini_img = file.read().replace("\n", "<br>")
        if not ans_content_gemini_img:
            ans_content_gemini_img = "-empty-"

    return {
        "qna_content": qna_content,
        "ans_content_gpt": ans_content_gpt,
        "ans_content_gemini": ans_content_gemini,
        "ans_content_gemini_img": ans_content_gemini_img,
    }


@app.post("/")
async def receive_txt(request: Request):
    text_dict = await request.json()
    TxtScreenshot.pasteTxtToClipboard(text_dict["text"])
    return True


if __name__ == "__main__":
    uvicorn.run(app=app, host="localhost", port=8008)

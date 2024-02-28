from tools.process_txt import TxtScreenshot
from handlers.qna_handler import Qna_handler
from handlers.openai_handler import Openai_handler
from handlers.gemini_handler import Gemini_handler
from handlers.gemini_img_handler import Gemini_img_handler
from handlers.typer_handler import Typer_handler
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, Request
import keyboard
import uvicorn


def startApp():
    print("Starting app")


def stopApp():
    print("Stopping app")

############################################################################
# QNA
############################################################################


# Create
def createQna():
    keyboard.add_hotkey("alt+0", Qna_handler.createQnaHandler)


# Clear
def clearQna():
    keyboard.add_hotkey("alt+9", Qna_handler.clearQnaHandler)


############################################################################
# OpenAI
############################################################################


# Create
def createAnsOpenAI():
    keyboard.add_hotkey("alt+1", Openai_handler.createAnsHandlerOpenAI)

# Clear
def clearAnsOpenAI():
    keyboard.add_hotkey("alt+8", Openai_handler.clearAnsHandlerOpenAI)


############################################################################
# Gemini
############################################################################


# Create
def createAnsGemini():
    keyboard.add_hotkey("alt+2", Gemini_handler.createAnsHandlerGemini)

# Clear
def clearAnsGemini():
    keyboard.add_hotkey("alt+7", Gemini_handler.clearAnsHandlerGemini)


############################################################################
# Gemini Img
############################################################################


# Create
def createAnsGeminiImg():
    keyboard.add_hotkey("alt+3", Gemini_img_handler.createAnsHandlerGeminiImg)


# Clear
def clearAnsGeminiImg():
    keyboard.add_hotkey("alt+6", Gemini_img_handler.clearAnsHandlerGeminiImg)


##################################################################
# Typer
##################################################################


# Create
def createTyper():
    keyboard.add_hotkey("ctrl+alt+1", Typer_handler.createTyperHandler)


# Start
def startTyper():
    keyboard.add_hotkey("ctrl+alt+2", Typer_handler.startTyperHandler)


# Clear
def clearTyper():
    keyboard.add_hotkey("ctrl+alt+3", Typer_handler.clearTyperHandler)


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
    # Questions
    createQna()  # alt+0
    clearQna()  # alt+9

    # OpenAI
    createAnsOpenAI()  # alt+1
    clearAnsOpenAI()  # alt+8

    # Gemini
    createAnsGemini()  # alt+2
    clearAnsGemini()  # alt+7

    # Gemini Img
    createAnsGeminiImg()  # alt+3
    clearAnsGeminiImg()  # alt+6

    # Typer
    createTyper()  # ctrl+alt+1
    startTyper()  # ctrl+alt+2
    clearTyper()  # ctrl+alt+3

    print("Hotkeys created")
except Exception as e:
    print(f"An error occurred: {str(e)}")


def read_file_content(file_path):
    with open(file_path, "r") as file:
        content = file.read().replace("\n", "<br>")
        if not content:
            content = "-empty-"
        return content


@app.get("/")
def read_root():
    qna_content = read_file_content("temp/qna.txt")
    ans_content_gpt = read_file_content("temp/ans.txt")
    ans_content_gemini = read_file_content("temp/ans_gemini.txt")
    ans_content_gemini_img = read_file_content("temp/ans_gemini_img.txt")

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

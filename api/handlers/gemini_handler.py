from tools.process_txt import TxtScreenshot
from tools.process_txt_file import TxtFile
from tools.process_ai_req import CallAi


class Gemini_handler:
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

    def clearAnsHandlerGemini():
        with open("temp/ans_gemini.txt", "w") as file:
            file.write("")
            print("Gemini Ans cleared")

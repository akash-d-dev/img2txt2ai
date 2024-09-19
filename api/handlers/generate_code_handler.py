from tools.process_txt import TxtScreenshot
from tools.process_txt_file import TxtFile
from tools.process_ai_req import CallAi
from tools.process_txt import TxtScreenshot


class Generate_code_handler:

    def GenerateCodeOpenAI():
        print("Started Ans Generating: OpenAI Code")
        error_message, qna_content = CallAi.openAiCode()
        if error_message is not None:
            if qna_content is not None:
                qna_doc = TxtScreenshot.formatTxtErorr(qna_content)
            else:
                qna_doc = TxtScreenshot.formatTxtErorr("-No Question Present-")
        else:
            qna_doc = qna_content
        TxtFile.add_t_to_file_typer(qna_doc)
        print("Ans created using OpenAI Code")
        TxtScreenshot.pasteTxtToClipboard(qna_doc)
        print("Ans pasted to clipboard")

    def GenerateCodeGemini():
        print("Started Ans Generating: Gemini Code")
        error_message, qna_content = CallAi.geminiCode()
        if error_message is not None:
            if qna_content is not None:
                qna_doc = TxtScreenshot.formatTxtErorr(qna_content)
            else:
                qna_doc = TxtScreenshot.formatTxtErorr("-No Question Present-")
        else:
            qna_doc = qna_content
        TxtFile.add_t_to_file_typer(qna_doc)
        print("Ans created using Gemini Code")
        TxtScreenshot.pasteTxtToClipboard(qna_doc)
        print("Ans pasted to clipboard")

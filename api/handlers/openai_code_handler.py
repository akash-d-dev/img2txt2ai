from tools.process_txt import TxtScreenshot
from tools.process_txt_file import TxtFile
from tools.process_ai_req import CallAi


class Openai_code_handler:

    def createAnsHandlerOpenAICode():
        print("Started Ans Generating: OpenAI Code")
        error_message, qna_content = CallAi.openAiCode()
        if error_message is not None:
            if qna_content is not None:
                qna_doc = TxtScreenshot.formatTxtErorr(qna_content)
            else:
                qna_doc = TxtScreenshot.formatTxtErorr("-No Question Present-")
        else:
            qna_doc = qna_content
        TxtFile.add_a_to_file_openai_code(qna_doc)
        print("Ans created using OpenAI Code")

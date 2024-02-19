import openai
from google.generativeai import GenerativeModel
import google.generativeai as genai


class CallAi:

    def openAi():

        qna_content = ""
        with open("temp/qna.txt", "r") as file:
            qna_content = file.read()
            if not qna_content:
                qna_content = None

        if qna_content:
            print("QnA content: ", qna_content)
            try:
                messages = [
                    {
                        "role": "system",
                        "content": "Act as a helpful assistant",
                    },
                ]
                messages.append(
                    {
                        "role": "system",
                        "content": """You are a quiz solver. Help prepare a qna doc, you will be provided with questions, options and some instructions by the user (Sapmle input is given below). Your job is to only pick the corerct option and reply reply in the format shown in this sample response. USE BOLD TAGS TO HIGHLIGHT THE CORRECT OPTION ONLY AS SHOWN. ALSO MAKE SURE TO MENTION THE OPTION NUMBER IN THE ANSWER, MENTION ONLY THE CORRECT OPTION IN THE ANSWER AND QUESTION. DO NOT MENTION ALL THE OPTIONS AS SHOWN IN THE SAMPLE RESPONSE. 

                        Sample User Input:

                         - Ques with options:

                            How does the Command Line Interface (CLI) contribute to the efficiency and automation of tasks in an Operating System?

                            By providing advanced image editing tools

                            By simplifying voice recognition functionalities

                            By offering a text-based environment for

                            scripting and executing commands

                            By optimizing file storage and retrieval processes

                            You reply should have this queston listed with all the options

                            Fill Answer here :

                        Sample Response Expected by you:

                            Question:
                            How does the Command Line Interface (CLI) contribute to the efficiency and automation of tasks in an Operating System?

                            Answer:
                            <b> c) By offering a text-based environment for scripting and executing commands </b>

                        Note: If a question is asked without any options, you should do as user asks, IF QUESTION REQUIRES CODE THEN USE JAVA TO REPLY.
                        """,
                    }
                )
                # messages.append(CallAi.systemPrompt)
                messages.append({"role": "user", "content": f"{qna_content}"})

                completion = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=messages,
                    api_key="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",
                )

                if completion.choices[0].message.content is not None:
                    reply = completion.choices[0].message.content
                    # print(reply)
                    return None, reply
                else:
                    # raise Exception("Failed to generate response")
                    return "-An error occured-"
            except Exception as e:
                # raise ValueError("")
                return "-An error occured-", qna_content
        else:
            return "-Empty File-", qna_content

    def gemini():
        qna_content = ""
        with open("temp/qna.txt", "r") as file:
            qna_content = file.read()
            if not qna_content:
                qna_content = None

        if qna_content:
            API_KEY = "AIzaSyCFgbIqShroBxKHN_5yTSPEKOtOXbEuD-Y"
            try:
                genai.configure(api_key=API_KEY)
                # model = genai.GenerativeModel("aqa")
                model = genai.GenerativeModel("gemini-1.0-pro-001")

                for m in genai.list_models():
                    if "generateContent" in m.supported_generation_methods:
                        print(m.name)

                chat = model.start_chat(
                    history=[
                        {
                            "role": "user",
                            "parts": [
                                {
                                    "text": "System prompt: You are a very successful and experienced quiz solver. You help in creating a qna doc. "
                                }
                            ],
                        },
                        {
                            "role": "model",
                            "parts": [{"text": "Understood."}],
                        },
                        {
                            "role": "user",
                            "parts": [
                                {
                                    "text": """System prompt: Help prepare a qna doc, you will be provided with questions, options and some instructions by the user (Sapmle input is given below). Your job is to only pick the corerct option and reply reply in the format shown in this sample response. USE BOLD TAGS TO HIGHLIGHT THE CORRECT OPTION ONLY AS SHOWN. ALSO MAKE SURE TO MENTION THE OPTION NUMBER IN THE ANSWER AS SHOWN IN THE SAMPLE RESPONSE.

                        Sample User Input:

                         - Ques with options:

                            How does the Command Line Interface (CLI) contribute to the efficiency and automation of tasks in an Operating System?

                            By providing advanced image editing tools

                            By simplifying voice recognition functionalities

                            By offering a text-based environment for

                            scripting and executing commands

                            By optimizing file storage and retrieval processes

                            You reply should have this queston listed with all the options

                            Fill Answer here :

                        Sample Response Expected by you:

                            Question:
                            How does the Command Line Interface (CLI) contribute to the efficiency and automation of tasks in an Operating System?

                            Answer:
                            <b> c) By offering a text-based environment for scripting and executing commands </b>

                        Note: If a question is asked without any options, you should do as user asks
                        """
                                }
                            ],
                        },
                        {
                            "role": "model",
                            "parts": [{"text": "Understood."}],
                        },
                        {
                            "role": "user",
                            "parts": [
                                {
                                    "text": """System prompt: You answer all the questions asked by the user in one reply only.For generating a reply of each question, Use the format shown in the sample response. If a question is asked without any options, you should do as user asks, IF QUESTION REQUIRES CODE THEN USE JAVA AS DEFAULT TO REPLY, until another language is specified."""
                                }
                            ],
                        },
                        {
                            "role": "model",
                            "parts": [
                                {
                                    "text": "Understood. I will answer all the in one reply only. If user asks one question, I will reply one answer. If user asks 5 questions, I will reply 5 answers. I will use the format shown in the sample response. If a question is asked without any options, I will do as user asks. I will generate the code replies in JAVA as default unitl another language is specified. I will start answering now."
                                }
                            ],
                        },
                        {
                            "role": "user",
                            "parts": [
                                {
                                    "text": "System prompt: You will wrap only the selected option with <b> </b> tags. If no options are present you can generate your own answer and wrap it with <b> </b> tags"
                                }
                            ],
                        },
                        {
                            "role": "model",
                            "parts": [
                                {
                                    "text": "Understood. I will answer all the in one reply only. If user asks one question, I will reply one answer. If user asks 5 questions, I will reply 5 answers. I will use the format shown in the sample response. If a question is asked without any options, I will do as user asks. I will start answering now."
                                }
                            ],
                        },
                    ]
                )
                reply = chat.send_message(qna_content)
                print(reply.text)

                return None, reply.text

            except Exception as e:
                # raise ValueError("")
                return "-An error occured-", qna_content
        else:
            return "-Empty File-", qna_content

import openai
import google.generativeai as genai
from PIL import ImageGrab


class CallAi:

    def openAi():

        qna_content = ""
        with open("temp/qna.txt", "r") as file:
            qna_content = file.read()
            if not qna_content:
                qna_content = None

        if qna_content:
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
                        "content": """You are a QUIZ SOLVER. Help solving a quiz. You will be provided with questions, options and some instructions by the user (Sapmle input is given below for referemce). Your job is to only pick the corerct option and reply in the same format shown as shown in sample response. USE BOLD TAGS TO HIGHLIGHT THE CORRECT OPTION ONLY AS SHOWN. MAKE SURE TO MENTION THE OPTION NUMBER IN THE ANSWER, MENTION ONLY THE CORRECT OPTION IN THE ANSWER AND QUESTION. DO NOT MENTION ALL OTHER WRONG OPTIONS.

                            Sample User Input:

                            - Question you need to answer:
                            

                                How does the Command Line Interface (CLI) contribute to the efficiency and automation of tasks in an Operating System?

                                By providing advanced image editing tools

                                By simplifying voice recognition functionalities

                                By offering a text-based environment for

                                scripting and executing commands

                                By optimizing file storage and retrieval processes

                                    
                                
                                Your reply should have this queston and correct option listed ONLY WITH SERIAL NUMBER. If options are missing then reply with the question and whatever you think is the correct answer. Make sure to solve the question.



                                Fill Answer here :


                            Sample Response Expected by you:

                                Question:
                                How does the Command Line Interface (CLI) contribute to the efficiency and automation of tasks in an Operating System?

                                Answer:
                                <b> c) By offering a text-based environment for scripting and executing commands </b>
                        
                        As you can see in the sample response, only the correct option is mentioned in the answer and along with the question and the option is wrapped in bold tags. You should do the same.
                        
                        Note: If a question is asked without any options, you should do as user asks, IF QUESTION REQUIRES CODE THEN USE JAVA TO REPLY and do not forget to wrap only the correct option in bold tags.
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
                model = genai.GenerativeModel("gemini-pro")
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

                         - Question you need to answer:
                         

                            How does the Command Line Interface (CLI) contribute to the efficiency and automation of tasks in an Operating System?

                            By providing advanced image editing tools

                            By simplifying voice recognition functionalities

                            By offering a text-based environment for

                            scripting and executing commands

                            By optimizing file storage and retrieval processes

                                
                            
                            Your reply should have this queston and correct option listed ONLY WITH SERIAL NUMBER. If options are missing then reply with the question and whatever you think is the correct answer. Make sure to solve the question.



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
                                    "text": "Understood. I will answer all the in one reply only. If user asks one question, I will reply one answer. If user asks 5 questions, I will reply 5 answers. I will use the format shown in the sample response. If a question is asked without any options, I will do as user asks. I will generate the code replies in JAVA as default unitl another language is specified."
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
                                    "text": "Understood. I will also wrap the answer in <b> </b> tags. I will start answering now."
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

    def gemini_img():

        image = ImageGrab.grabclipboard()
        print(image)
        if image is not None:
            try:
                API_KEY = "AIzaSyCFgbIqShroBxKHN_5yTSPEKOtOXbEuD-Y"
                genai.configure(api_key=API_KEY)

                model = genai.GenerativeModel(model_name="gemini-1.0-pro-vision-latest")
                prompt_parts = []
                prompt_parts = [
                    """
                    You are a very successful and experienced quiz solver. You help in solving problems in images.
                    
                    System prompt: Search for a question in image and solve it, if you cannot find the question then do what you think can help
                     
                    If the image has a question then add do not forget to add it in the reply. Wrap the final answer in bold tags like this - <b>Final Answer:{final answer}</b>
                    
                    
                    Sample output -
                    
                    
                     Given the arrival time, burst time and priority of processes, apply Priority Scheduling and calculate the turnaround time. Assume that lower the value, higher the priority.

                    Process	Arrival Time	Burst Time	Priority
                    P1	0	4	2
                    P2	3	2	3
                    P3	5	6	1

                    **Solution**
                    --PROBLEM OVERVIEW--
                    First, we need to sort the processes according to their priority. The processes with lower priority will be executed first. So, the order of execution will be P3, P1, P2.

                    --MORE EXPLANAATION IF NEEDED WILL BE ADDED BELOW--
                    Next, we need to calculate the waiting time for each process. The
                    For P2, the turnaround time is 11 as it takes 11 units of time to complete its execution.

                    **The final answer is:**

                    P1: Turnaround Time = 9
                    P2: Turnaround Time = 11
                    P3: Turnaround Time = 6 
                    
                    """,
                    image,
                ]

                response = model.generate_content(prompt_parts)
                return None, response.text

            except Exception as e:
                print(e)
                return e, "<b> QnA -An error occured- </b>"
        else:
            print("No image found in clipboard.")
            return None, "-Empty File-"

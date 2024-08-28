import openai
import google.generativeai as genai
from PIL import ImageGrab
from Constants import Constants
from tools.read_file import ReadFile


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
                        "content": f"""You are a QUIZ SOLVER. Help solving a quiz. You will be provided with questions, options and some instructions by the user (Sapmle input is given below for referemce). Your job is to only pick the corerct option and reply in the same format shown as shown in sample response. USE BOLD TAGS TO HIGHLIGHT THE CORRECT OPTION ONLY AS SHOWN. MAKE SURE TO MENTION THE OPTION NUMBER IN THE ANSWER, MENTION ONLY THE CORRECT OPTION IN THE ANSWER AND QUESTION. DO NOT MENTION ALL OTHER WRONG OPTIONS.

                        Sample User Input:
                        
                        
                        
                        - Question you need to answer:
                        

                        A local library struggles with low visitation. They transform a section into a community co-working space. Which aspect of lateral thinking does this transformation illustrate?

                        No lateral thinking aspect is utilised

                        Problem Solving

                        Description

                        Trimming and Splitting


                        PICK ONE CORRECT OPTION

                       Your reply should have this question and correct option listed ONLY along WITH SERIAL NUMBER, if you think the question is very long hen use ... . If options are missing then reply with the question and whatever you think is the correct answer.


                        - Question you need to answer:


                        The students of XYZ school are struggling with academic stress. Their performance has dropped significantly in the recent times. They introduce mindfulness sessions. Which lateral thinking aspect does this solution highlight?

                        Problem Solving

                        Design

                        Abstraction and Extraction

                        Description


                        PICK ONE CORRECT OPTION

                       Your reply should have this question and correct option listed ONLY along WITH SERIAL NUMBER, if you think the question is very long hen use ... . If options are missing then reply with the question and whatever you think is the correct answer.



                        Sample Response Expected by you:
                        

                        Question: A local library struggles with low visitation. They transform a section into a community co-working space...illustrate?

                        <b>Answer: B) Problem Solving</b>

                        Question: The students of XYZ school are struggling with academic stress. Their performance has dropped significantly in the recent times...highlight?

                        <b>Answer: A) Problem Solving</b>

                        
                       
                        
                        NOTE: As you can see in the sample response, only the correct option is mentioned in the answer and along with the question and the option is wrapped in bold tags. You should do the same. If a question is asked without any options, you should do as user asks, IF QUESTION REQUIRES CODE THEN USE f{Constants.CODE_LANGUAGE} TO REPLY and do not forget to wrap only the correct option in bold tags.
                        """,
                    }
                )
                # messages.append(CallAi.systemPrompt)
                messages.append({"role": "user", "content": f"{qna_content}"})

                completion = openai.ChatCompletion.create(
                    model=Constants.OPENAI_MODEL,
                    messages=messages,
                    api_key=Constants.OPENAI_API_KEY,
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

    def openAiCode():

        qna_content = ReadFile.read_file_content("temp/paste.txt")

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
                        "content": f"""You are a Coder. Help solving a coding problem. You will be provided with a coding problem and some instructions by the user. Your job is to only write the code and reply in the same format shown as shown in sample response. USE {Constants.CODE_LANGUAGE} AS DEFAULT TO REPLY, until another language is specified.
                        
                        
                        Here are some instructions for you:
                        1) Do not write comments
                        2) Always take input form user so that the code is dynamic
                        3) Use leetcode ready code, but still write the main function and take input from user
                        4) Keep the code readable and clean  
                        5) Reply only with the code, no explanation is needed
                        6) Do not do any formatting in your reply like adding ``` ``` or anything
                            """,
                    }
                )
                # messages.append(CallAi.systemPrompt)
                messages.append({"role": "user", "content": f"{qna_content}"})

                completion = openai.ChatCompletion.create(
                    model=Constants.OPENAI_MODEL,
                    messages=messages,
                    api_key=Constants.OPENAI_API_KEY,
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
            try:
                genai.configure(api_key=Constants.GEMINI_API_KEY)
                model = genai.GenerativeModel(Constants.GEMINI_MODEL)
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
                        

                        A local library struggles with low visitation. They transform a section into a community co-working space. Which aspect of lateral thinking does this transformation illustrate?

                        No lateral thinking aspect is utilised

                        Problem Solving

                        Description

                        Trimming and Splitting


                        PICK ONE CORRECT OPTION

                       Your reply should have this question and correct option listed ONLY along WITH SERIAL NUMBER, if you think the question is very long hen use ... . If options are missing then reply with the question and whatever you think is the correct answer.


                        - Question you need to answer:


                        The students of XYZ school are struggling with academic stress. Their performance has dropped significantly in the recent times. They introduce mindfulness sessions. Which lateral thinking aspect does this solution highlight?

                        Problem Solving

                        Design

                        Abstraction and Extraction

                        Description


                        PICK ONE CORRECT OPTION

                       Your reply should have this question and correct option listed ONLY along WITH SERIAL NUMBER, if you think the question is very long hen use ... . If options are missing then reply with the question and whatever you think is the correct answer.



                        Sample Response Expected by you:
                        

                        Question: A local library struggles with low visitation. They transform a section into a community co-working space...illustrate?

                        Answer: B) Problem Solving

                        Question: The students of XYZ school are struggling with academic stress. Their performance has dropped significantly in the recent times...highlight?

                        Answer: A) Problem Solving

                        
                        NOTE: If a question is asked without any options, you should do as user asks
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
                                    "text": f"""System prompt: You answer all the questions asked by the user in one reply only.For generating a reply of each question, Use the format shown in the sample response. If a question is asked without any options, you should do as user asks, IF QUESTION REQUIRES CODE THEN USE {Constants.CODE_LANGUAGE} AS DEFAULT TO REPLY, until another language is specified."""
                                }
                            ],
                        },
                        {
                            "role": "model",
                            "parts": [
                                {
                                    "text": f"Understood. I will answer all the in one reply only. If user asks one question, I will reply one answer. If user asks 5 questions, I will reply 5 answers. I will use the format shown in the sample response. If a question is asked without any options, I will do as user asks. I will generate the code replies in {Constants.CODE_LANGUAGE} as default unitl another language is specified."
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
                                    "text": "Understood. I will also wrap the answer in <b> </b> tags. Like <b> Answer: A) Problem Solving</b>. I will start answering now."
                                }
                            ],
                        },
                    ]
                )
                reply = chat.send_message(qna_content)
                return None, reply.text

            except Exception as e:
                return "-An error occured-", qna_content
        else:
            return "-Empty File-", qna_content

    def gemini_img():

        image = ImageGrab.grabclipboard()
        print(image)
        if image is not None:
            try:
                genai.configure(api_key=Constants.GEMINI_API_KEY)

                model = genai.GenerativeModel(model_name=Constants.GEMINI_IMG_MODEL)
                prompt_parts = []
                prompt_parts = [
                    """
                    You are a very successful and experienced quiz solver. You help in solving problems in images.
                    
                    System prompt: Search for a question in image and solve it, if you cannot find the question then do what you think can help
                     
                    If the image has a question then add do not forget to add it in the reply. Wrap the final answer in bold tags like this - <b>Final Answer:{final answer}</b>
                    
                    
                    Sample output of a problem-
                    
                    
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
                    
                    
                    NOTE: The above problem is only a sample do not use it as a reference for the current problem. Do not answer the sample problem.
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

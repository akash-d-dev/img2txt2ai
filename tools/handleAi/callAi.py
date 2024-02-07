import openai


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
                        "content": "You need to prepare a question and an answer doc, you will be provided with questions and options and some instructions by the user. Your job is to only pick the corerct option and add it where user has asked. Do not change the doc format, reply is similar format as user has provided",
                    }
                )
                messages.append({"role": "user", "content": f"{qna_content}"})

                completion = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=messages,
                    api_key="OPENAI_KEY",
                )

                if completion.choices[0].message.content is not None:
                    reply = completion.choices[0].message.content
                    return reply
                else:
                    # raise Exception("Failed to generate response")
                    return "-An error occured-"
            except Exception as e:
                # raise ValueError("")
                return "-An error occured-"

class TxtFile:
    async def add_q_to_file(text):
        filename = "temp/" + "qna.txt"
        text = text + "\n\n\n"

        with open(filename, "a") as file:
            file.write(text)
        return True

    async def add_a_to_file(text):
        print(text)
        filename = "temp/" + "ans.txt"
        text = text + "\n\n\n"

        with open(filename, "a") as file:
            file.write(text)
        return True

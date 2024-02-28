class TxtFile:
    def add_q_to_file(text):
        filename = "temp/" + "qna.txt"
        text = text + "\n\n"

        with open(filename, "a") as file:
            file.write(text)
        return True

    def add_a_to_file_openai(text):
        print(text)
        filename = "temp/" + "ans.txt"
        text = text + "\n\n"

        with open(filename, "a") as file:
            file.write(text)
        return True

    def add_a_to_file_gemini(text):
        filename = "temp/" + "ans_gemini.txt"
        text = text + "\n\n"

        with open(filename, "a") as file:
            file.write(text)
        return True

    def add_a_to_file_gemini_img(text):
        filename = "temp/" + "ans_gemini_img.txt"
        text = text + "\n\n"

        with open(filename, "a") as file:
            file.write(text)
        return True

    def add_t_to_file_typer(text):
        filename = "temp/" + "typer.txt"
        text = text + "\n\n"

        with open(filename, "w") as file:
            file.write(text)
        return True

class TxtFile:

    def add_to_file(filename, text):
        text = text + "\n\n"

        with open(filename, "a+") as file:
            file.write(text)
        return True

    def add_q_to_file(text):
        return TxtFile.add_to_file("temp/qna.txt", text)

    def add_a_to_file_openai(text):
        return TxtFile.add_to_file("temp/ans.txt", text)

    def add_a_to_file_openai_code(text):
        return TxtFile.add_to_file("temp/typer.txt", text)

    def add_a_to_file_gemini(text):
        return TxtFile.add_to_file("temp/ans_gemini.txt", text)

    def add_a_to_file_gemini_img(text):
        return TxtFile.add_to_file("temp/ans_gemini_img.txt", text)

    def add_t_to_file_typer(text):
        return TxtFile.add_to_file("temp/typer.txt", text)

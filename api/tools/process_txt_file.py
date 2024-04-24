class TxtFile:

    def add_to_file(filename, text, gap2x=True):
        if gap2x:
            text = text + "\n\n\n"
        else:
            text = text + "\n\n"

        with open(filename, "a+") as file:
            try:
                file.write(text)
                print("Text added to file: ", text)
                return True
            except:
                print(
                    """
                    **********************************
                    An error occurred while saving txt.
                    Remove speical characters from text
                    Or
                    Try breaking the text in smaller parts
                    **********************************
                    """
                )
                return False

    def add_t_to_file_paste(text):
        return TxtFile.add_to_file("temp/paste.txt", text, gap2x=False)

    def add_q_to_file_qna(text):
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

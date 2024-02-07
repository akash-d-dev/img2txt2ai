class TxtFile:
    def add_txt_to_file(text, filename):
        filename = "temp/" + "qna.txt"
        text = text + "\n\n\n"

        with open(filename, "a") as file:
            file.write(text)
        return True

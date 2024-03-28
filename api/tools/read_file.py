class ReadFile:
    def read_file_content(file_path):
        with open(file_path, "r") as file:
            content = file.read().replace("\n", "<br>")
            if not content:
                content = "-empty-"
            return content

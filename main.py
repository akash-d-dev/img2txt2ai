from tools.handleSS.process_image import Screenshot
from tools.handleTxtSS.process_txt import TxtScreenshot
from tools.handleTxtFile.process_txt_file import TxtFile


def main():
    # filename = Screenshot.process_image()
    # print(f"Screenshot saved as {filename}")
    # if filename:
    #     text = Screenshot.extract_text(filename)
    # print(text)
    text = TxtScreenshot.getTxtFromClipboard()
    formatted_text = TxtScreenshot.formatTxt(text)
    print(formatted_text)

    TxtFile.add_txt_to_file(formatted_text, "qna.txt")

    # text = TxtScreenshot.getTxtFromClipboard()
    # formatted_text = TxtScreenshot.formatTxt(text)
    # print(formatted_text)

    # TxtFile.add_txt_to_file(formatted_text, "qna.txt")


if __name__ == "__main__":
    main()

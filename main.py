from tools.handleSS.process_image import Screenshot


def main():
    filename = Screenshot.process_image()
    print(f"Screenshot saved as {filename}")
    # if filename:
    # text = Screenshot.extract_text("1707296505_e3766fbb.png")
    print(Screenshot.extract_text("1707296505_e3766fbb.png"))


if __name__ == "__main__":
    main()

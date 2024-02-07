from process_image import Screenshot


def main():
    filename = Screenshot.process_image()
    print(f"Screenshot saved as {filename}")
    text = Screenshot.extract_text(filename)
    print(text)


if __name__ == "__main__":
    main()

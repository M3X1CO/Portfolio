def main():
    user_input = input("emoji loading: ")
    converted_text = convert(user_input)
    print(converted_text)



def convert(text):
    text = text.replace(":)", "\U0001F642")
    text = text.replace(":(", "\U0001F641")
    return text


main()
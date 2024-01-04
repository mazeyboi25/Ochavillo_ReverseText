def reverse_text(input_text):
    reversed_text = ''
    for char in input_text:
        reversed_text = char + reversed_text
    return reversed_text


def main():
    while True:
        user_input = input("Enter a text: ")

        if user_input.isalpha():  # isalpha is to check if all the characters are alphabets
            reversed_text = ""
            for char in user_input:
                reversed_text = char + reversed_text
            print("Reversed text:", reversed_text)
        else:
            print("Error Reported! Enter text only")


main()

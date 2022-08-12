from dict import translate_dictionary
import winsound
import time

user_input = input("Type in the phrase you want to translate:")
user_input = user_input.upper()


def reproduce_morse_code(code: str):
    for char in code:
        if char == '.':
            winsound.Beep(1000, 100)
        elif char == '-':
            winsound.Beep(800, 300)
        elif char == " ":
            time.sleep(1)
        elif char == "/":
            time.sleep(3)
        time.sleep(0.1)


morse_char_list = [translate_dictionary[char] for char in user_input]
morse_code = ' '.join(morse_char_list)

print(f'Your phrase in morse code is: {morse_code.replace("/"," ")}')

reproduce_morse_code(morse_code)


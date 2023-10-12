
morse_dict = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'j': '.---', 'K': '-.-', 'L': '.-..', 'M': '--' 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----', ',': '--..--', '.': '.-.-.-', '?': '..--..', '"': '.-..-.', ':': '---...', "'": '.----.', '-': '-....-', '/': '-..-.', '(': '-.--.', ')': '-.--.-'}

def from_morse_code(morse_code):

    message = ''
    morse_code = morse_code.split(' ')
    for code in morse_code:
        for char, morse in morse_dict.items():
            if morse == code:
                message += char
    return message

def main():
    morse_code_sequence = ".. / .- -- / .- / -... --- -.-- .-.-.-"
    print("Morse code sequence: ", morse_code_sequence, "\nMessage: ", from_morse_code(morse_code_sequence))

user_1 = int(input("What sentence do  you want to turn into morse code?"))
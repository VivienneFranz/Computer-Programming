
morse_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', '.': '.-.-.-', ',': '--..--',
    '?': '..--..', "'": '.----.', '!': '-.-.--', '/': '-..-.', '(': '-.--.', ')': '-.--.-',
    ':': '---...', ';': '-.-.-.', '=': '-...-', '+': '.-.-.', '-': '-....-', '_': '..--.-', '"': '.-..-.',
    '$': '...-..-', '@': '.--.-.', ' ': '/'}

message_to_code = input("What message would you like to turn into morse code? Hit enter to choose below ")

def to_morse_code(message):
    
    morse_code = ''
    for char in message.upper():
        if char in morse_dict:
            morse_code += morse_dict[char] + ' '
    return morse_code

def main():
    while True:
        choice = input("Choose an option:\nPress 1 to convert text to Morse code\nPress 2 to convert Morse code to text\nPress -1 to quit\n")
        if choice == '1':
            message = input("Enter a message to translate to Morse code: ")
            morse_code = to_morse_code(message)
            print(morse_code)
        
        elif choice == '2':
            morse_code = input("Quitted successfully")
            break
        
        else:
            print("Erorr in choice, please choose from our options.")

if __name__ == "__main__":
    main()
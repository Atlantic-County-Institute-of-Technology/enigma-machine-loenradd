# Leonard DeMarco, 12/2/25 - 1/9/25, Enigma Machine

import os
import re

UPPER_ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
LOWER_ALPHABET = "abcdefghijklmnopqrstuvwxyz"

def main():
    os.system('cls' if os.name == 'nt' else 'clear')  # terminal clear command my beloved
    print(
        "[1] Encode + write to file \n[2] Encode file \n[3] Decode file \n "
    )
    match input("Please select an option: "):
        case "1":
            encode_write()
        case "2":
            work_magic(True)
        case "3":
            work_magic(False)
        case _:
            input("[!] Please select a valid option.")
            main()


def vignere_cipher(phrase:str, key: str, method: bool):  # encode = true, decode = false
    encrypted = ""
    subtracter = 0  # Offset from rotation if a non-alphabetic character is used
    key = re.sub('[^A-Za-z]+', '', key)  # Remove special characters from key if there are any
    if key == '':  # tomfoolery prevention
        raise ValueError("The key you've provided is empty or only consists of non-alphabetic characters. Vignere cipher keys must have letters from the English alphabet in order to encode a message.")  # holy yap fest
    for i in range(len(phrase)):
        if phrase[i].isalpha():
            charset = (UPPER_ALPHABET if phrase[i].isupper() else LOWER_ALPHABET)  # Set charset
            key_correct = (key.upper() if phrase[i].isupper() else key.lower())  # Make key uppercase if the current letter is uppercase
            rotIndex = ((i - subtracter) if (i-subtracter) < len(key_correct) else ((i-subtracter) % len(key_correct)))  # Ensure rotation will be looped if the key is shorter
            rot = (charset.index(key_correct[rotIndex]))  # Set rotation
            encrypted += ((charset[(charset.index(phrase[i]) + rot) % 26]) if method == True else (charset[(charset.index(phrase[i]) - rot) % 26]))  # Add rotated character to encrypted string
        else:
            encrypted += phrase[i]  # If character is not alphabetic, add to string unchanged
            subtracter += 1
    return encrypted


def encode_write():
    os.system('cls' if os.name == 'nt' else 'clear')  # terminal clear command my beloved
    msg = input("[-] Message: ")
    key = input("[-] Key: ")
    out = vignere_cipher(msg, key, True)
    print(out)
    file_input = input("[!] Would you like to write the output to a new file? (y/n)")
    if file_input == "y":
        write_file(out)


def work_magic(method:bool):
    os.system('cls' if os.name == 'nt' else 'clear')  # terminal clear command my beloved
    if method == True:
        file_to_open = (input("[-] Please input the name of the file you would like to encode (no file extension, txt files only): ") + ".txt")
    else:
        file_to_open = (input("[-] Please input the name of the file you would like to decode (no file extension, txt files only): ") + ".txt")
    if os.path.exists(file_to_open):
        msg = open(file_to_open, "r").read()  # Open file for reading first to save the file contents
        key = str(input("[-] Key:"))
        out = vignere_cipher(msg, key, method)
        with open(file_to_open, "w") as file:  # Open file for writing, which deletes all data in the file
            write = True
            while write:
                try:
                    os.system('cls' if os.name == 'nt' else 'clear')  # terminal clear command my beloved
                    match int(input(f"[!] Output : {out} \n[!] Would you like to overwrite the existing file or create a new one? \n \n[1] Overwrite file \n[2] Create new file \n \n[-]: ")):
                        case 1:
                            file.write(out)
                            print("[!] File saved.")
                            quit()
                        case 2:
                            write_file(out)

                except ValueError:
                    input("[!] Please select a valid option.")
    else:
        input("[!] File does not exist. ")
        work_magic(method)


def write_file(data):
    os.system('cls' if os.name == 'nt' else 'clear')  # terminal clear command my beloved
    file_to_open = (input("[-] Input the name of the file you would like to write the output to (no file extension, txt files only): ") + ".txt")
    with open(file_to_open, "w") as file:
        file.write(data)
        print("[!] File saved.")
        quit()

if __name__ == "__main__":
    main()

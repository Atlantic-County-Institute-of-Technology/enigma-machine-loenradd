
import os
import sys

UPPER_ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
LOWER_ALPHABET = "abcdefghijklmnopqrstuvwxyz"

def main():
    os.system('cls' if os.name == 'nt' else 'clear')  # terminal clear command my beloved
    print(
        "[1] Encode + write to file \n[2] Encode file \n[3] Decode file \n "
    )
    try:
        match int(input("Please select an option: ")):
            case 1:
                encode_write()
            case 2:
                workmagic(True)
            case 3:
                workmagic(False)
    except ValueError:
        input("[!] Please select a valid option. ")
        main()


def vignere_cipher(phrase:str,key:str, method:bool):  # encoode = true, decode = false
    encrypted = ""
    subtracter = 0  # Offset from rotation if a non-alphabetic character is used
    for i in range(len(phrase)):
        if phrase[i].isalpha():
            charset = (UPPER_ALPHABET if phrase[i].isupper() else LOWER_ALPHABET)  # Set charset
            key_correct = (key.upper() if phrase[i].isupper() else key.lower())  # Make key uppercase if the current letter is uppercase
            rotIndex = ((i - subtracter) if (i-subtracter) < len(key_correct) else ((i-subtracter) % len(key_correct)))  # Ensure rotation will be looped if the key is shorter
            rot = (charset.index(key_correct[rotIndex]))  #  Set rotation
            encrypted += ((charset[(charset.index(phrase[i]) + rot) % 26]) if method == True else (charset[(charset.index(phrase[i]) - rot) % 26]))  # Add rotated character to encrypted string
        else:
            encrypted += phrase[i]  # If character is not alphabetic, add to string unchanged
            subtracter += 1
    return encrypted




def encode_write():
    os.system('cls' if os.name == 'nt' else 'clear')  # terminal clear command my beloved
    msg = input("[-] Message: ")
    key = input("[-] Key: ")
    vig_method = input("[-] Type 'e' to encrypt, ignore to decrypt:")
    out = (vignere_cipher(msg,key,True) if vig_method == "e" else vignere_cipher(msg,key,False))
    print(out)
    isitokay = input("[!] Would you like to write the output to a new file? (y/n)")
    if isitokay == "y":
        write_file(out)


def workmagic(method:bool):
    os.system('cls' if os.name == 'nt' else 'clear')  # terminal clear command my beloved
    file_to_open = (input("[-] Please input the name of the file you would like to encode (no file extension, txt files only): ")+".txt")
    if os.path.exists(file_to_open):
        msg = open(file_to_open, "r").read()
        key = str(input("[-] Key:"))
        with open(file_to_open, "w") as file:
            out = vignere_cipher(msg, key, method)
            write = True
            while write:
                try:
                    os.system('cls' if os.name == 'nt' else 'clear')  # terminal clear command my beloved
                    match int(input(f"[!] Output : {out} \n[!] Would you like to overwrite the existing file or create a new one? \n \n[1] Overwrite file \n[2] Create new file \n \n[-]: ")):
                        case 1:
                            file.write(out)
                            quit()
                        case 2:
                            write_file(out)

                except ValueError:
                    input("[!] Please select a valid option.")
    else:
        input("[!] File does not exist. ")
        workmagic(method)


def write_file(data):
    os.system('cls' if os.name == 'nt' else 'clear')  # terminal clear command my beloved
    file_to_open = (input("[-] Input the name of the file you would like to write the output to (no file extension, txt files only): ") + ".txt")
    with open(file_to_open, "w") as file:
        file.write(data)
        quit()

if __name__ == "__main__":
    main()

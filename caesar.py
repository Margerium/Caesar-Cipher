# Program to encrypt / de-crypt a plain text file of the users choosing using the Caesar Cipher.

import time
import argparse


def cipher(code_type, text, user_key):
    """This function will encode/decode your input text and return the output"""

    if type(user_key) != int:
        return "user key must be an integer between 1 and 25"

    elif user_key < 1 or user_key > 25:
        return "user key must be an integer between 1 and 25"

    start_time = time.time()

    if type(code_type) != str:
        return "Function expects either command '-e' to encode or '-d' to decode"

    elif code_type.lower() != "d" and code_type.lower() != "e":
        return "Function expects either command '-e' to encode or '-d' to decode"

    elif code_type == "d":
        user_key = -user_key
        print("\nThe program is now decoding your file")

    elif code_type == "e":
        print("\nThe program is now encoding your file")

    translated = ""

    for symbol in text:

        if symbol.isalpha():

            num = ord(symbol)
            num = num + user_key

            if symbol.isupper():

                if num > ord("Z"):
                    num = num - 26

                elif num < ord("A"):
                    num = num + 26

            elif symbol.islower():

                if num > ord("z"):
                    num = num - 26

                elif num < ord("a"):
                    num = num + 26

            translated = translated + chr(num)

        else:

            translated = translated + symbol

    print("\nThe operation took %s seconds to perform" % (time.time() - start_time))
    return translated


parser = argparse.ArgumentParser()

group = parser.add_mutually_exclusive_group()
group.add_argument("-e", "--encode", action="store_true", help="Tells the program to encode your text")
group.add_argument("-d", "--decode", action="store_true", help="Tells the program to decode your text")
group.add_argument("-l", "--text_length", action="store_true", help="Shows the total length of your text")

parser.add_argument("-r", type=int, required=True, help="(Rotation) Your key that determines the cipher shift, "
                                                        "must be between 1 and 25")
parser.add_argument("-i", type=str, required=True, help="Provide a name for your input file")
parser.add_argument("-o", type=str, required=True, help="Provide a name for your output file")
parser.add_argument("-s", type=int, required=False, help="Tells the program to start from a certain character in the "
                                                         "text")
parser.add_argument("-n", type=int, required=False, help="Tells the program to output a certain number of characters "
                                                         "from the text")
parser.add_argument("-p", "--print_to_screen", action="store_true", required=False, help="Tells the program to print "
                                                                                         "the output to the console")

args = parser.parse_args()

program_key = args.r
input_file_name = args.i
output_file_name = args.o
starting_character_in_file = args.s
number_of_characters_to_output = args.n

input_file = open(input_file_name, "r", encoding="utf8")
input_text = input_file.read()
input_file.close()

input_text = input_text[starting_character_in_file:]
input_text = input_text[:number_of_characters_to_output]

if program_key < 1 or program_key > 25:
    print("\nYour key must be an integer between 1 and 25!")
    exit(0)

elif args.encode:
    output_file = open(output_file_name, "w", encoding="utf8")
    output_file.write(cipher("e", input_text, program_key))
    output_file.close()
    if args.print_to_screen:
        output_file = open(output_file_name, "r", encoding="utf8")
        output_text = output_file.read()
        output_file.close()
        if len(output_text) > 1000:
            print("\nRemember, when running this program you can use the -s and -n commands to set a start point and "
                  "max number of characters to output respectively")
            print_text = input("\nYour text is more than 1000 characters, are you sure you want to print to "
                               "console? (Y/N): ")
            while print_text.upper() != "Y" and print_text.upper() != "N":
                print_text = input("\nPlease enter 'Y' or 'N': ")
            if print_text.upper() == "Y":
                print("\n", output_text)

            else:
                exit(0)

elif args.decode:
    output_file = open(output_file_name, "w", encoding="utf8")
    output_file.write(cipher("d", input_text, program_key))
    output_file.close()
    if args.print_to_screen:
        output_file = open(output_file_name, "r", encoding="utf8")
        output_text = output_file.read()
        output_file.close()
        if len(output_text) > 1000:
            print("\nRemember, when running this program you can use the -s and -n commands to set a start point and "
                  "max number of characters to output respectively")
            print_text = input("\nYour text is more than 1000 characters, are you sure you want to print to "
                               "console? (Y/N): ")
            while print_text.upper() != "Y" and print_text.upper() != "N":
                print_text = input("\nPlease enter 'Y' or 'N': ")
            if print_text.upper() == "Y":
                print("\n", output_text)

            else:
                exit(0)


elif args.text_length:
    print("\nyour text file contains", len(input_text), "characters")

else:
    print("\nPlease provide one of the following arguments:")
    print("\n '-e' to encode your text ")
    print("\n '-d' to decode your text")
    print("\n '-l' to show the length of your text")
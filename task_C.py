# DA-108 : Python Programming - Task C
# Write a python program (script) which will remove vowels from user input.

import shutil

terminal_width = shutil.get_terminal_size().columns #linebreak based on terminal width
linebreak = ("━" * terminal_width) # Special Character (Box Drawings Heavy Horizontal - Unicode code point - U+2501)

title = "Task_C - Vowel Vanisher"
padding = (terminal_width - len(title)) // 2 # Calculate padding for centering
centered_title = " " * max(0, padding) + title
print(linebreak)
print(centered_title)
print(linebreak)

while True:
    user_input = input("Type something fun ('q' to quit): ")
    
    if user_input.lower() == 'q':  # if user input either q or Q the program will quit
        print(linebreak)
        print("Goodbye! Hope to see you again soon!")
        print(linebreak)
        break

    if not any(char.isalpha() for char in user_input):  # Check if user input special char or numbers
        print(linebreak)
        print("> Ohh :( this will work on words only... Try Again!")
        print(linebreak)
        continue

    vowels = "aeiouAEIOU"  # vowels in English alphabet
    stripped_string = '' # empty string to cotain the stripped string
    
    for char in user_input:
        if char not in vowels:  # only strip vowels, keep spaces
            stripped_string = stripped_string + char

    print(linebreak)
    print("After the vowel diet :", stripped_string)
    print(linebreak)

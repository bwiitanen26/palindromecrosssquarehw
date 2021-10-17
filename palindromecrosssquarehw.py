#Importing the English Dictionary
import EnglishDictionary

#Main Menu
def print_menu():
    print("Main Menu:")
    print("1. Is it a palindrome?")
    print("2. Is it a crossword square?")
    print("3. Quit.")
    print()

#Get Menu Choice
def get_menu_choice():
    menu_choice = 0
    while not (menu_choice == 1 or menu_choice == 2 or menu_choice == 3):
        menu_choice = int(input("Choose an option:"))
    return menu_choice

#Get Phrase
def get_phrase():
    phrase = ""
    while len(phrase) < 1:
        phrase = str(input("Enter a phrase: "))
    return phrase

#Is palindrome
def is_palindrome(phrase):
    phrase = phrase.lower()
    i = 0
    j = len(phrase) - 1
    while i < j:
        if not phrase[i].isalpha():
            i += 1
        elif not phrase[j].isalpha():
            j -= 1
        else:
            if phrase[i] != phrase[j]:
                return False
            i += 1
            j -= 1
    return True

#Menu check palindrome
def menu_check_palindrome():
    phrase = get_phrase()
    palindrome = is_palindrome(phrase)
    if palindrome == True:
        print('"', phrase, '" is a palindrome!')
        print()
    else:
        print('"', phrase,'" is not a palindrome.')
        print()

#Get Crossword square
def get_crossword_square():
    square = ""
    square_input1 = str(input("Enter the first line of the crossword square: "))
    mag = len(square_input1)
    square += square_input1
    for i in range(1, mag):
        square_input1 = str(input("Enter the next line of the crossword square: "))
        square += square_input1
    return square

#Check Crossword square
def check_crossword_square(square):
    mag = int(len(square) ** (1/2))
    a = 0
    b = mag
    z = 0
    for i in range(0, mag):
        miniword = square[a:b]
        if EnglishDictionary.is_word(miniword) == False:
            return False
        a += mag
        b += mag
    for j in range(0, mag):
        vertslice = ""
        for k in range(z, len(square), mag):
            vertslice = vertslice + square[k]
        if EnglishDictionary.is_word(vertslice) == False:
            return False
        if z < mag:
            z += 1
    return True

#Menu check crossword square
def menu_check_crossword_square():
    square = get_crossword_square()
    is_square = check_crossword_square(square)
    print()
    mag = int(len(square) ** (1/2))
    a = 0
    b = mag
    if is_square == True:
        for i in range(0, mag):
            print(square[a:b])
            a += mag
            b += mag
        print("is a crossword square!")
        print()
    if is_square == False:
        for i in range(0, mag):
            print(square[a:b])
            a += mag
            b += mag
        print("is not a crossword square:(")
        print()

#Main function definition
def main():
    print_menu()
    menu_choice = get_menu_choice()
    if menu_choice == 1:
        menu_check_palindrome()
    elif menu_choice == 2:
        menu_check_crossword_square()
    elif menu_choice == 3:
        return 3

#Declaring variables
menu_choice = 0
mag = 0

#Looping the whole program
while not (menu_choice == 3):
    menu_choice = main()

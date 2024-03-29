
# Created by Oscar Dahlberg for course d009e 2019-09-29 970314-6994


def two_lists():
    word_list = [""]
    definition_list = [""]

    while True:
        menu()
        user_choice = input()
        if user_choice == "1":
            list_insert(word_list, definition_list)
        elif user_choice == "2":
            list_lookup(word_list, definition_list)
        elif user_choice == "3":
            break
        else:
            print("Try again, this time choose a number 1 through 3")


def list_insert(word_list, definition_list):
    user_choice = "1"
    no_dublicate = 0

    while True:
        print("Word to insert: ")
        word = input()
        position = 0
        for duplicate in word_list:
            no_dublicate = 0
            if duplicate == word:
                print("This word already exists, its definiton is: " + definition_list[position])
                while True:
                    print("Want to input another word?")
                    print("1: Yes")
                    print("2: No")
                    user_choice = input()
                    if user_choice == "1" or user_choice == "2":
                        break
                    else:
                        print("Retype please")
                break
            else:
                no_dublicate = "true"
            position += 1
        if user_choice == "2" or no_dublicate == "true":
            break
    if user_choice == "1":
        word_list.append(word)
        print("Description of word: ")
        definition = input()
        definition_list.append(definition)
        print("Word added")


def list_lookup(word_list, definition_list):
    position = 0
    print("Word to lookup: ")
    word_lookup = input()
    for word in word_list:
        if word_lookup == word:
            print("Description for word \"" + word_lookup + "\": " + definition_list[position])
            break
        position += 1
        if position == len(word_list):
            print("Word not found")


def tuple_list():
    list_of_tuples = [("", "")]

    while True:
        menu()
        user_choice = input()
        if user_choice == "1":
            tuple_insert(list_of_tuples)
        elif user_choice == "2":
            tuple_lookup(list_of_tuples)
        elif user_choice == "3":
            break
        else:
            print("Try again, this time choose a number 1 through 3")


def tuple_insert(list_of_tuples):
    user_choice = "1"

    while True:
        print("Word to insert: ")
        word = input()
        position = 0
        while True:
            no_dublicate = 0
            if word == list_of_tuples[position][0]:
                print("This word already exists, its definiton is: " + list_of_tuples[position][1])
                while True:
                    print("Want to input another word?")
                    print("1: Yes")
                    print("2: No")
                    user_choice = input()
                    if user_choice == "1" or user_choice == "2":
                        break
                    else:
                        print("Retype please")
                break
            else:
                no_dublicate = "true"
            if position + 1 == len(list_of_tuples):
                break
            position += 1
        if user_choice == "2" or no_dublicate == "true":
            break
    if user_choice == "1":
        print("Description of word: ")
        definition = input()
        list_of_tuples.append([word, definition])
        print("Word added")


def tuple_lookup(list_of_tuples):
    print("Word to lookup: ")
    word_lookup = input()
    position = 0
    while True:
        if word_lookup == list_of_tuples[position][0]:
            print("Description for word \"" + word_lookup + "\": " + list_of_tuples[position][1])
            break
        position += 1
        if position == len(list_of_tuples):
            print("Word not found")
            break


def dictionary_list():
    dictionary = {"": ""}

    while True:
        menu()
        user_choice = input()
        if user_choice == "1":
            dictionary_insert(dictionary)
        elif user_choice == "2":
            dictionary_lookup(dictionary)
        elif user_choice == "3":
            break
        else:
            print("Try again, this time choose a number 1 through 3")


def dictionary_insert(dictionary):
    user_choice = "1"
    no_dublicate = 0

    while True:
        print("Word to insert: ")
        word = input()
        for duplicate in dictionary:
            no_dublicate = 0
            if duplicate == word:
                print("This word already exists, its definiton is: " + dictionary[word])
                while True:
                    print("Want to input another word?")
                    print("1: Yes")
                    print("2: No")
                    user_choice = input()
                    if user_choice == "1" or user_choice == "2":
                        break
                    else:
                        print("Retype please")
                break
            else:
                no_dublicate = "true"
        if user_choice == "2" or no_dublicate == "true":
            break
    if user_choice == "1":
        print("Description of word: ")
        definition = input()
        dictionary[word] = definition
        print("Word added")


def dictionary_lookup(dictionary):
    print("Word to lookup: ")
    word_lookup = input()
    for key in dictionary:
        if word_lookup == key:
            print("Description for \"" + word_lookup + "\": " + dictionary[key])
            break


def menu():
    print("Menu for dictionary")
    print("1: Insert")
    print("2: Lookup")
    print("3: Exit Program")


while True:
    print("Which type of dictionary do you want to try?")
    print("1: Dictionary made up of two lists")
    print("2: Dictionary made up of a list of pairs of tuples")
    print("3: Dictionary made up of a dictionary")
    print("4: End program")
    user_choice = input()
    if user_choice == "1":
        two_lists()
    elif user_choice == "2":
        tuple_list()
    elif user_choice == "3":
        dictionary_list()
    elif user_choice == "4":
        break
    else:
        print("Try again, this time choose a number 1 through 4")


# Created by Oscar Dahlberg for course d0015e Introduction to programming Labb 3 Uppgift 1b
# Finished 2019-09-11

list_of_tuples = [(["", ""])]
# En lista av tupla par

while True:
    print("Menu for dictionary")
    print("1: Insert")
    print("2: Lookup")
    print("3: Exit Program")
    user_choice = input()
    if user_choice == "3":
        break
    if user_choice == "2":
        print("Word to lookup: ")
        user_input = input()
        m = 0
        while True:
            if user_input == list_of_tuples[m][0]:
                print("Description for " + list_of_tuples[m][0] + ": " + list_of_tuples[m][1] + "\n")
                break
            m += 1
            if m == len(list_of_tuples):
                print("Word not found")
                break
    if user_choice == "1":
        print("Word to insert: ")
        word = input()
        print("Description of word: ")
        definition = input()
        list_of_tuples.append([word, definition])
        print("Word added")

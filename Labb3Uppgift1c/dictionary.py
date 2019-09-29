
# Created by Oscar Dahlberg for course D009e 2019-09-29 970314-6994

dictionary = {}

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
        for key in dictionary:
            if user_input == key:
                print("Description for " + user_input + ": " + dictionary[key] + "\n")
                break
        if m == 1:
            print("Word not found")
    if user_choice == "1":
        print("Word to insert: ")
        word = input()
        print("Description of word: ")
        description = input()
        dictionary[word] = description
        print(dictionary[word])
        print("Word added")

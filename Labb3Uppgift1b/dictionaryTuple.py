
# Created by Oscar Dahlberg for course d0015e Introduction to programming Labb 3 Uppgift 1b
# Finished 2019-09-11

with open("ordlista1.txt", "a+") as f:
    f.seek(0)
    list_of_tuples_of_words = [(["", ""])]
    # En lista av tupla par

    position_ord = 0
    # Vilken position programmet är på för ordet
    position_definition = 0
    # Vilken position programmet är på för defintionen för ordet
    position_rad = 0
    # Vilken rad programmet är på

    while True:
        temporary = (["", ""], 1)
        en_rad = str(f.readlines()[position_rad])
        f.seek(0)
        while True:
            if en_rad[position_ord] == " ":
                position_definition = position_ord
                while True:
                    if en_rad[position_definition + 1] == "1":
                        break
                    temporary[0][1] += en_rad[position_definition + 1]
                    position_definition += 1
                break
            temporary[0][0] += en_rad[position_ord]
            position_ord += 1
        list_of_tuples_of_words[position_rad] = temporary[0]
        if len(f.readlines()) == position_rad + 1:
            break
        list_of_tuples_of_words.append("")
        f.seek(0)
        position_rad += 1
        position_ord = 0

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

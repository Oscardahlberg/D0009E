with open("ordlista2.txt", "a+") as f:
    f.seek(0)
    dictionary = {}

    position_ord = 0
    # Vilken position programmet är på för ordet
    position_definition = 0
    # Vilken position programmet är på för defintionen för ordet
    position_rad = 0
    # Vilken rad programmet är på

    while True:
        word_from_list = ""
        en_rad = str(f.readlines()[position_rad])
        f.seek(0)
        while True:
            if en_rad[position_ord] == " ":
                position_definition = position_ord
                definition = ""
                while True:
                    if en_rad[position_definition + 1] == "1":
                        dictionary[word_from_list] = definition
                        break
                    definition += en_rad[position_definition + 1]
                    position_definition += 1
                break
            word_from_list += en_rad[position_ord]
            position_ord += 1
        if len(f.readlines()) == position_rad + 1:
            break
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
            for key in dictionary:
                if user_input == key:
                    print("Description for " + user_input + ": " + dictionary[key] + "\n")
                    break
            if m == 1:
                print("Word not found pepehands")
        if user_choice == "1":
            print("Word to insert: ")
            nytt_ord = input()
            print("Description of word: ")
            ny_beskrivning = input()
            dictionary[nytt_ord] = ny_beskrivning
            print(dictionary[nytt_ord])
            f.write("\n" + nytt_ord + " " + ny_beskrivning + "1")
            print("Word added, type '3' to save the word for future use")

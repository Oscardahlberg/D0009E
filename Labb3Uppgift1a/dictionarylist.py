
# Created by Oscar Dahlberg for course d0015e Introduction to programming Labb 3 Uppgift 1a
# Finished 2019-09-10

with open("ordlista.txt", "a+") as f:
    f.seek(0)

    ord_lista = [0]
    ord_lista[0] = ""
    # En lista av alla ord

    ord_definition = [0]
    ord_definition[0] = ""
    # En lista av alla definitioner

    position_ord = 0
    # Vilken position programmet är på för ordet
    position_defintion = 0
    # Vilken position programmet är på för defintionen för ordet
    position_rad = 0
    # Vilken rad programmet är på
    
    while True:
        ett_ord = f.readlines()[position_rad]
        position_ord = 0
        while True:
            if ett_ord[position_ord] == " ":
                p = position_ord
                while True:
                    if ett_ord[position_ord + 1] == "1":
                        position_defintion += 1
                        break
                    ord_definition[position_defintion] = ord_definition[position_defintion] + ett_ord[position_ord + 1]
                    position_ord += 1
                position_ord = p
                f.seek(0)
                if len(ord_definition) == len(f.readlines()):
                    break
                ord_definition.append("")
                break
            else:
                ord_lista[position_rad] = ord_lista[position_rad] + ett_ord[position_ord]
            position_ord += 1
        position_rad += 1
        f.seek(0)
        if len(f.readlines()) == position_rad:
            break
        f.seek(0)
        ord_lista.append("")

    while True:
        print("Menu for dictionary")
        print("1: Insert")
        print("2: Lookup")
        print("3: Exit Program")
        user_choice = input()
        if user_choice == "end":
            break
        m = 0
        if user_choice == "2":
            print("Word to lookup: ")
            user_input = input()
            while True:
                if user_input == ord_lista[m]:
                    print("Description for " + user_input + ": " + ord_definition[m] + "\n")
                    break
                m += 1
                if m == len(ord_lista):
                    print("Word not found pepehands")
                    break
        if user_choice == "1":
            print("Word to insert: ")
            nytt_ord = input()
            ord_lista.append(nytt_ord)
            print("Description of word: ")
            ny_definition = input()
            ord_definition.append(ny_definition)
            f.write("\n" + nytt_ord + " " + ny_definition + "1")
            print("Word added, type '3' to save the word for future use")
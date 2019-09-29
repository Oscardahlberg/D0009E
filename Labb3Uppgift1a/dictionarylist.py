
# Created by Oscar Dahlberg for course D009e 2019-09-29 970314-6994

ord_lista = [0]
ord_lista[0] = ""
# Definierar en lista av alla ord

ord_definition = [0]
ord_definition[0] = ""
# Definierar en lista av alla definitioner

while True:
    print("Menu for dictionary")
    print("1: Insert")
    print("2: Lookup")
    print("3: Exit Program")
    user_choice = input()
    if user_choice == "3":
        break
    m = 0
    if user_choice == "2":
        print("Word to lookup: ")
        user_input = input()
        while True:
            if user_input == ord_lista[m]:
                print("Description for word '" + user_input + "': " + ord_definition[m] + "\n")
                break
            m += 1
            if m == len(ord_lista):
                print("Word not found")
                break
    if user_choice == "1":
        print("Word to insert: ")
        nytt_ord = input()
        ord_lista.append(nytt_ord)
        print("Description of word: ")
        ny_definition = input()
        ord_definition.append(ny_definition)
        print("Word added")


# =========================================================
# Writen by Oscar Dahlberg for course D009E at 2019-10-07

# This program is a telephone book where the user can
# add, change, create aliases and lookup names from a list
# The list can be saved with the command "save" where it will
# be saved onto a file in the directory named "telefon_bok"
# If no such file exists, it will create one

# A more complete command sheet exists on Github
# =========================================================


def int_check(symbol):
    # This function checks that "symbol" contain any integers, and will return True if it does.
    # otherwise it will return False

    try:
        int(symbol)
        return True
    except ValueError:
        return False


class Telefonbok:
    def __init__(self):
        # Creates the necesary variables for the program and starts the main function "loop"

        self.on = True
        self.telefonbok = []
        self.user_input = ""
        self.word1 = ""
        self.word2 = ""
        self.word3 = ""
        self.word_max = 0
        self.word_min = 0
        self.word_count = 0
        self.double_str = False
        self.name_counter = 0
        self.length = 0
        self.position = 0
        self.word_already_exists = False

        self.loop()

    def loop(self):
        # Main loop of this program, will run until bolean variable "on" is False

        while self.on:
            self.set_user_input()
            self.menu()
            self.reset_words()
            print(self.telefonbok)

    def reset_words(self):
        # Resets user input
        # This function will be run every cycle to make sure that the strings are empty once they are used again

        self.word1 = ""
        self.word2 = ""
        self.word3 = ""

    def set_user_input(self):
        # Reads user input and creates the correct prompt

        self.user_input = input("telebok> ")

    def correct_user_input(self, position):
        # Removes the words "add " or "change " from the input so that the input can be further proccessed
        # Amount of strings removed from user_input is based on the intager "position"

        self.user_input = self.user_input[position:]

    def lookup_number_bolean(self):
        # Looks in main list to see if the number "word2" exists
        # It has already been checked so that "word2" is always a number going into this function

        for line in self.telefonbok:
            number = ""
            for symbol in line:
                number += symbol
                if symbol == ";":
                    number = number[:-1]
                    break
            if number == self.word2:
                return True
        return False

    def lookup_name_counter(self):
        # This function has mutiple uses
        # 1. Checks if a word the the user has input already exists in the list
        # 2. Checks how many times a word exists in the list
        # 3. Checks the position of where a word already exists
        # This is so that the function can be used for a multiple of uses
        # instead of having one function for each use

        self.position = 0
        self.length = 0
        self.name_counter = 0
        self.word_already_exists = False

        for line in self.telefonbok:   # For every index in telefonbok
            name = ""
            number = ""
            for symbol in line:  # For every string in index

                if int_check(symbol):  # Reads number from index
                    number += symbol
                if not int_check(symbol) and not symbol == ";":   # Reads names from index
                    name += symbol

                if symbol == ";":  # When a name has been read from the index
                    if self.word_count == 3:  # If the user input has three words
                        if number == self.word2:
                            if name == self.word1:
                                self.word_already_exists = True
                            if name == self.word3:
                                self.name_counter += 1
                            self.position = self.length

                    else:  # If the user input has two words
                        if name == self.word1:
                            self.name_counter += 1
                            self.position = self.length

                    name = ""
            self.length += 1

    def lookup_length(self):
        # Checks how many names exists at the index "position" in the list

        name_counter = -1

        for symbol in self.telefonbok[self.position]:
            if symbol == ";":
                name_counter += 1

        return name_counter

    def lookup_alias(self):
        # Checks if a alias already exists in the list

        name = ""

        for symbol in self.telefonbok[self.position]:
            if not int_check(symbol) and not symbol == ";":
                name += symbol
            if symbol == ";":
                if name == self.word2:
                    self.word_already_exists = True
                name = ""

        return self.word_already_exists

    def add_fix(self):
        # When adding a word, the two words will be a string and a number and the maximum
        # amount of words allowed will be 2
        # This is all to make sure that the user input is correctly formated

        self.double_str = False
        self.word_max = 2
        self.word_min = 2
        self.correct_user_input(4)
        self.seperate()
        if self.input_check():
            return True

    def lookup_fix(self):
        # Makes sure that the user input is correctly formated for the "lookup" function

        self.double_str = False
        self.word_max = 1
        self.word_min = 1
        self.correct_user_input(7)
        self.seperate()
        if self.input_check():
            return True

    def alias_change_fix(self, length):
        # Makes sure that the user input is correctly formated for the "alias" and "change" function

        self.double_str = False
        self.word_max = 3
        self.word_min = 2
        self.correct_user_input(length)
        self.seperate()
        if self.word_count == 2:
            self.double_str = True
        if self.input_check():
            return True

    def remove_fix(self):
        # Makes sure that the user input is correctly formated for the "remove" function

        self.double_str = False
        self.word_max = 2
        self.word_min = 1
        self.correct_user_input(7)
        self.seperate()
        if self.input_check():
            return True

    def menu(self):
        # Checks the user input for the first couple of strings and then decides which function to run

        if self.user_input[:3] == "add":
            self.add()

        elif self.user_input[:6] == "lookup":
            self.lookup()

        elif self.user_input[:5] == "alias":
            self.alias()

        elif self.user_input[:6] == "change":
            self.change()

        elif self.user_input[:6] == "remove":
            self.remove()

        elif self.user_input[:4] == "save":
            self.save()

        elif self.user_input[:4] == "load":
            self.load()

        elif self.user_input[:4] == "quit":
            self.quit()

        else:
            print("Wrong format used")

    def input_check(self):
        # Checks the input for the correct amount of words and numbers
        # Meaning the input is correctly formated

        if not self.word_max >= self.word_count >= self.word_min:
            print("Wrong format used")
            return False

        for symbol in self.word1:
            if int_check(symbol):
                print("Wrong format used")
                return False

        if self.word_count == 3:
            for symbol in self.word2:
                if not int_check(symbol):
                    print("Wrong format used")
                    return False

        if self.word_count == 2:
            for symbol in self.word2:
                if self.double_str:
                    if int_check(symbol):
                        print("Wrong format used")
                        return False
                else:
                    if not int_check(symbol):
                        print("Wrong format used")
                        return False

        if self.word_count == 3:
            for symbol in self.word3:
                if int_check(symbol):
                    print("Wrong format used")
                    return False

        if self.word_count == 2 or self.word_count == 3:
            if self.word1 == self.word2 or self.word1 == self.word3:
                print("Name is already in list")
                return False

        return True

    def seperate(self):
        # This function will seperate the words into three parts which will get further proccessed later on

        self.word_count = 1
        for symbol in self.user_input:
            if self.word_count == 1:
                self.word1 += symbol
            if self.word_count == 2:
                self.word2 += symbol
            if self.word_count == 3:
                self.word3 += symbol
            if symbol == " ":
                self.word_count += 1

        self.word1 = self.word1.replace(" ", "")
        self.word2 = self.word2.replace(" ", "")

    def add(self):
        # Adds the inputed name and number into the list while checking so that the
        # word does not already exist

        if not self.add_fix():
            return

        if self.lookup_number_bolean():
            print("This number is already listed")
        else:
            self.telefonbok.append(self.word2 + ";" + self.word1 + ";")

    def lookup(self):
        # Lookups the numbers correlating with the inputed name

        if not self.lookup_fix():
            return

        length = 0
        bolean = False

        for line in self.telefonbok:
            name = ""
            number = ""
            for symbol in line:
                if symbol == "\\":
                    break
                if int_check(symbol) and not symbol == ";":
                    number += symbol
                if symbol == ";":
                    bolean = True
                if not int_check(symbol) and not symbol == ";":
                    if bolean:
                        name = ""
                        bolean = False
                    name += symbol
                    if name == self.word1:
                        print(number)
            if len(self.telefonbok) == length:
                print("No number found")
            length += 1

    def alias(self):
        # Adds a alias of a name with the same number to the list
        # If there are mutiple numbers with the same name it will send out a error message
        # asking for a number

        if not self.alias_change_fix(6):
            return

        self.lookup_name_counter()

        if self.word_count == 3:
            if self.word_already_exists:
                if self.name_counter == 0:
                    self.telefonbok[self.position] += self.word3 + ";"
                else:
                    print("Name is already in list")
            else:
                print("Name not in list")

        if self.word_count == 2:
            if not self.lookup_alias():
                if self.name_counter == 1:
                    self.telefonbok[self.position] += self.word2 + ";"
                else:
                    print("Multiple names found, please specifiy with number")
            else:
                print("Name is already in list")

    def change(self):
        # Changes a specified name with a new name
        # If there are mutiple numbers with the same name it will send out a error message
        # asking for a number

        if not self.alias_change_fix(7):
            return

        self.lookup_name_counter()

        if self.word_count == 3:
            if self.word_already_exists:
                if self.name_counter == 1:
                    print("Name already in list")
                else:
                    self.telefonbok[self.position] = self.telefonbok[self.position].replace(self.word1, self.word3)
            else:
                print("Name not in list")

        if self.word_count == 2:
            if self.lookup_alias():
                print("Name already in list")
            else:
                if self.name_counter == 1:
                    self.telefonbok[self.position] = self.telefonbok[self.position].replace(self.word1, self.word2)
                else:
                    print("Multiple names found, please specifiy with number")

    def remove(self):
        # Removes specified name
        # If there are mutiple numbers with the same name it will send out a error message
        # asking for a number
        # If there is only one name with a number it will remove both of them from the list

        if not self.remove_fix():
            return

        if self.word_count == 1:
            self.word_count = 2
        else:
            self.word_count = 3

        self.lookup_name_counter()

        if self.word_count == 3:
            if self.word_already_exists:
                if self.lookup_length() == 1:
                    self.telefonbok.pop(self.position)
                else:
                    self.telefonbok[self.position] = self.telefonbok[self.position].replace(";" + self.word1, "")
            else:
                print("Name not in list")

        if self.word_count == 2:
            if self.name_counter == 0:
                print("Name not in list")
            elif self.name_counter == 1:
                if self.lookup_length() == 1:
                    self.telefonbok.pop(self.position)
                else:
                    self.telefonbok[self.position] = self.telefonbok[self.position].replace(";" + self.word1, "")
            else:
                print("Multiple names found, please specifiy with number")

    def save(self):
        # Saves the list onto a txt file in the directory with the name telefon_bok
        # If no such list exists it will create one and save the list onto it

        file = open("telefon_bok", "w")
        for line in self.telefonbok:
            file.write(line + "\n")
        file.close()

    def load(self):
        # Loads a file in the directory named telefon_bok and creates a list
        # from the information in every line
        # If no such file exists it will print out an error

        self.telefonbok = []

        try:
            file = open("telefon_bok", "r")
            for line in file:
                self.telefonbok.append(line.replace("\n", ""))
            file.close()
        except FileNotFoundError:
            print("Text file with name telefon_bok not found")

    def quit(self):
        # Quits the program

        self.on = False


x = Telefonbok()

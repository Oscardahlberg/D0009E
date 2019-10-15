
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
    # This function checks that 'symbol' contain any integers, and will return True if it does.
    # otherwise it will return False

    try:
        int(symbol)
        return True
    except ValueError:
        return False


class Telefonbok:
    def __init__(self):
        # Creates the necesary variables for the program and starts the main function 'loop'

        self.on = True
        self.telefonbok = []

        self.user_input = ""
        self.word1 = ""
        self.word2 = ""
        self.word3 = ""

        self.word_max = 0
        self.word_min = 0

        self.word_count = 0
        self.name_counter = 0
        self.number = 0
        self.position = 0

        self.double_str = False
        self.double_int = False
        self.word_already_exists = False

        self.loop()

    def loop(self):
        # Main loop of this program, will run until bolean variable 'on' is False

        while self.on:
            self.set_user_input()
            self.menu()
            print(self.telefonbok)

    def set_user_input(self):
        # Reads user input and creates the correct prompt

        self.user_input = input("telebok> ")

    def correct_user_input(self, position):
        # Removes the words 'add ' or 'change ' from the input so that the input can be further processed

        self.user_input = self.user_input[position:]

    def lookup_number_bolean(self, number_lookup):
        # Looks in main list to see if the number 'word2' exists
        # It has already been checked so that 'word2' is always a number going into this function

        for line in self.telefonbok:
            number = ""
            for symbol in line:

                number += symbol
                if symbol == ";":
                    number = number[:-1]
                    break
            if number == number_lookup:
                return True
        return False

    def lookup_name_counter(self):
        # This function has mutiple uses
        # 1. Checks if a name or number the user wants changed or added already exists in the list
        # 2. Remembers the index for a specific name and number in the list so that it can be changed or removed

        length = 0
        self.position = 0
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
                                self.number = number
                                self.word_already_exists = True
                            if name == self.word3:
                                self.name_counter += 1
                            self.position = length

                    else:  # If the user input has two words
                        if name == self.word1:
                            self.name_counter += 1
                            self.number = number
                            self.position = length

                    name = ""
            length += 1

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
        # Makes sure that the user input is correctly formated for the 'add' function

        self.double_str = False

        self.word_max = 2
        self.word_min = 2

        self.correct_user_input(4)
        self.seperate()

        if self.input_check():
            return True
        return False

    def lookup_fix(self):
        # Makes sure that the user input is correctly formated for the 'lookup' function

        self.double_str = False
        self.word_max = 1
        self.word_min = 1

        self.correct_user_input(7)
        self.seperate()

        if self.input_check():
            return True
        return False

    def alias_fix(self):
        # Makes sure that the user input is correctly formated for the "alias" function

        self.double_int = False
        self.double_str = False

        self.word_max = 3
        self.word_min = 2

        self.correct_user_input(6)
        self.seperate()

        if self.word_count == 2:
            self.double_str = True
        if self.input_check():
            return True
        return False

    def change_fix(self):
        # Makes sure that the user input is correctly formated for the "change" function

        self.double_str = False
        self.double_int = False

        self.word_max = 3
        self.word_min = 2

        self.correct_user_input(7)
        self.seperate()

        if self.word_count == 3:
            self.double_int = True

        if self.input_check():
            return True
        return False

    def remove_fix(self):
        # Makes sure that the user input is correctly formated for the "remove" function

        self.double_str = False

        self.word_max = 2
        self.word_min = 1

        self.correct_user_input(7)
        self.seperate()
        if self.input_check():
            return True
        return False

    def input_check(self):
        # Checks the user input so that it is correctly formated
        # Checks so that the names does not contain any numbers and the numbers
        # does not contain any letters

        if not self.word_max >= self.word_count >= self.word_min:
            print("Wrong format used")
            return False

        for symbol in self.word1:
            if int_check(symbol):
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
            for symbol in self.word2:
                if not int_check(symbol):
                    print("Wrong format used")
                    return False
            for symbol in self.word3:
                if self.double_int:
                    if not int_check(symbol):
                        print("Wrong format used")
                        return False
                else:
                    if int_check(symbol):
                        print("Wrong format used")
                        return False

        if self.word1 == self.word2 or self.word1 == self.word3:
            print("Name is already in list")
            return False

        return True

    def seperate(self):
        # Seperates the words into three individual
        # parts to get futher processed

        self.word_count = 1

        self.word1 = ""
        self.word2 = ""
        self.word3 = ""

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

    def menu(self):

        if self.user_input[:3] == "add":
            self.add()

        elif self.user_input[:6] == "lookup":
            if len(self.telefonbok) == 0:
                print("Telefonbok is empty")
                return
            self.lookup()

        elif self.user_input[:5] == "alias":
            if len(self.telefonbok) == 0:
                print("Telefonbok is empty")
                return
            self.alias()

        elif self.user_input[:6] == "change":
            if len(self.telefonbok) == 0:
                print("Telefonbok is empty")
                return
            self.change()

        elif self.user_input[:6] == "remove":
            if len(self.telefonbok) == 0:
                print("Telefonbok is empty")
                return
            self.remove()

        elif self.user_input[:4] == "save":
            if len(self.telefonbok) == 0:
                print("Telefonbok is empty")
                return
            self.save()

        elif self.user_input[:4] == "load":
            self.load()

        elif self.user_input[:4] == "quit":
            self.quit()

        else:
            print("Wrong format used")

    def add(self):
        # Adds the inputed name and number into the list while checking so that the
        # number is not already registered

        if not self.add_fix():
            return

        if self.lookup_number_bolean(self.word2):
            print("This number is already listed")
        else:
            self.telefonbok.append(self.word2 + ";" + self.word1 + ";")

    def lookup(self):
        # Look up the number(s) correlating with the inputed name

        if not self.lookup_fix():
            return

        word = False
        not_in_list = False

        for line in self.telefonbok:
            name = ""
            number = ""
            for symbol in line:

                if symbol == "\\":
                    break
                if int_check(symbol) and not symbol == ";":
                    number += symbol
                if symbol == ";":
                    word = True
                if not int_check(symbol) and not symbol == ";":

                    if word:
                        name = ""
                        word = False
                    name += symbol
                    if name == self.word1:
                        print(number)
                        not_in_list = True

        if not not_in_list:
            print("Name not in list")

    def alias(self):
        # Adds a alias of a name with the same number to the list
        # If there are mutiple numbers with the same name it will send out a error message
        # asking for a number

        if not self.alias_fix():
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
                if self.name_counter == 0:
                    print("Name not in list")
                elif self.name_counter == 1:
                    self.telefonbok[self.position] += self.word2 + ";"
                else:
                    print("Multiple names found, please specifiy with number")
            else:
                print("Name is already in list")

    def change(self):
        # Changes number correlating with given name and all it's aliases
        # into a new number
        # If there are multiple names it will ask for the specified names number aswell

        if not self.change_fix():
            return

        self.lookup_name_counter()

        if self.word_count == 3:
            if self.word_already_exists:
                if not self.lookup_number_bolean(self.word3):
                    self.telefonbok[self.position] = self.telefonbok[self.position].replace(self.number, self.word3)
                else:
                    print("Number already exists in list")
            else:
                print("Name not in list")

        if self.word_count == 2:
            if self.name_counter == 1:
                if not self.lookup_number_bolean(self.word2):
                    self.telefonbok[self.position] = self.telefonbok[self.position].replace(self.number, self.word2)
                else:
                    print("Number already exists in list")
            elif self.name_counter == 0:
                print("Name not in list")
            else:
                print("Multiple names exist, specify with number")

    def remove(self):
        # Removes specified name
        # If there are mutiple numbers with the same name it will send out a error message
        # asking for the number correlating with name

        if not self.remove_fix():
            return

        if self.word_count == 1:
            self.word_count = 2
        else:
            self.word_count = 3

        self.lookup_name_counter()

        if self.word_count == 3:
            if self.word_already_exists:
                self.telefonbok.pop(self.position)
            else:
                print("Name not in list")

        if self.word_count == 2:
            if self.name_counter == 0:
                print("Name not in list")
            elif self.name_counter == 1:
                self.telefonbok.pop(self.position)
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
            print("Text file with name \'telefon_bok\' not found")

    def quit(self):
        self.on = False


x = Telefonbok()

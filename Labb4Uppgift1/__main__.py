def int_check(symbol):
    # Checks if 'symbol' can be converted into a int or not

    try:
        int(symbol)
        return True
    except ValueError:
        return False


class Telefonbok:
    def __init__(self):

        self.telefonbok = {}

        self.user_input = ""
        self.word1 = ""
        self.word2 = ""

        self.on = True
        self.one_word = False

        self.number = 0
        self.word_count = 1

        self.loop()

    def loop(self):
        # Main loop of this program, runs until 'self.on' is false

        while self.on:
            self.set_user_input()
            self.menu()
            # print(self.telefonbok)

    def set_user_input(self):
        self.user_input = input("telebok> ")

    def correct_user_input(self, position):
        # Removes the 'add ' or 'change ' part from the user input
        # So that the information can be further processed

        self.user_input = self.user_input[position:]
        self.seperate()

    def seperate(self):
        # Seperates the user input into two words

        self.word1 = ""
        self.word2 = ""
        self.word_count = 1

        for symbol in self.user_input:
            if self.word_count == 1:
                self.word1 += symbol
            if self.word_count == 2:
                self.word2 += symbol
            if symbol == " ":
                self.word_count += 1

        self.word1 = self.word1.replace(" ", "")

    def input_check(self, double_str):
        # Checks so that the user input is correctly formated

        for symbol in self.word2:

            if double_str:
                if int_check(symbol):
                    print("Wrong format used")
                    return False
            else:
                if not int_check(symbol):
                    print("Wrong format used")
                    return False

        for symbol in self.word1:
            if int_check(symbol):
                print("Wrong format used")
                return False

        return True

    def lookup_name_bolean(self):
        # Looks up 'self.word1' in the dictionary

        for name in self.telefonbok:
            if name == self.word1:
                return True

        return False

    def lookup_number_bolean(self):
        # Looks up 'self.word2' in the dictionary

        for key in self.telefonbok:
            if self.telefonbok[key] == self.word2:
                return True

        return False

    def add(self):
        # Adds the name 'self.word1' with the number 'self.word2' into the dictionary

        self.correct_user_input(4)
        if not self.input_check(False):
            return

        if self.lookup_name_bolean():
            print("Name is already in list")
        elif self.lookup_number_bolean():
            print("Number is already in list")
        else:
            self.telefonbok[self.word1] = self.word2

    def lookup(self):
        # Looks up the number correlating with the name 'self.word1'

        self.correct_user_input(7)
        if not self.input_check(True):
            return

        if self.lookup_name_bolean():
            print(self.telefonbok[self.word1])
        else:
            print("Name is not listed")

    def alias(self):
        # Makes a alias with the name 'self.word2'
        # It will have the same number as 'self.word1'

        self.correct_user_input(6)
        if not self.input_check(True):
            return

        if self.word1 == self.word2:
            print("Name is already in list")
            return

        if self.lookup_name_bolean():
            self.telefonbok[self.word2] = self.telefonbok[self.word1]
        else:
            print("Name is not listed")

    def change(self):
        # Changes the number of 'self.word1' into 'self.word2'

        self.correct_user_input(7)
        if not self.input_check(False):
            return

        number = ""

        if self.lookup_name_bolean():
            if not self.lookup_number_bolean():
                for key in self.telefonbok:
                    if key == self.word1:
                        number = self.telefonbok[key]
            else:
                print("Number is already in list")
        else:
            print("Name is not listed")

        for key in self.telefonbok:
            if self.telefonbok[key] == number:
                self.telefonbok[key] = self.word2

    def save(self):
        # Saves the dictionary into a txt file with the name 'telefon_bok'
        # If no such file exists it will create one

        file = open("telefon_bok", "w")
        for key in self.telefonbok:
            name = key
            number = self.telefonbok[key]
            file.write(number + ";" + name + "\n")
        file.close()

    def load(self):
        # Clears the current dictionary and reads a new list from a txt file named
        # 'telefon_bok', will only work if such a file exists

        dict.clear(self.telefonbok)

        self.word_count = 1
        self.word1 = ""
        self.word2 = ""

        try:
            file = open("telefon_bok", "r")
            file.close()
            for line in file:
                for symbol in line:
                    if symbol == "\\":  # To skip newline
                        break
                    if self.word_count == 1:
                        self.word1 += symbol
                    if self.word_count == 2:
                        self.word2 += symbol
                    if symbol == ";":
                        self.word_count += 1
                self.telefonbok[str(self.word1)] = self.word2
        except FileNotFoundError:
            print("Text file with name 'telefon_bok' not found")

    def quit(self):
        self.on = False

    def menu(self):

        if self.user_input[:3] == "add":
            self.add()

        elif self.user_input[:6] == "lookup":
            self.lookup()

        elif self.user_input[:5] == "alias":
            self.alias()

        elif self.user_input[:6] == "change":
            self.change()

        elif self.user_input[:4] == "save":
            self.save()

        elif self.user_input[:4] == "load":
            self.load()

        elif self.user_input[:4] == "quit":
            self.quit()

        else:
            print("Wrong format used")


x = Telefonbok()

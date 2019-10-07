
def int_check(symbol):
    try:
        int(symbol)
        return True
    except ValueError:
        return False


class Telefonbok:
    def __init__(self):
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
        self.name_check = False

    def reset_word2(self):
        self.word2 = ""

    def loop(self):
        self.set_user_input()
        self.menu()
        self.reset_words()
        print(self.telefonbok)

    def reset_words(self):
        self.word1 = ""
        self.word2 = ""
        self.word3 = ""

    def set_user_input(self):
        self.user_input = input("telebok> ")

    def correct_user_input(self, position):
        self.user_input = self.user_input[position:]

    def get_on(self):
        return self.on

    def lookup_number_bolean(self):
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
        self.position = 0
        self.length = 0
        self.name_counter = 0
        self.word_already_exists = False
        self.name_check = False

        for line in self.telefonbok:
            name = ""
            number = ""
            for symbol in line:

                if int_check(symbol) and not symbol == ";":
                    number += symbol
                if symbol == ";":
                    name = ""
                if not int_check(symbol) and not symbol == ";":
                    name += symbol

                    if self.word_count == 3:
                        if number == self.word2:
                            if name == self.word1:
                                self.name_check = True
                            if name == self.word3:
                                self.name_counter += 1
                            self.position = self.length
                    else:
                        if name == self.word1:
                            self.name_counter += 1
                            self.position = self.length
                        if name == self.word2:
                            self.word_already_exists = True

            self.length += 1

    def lookup_length(self):
        name_counter = -1

        for symbol in self.telefonbok[self.position]:
            if symbol == ";":
                name_counter += 1

        return name_counter

    def add_fix(self):
        self.double_str = False
        self.word_max = 2
        self.word_min = 2
        self.correct_user_input(4)
        self.seperate()
        if self.input_check():
            return True

    def lookup_fix(self):
        self.double_str = False
        self.word_max = 1
        self.word_min = 1
        self.correct_user_input(7)
        self.seperate()
        if self.input_check():
            return True

    def alias_change_fix(self, length):
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
        self.double_str = False
        self.word_max = 2
        self.word_min = 1
        self.correct_user_input(7)
        self.seperate()
        if self.input_check():
            return True

    def menu(self):
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

        if not self.add_fix():
            return

        if self.lookup_number_bolean():
            print("This number is already listed")
        else:
            self.telefonbok.append(self.word2 + ";" + self.word1 + ";")

    def lookup(self):

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

        if not self.alias_change_fix(6):
            return

        self.lookup_name_counter()

        if self.word_count == 3:
            if self.name_counter == 0:
                self.telefonbok[self.position] += self.word3 + ";"
            else:
                print("Name is already in list")

        if self.word_count == 2:
            if not self.word_already_exists:
                if self.name_counter == 1:
                    self.telefonbok[self.position] += self.word2 + ";"
                else:
                    print("Multiple names found, please specifiy with number")
            else:
                print("Name is already in list")

    def change(self):

        if not self.alias_change_fix(7):
            return

        self.lookup_name_counter()

        if self.word_count == 3:
            if self.name_check:
                self.telefonbok[self.position] = self.telefonbok[self.position].replace(self.word1, self.word3)
            else:
                print("Name not in list")

        if self.word_count == 2:
            if self.name_counter == 1:
                self.telefonbok[self.position] = self.telefonbok[self.position].replace(self.word1, self.word2)
            else:
                print("Multiple names found, please specifiy with number")

    def remove(self):

        if not self.remove_fix():
            return

        if self.word_count == 1:
            self.word_count = 2
        else:
            self.word_count = 3

        self.lookup_name_counter()

        if self.word_count == 3:
            if self.name_check:
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
        file = open("telefon_bok", "w")
        for line in self.telefonbok:
            file.write(line + "\n")
        file.close()

    def load(self):
        self.telefonbok = []

        try:
            file = open("telefon_bok", "r")
            for line in file:
                self.telefonbok.append(line.replace("\n", ""))
            file.close()
        except FileNotFoundError:
            print("Text file with name telefon_bok not found")

    def quit(self):
        self.on = False


x = Telefonbok()
while x.get_on():
    x.loop()

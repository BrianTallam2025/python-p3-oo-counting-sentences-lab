#!/usr/bin/env python3

class MyString:
    def __init__(self, value=""):
        self._value = ""
        self.value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        if isinstance(value, str):
            self._value = value
        else:
            print("The value must be a string.")

    def is_sentence(self):
        return self._value.endswith(".")

    def is_question(self):
        return self._value.endswith("?")

    def is_exclamation(self):
        return self._value.endswith("!")

    def count_sentences(self):
        end_marks = [".", "?", "!"]
        count = 0
        prev_char = ""
        for char in self._value:
            if char in end_marks and prev_char not in end_marks:
                count += 1
            prev_char = char
        return count

from token import *


class Scanner:
    def __init__(self, script):
        self.script = script
        self.index = -1
        self.current_char = None
        self.next_char()

    def next_char(self):
        self.index += 1
        if self.index <= len(self.script) - 1:
            self.current_char = self.script[self.index]

    def make_tokens(self):
        while self.index <= len(self.script) - 1:
            self.check_token()
            self.next_char()

    def check_token(self):
        ...



from scanner import Scanner


class Kpyn:
    has_error = False

    def __init__(self, file=None):
        if file:
            Kpyn.read_file(file)
        else:
            Kpyn.run_prompt()

    @staticmethod
    def read_file(file):
        ...

    @staticmethod
    def run_prompt():
        while True:
            Kpyn.has_error = False

            prompt = input('> ')
            Kpyn.run(prompt)

    @staticmethod
    def run(script):
        scanner = Scanner(script)
        tokens = scanner.make_tokens()

    @staticmethod
    def error(line, message):
        Kpyn.write_error(line, message)

    @staticmethod
    def write_error(line, message):
        print(f'Error on line {line}: {message}')
        Kpyn.has_error = True


if __name__ == "__main__":
    Kpyn()


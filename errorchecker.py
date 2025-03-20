from antlr4.error.ErrorListener import ErrorListener

class CustomErrorListener(ErrorListener):
    def __init__(self):
        super(CustomErrorListener, self).__init__()
        self.errors = []

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        error_msg = f"Błąd składniowy w linii {line}, kolumna {column}: {msg}"
        self.errors.append(error_msg)
        print(error_msg)

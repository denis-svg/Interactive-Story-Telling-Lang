from antlr4.error.ErrorListener import ErrorListener

class NotDeclaredVariable(Exception):
    def __init__(self, var_name, start, line=None) -> None:
        message = f"""Variable {var_name} hasn't been declared, {start.line}:{start.column}"""
        if line is not None:
            message += "\n" + line
            message += "\n" + " " * start.column + start.column * "^"
        super().__init__(message)

class VarValueError(Exception):
    def __init__(self, value, start, line) -> None:
        message = f"""Value not in string or number, {start.line}:{start.column}"""
        message += "\n" + line
        message += "\n" + "  " + (len(line) - 4) * "^"
        super().__init__(message)

class MyErrorParserListener(ErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        raise Exception("ERROR: when parsing line %d column %d: %s\n" % \
                        (line, column, msg))
    
class MyErrorLexerListener(ErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        raise Exception("ERROR: when tokenizing line %d column %d: %s\n" % \
                        (line, column, msg))
    
class CannotPerformMixOperations(Exception):
    def __init__(self, start) -> None:
        message = f"""Cannot perform mixed operations, {start.line}:{start.column}"""
        super().__init__(message)

class NotValidOperationOnString(Exception):
    def __init__(self, op, start) -> None:
        message = f"""Cannot perform {op}, on strings {start.line}:{start.column}"""
        super().__init__(message)
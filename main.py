import sys
from antlr4 import *
from ExprLexer import ExprLexer
from ExprParser import ExprParser
from Interpreter import Interpreter
from errors import MyErrorParserListener, MyErrorLexerListener

def format_code(file_name):
    f = open(file_name, 'r')
    out = ""
    mode = False
    for line in f.readlines():
        if mode:
            out += ".newLine " + line
        else:
            out += line
        if "{" in line:
            mode = True
        if '}' in line:
            mode = False
    f.close()

    return out

def main(argv):
    input_stream = InputStream(format_code(argv[1]))
    
    lexer = ExprLexer(input_stream)
    lexer.removeErrorListeners()
    lexer.addErrorListener(MyErrorLexerListener())

    stream = CommonTokenStream(lexer)
    parser = ExprParser(stream)
    parser.removeErrorListeners()
    parser.addErrorListener(MyErrorParserListener())
    tree = parser.program()

    tj = Interpreter(tree)
    print(tree.toStringTree())
    print(tree.toStringTree(recog=parser))
    print()
    tj.execute()

 
if __name__ == '__main__':
    main(sys.argv)

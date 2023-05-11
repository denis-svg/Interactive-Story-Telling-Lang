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
    choise = False
    for line in f.readlines():
        if "{" in line:
            mode = True
            out += line[0:-1] + '\n'
            continue
        if '}' in line:
            mode = False
        tokens = line.split()
        for token in tokens:
            if "((!" in token:
                choise = True
            if choise and "))" in token:
                choise = False
        
        if mode and not choise:
            out += line[0:-1] + " .newLine" + '\n'
        else:
            out += line
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
    
    #print(tree.toStringTree())
    #print(tree.toStringTree(recog=parser))
    #print()

    tj.execute()

 
if __name__ == '__main__':
    main(sys.argv)

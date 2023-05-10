import sys
from antlr4 import *
from ExprLexer import ExprLexer
from ExprParser import ExprParser
from Interpreter import Interpreter
from errors import MyErrorParserListener, MyErrorLexerListener

def main(argv):
    input_stream = FileStream(argv[1])
    
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

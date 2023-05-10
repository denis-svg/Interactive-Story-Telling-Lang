# Generated from Expr.g4 by ANTLR 4.12.0
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,21,214,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,1,0,5,0,44,8,0,10,0,12,0,47,9,0,1,0,4,0,50,8,0,11,0,12,0,51,
        1,0,1,0,1,1,1,1,1,1,5,1,59,8,1,10,1,12,1,62,9,1,1,1,1,1,1,2,1,2,
        1,2,1,2,1,3,1,3,3,3,72,8,3,1,4,1,4,1,5,1,5,5,5,78,8,5,10,5,12,5,
        81,9,5,1,5,1,5,1,6,1,6,1,6,1,6,1,6,1,6,1,6,3,6,92,8,6,1,7,1,7,1,
        7,1,7,1,7,1,7,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,9,1,9,1,9,1,9,1,
        9,1,9,3,9,114,8,9,1,9,1,9,1,9,1,9,1,9,3,9,121,8,9,1,9,5,9,124,8,
        9,10,9,12,9,127,9,9,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,
        1,10,1,10,1,10,1,10,1,10,3,10,143,8,10,1,10,5,10,146,8,10,10,10,
        12,10,149,9,10,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,3,11,159,
        8,11,1,11,1,11,1,11,1,11,1,11,1,11,5,11,167,8,11,10,11,12,11,170,
        9,11,1,12,1,12,1,12,1,12,1,13,1,13,1,13,1,13,1,13,1,13,1,14,1,14,
        1,14,1,14,1,14,1,15,1,15,1,15,5,15,190,8,15,10,15,12,15,193,9,15,
        1,15,1,15,1,15,1,16,1,16,1,16,1,16,1,17,5,17,203,8,17,10,17,12,17,
        206,9,17,1,18,1,18,1,19,1,19,1,20,1,20,1,20,0,3,18,20,22,21,0,2,
        4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,0,3,1,0,19,
        20,1,0,15,16,1,0,17,18,219,0,45,1,0,0,0,2,55,1,0,0,0,4,65,1,0,0,
        0,6,71,1,0,0,0,8,73,1,0,0,0,10,75,1,0,0,0,12,91,1,0,0,0,14,93,1,
        0,0,0,16,99,1,0,0,0,18,113,1,0,0,0,20,128,1,0,0,0,22,158,1,0,0,0,
        24,171,1,0,0,0,26,175,1,0,0,0,28,181,1,0,0,0,30,186,1,0,0,0,32,197,
        1,0,0,0,34,204,1,0,0,0,36,207,1,0,0,0,38,209,1,0,0,0,40,211,1,0,
        0,0,42,44,3,4,2,0,43,42,1,0,0,0,44,47,1,0,0,0,45,43,1,0,0,0,45,46,
        1,0,0,0,46,49,1,0,0,0,47,45,1,0,0,0,48,50,3,2,1,0,49,48,1,0,0,0,
        50,51,1,0,0,0,51,49,1,0,0,0,51,52,1,0,0,0,52,53,1,0,0,0,53,54,5,
        0,0,1,54,1,1,0,0,0,55,56,5,20,0,0,56,60,5,9,0,0,57,59,3,12,6,0,58,
        57,1,0,0,0,59,62,1,0,0,0,60,58,1,0,0,0,60,61,1,0,0,0,61,63,1,0,0,
        0,62,60,1,0,0,0,63,64,5,10,0,0,64,3,1,0,0,0,65,66,3,38,19,0,66,67,
        5,6,0,0,67,68,3,6,3,0,68,5,1,0,0,0,69,72,3,8,4,0,70,72,3,10,5,0,
        71,69,1,0,0,0,71,70,1,0,0,0,72,7,1,0,0,0,73,74,5,19,0,0,74,9,1,0,
        0,0,75,79,5,11,0,0,76,78,7,0,0,0,77,76,1,0,0,0,78,81,1,0,0,0,79,
        77,1,0,0,0,79,80,1,0,0,0,80,82,1,0,0,0,81,79,1,0,0,0,82,83,5,11,
        0,0,83,11,1,0,0,0,84,92,3,40,20,0,85,92,3,24,12,0,86,92,3,26,13,
        0,87,92,3,28,14,0,88,92,3,30,15,0,89,92,3,14,7,0,90,92,3,16,8,0,
        91,84,1,0,0,0,91,85,1,0,0,0,91,86,1,0,0,0,91,87,1,0,0,0,91,88,1,
        0,0,0,91,89,1,0,0,0,91,90,1,0,0,0,92,13,1,0,0,0,93,94,5,13,0,0,94,
        95,3,38,19,0,95,96,5,6,0,0,96,97,3,22,11,0,97,98,5,14,0,0,98,15,
        1,0,0,0,99,100,5,7,0,0,100,101,5,7,0,0,101,102,5,1,0,0,102,103,3,
        18,9,0,103,104,3,24,12,0,104,105,5,8,0,0,105,106,5,8,0,0,106,17,
        1,0,0,0,107,108,6,9,-1,0,108,109,5,7,0,0,109,110,3,18,9,0,110,111,
        5,8,0,0,111,114,1,0,0,0,112,114,3,20,10,0,113,107,1,0,0,0,113,112,
        1,0,0,0,114,125,1,0,0,0,115,120,10,3,0,0,116,117,5,2,0,0,117,121,
        5,2,0,0,118,119,5,3,0,0,119,121,5,3,0,0,120,116,1,0,0,0,120,118,
        1,0,0,0,121,122,1,0,0,0,122,124,3,18,9,4,123,115,1,0,0,0,124,127,
        1,0,0,0,125,123,1,0,0,0,125,126,1,0,0,0,126,19,1,0,0,0,127,125,1,
        0,0,0,128,129,6,10,-1,0,129,130,3,22,11,0,130,147,1,0,0,0,131,142,
        10,2,0,0,132,143,5,4,0,0,133,143,5,5,0,0,134,135,5,12,0,0,135,143,
        5,6,0,0,136,137,5,6,0,0,137,143,5,6,0,0,138,139,5,4,0,0,139,143,
        5,6,0,0,140,141,5,5,0,0,141,143,5,6,0,0,142,132,1,0,0,0,142,133,
        1,0,0,0,142,134,1,0,0,0,142,136,1,0,0,0,142,138,1,0,0,0,142,140,
        1,0,0,0,143,144,1,0,0,0,144,146,3,20,10,3,145,131,1,0,0,0,146,149,
        1,0,0,0,147,145,1,0,0,0,147,148,1,0,0,0,148,21,1,0,0,0,149,147,1,
        0,0,0,150,151,6,11,-1,0,151,159,3,8,4,0,152,153,5,7,0,0,153,154,
        3,22,11,0,154,155,5,8,0,0,155,159,1,0,0,0,156,159,3,10,5,0,157,159,
        3,38,19,0,158,150,1,0,0,0,158,152,1,0,0,0,158,156,1,0,0,0,158,157,
        1,0,0,0,159,168,1,0,0,0,160,161,10,6,0,0,161,162,7,1,0,0,162,167,
        3,22,11,7,163,164,10,5,0,0,164,165,7,2,0,0,165,167,3,22,11,6,166,
        160,1,0,0,0,166,163,1,0,0,0,167,170,1,0,0,0,168,166,1,0,0,0,168,
        169,1,0,0,0,169,23,1,0,0,0,170,168,1,0,0,0,171,172,5,7,0,0,172,173,
        3,36,18,0,173,174,5,8,0,0,174,25,1,0,0,0,175,176,5,7,0,0,176,177,
        5,7,0,0,177,178,3,38,19,0,178,179,5,8,0,0,179,180,5,8,0,0,180,27,
        1,0,0,0,181,182,5,7,0,0,182,183,5,12,0,0,183,184,3,34,17,0,184,185,
        5,8,0,0,185,29,1,0,0,0,186,187,5,7,0,0,187,191,5,7,0,0,188,190,3,
        32,16,0,189,188,1,0,0,0,190,193,1,0,0,0,191,189,1,0,0,0,191,192,
        1,0,0,0,192,194,1,0,0,0,193,191,1,0,0,0,194,195,5,8,0,0,195,196,
        5,8,0,0,196,31,1,0,0,0,197,198,5,12,0,0,198,199,3,34,17,0,199,200,
        3,24,12,0,200,33,1,0,0,0,201,203,7,0,0,0,202,201,1,0,0,0,203,206,
        1,0,0,0,204,202,1,0,0,0,204,205,1,0,0,0,205,35,1,0,0,0,206,204,1,
        0,0,0,207,208,5,20,0,0,208,37,1,0,0,0,209,210,7,0,0,0,210,39,1,0,
        0,0,211,212,7,0,0,0,212,41,1,0,0,0,16,45,51,60,71,79,91,113,120,
        125,142,147,158,166,168,191,204
    ]

class ExprParser ( Parser ):

    grammarFileName = "Expr.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'?'", "'&'", "'|'", "'>'", "'<'", "'='", 
                     "'('", "')'", "'{'", "'}'", "'\"'", "'!'", "'['", "']'", 
                     "'*'", "'/'", "'-'", "'+'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "EQ", "LPAREN", "RPAREN", 
                      "LCURLY", "RCURLY", "GH", "EXLAM", "L", "R", "MULT", 
                      "DIVIDE", "SUB", "ADD", "INT", "ID", "WS" ]

    RULE_program = 0
    RULE_knot = 1
    RULE_var = 2
    RULE_value = 3
    RULE_int = 4
    RULE_str = 5
    RULE_content = 6
    RULE_var_op = 7
    RULE_if = 8
    RULE_logic_expr = 9
    RULE_bool_expr = 10
    RULE_expr = 11
    RULE_goto = 12
    RULE_print = 13
    RULE_npc = 14
    RULE_choice = 15
    RULE_pair = 16
    RULE_option_text = 17
    RULE_knot_name = 18
    RULE_var_name = 19
    RULE_text = 20

    ruleNames =  [ "program", "knot", "var", "value", "int", "str", "content", 
                   "var_op", "if", "logic_expr", "bool_expr", "expr", "goto", 
                   "print", "npc", "choice", "pair", "option_text", "knot_name", 
                   "var_name", "text" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    EQ=6
    LPAREN=7
    RPAREN=8
    LCURLY=9
    RCURLY=10
    GH=11
    EXLAM=12
    L=13
    R=14
    MULT=15
    DIVIDE=16
    SUB=17
    ADD=18
    INT=19
    ID=20
    WS=21

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.12.0")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(ExprParser.EOF, 0)

        def var(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.VarContext)
            else:
                return self.getTypedRuleContext(ExprParser.VarContext,i)


        def knot(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.KnotContext)
            else:
                return self.getTypedRuleContext(ExprParser.KnotContext,i)


        def getRuleIndex(self):
            return ExprParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)




    def program(self):

        localctx = ExprParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 45
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,0,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 42
                    self.var() 
                self.state = 47
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,0,self._ctx)

            self.state = 49 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 48
                self.knot()
                self.state = 51 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==20):
                    break

            self.state = 53
            self.match(ExprParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class KnotContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(ExprParser.ID, 0)

        def LCURLY(self):
            return self.getToken(ExprParser.LCURLY, 0)

        def RCURLY(self):
            return self.getToken(ExprParser.RCURLY, 0)

        def content(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.ContentContext)
            else:
                return self.getTypedRuleContext(ExprParser.ContentContext,i)


        def getRuleIndex(self):
            return ExprParser.RULE_knot

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterKnot" ):
                listener.enterKnot(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitKnot" ):
                listener.exitKnot(self)




    def knot(self):

        localctx = ExprParser.KnotContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_knot)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 55
            self.match(ExprParser.ID)
            self.state = 56
            self.match(ExprParser.LCURLY)
            self.state = 60
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1581184) != 0):
                self.state = 57
                self.content()
                self.state = 62
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 63
            self.match(ExprParser.RCURLY)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VarContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var_name(self):
            return self.getTypedRuleContext(ExprParser.Var_nameContext,0)


        def EQ(self):
            return self.getToken(ExprParser.EQ, 0)

        def value(self):
            return self.getTypedRuleContext(ExprParser.ValueContext,0)


        def getRuleIndex(self):
            return ExprParser.RULE_var

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVar" ):
                listener.enterVar(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVar" ):
                listener.exitVar(self)




    def var(self):

        localctx = ExprParser.VarContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_var)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 65
            self.var_name()
            self.state = 66
            self.match(ExprParser.EQ)
            self.state = 67
            self.value()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ValueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def int_(self):
            return self.getTypedRuleContext(ExprParser.IntContext,0)


        def str_(self):
            return self.getTypedRuleContext(ExprParser.StrContext,0)


        def getRuleIndex(self):
            return ExprParser.RULE_value

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterValue" ):
                listener.enterValue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitValue" ):
                listener.exitValue(self)




    def value(self):

        localctx = ExprParser.ValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_value)
        try:
            self.state = 71
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [19]:
                self.enterOuterAlt(localctx, 1)
                self.state = 69
                self.int_()
                pass
            elif token in [11]:
                self.enterOuterAlt(localctx, 2)
                self.state = 70
                self.str_()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IntContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(ExprParser.INT, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_int

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInt" ):
                listener.enterInt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInt" ):
                listener.exitInt(self)




    def int_(self):

        localctx = ExprParser.IntContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_int)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 73
            self.match(ExprParser.INT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StrContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def GH(self, i:int=None):
            if i is None:
                return self.getTokens(ExprParser.GH)
            else:
                return self.getToken(ExprParser.GH, i)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(ExprParser.ID)
            else:
                return self.getToken(ExprParser.ID, i)

        def INT(self, i:int=None):
            if i is None:
                return self.getTokens(ExprParser.INT)
            else:
                return self.getToken(ExprParser.INT, i)

        def getRuleIndex(self):
            return ExprParser.RULE_str

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStr" ):
                listener.enterStr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStr" ):
                listener.exitStr(self)




    def str_(self):

        localctx = ExprParser.StrContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_str)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 75
            self.match(ExprParser.GH)
            self.state = 79
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==19 or _la==20:
                self.state = 76
                _la = self._input.LA(1)
                if not(_la==19 or _la==20):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 81
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 82
            self.match(ExprParser.GH)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ContentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def text(self):
            return self.getTypedRuleContext(ExprParser.TextContext,0)


        def goto(self):
            return self.getTypedRuleContext(ExprParser.GotoContext,0)


        def print_(self):
            return self.getTypedRuleContext(ExprParser.PrintContext,0)


        def npc(self):
            return self.getTypedRuleContext(ExprParser.NpcContext,0)


        def choice(self):
            return self.getTypedRuleContext(ExprParser.ChoiceContext,0)


        def var_op(self):
            return self.getTypedRuleContext(ExprParser.Var_opContext,0)


        def if_(self):
            return self.getTypedRuleContext(ExprParser.IfContext,0)


        def getRuleIndex(self):
            return ExprParser.RULE_content

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterContent" ):
                listener.enterContent(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitContent" ):
                listener.exitContent(self)




    def content(self):

        localctx = ExprParser.ContentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_content)
        try:
            self.state = 91
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 84
                self.text()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 85
                self.goto()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 86
                self.print_()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 87
                self.npc()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 88
                self.choice()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 89
                self.var_op()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 90
                self.if_()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_opContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def L(self):
            return self.getToken(ExprParser.L, 0)

        def var_name(self):
            return self.getTypedRuleContext(ExprParser.Var_nameContext,0)


        def EQ(self):
            return self.getToken(ExprParser.EQ, 0)

        def expr(self):
            return self.getTypedRuleContext(ExprParser.ExprContext,0)


        def R(self):
            return self.getToken(ExprParser.R, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_var_op

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVar_op" ):
                listener.enterVar_op(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVar_op" ):
                listener.exitVar_op(self)




    def var_op(self):

        localctx = ExprParser.Var_opContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_var_op)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 93
            self.match(ExprParser.L)
            self.state = 94
            self.var_name()
            self.state = 95
            self.match(ExprParser.EQ)
            self.state = 96
            self.expr(0)
            self.state = 97
            self.match(ExprParser.R)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LPAREN(self, i:int=None):
            if i is None:
                return self.getTokens(ExprParser.LPAREN)
            else:
                return self.getToken(ExprParser.LPAREN, i)

        def logic_expr(self):
            return self.getTypedRuleContext(ExprParser.Logic_exprContext,0)


        def goto(self):
            return self.getTypedRuleContext(ExprParser.GotoContext,0)


        def RPAREN(self, i:int=None):
            if i is None:
                return self.getTokens(ExprParser.RPAREN)
            else:
                return self.getToken(ExprParser.RPAREN, i)

        def getRuleIndex(self):
            return ExprParser.RULE_if

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIf" ):
                listener.enterIf(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIf" ):
                listener.exitIf(self)




    def if_(self):

        localctx = ExprParser.IfContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_if)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 99
            self.match(ExprParser.LPAREN)
            self.state = 100
            self.match(ExprParser.LPAREN)
            self.state = 101
            self.match(ExprParser.T__0)
            self.state = 102
            self.logic_expr(0)
            self.state = 103
            self.goto()
            self.state = 104
            self.match(ExprParser.RPAREN)
            self.state = 105
            self.match(ExprParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Logic_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LPAREN(self):
            return self.getToken(ExprParser.LPAREN, 0)

        def logic_expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.Logic_exprContext)
            else:
                return self.getTypedRuleContext(ExprParser.Logic_exprContext,i)


        def RPAREN(self):
            return self.getToken(ExprParser.RPAREN, 0)

        def bool_expr(self):
            return self.getTypedRuleContext(ExprParser.Bool_exprContext,0)


        def getRuleIndex(self):
            return ExprParser.RULE_logic_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLogic_expr" ):
                listener.enterLogic_expr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLogic_expr" ):
                listener.exitLogic_expr(self)



    def logic_expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ExprParser.Logic_exprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 18
        self.enterRecursionRule(localctx, 18, self.RULE_logic_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 113
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.state = 108
                self.match(ExprParser.LPAREN)
                self.state = 109
                self.logic_expr(0)
                self.state = 110
                self.match(ExprParser.RPAREN)
                pass

            elif la_ == 2:
                self.state = 112
                self.bool_expr(0)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 125
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,8,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ExprParser.Logic_exprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_logic_expr)
                    self.state = 115
                    if not self.precpred(self._ctx, 3):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                    self.state = 120
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [2]:
                        self.state = 116
                        self.match(ExprParser.T__1)
                        self.state = 117
                        self.match(ExprParser.T__1)
                        pass
                    elif token in [3]:
                        self.state = 118
                        self.match(ExprParser.T__2)
                        self.state = 119
                        self.match(ExprParser.T__2)
                        pass
                    else:
                        raise NoViableAltException(self)

                    self.state = 122
                    self.logic_expr(4) 
                self.state = 127
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,8,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Bool_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(ExprParser.ExprContext,0)


        def bool_expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.Bool_exprContext)
            else:
                return self.getTypedRuleContext(ExprParser.Bool_exprContext,i)


        def EXLAM(self):
            return self.getToken(ExprParser.EXLAM, 0)

        def EQ(self, i:int=None):
            if i is None:
                return self.getTokens(ExprParser.EQ)
            else:
                return self.getToken(ExprParser.EQ, i)

        def getRuleIndex(self):
            return ExprParser.RULE_bool_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBool_expr" ):
                listener.enterBool_expr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBool_expr" ):
                listener.exitBool_expr(self)



    def bool_expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ExprParser.Bool_exprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 20
        self.enterRecursionRule(localctx, 20, self.RULE_bool_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 129
            self.expr(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 147
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,10,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ExprParser.Bool_exprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_bool_expr)
                    self.state = 131
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 142
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
                    if la_ == 1:
                        self.state = 132
                        self.match(ExprParser.T__3)
                        pass

                    elif la_ == 2:
                        self.state = 133
                        self.match(ExprParser.T__4)
                        pass

                    elif la_ == 3:
                        self.state = 134
                        self.match(ExprParser.EXLAM)
                        self.state = 135
                        self.match(ExprParser.EQ)
                        pass

                    elif la_ == 4:
                        self.state = 136
                        self.match(ExprParser.EQ)
                        self.state = 137
                        self.match(ExprParser.EQ)
                        pass

                    elif la_ == 5:
                        self.state = 138
                        self.match(ExprParser.T__3)
                        self.state = 139
                        self.match(ExprParser.EQ)
                        pass

                    elif la_ == 6:
                        self.state = 140
                        self.match(ExprParser.T__4)
                        self.state = 141
                        self.match(ExprParser.EQ)
                        pass


                    self.state = 144
                    self.bool_expr(3) 
                self.state = 149
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,10,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def int_(self):
            return self.getTypedRuleContext(ExprParser.IntContext,0)


        def LPAREN(self):
            return self.getToken(ExprParser.LPAREN, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.ExprContext)
            else:
                return self.getTypedRuleContext(ExprParser.ExprContext,i)


        def RPAREN(self):
            return self.getToken(ExprParser.RPAREN, 0)

        def str_(self):
            return self.getTypedRuleContext(ExprParser.StrContext,0)


        def var_name(self):
            return self.getTypedRuleContext(ExprParser.Var_nameContext,0)


        def MULT(self):
            return self.getToken(ExprParser.MULT, 0)

        def DIVIDE(self):
            return self.getToken(ExprParser.DIVIDE, 0)

        def ADD(self):
            return self.getToken(ExprParser.ADD, 0)

        def SUB(self):
            return self.getToken(ExprParser.SUB, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ExprParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 22
        self.enterRecursionRule(localctx, 22, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 158
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.state = 151
                self.int_()
                pass

            elif la_ == 2:
                self.state = 152
                self.match(ExprParser.LPAREN)
                self.state = 153
                self.expr(0)
                self.state = 154
                self.match(ExprParser.RPAREN)
                pass

            elif la_ == 3:
                self.state = 156
                self.str_()
                pass

            elif la_ == 4:
                self.state = 157
                self.var_name()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 168
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,13,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 166
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
                    if la_ == 1:
                        localctx = ExprParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 160
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 161
                        _la = self._input.LA(1)
                        if not(_la==15 or _la==16):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 162
                        self.expr(7)
                        pass

                    elif la_ == 2:
                        localctx = ExprParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 163
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 164
                        _la = self._input.LA(1)
                        if not(_la==17 or _la==18):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 165
                        self.expr(6)
                        pass

             
                self.state = 170
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,13,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class GotoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LPAREN(self):
            return self.getToken(ExprParser.LPAREN, 0)

        def knot_name(self):
            return self.getTypedRuleContext(ExprParser.Knot_nameContext,0)


        def RPAREN(self):
            return self.getToken(ExprParser.RPAREN, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_goto

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGoto" ):
                listener.enterGoto(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGoto" ):
                listener.exitGoto(self)




    def goto(self):

        localctx = ExprParser.GotoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_goto)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 171
            self.match(ExprParser.LPAREN)
            self.state = 172
            self.knot_name()
            self.state = 173
            self.match(ExprParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrintContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LPAREN(self, i:int=None):
            if i is None:
                return self.getTokens(ExprParser.LPAREN)
            else:
                return self.getToken(ExprParser.LPAREN, i)

        def var_name(self):
            return self.getTypedRuleContext(ExprParser.Var_nameContext,0)


        def RPAREN(self, i:int=None):
            if i is None:
                return self.getTokens(ExprParser.RPAREN)
            else:
                return self.getToken(ExprParser.RPAREN, i)

        def getRuleIndex(self):
            return ExprParser.RULE_print

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrint" ):
                listener.enterPrint(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrint" ):
                listener.exitPrint(self)




    def print_(self):

        localctx = ExprParser.PrintContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_print)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 175
            self.match(ExprParser.LPAREN)
            self.state = 176
            self.match(ExprParser.LPAREN)
            self.state = 177
            self.var_name()
            self.state = 178
            self.match(ExprParser.RPAREN)
            self.state = 179
            self.match(ExprParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NpcContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LPAREN(self):
            return self.getToken(ExprParser.LPAREN, 0)

        def EXLAM(self):
            return self.getToken(ExprParser.EXLAM, 0)

        def option_text(self):
            return self.getTypedRuleContext(ExprParser.Option_textContext,0)


        def RPAREN(self):
            return self.getToken(ExprParser.RPAREN, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_npc

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNpc" ):
                listener.enterNpc(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNpc" ):
                listener.exitNpc(self)




    def npc(self):

        localctx = ExprParser.NpcContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_npc)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 181
            self.match(ExprParser.LPAREN)
            self.state = 182
            self.match(ExprParser.EXLAM)
            self.state = 183
            self.option_text()
            self.state = 184
            self.match(ExprParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ChoiceContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LPAREN(self, i:int=None):
            if i is None:
                return self.getTokens(ExprParser.LPAREN)
            else:
                return self.getToken(ExprParser.LPAREN, i)

        def RPAREN(self, i:int=None):
            if i is None:
                return self.getTokens(ExprParser.RPAREN)
            else:
                return self.getToken(ExprParser.RPAREN, i)

        def pair(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.PairContext)
            else:
                return self.getTypedRuleContext(ExprParser.PairContext,i)


        def getRuleIndex(self):
            return ExprParser.RULE_choice

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterChoice" ):
                listener.enterChoice(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitChoice" ):
                listener.exitChoice(self)




    def choice(self):

        localctx = ExprParser.ChoiceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_choice)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 186
            self.match(ExprParser.LPAREN)
            self.state = 187
            self.match(ExprParser.LPAREN)
            self.state = 191
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==12:
                self.state = 188
                self.pair()
                self.state = 193
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 194
            self.match(ExprParser.RPAREN)
            self.state = 195
            self.match(ExprParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PairContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EXLAM(self):
            return self.getToken(ExprParser.EXLAM, 0)

        def option_text(self):
            return self.getTypedRuleContext(ExprParser.Option_textContext,0)


        def goto(self):
            return self.getTypedRuleContext(ExprParser.GotoContext,0)


        def getRuleIndex(self):
            return ExprParser.RULE_pair

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPair" ):
                listener.enterPair(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPair" ):
                listener.exitPair(self)




    def pair(self):

        localctx = ExprParser.PairContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_pair)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 197
            self.match(ExprParser.EXLAM)
            self.state = 198
            self.option_text()
            self.state = 199
            self.goto()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Option_textContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(ExprParser.ID)
            else:
                return self.getToken(ExprParser.ID, i)

        def INT(self, i:int=None):
            if i is None:
                return self.getTokens(ExprParser.INT)
            else:
                return self.getToken(ExprParser.INT, i)

        def getRuleIndex(self):
            return ExprParser.RULE_option_text

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOption_text" ):
                listener.enterOption_text(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOption_text" ):
                listener.exitOption_text(self)




    def option_text(self):

        localctx = ExprParser.Option_textContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_option_text)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 204
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==19 or _la==20:
                self.state = 201
                _la = self._input.LA(1)
                if not(_la==19 or _la==20):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 206
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Knot_nameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(ExprParser.ID, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_knot_name

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterKnot_name" ):
                listener.enterKnot_name(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitKnot_name" ):
                listener.exitKnot_name(self)




    def knot_name(self):

        localctx = ExprParser.Knot_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_knot_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 207
            self.match(ExprParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_nameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(ExprParser.ID, 0)

        def INT(self):
            return self.getToken(ExprParser.INT, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_var_name

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVar_name" ):
                listener.enterVar_name(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVar_name" ):
                listener.exitVar_name(self)




    def var_name(self):

        localctx = ExprParser.Var_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_var_name)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 209
            _la = self._input.LA(1)
            if not(_la==19 or _la==20):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TextContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(ExprParser.ID, 0)

        def INT(self):
            return self.getToken(ExprParser.INT, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_text

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterText" ):
                listener.enterText(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitText" ):
                listener.exitText(self)




    def text(self):

        localctx = ExprParser.TextContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_text)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 211
            _la = self._input.LA(1)
            if not(_la==19 or _la==20):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[9] = self.logic_expr_sempred
        self._predicates[10] = self.bool_expr_sempred
        self._predicates[11] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def logic_expr_sempred(self, localctx:Logic_exprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 3)
         

    def bool_expr_sempred(self, localctx:Bool_exprContext, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 5)
         





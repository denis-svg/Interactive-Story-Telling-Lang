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
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,1,0,
        5,0,42,8,0,10,0,12,0,45,9,0,1,0,4,0,48,8,0,11,0,12,0,49,1,0,1,0,
        1,1,1,1,1,1,5,1,57,8,1,10,1,12,1,60,9,1,1,1,1,1,1,2,1,2,1,2,1,2,
        1,3,1,3,3,3,70,8,3,1,4,1,4,1,5,1,5,5,5,76,8,5,10,5,12,5,79,9,5,1,
        5,1,5,1,6,1,6,1,6,1,6,1,6,1,6,1,6,3,6,90,8,6,1,7,1,7,1,7,1,7,1,7,
        1,7,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,9,1,9,1,9,1,9,1,9,1,9,3,9,
        112,8,9,1,9,1,9,1,9,1,9,1,9,3,9,119,8,9,1,9,5,9,122,8,9,10,9,12,
        9,125,9,9,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,
        1,10,1,10,1,10,3,10,141,8,10,1,10,5,10,144,8,10,10,10,12,10,147,
        9,10,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,3,11,157,8,11,1,11,
        1,11,1,11,1,11,1,11,1,11,5,11,165,8,11,10,11,12,11,168,9,11,1,12,
        1,12,1,12,1,12,1,13,1,13,1,13,1,13,1,13,1,13,1,14,1,14,1,14,4,14,
        183,8,14,11,14,12,14,184,1,14,1,14,1,15,1,15,1,15,5,15,192,8,15,
        10,15,12,15,195,9,15,1,15,1,15,1,15,1,16,1,16,4,16,202,8,16,11,16,
        12,16,203,1,16,1,16,1,17,1,17,1,18,1,18,1,19,1,19,1,19,0,3,18,20,
        22,20,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,0,3,
        1,0,19,20,1,0,15,16,1,0,17,18,221,0,43,1,0,0,0,2,53,1,0,0,0,4,63,
        1,0,0,0,6,69,1,0,0,0,8,71,1,0,0,0,10,73,1,0,0,0,12,89,1,0,0,0,14,
        91,1,0,0,0,16,97,1,0,0,0,18,111,1,0,0,0,20,126,1,0,0,0,22,156,1,
        0,0,0,24,169,1,0,0,0,26,173,1,0,0,0,28,179,1,0,0,0,30,188,1,0,0,
        0,32,199,1,0,0,0,34,207,1,0,0,0,36,209,1,0,0,0,38,211,1,0,0,0,40,
        42,3,4,2,0,41,40,1,0,0,0,42,45,1,0,0,0,43,41,1,0,0,0,43,44,1,0,0,
        0,44,47,1,0,0,0,45,43,1,0,0,0,46,48,3,2,1,0,47,46,1,0,0,0,48,49,
        1,0,0,0,49,47,1,0,0,0,49,50,1,0,0,0,50,51,1,0,0,0,51,52,5,0,0,1,
        52,1,1,0,0,0,53,54,5,20,0,0,54,58,5,9,0,0,55,57,3,12,6,0,56,55,1,
        0,0,0,57,60,1,0,0,0,58,56,1,0,0,0,58,59,1,0,0,0,59,61,1,0,0,0,60,
        58,1,0,0,0,61,62,5,10,0,0,62,3,1,0,0,0,63,64,3,36,18,0,64,65,5,6,
        0,0,65,66,3,6,3,0,66,5,1,0,0,0,67,70,3,8,4,0,68,70,3,10,5,0,69,67,
        1,0,0,0,69,68,1,0,0,0,70,7,1,0,0,0,71,72,5,19,0,0,72,9,1,0,0,0,73,
        77,5,11,0,0,74,76,7,0,0,0,75,74,1,0,0,0,76,79,1,0,0,0,77,75,1,0,
        0,0,77,78,1,0,0,0,78,80,1,0,0,0,79,77,1,0,0,0,80,81,5,11,0,0,81,
        11,1,0,0,0,82,90,3,38,19,0,83,90,3,24,12,0,84,90,3,26,13,0,85,90,
        3,28,14,0,86,90,3,30,15,0,87,90,3,14,7,0,88,90,3,16,8,0,89,82,1,
        0,0,0,89,83,1,0,0,0,89,84,1,0,0,0,89,85,1,0,0,0,89,86,1,0,0,0,89,
        87,1,0,0,0,89,88,1,0,0,0,90,13,1,0,0,0,91,92,5,13,0,0,92,93,3,36,
        18,0,93,94,5,6,0,0,94,95,3,22,11,0,95,96,5,14,0,0,96,15,1,0,0,0,
        97,98,5,7,0,0,98,99,5,7,0,0,99,100,5,1,0,0,100,101,3,18,9,0,101,
        102,3,24,12,0,102,103,5,8,0,0,103,104,5,8,0,0,104,17,1,0,0,0,105,
        106,6,9,-1,0,106,107,5,7,0,0,107,108,3,18,9,0,108,109,5,8,0,0,109,
        112,1,0,0,0,110,112,3,20,10,0,111,105,1,0,0,0,111,110,1,0,0,0,112,
        123,1,0,0,0,113,118,10,3,0,0,114,115,5,2,0,0,115,119,5,2,0,0,116,
        117,5,3,0,0,117,119,5,3,0,0,118,114,1,0,0,0,118,116,1,0,0,0,119,
        120,1,0,0,0,120,122,3,18,9,4,121,113,1,0,0,0,122,125,1,0,0,0,123,
        121,1,0,0,0,123,124,1,0,0,0,124,19,1,0,0,0,125,123,1,0,0,0,126,127,
        6,10,-1,0,127,128,3,22,11,0,128,145,1,0,0,0,129,140,10,2,0,0,130,
        141,5,4,0,0,131,141,5,5,0,0,132,133,5,12,0,0,133,141,5,6,0,0,134,
        135,5,6,0,0,135,141,5,6,0,0,136,137,5,4,0,0,137,141,5,6,0,0,138,
        139,5,5,0,0,139,141,5,6,0,0,140,130,1,0,0,0,140,131,1,0,0,0,140,
        132,1,0,0,0,140,134,1,0,0,0,140,136,1,0,0,0,140,138,1,0,0,0,141,
        142,1,0,0,0,142,144,3,20,10,3,143,129,1,0,0,0,144,147,1,0,0,0,145,
        143,1,0,0,0,145,146,1,0,0,0,146,21,1,0,0,0,147,145,1,0,0,0,148,149,
        6,11,-1,0,149,157,3,8,4,0,150,151,5,7,0,0,151,152,3,22,11,0,152,
        153,5,8,0,0,153,157,1,0,0,0,154,157,3,10,5,0,155,157,3,36,18,0,156,
        148,1,0,0,0,156,150,1,0,0,0,156,154,1,0,0,0,156,155,1,0,0,0,157,
        166,1,0,0,0,158,159,10,6,0,0,159,160,7,1,0,0,160,165,3,22,11,7,161,
        162,10,5,0,0,162,163,7,2,0,0,163,165,3,22,11,6,164,158,1,0,0,0,164,
        161,1,0,0,0,165,168,1,0,0,0,166,164,1,0,0,0,166,167,1,0,0,0,167,
        23,1,0,0,0,168,166,1,0,0,0,169,170,5,7,0,0,170,171,3,34,17,0,171,
        172,5,8,0,0,172,25,1,0,0,0,173,174,5,7,0,0,174,175,5,7,0,0,175,176,
        3,36,18,0,176,177,5,8,0,0,177,178,5,8,0,0,178,27,1,0,0,0,179,180,
        5,7,0,0,180,182,5,12,0,0,181,183,3,38,19,0,182,181,1,0,0,0,183,184,
        1,0,0,0,184,182,1,0,0,0,184,185,1,0,0,0,185,186,1,0,0,0,186,187,
        5,8,0,0,187,29,1,0,0,0,188,189,5,7,0,0,189,193,5,7,0,0,190,192,3,
        32,16,0,191,190,1,0,0,0,192,195,1,0,0,0,193,191,1,0,0,0,193,194,
        1,0,0,0,194,196,1,0,0,0,195,193,1,0,0,0,196,197,5,8,0,0,197,198,
        5,8,0,0,198,31,1,0,0,0,199,201,5,12,0,0,200,202,3,38,19,0,201,200,
        1,0,0,0,202,203,1,0,0,0,203,201,1,0,0,0,203,204,1,0,0,0,204,205,
        1,0,0,0,205,206,3,24,12,0,206,33,1,0,0,0,207,208,5,20,0,0,208,35,
        1,0,0,0,209,210,7,0,0,0,210,37,1,0,0,0,211,212,7,0,0,0,212,39,1,
        0,0,0,17,43,49,58,69,77,89,111,118,123,140,145,156,164,166,184,193,
        203
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
    RULE_knot_name = 17
    RULE_var_name = 18
    RULE_text = 19

    ruleNames =  [ "program", "knot", "var", "value", "int", "str", "content", 
                   "var_op", "if", "logic_expr", "bool_expr", "expr", "goto", 
                   "print", "npc", "choice", "pair", "knot_name", "var_name", 
                   "text" ]

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
            self.state = 43
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,0,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 40
                    self.var() 
                self.state = 45
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,0,self._ctx)

            self.state = 47 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 46
                self.knot()
                self.state = 49 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==20):
                    break

            self.state = 51
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
            self.state = 53
            self.match(ExprParser.ID)
            self.state = 54
            self.match(ExprParser.LCURLY)
            self.state = 58
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1581184) != 0):
                self.state = 55
                self.content()
                self.state = 60
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 61
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
            self.state = 63
            self.var_name()
            self.state = 64
            self.match(ExprParser.EQ)
            self.state = 65
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
            self.state = 69
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [19]:
                self.enterOuterAlt(localctx, 1)
                self.state = 67
                self.int_()
                pass
            elif token in [11]:
                self.enterOuterAlt(localctx, 2)
                self.state = 68
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
            self.state = 71
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
            self.state = 73
            self.match(ExprParser.GH)
            self.state = 77
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==19 or _la==20:
                self.state = 74
                _la = self._input.LA(1)
                if not(_la==19 or _la==20):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 79
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 80
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
            self.state = 89
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 82
                self.text()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 83
                self.goto()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 84
                self.print_()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 85
                self.npc()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 86
                self.choice()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 87
                self.var_op()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 88
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
            self.state = 91
            self.match(ExprParser.L)
            self.state = 92
            self.var_name()
            self.state = 93
            self.match(ExprParser.EQ)
            self.state = 94
            self.expr(0)
            self.state = 95
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
            self.state = 97
            self.match(ExprParser.LPAREN)
            self.state = 98
            self.match(ExprParser.LPAREN)
            self.state = 99
            self.match(ExprParser.T__0)
            self.state = 100
            self.logic_expr(0)
            self.state = 101
            self.goto()
            self.state = 102
            self.match(ExprParser.RPAREN)
            self.state = 103
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
            self.state = 111
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.state = 106
                self.match(ExprParser.LPAREN)
                self.state = 107
                self.logic_expr(0)
                self.state = 108
                self.match(ExprParser.RPAREN)
                pass

            elif la_ == 2:
                self.state = 110
                self.bool_expr(0)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 123
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,8,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ExprParser.Logic_exprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_logic_expr)
                    self.state = 113
                    if not self.precpred(self._ctx, 3):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                    self.state = 118
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [2]:
                        self.state = 114
                        self.match(ExprParser.T__1)
                        self.state = 115
                        self.match(ExprParser.T__1)
                        pass
                    elif token in [3]:
                        self.state = 116
                        self.match(ExprParser.T__2)
                        self.state = 117
                        self.match(ExprParser.T__2)
                        pass
                    else:
                        raise NoViableAltException(self)

                    self.state = 120
                    self.logic_expr(4) 
                self.state = 125
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
            self.state = 127
            self.expr(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 145
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,10,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ExprParser.Bool_exprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_bool_expr)
                    self.state = 129
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 140
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
                    if la_ == 1:
                        self.state = 130
                        self.match(ExprParser.T__3)
                        pass

                    elif la_ == 2:
                        self.state = 131
                        self.match(ExprParser.T__4)
                        pass

                    elif la_ == 3:
                        self.state = 132
                        self.match(ExprParser.EXLAM)
                        self.state = 133
                        self.match(ExprParser.EQ)
                        pass

                    elif la_ == 4:
                        self.state = 134
                        self.match(ExprParser.EQ)
                        self.state = 135
                        self.match(ExprParser.EQ)
                        pass

                    elif la_ == 5:
                        self.state = 136
                        self.match(ExprParser.T__3)
                        self.state = 137
                        self.match(ExprParser.EQ)
                        pass

                    elif la_ == 6:
                        self.state = 138
                        self.match(ExprParser.T__4)
                        self.state = 139
                        self.match(ExprParser.EQ)
                        pass


                    self.state = 142
                    self.bool_expr(3) 
                self.state = 147
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
            self.state = 156
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.state = 149
                self.int_()
                pass

            elif la_ == 2:
                self.state = 150
                self.match(ExprParser.LPAREN)
                self.state = 151
                self.expr(0)
                self.state = 152
                self.match(ExprParser.RPAREN)
                pass

            elif la_ == 3:
                self.state = 154
                self.str_()
                pass

            elif la_ == 4:
                self.state = 155
                self.var_name()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 166
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,13,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 164
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
                    if la_ == 1:
                        localctx = ExprParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 158
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 159
                        _la = self._input.LA(1)
                        if not(_la==15 or _la==16):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 160
                        self.expr(7)
                        pass

                    elif la_ == 2:
                        localctx = ExprParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 161
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 162
                        _la = self._input.LA(1)
                        if not(_la==17 or _la==18):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 163
                        self.expr(6)
                        pass

             
                self.state = 168
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
            self.state = 169
            self.match(ExprParser.LPAREN)
            self.state = 170
            self.knot_name()
            self.state = 171
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
            self.state = 173
            self.match(ExprParser.LPAREN)
            self.state = 174
            self.match(ExprParser.LPAREN)
            self.state = 175
            self.var_name()
            self.state = 176
            self.match(ExprParser.RPAREN)
            self.state = 177
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

        def RPAREN(self):
            return self.getToken(ExprParser.RPAREN, 0)

        def text(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.TextContext)
            else:
                return self.getTypedRuleContext(ExprParser.TextContext,i)


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
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 179
            self.match(ExprParser.LPAREN)
            self.state = 180
            self.match(ExprParser.EXLAM)
            self.state = 182 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 181
                self.text()
                self.state = 184 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==19 or _la==20):
                    break

            self.state = 186
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
            self.state = 188
            self.match(ExprParser.LPAREN)
            self.state = 189
            self.match(ExprParser.LPAREN)
            self.state = 193
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==12:
                self.state = 190
                self.pair()
                self.state = 195
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 196
            self.match(ExprParser.RPAREN)
            self.state = 197
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

        def goto(self):
            return self.getTypedRuleContext(ExprParser.GotoContext,0)


        def text(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.TextContext)
            else:
                return self.getTypedRuleContext(ExprParser.TextContext,i)


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
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 199
            self.match(ExprParser.EXLAM)
            self.state = 201 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 200
                self.text()
                self.state = 203 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==19 or _la==20):
                    break

            self.state = 205
            self.goto()
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
        self.enterRule(localctx, 34, self.RULE_knot_name)
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
        self.enterRule(localctx, 36, self.RULE_var_name)
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
        self.enterRule(localctx, 38, self.RULE_text)
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
         





# Generated from Expr.g4 by ANTLR 4.12.0
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .ExprParser import ExprParser
else:
    from ExprParser import ExprParser

# This class defines a complete listener for a parse tree produced by ExprParser.
class ExprListener(ParseTreeListener):

    # Enter a parse tree produced by ExprParser#program.
    def enterProgram(self, ctx:ExprParser.ProgramContext):
        pass

    # Exit a parse tree produced by ExprParser#program.
    def exitProgram(self, ctx:ExprParser.ProgramContext):
        pass


    # Enter a parse tree produced by ExprParser#knot.
    def enterKnot(self, ctx:ExprParser.KnotContext):
        pass

    # Exit a parse tree produced by ExprParser#knot.
    def exitKnot(self, ctx:ExprParser.KnotContext):
        pass


    # Enter a parse tree produced by ExprParser#var.
    def enterVar(self, ctx:ExprParser.VarContext):
        pass

    # Exit a parse tree produced by ExprParser#var.
    def exitVar(self, ctx:ExprParser.VarContext):
        pass


    # Enter a parse tree produced by ExprParser#value.
    def enterValue(self, ctx:ExprParser.ValueContext):
        pass

    # Exit a parse tree produced by ExprParser#value.
    def exitValue(self, ctx:ExprParser.ValueContext):
        pass


    # Enter a parse tree produced by ExprParser#int.
    def enterInt(self, ctx:ExprParser.IntContext):
        pass

    # Exit a parse tree produced by ExprParser#int.
    def exitInt(self, ctx:ExprParser.IntContext):
        pass


    # Enter a parse tree produced by ExprParser#str.
    def enterStr(self, ctx:ExprParser.StrContext):
        pass

    # Exit a parse tree produced by ExprParser#str.
    def exitStr(self, ctx:ExprParser.StrContext):
        pass


    # Enter a parse tree produced by ExprParser#content.
    def enterContent(self, ctx:ExprParser.ContentContext):
        pass

    # Exit a parse tree produced by ExprParser#content.
    def exitContent(self, ctx:ExprParser.ContentContext):
        pass


    # Enter a parse tree produced by ExprParser#var_op.
    def enterVar_op(self, ctx:ExprParser.Var_opContext):
        pass

    # Exit a parse tree produced by ExprParser#var_op.
    def exitVar_op(self, ctx:ExprParser.Var_opContext):
        pass


    # Enter a parse tree produced by ExprParser#if.
    def enterIf(self, ctx:ExprParser.IfContext):
        pass

    # Exit a parse tree produced by ExprParser#if.
    def exitIf(self, ctx:ExprParser.IfContext):
        pass


    # Enter a parse tree produced by ExprParser#logic_expr.
    def enterLogic_expr(self, ctx:ExprParser.Logic_exprContext):
        pass

    # Exit a parse tree produced by ExprParser#logic_expr.
    def exitLogic_expr(self, ctx:ExprParser.Logic_exprContext):
        pass


    # Enter a parse tree produced by ExprParser#bool_expr.
    def enterBool_expr(self, ctx:ExprParser.Bool_exprContext):
        pass

    # Exit a parse tree produced by ExprParser#bool_expr.
    def exitBool_expr(self, ctx:ExprParser.Bool_exprContext):
        pass


    # Enter a parse tree produced by ExprParser#expr.
    def enterExpr(self, ctx:ExprParser.ExprContext):
        pass

    # Exit a parse tree produced by ExprParser#expr.
    def exitExpr(self, ctx:ExprParser.ExprContext):
        pass


    # Enter a parse tree produced by ExprParser#goto.
    def enterGoto(self, ctx:ExprParser.GotoContext):
        pass

    # Exit a parse tree produced by ExprParser#goto.
    def exitGoto(self, ctx:ExprParser.GotoContext):
        pass


    # Enter a parse tree produced by ExprParser#print.
    def enterPrint(self, ctx:ExprParser.PrintContext):
        pass

    # Exit a parse tree produced by ExprParser#print.
    def exitPrint(self, ctx:ExprParser.PrintContext):
        pass


    # Enter a parse tree produced by ExprParser#npc.
    def enterNpc(self, ctx:ExprParser.NpcContext):
        pass

    # Exit a parse tree produced by ExprParser#npc.
    def exitNpc(self, ctx:ExprParser.NpcContext):
        pass


    # Enter a parse tree produced by ExprParser#choice.
    def enterChoice(self, ctx:ExprParser.ChoiceContext):
        pass

    # Exit a parse tree produced by ExprParser#choice.
    def exitChoice(self, ctx:ExprParser.ChoiceContext):
        pass


    # Enter a parse tree produced by ExprParser#pair.
    def enterPair(self, ctx:ExprParser.PairContext):
        pass

    # Exit a parse tree produced by ExprParser#pair.
    def exitPair(self, ctx:ExprParser.PairContext):
        pass


    # Enter a parse tree produced by ExprParser#knot_name.
    def enterKnot_name(self, ctx:ExprParser.Knot_nameContext):
        pass

    # Exit a parse tree produced by ExprParser#knot_name.
    def exitKnot_name(self, ctx:ExprParser.Knot_nameContext):
        pass


    # Enter a parse tree produced by ExprParser#var_name.
    def enterVar_name(self, ctx:ExprParser.Var_nameContext):
        pass

    # Exit a parse tree produced by ExprParser#var_name.
    def exitVar_name(self, ctx:ExprParser.Var_nameContext):
        pass


    # Enter a parse tree produced by ExprParser#text.
    def enterText(self, ctx:ExprParser.TextContext):
        pass

    # Exit a parse tree produced by ExprParser#text.
    def exitText(self, ctx:ExprParser.TextContext):
        pass



del ExprParser
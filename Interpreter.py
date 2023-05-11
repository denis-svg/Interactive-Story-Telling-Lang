from ExprParser import ExprParser
from errors import *

class Interpreter:
    def __init__(self, tree) -> None:
        self.tree = tree
        self.vars = {}
    
    def getVars(self):
        index = 0
        root = self.tree.getChild(index)
        while root is not None:
            if isinstance(root, ExprParser.VarContext):
                var_name = root.getChild(0).getChild(0).getText()
                value_node = root.getChild(2).getChild(0)
                typ = None
                value = None
                if isinstance(value_node, ExprParser.IntContext):
                    typ = "int"
                    value = value_node.getText()
                elif isinstance(value_node, ExprParser.StrContext):
                    typ = "string"
                    str_index = 0
                    value_token = value_node.getChild(str_index)
                    value = ""
                    while value_token is not None:
                        value_text = value_token.getText()
                        if value_text != '"':
                            value = value + " " + value_text

                        # Increment string token
                        str_index += 1
                        value_token = value_node.getChild(str_index)
                else:
                    raise VarValueError(value, value_node.start, root.getText())
                self.vars[var_name] = {"value": value, "type": typ}
            
            # Increment child token
            index += 1
            root = self.tree.getChild(index)
    
    def getKnotByIndex(self, i:int):
        index = 0
        root = self.tree.getChild(index)
        counter = -1
        while root is not None:
            if isinstance(root, ExprParser.KnotContext):
                counter += 1

            if counter == i:
                return root
            
            # Increment child token
            index += 1
            root = self.tree.getChild(index)
        return None
    
    def getKnotByName(self, name:str):
        index = 0
        root = self.tree.getChild(index)
        while root is not None:
            if isinstance(root, ExprParser.KnotContext):
                knot_name = root.getChild(0).getText()
                if knot_name == name:
                    return root
            
            # Increment child token
            index += 1
            root = self.tree.getChild(index)
        return None

    def execute(self):
        self.getVars()
        # starting knot is considered knot number 0
        start_knot = self.getKnotByIndex(0)

        index_child = 0
        knot_content = start_knot.getChild(index_child)
        text = ""
        while knot_content is not None:
            if isinstance(knot_content, ExprParser.ContentContext):
                content = knot_content.getChild(0)
                if isinstance(content, ExprParser.PrintContext):
                    text = self.printContext(content, text)
                if isinstance(content, ExprParser.TextContext):
                    text = self.textContext(content, text)
                if isinstance(content, ExprParser.NpcContext):
                    text = self.npcContext(content, text)
                if isinstance(content, ExprParser.Var_opContext):
                    self.expressionContext(content)
                if isinstance(content, ExprParser.GotoContext):
                    knot_name = content.getChild(1).getText()
                    print(knot_content)

            index_child += 1
            knot_content = start_knot.getChild(index_child)
        print(text)
        print(self.vars)

    def printContext(self, content, text):
        var_name = content.getChild(2).getText()
        if var_name in self.vars:
            text += self.vars[var_name]['value']
        else:
            raise NotDeclaredVariable(var_name, content.getChild(2).start, content.getText())
        return text

    def textContext(self, content, text):
        if content.getText() == '.newLine':
            text += "\n"
        else:
            if text[-1] != '\n':
                text += ' ' + content.getText()
            else:
                text += content.getText()
        return text

    def npcContext(self, content, text):
        i = 2
        cont = content.getChild(i)
        while isinstance(cont, ExprParser.TextContext):
            if cont.getText() == '.newLine':
                text += "\n"
            else:
                if text[-1] != '\n':
                    text += ' ' + cont.getText()
                else:
                    text += cont.getText()
            i += 1
            cont = content.getChild(i)
        return text
    
    def expressionContext(self, expr):
        var_name = expr.getChild(1).getText()
        if var_name not in self.vars:
            raise NotDeclaredVariable(var_name, expr.getChild(1).start, expr.getText())
        expr_val = self.calculateExpr(expr.getChild(3))
        if isinstance(expr_val, str) and self.vars[var_name]['type'] == "int":
            raise CannotPerformMixOperations(expr.start)
        if isinstance(expr_val, int) and self.vars[var_name]['type'] == "string":
            raise CannotPerformMixOperations(expr.start)
        self.vars[var_name]['value'] = expr_val



    def calculateExpr(self, expr):
        if isinstance(expr.getChild(0), ExprParser.StrContext):
            return expr.getText()[1:-1]
        if expr.getChild(0).getText() == '(':
            return self.calculateExpr(expr.getChild(1))
        if isinstance(expr.getChild(0), ExprParser.IntContext):
            return int(expr.getText())
        if isinstance(expr.getChild(0), ExprParser.Var_nameContext):
            var_name = expr.getText()
            if var_name not in self.vars:
                raise NotDeclaredVariable(var_name, expr.start)
            if self.vars[var_name]['type'] == 'int':
                return int(self.vars[var_name]['value'])
            else:
                return self.vars[var_name]['value']
        
        left_sum = self.calculateExpr(expr.getChild(0))
        right_sum = self.calculateExpr(expr.getChild(2))
        if not isinstance(left_sum, type(right_sum)):
            raise CannotPerformMixOperations(expr.start)

        if expr.getChild(1).getText() == "+":
            return left_sum + right_sum
        if isinstance(left_sum, int) and isinstance(right_sum, int):
            if expr.getChild(1).getText() == "-":
                return left_sum - right_sum
            if expr.getChild(1).getText() == "*":
                return left_sum * right_sum
            if expr.getChild(1).getText() == "/":
                return left_sum // right_sum
        else:
            raise NotValidOperationOnString(expr.getChild(1).getText(), expr.start)

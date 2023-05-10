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
                    
                    value = value.strip()
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
                    var_name = content.getChild(2).getText()
                    if var_name in self.vars:
                        text += self.vars[var_name]['value']
                    else:
                        raise NotDeclaredVariable(var_name, content.getChild(2).start, content.getText())
                if isinstance(content, ExprParser.TextContext):
                    text += ' ' + content.getText()
            index_child += 1
            knot_content = start_knot.getChild(index_child)
        print(text)
        print(self.vars)
        

from app.utils.stack import Stack

class NpiCalculator:
    def __init__(self, expr: str):
        self.stack = Stack()
        self.expr = expr
        self.operators = ['+', '-', '*', '/']

    def evaluate(self):
        tokens = self.expr.split()
        count_operators = 0

        if len(tokens) == 0:
            return 0

        for token in tokens:
            if token.isdigit():
                self.stack.push(int(token))

            elif token in self.operators:
                item1 = self.stack.pop()
                item2 = self.stack.pop()

                count_operators += 1
                
                if token == "+":
                    self.stack.push(item2 + item1)
                elif token == "-":
                    self.stack.push(item2 - item1)
                elif token == "*":
                    self.stack.push(item2 * item1)
                else:
                    self.stack.push(item2 / item1)
            else:
                raise ValueError("Invalid token")

        if count_operators == 0 and len(tokens) > 1:
            raise ValueError("Invalid expression")
        
        return self.stack.pop()
        

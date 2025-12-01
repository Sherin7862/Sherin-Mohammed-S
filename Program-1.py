class Calculator:
    def operate(self, a: float, b: float, op: str):
        if op == "add":
            return a + b
        elif op == "sub":
            return a - b
        elif op == "mul":
            return a * b
        elif op == "div":
            return a / b
        else:
            return "Invalid operation"

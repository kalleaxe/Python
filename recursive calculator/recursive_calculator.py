import math
from tokenize import TokenError  
from tokenizer import TokenizeWrapper
assert math.isclose(math.sin(math.pi), 0, abs_tol=1e-14)            # sin(PI) is output to 1.2246467991473532e-16 instead of 0. 
                                                                    # This is the solution i managed.

class SyntaxError(Exception):
    def __init__(self, arg):
        self.arg = arg
        super().__init__(self.arg)

class EvaluationError(Exception):
    def __init__(self, arg):
        self.arg = arg
        super().__init__(self.arg)

def fac(n):
    if n-int(n) != 0:
        raise EvaluationError("Input to factorial must be an integer")
    elif n < 0:
        raise EvaluationError("Input to factorial must be positive")
    n = int(n)
    result = 1
    if n == 0 or n == 1:
        return result
    for i in range(2, n + 1):
        result *= i
    return result

def log(x):
    if x <= 0:
        raise EvaluationError("Input to log must be positive")
    else: return math.log(x)

def statement(wtok, variables):
    """ See syntax chart for statement"""
    result = assignment(wtok, variables)
    if not wtok.is_at_end():
        raise SyntaxError('Expected end of line')
    return result

def assignment(wtok, variables):
    """ See syntax chart for assignment"""
    result = expression(wtok, variables)        
    while wtok.get_current() is '=':
        wtok.next()                     # Jumps over '='
        if wtok.is_name():
            if wtok.get_current() in function_1 or wtok.get_current() in function_n:            # Checks if the variable name is a predefined function name.
                raise SyntaxError("attempted to assign a value to a predefined function ")
            var_name = wtok.get_current()
            variables[var_name] = result    # Assign the result to the variable
            wtok.next()                     # Move to the next token
        else:
            raise SyntaxError("Expected name after '='")            # For situations where there is a '=' but no name following
    return result

def expression(wtok, variables):
    """ See syntax chart for expression"""
    result = term(wtok, variables)
    while wtok.get_current() in ['+', '-']:             # While loop for if there are several terms
        if(wtok.get_current() == '+'):
            wtok.next()                                 # Move past token '+'
            result = result + term(wtok, variables)
        elif(wtok.get_current() == '-'):     
            wtok.next()                                 # Move past token '-'
            result = result - term(wtok, variables)            
    return result

def term(wtok, variables):
    """ See syntax chart for term"""
    result = factor(wtok, variables)
    while wtok.get_current() in ['*', '/']:                 # while loop if there are several factors
        if(wtok.get_current() == '*'):
            wtok.next()                                     # Move past '*'
            result = result * factor(wtok, variables)
        if(wtok.get_current() == '/'):
            wtok.next()                             # Move past token '/'
            denominator = factor(wtok, variables)
            if denominator == 0:
                raise EvaluationError("Undefined: division by zero")
            result = result / denominator
    return result

def arglist(wtok, variables):
    args = []
    if wtok.get_current() != '(':
        raise SyntaxError("Expected '('")
    wtok.next()                                         # Move past token '('
    while wtok.get_current() != ')':                    # while loop until the other end of the parenthesis is reached
        args.append(assignment(wtok,variables))
        if wtok.get_current() == ',':
            wtok.next()                                 # Move past the comma
        else:
            if wtok.get_current() != ')':               # for the occasion where there is a blank space between inputs instead of comma
                raise SyntaxError("Expected ','")
    wtok.next()                                         # Move past token ')'
    return args

def factor(wtok, variables):
    
    """ See syntax chart for factor"""
    #print(f"Current token: {wtok.get_current()}")

    if wtok.get_current() == '(':
        wtok.next()                                     # Move past token '('
        result = assignment(wtok, variables)
        if wtok.get_current() != ')':
            raise SyntaxError("Expected ')'")
        else:
            wtok.next()                                     # Move past token ')'
            return result 

    elif wtok.get_current() in function_1:
        func_name = wtok.get_current()                      # Get the function name
        wtok.next()                                         # Move past function name
        if wtok.get_current() == '(':
            wtok.next()                                     # Move past token '('
            arg = assignment(wtok, variables) 
            result = function_1[func_name](arg)  # Applies function to the argument
            if wtok.get_current() != ')':
                raise SyntaxError("Expected ')' after function argument")
            wtok.next()
            return result
        else:
            raise SyntaxError("Expected '(' after function name, before function argument")
        
    elif wtok.get_current() in function_n:
        func_name = wtok.get_current()                      # Get the function name token
        wtok.next()                                         # Move past name token
        args = arglist(wtok, variables)                     # Returns a list with all arguments. Skips the last ')'
        result = function_n[func_name](args)                # Function with list of args as parameter
        return result
        
    elif wtok.is_name():
        var_name = wtok.get_current()
        if var_name in variables:
            result = variables[var_name] 
        else:
            raise EvaluationError(f"Unknown variable '{var_name}'")     
        wtok.next()                                                     # Move past Name token
        return result  

    elif wtok.is_number():
        result = float(wtok.get_current())
        wtok.next()                             # Move past number token
        return result  
    
    elif wtok.get_current() == '-':         # unärt minustecken.
        wtok.next()                         # Move past token '-'
        return -factor(wtok, variables)

    else:
        raise SyntaxError("Expected number, variable, or function")

# Global dictionaries with all functions
function_1 = {
    'sin': math.sin,
    'cos': math.cos,
    'exp': math.exp,
    'log': log,
    'fac': fac,
    'abs': abs
}
    
function_n = {
    'sum': sum,
    'max': max
}
         
def main():
    """
    Handles:
       the iteration over input lines,
       commands like 'quit' and 'vars' and
       raised exceptions.
    Starts with reading the init file
    """
    
    print("Numerical calculator")
    variables = {"ans": 0.0, "E": math.e, "PI": math.pi}
    # Note: The unit test file initiate variables in this way. If your implementation 
    # requires another initiation you have to update the test file accordingly.
    init_file = 'init.txt'
    lines_from_file = ''
    try:
        with open(init_file, 'r') as file:
            lines_from_file = file.readlines()
    except FileNotFoundError:
        pass

    while True:
        if lines_from_file:
            line = lines_from_file.pop(0).strip()
            print('init  :', line)
        else:
            line = input('\nInput : ')
        if line == '' or line[0]=='#':
            continue
        wtok = TokenizeWrapper(line)

        if wtok.get_current() == 'quit':
            print('Bye')
            exit()
        elif wtok.get_current() == 'vars':
            for var, value in variables.items():
                print(f'{var} = {value}')
        else:
            try:
                result = statement(wtok, variables)
                variables['ans'] = result
                print('Result:', result)

            except SyntaxError as se:
                print("*** Syntax error: ", se)
                print(
                f"Error occurred at '{wtok.get_current()}' just after '{wtok.get_previous()}'")

            except EvaluationError as ee:
                print("*** evaluation error: ", ee)
                print(
                f"Error occurred at '{wtok.get_current()}' just after '{wtok.get_previous()}'")

            except TokenError as te:
                print('*** Syntax error: Unbalanced parentheses')
 
if __name__ == "__main__":
    main()

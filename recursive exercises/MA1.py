import time

def multiply(m: int, n: int) -> int:  
    """ Computes m*n using additions"""
    if n == 0:
        return 0
    return m+multiply(m, n-1)


def harmonic(n: int) -> float:              
    """ Computes and returns the harmonc sum 1 + 1/2 + 1/3 + ... + 1/n"""
    if n == 0:
        return 0
    return 1/n + harmonic(n-1)


def get_binary(x: int) -> str:              
    """ Returns the binary representation of x """
    if x < 0:
        return '-'+ get_binary(-x)
    elif x == 0:
        return '0'
    elif x == 1:
        return '1'
    else:
        return get_binary(x//2) + str(x % 2)


def reverse_string(s: str) -> str:        
    """ Returns the s reversed """
    if len(s) <= 1:
        return(s)
    else:
        return(s[-1])+reverse_string(s[:-1])


def largest(a: iter):                     
    """ Returns the largest element in a"""
    if len(a) == 1:                          # kollar om listan enbart innehåller ett element, vilket lär vara störst
        return a[0]                          # är startvilkoret för värdet på max.

    max = largest(a[1:])                     # rekursiva delen för att hitta max-värdet, skär av första värdet tills bara ett värde är kvar.
    if a[0] > max:                           # kollar om index n är större än n-1 (som är "max"), returnerar största värdet.
        return a[0] 
    else:
        return max       


def count(x, s: list) -> int:                
    """ Counts the number of occurrences of x on all levels in s"""
    counter = 0
    if len(s) == 0:                     #scenario 1: tom lista
        return 0
    elif s[-1] == x:                    #scenario 2: kollar om sista i listan är x
        counter += 1
    elif type(s[-1]) == list:           #scenario 3: kollar om sista i listan s är en sublist, kör recursivt igenom den isf.
        counter += count(x, s[-1])
    counter += count(x, s[:-1])        #efter: går vidare rekursivt genom slicing av sista index som ny lista.
    return counter


def bricklek(f: str, t: str, h: str, n: int) -> str:  
    """ Returns a string of instruction ow to move the tiles """
    if n == 0: return []                                                        # Undantagsfall.
    if n == 1: return [f'{f}->{t}']                                             # Sista steget, tar minsta brickan från "f"...
                                                                                # ...och lägger på resterande större brickor som ligger på "t".
    return (bricklek(f, h, t, n-1) + [f'{f}->{t}'] + bricklek(h, t, f, n-1))    # alla andra situationer, urspringliga algoritmen
                                                                                # 1. instruktioner genom att rekursivt flytta n-1 från f till h, 
                                                                                # 2. sista som är kvar från f till t,
                                                                                # 3. instruktioner för att flytta n-1 från h till t, med f som hjälp.
    

def fib(n: int) -> int:                      
    """ Returns the n:th Fibonacci number """
    # You should verify that the time for this function grows approximately as
    # Theta(1.618^n) and also estimate how long time the call fib(100) would take.
    # The time estimate for fib(100) should be in reasonable units (most certainly
    # years) and, since it is just an estimate, with no more than two digits precision.
    #
    # Put your code at the end of the main function below!
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)


def fib_mem(n):
    memory = {0:0, 1:1}

    def fib_mem2(n):
        if n not in memory:
            memory[n] = fib_mem2(n-1) + fib_mem2(n-2)
        return memory[n]
    
    return fib_mem2(n)


def main():
    pass


if __name__ == "__main__":
    main()
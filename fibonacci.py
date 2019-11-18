# Emmett Platt
# CSCI 102-Section D
# GitHub
def fib():
    fibs = [1, 2]

    for i in range(1,9):
        a=0
        b=1
        while b < 145:
            print(b)
            a, b = b, a+b 

        

    return fibs

def main():
    print('OUTPUT', fib())

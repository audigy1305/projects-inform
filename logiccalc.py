def userinput():
    while True:
        a = int(input('enter a value '))
        if a>1:
            print('invalid')
        elif a==1:
            return 1
            break
        elif a==0:
            return 0
            break

def reverse(a):
    if a==1:
        return 0
    else:
        return 1

def conjunc(a, b):
    if a==1 and b==1:
        return 1
    else:
        return 0

def disjunc(a, b):
    if a==0 and b==0:
        return 0
    else:
        return 1

def implic(a, b):
    if a==1 and b==0:
        return 0
    else:
        return 1

def equal(a, b):
    if a==b:
        return 1
    else:
        return 0

def xor(a, b):
    if a==b:
        return 0
    else:
        return 1

a1 = userinput()
b1 = userinput()
ops = {1: reverse(a1), 2: conjunc(a1, b1), 3: disjunc(a1, b1), 4: implic(a1, b1), 5: equal(a1, b1), 6: xor(a1, b1)}
op = int(input('what operator: 1. reverse 2. conjunction 3. disjunction 4. implication 5.equality 6. XOR'))
while True:
    if op>6:
        print('invalid')
    else:
        result = ops[op]
        print(result)
        break
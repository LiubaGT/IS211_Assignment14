def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def gcd(a, b):
    if b > a:
        a, b = b, a

    if a % b == 0:
        return b

    return gcd(b, a % b)

def compareTo(s1, s2):
    move_slice1 = 0
    move_slice2 = 1
    if s1[move_slice1:move_slice2] == '' and s2[move_slice1:move_slice2] == '':
        return 0
    elif s1[move_slice1:move_slice2] == '' and s2[move_slice1:move_slice2] != '':
        return len(s2) * -1
    elif s1[move_slice1:move_slice2] != '' and s2[move_slice1:move_slice2] == '':
        return len(s1)
    else:
        move_slice1 += 1
        move_slice2 += 1

    return compareTo(s1[1:], s2[1:])

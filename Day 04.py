
import re

def find_all_one():
    passwords = set()
    for a in range(1, 7):
        for b in range(a, 10):
            for c in range(b, 10):
                for d in range(c, 10):
                    for e in range(d, 10):
                        for f in range(e, 10):
                            attempt = str(a) + str(b) + str(c) + str(d) + str(e) + str(f)
                            if 130254 <= int(attempt) <= 678275:
                                double = False
                                for i in range(5):
                                    if attempt[i] == attempt[i + 1]:
                                        double = True
                                        break
                                if double:
                                    passwords.add(attempt)
    print(passwords)
    print(len(passwords))

def find_all_two():
    passwords = set()
    for a in range(1, 7):
        for b in range(a, 10):
            for c in range(b, 10):
                for d in range(c, 10):
                    for e in range(d, 10):
                        for f in range(e, 10):
                            attempt = str(a) + str(b) + str(c) + str(d) + str(e) + str(f)
                            if 130254 <= int(attempt) <= 678275 and check_for_doubles(attempt):
                                passwords.add(attempt)
    print(passwords)
    print(len(passwords))

def check_for_doubles(number):
    matches = re.findall("00+|11+|22+|33+|44+|55+|66+|77+|88+|99+", number)
    if matches and min([len(match) for match in matches]) == 2:
        return True
    else:
        return False

find_all_two()                          

# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next in "([{":
            opening_brackets_stack.append(Bracket(next, i))


        if next in ")]}":
            if not opening_brackets_stack:
                return i
            else:
                last_opening_bracket = opening_brackets_stack.pop()
                if not are_matching(last_opening_bracket.char, next):
                    return i


    if opening_brackets_stack:
        return opening_brackets_stack.pop().position

    return True


def main():
    text = input()
    mismatch = find_mismatch(text)
    if mismatch == True:
        print("Success")
        
    else:

        print(mismatch + 1) 

if __name__ == "__main__":
    main()

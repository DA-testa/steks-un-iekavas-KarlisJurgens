# python3
import os 
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
                return i + 1
            else:
                last_bracket = opening_brackets_stack.pop()
                if not are_matching(last_bracket.char, next):
                    return i + 1


    if opening_brackets_stack:
        return opening_brackets_stack.pop().position

    return "Success"


def main():
    FileOrInput=input()
    if FileOrInput == 'I':
        text = input()
        text.strip()
        mismatch = find_mismatch(text)
        if mismatch == "Success":
            print("Success")

        else:
            print(mismatch) 
    elif FileOrInput =='F':
        test_dir = 'test'
        files = os.listdir(test_dir)
        files.sort()
        for i in range(0, len(files), 2):
    
            file_name = os.path.join(test_dir, files[i])
            answer_name = os.path.join(test_dir, files[i+1])

    
            with open(file_name, 'r') as f:
                file_contents = f.read().strip()

            with open(answer_name, 'r') as f:
                answer_contents = f.read().strip()

            

            if str(find_mismatch(file_contents)) == answer_contents:
                print(f"{file_name} Passed")
            else:
                print(f"{file_name} Failed.")
                print(find_mismatch(file_contents))
        

if __name__ == "__main__":
    main()

def txtreader(filename):
    while True:
        try:
            with open(filename, "r") as file:
                lines = file.readlines()
            break
        except FileNotFoundError:
            print(f"File not found: {filename}")
            filename = input("Enter the path to the text file: ")
        except Exception as e:
            print(f"Error reading {filename}: {e}")
            filename = input("Enter the path to the text file: ")
    return [line.strip() for line in lines]

def main():
    filename = input("Enter the path to the text file: ")
    lines = txtreader(filename)

    for line in lines:
        print(f"Processing line: {line}")
        if balance(line):
            print("The line is balanced.")
        else:
            print("The line is not balanced.")
        print()

def balance(line):
    stack = []
    starts = ['(', '[', '{']
    ends = {')': '(', ']': '[', '}': '{'}

    for char in line:
        if char in starts:
            stack.append(char)
            print(f"{char} pushed to stack")
        elif char in ends:
            if ends[char] in stack:
                stack.pop()
                print(f"{char} popped from stack")
            else:
                print(f"Unmatched {char} found")
                return False
        else:
            continue
    return True

main()
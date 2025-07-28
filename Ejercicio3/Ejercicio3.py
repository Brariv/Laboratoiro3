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


def formatRegEx(regex):
    alloperators = ['|', '?', '+', '*', '^', ')']
    binaryoperators = ['|', '^', '(']
    res = ""


    for i in range(0, len(regex)):
        c1 = regex[i]

        if c1 == '\\' and i + 1 < len(regex):
            res += c1 + regex[i + 1]
            i += 1
            continue


        res += c1
        
        if (i + 1 < len(regex)):
            c2 = regex[i + 1]

            if c2 == '\\' and i + 2 < len(regex):
                c2 = regex[i + 2]

            if c1 != '(' and c2 != ')' and c2 not in alloperators and c1 not in binaryoperators:
                res += '∘'
    return res

def infixToPostfix(regex):
    postfix= ""
    stack = []
    formattedRegEx = formatRegEx(regex)

    Precedence = { '(': 1, '|': 2, '∘': 3, '?': 4, '+': 4, '*': 4, '^': 5 }

    print (f"Formatted regex: {formattedRegEx}")


    for i in range(len(formattedRegEx)):
        if formattedRegEx[i] == '\\' and i + 1 < len(formattedRegEx):
            postfix += formattedRegEx[i]
            postfix += formattedRegEx[i + 1]
            print(f"Escaped character: {formattedRegEx[i + 1]}")
            print(f"Actual Output: {postfix} | Actual Stack: {stack}")
            i += 1
            continue


        char = formattedRegEx[i]

        if char == '(':
            stack.append(char)
        elif char == ')':
            while stack and stack[-1] != '(':
                postfix += stack.pop()
            stack.pop()
        elif char not in Precedence:
            postfix += char
        else:
            while (len(stack)):
                peekedChar = stack[-1]
                peekedCharPrecedence = Precedence[peekedChar]
                currentCharPrecedence = Precedence[char]
                if peekedCharPrecedence >= currentCharPrecedence:
                    postfix += stack.pop()
                else:
                    break
            stack.append(char)
            print(f"Operator {char} pushed to stack")
            print(f"Actual Output: {postfix} | Actual Stack: {stack}")

    while (len(stack) > 0):
        postfix += stack.pop()
        print(f"Actual Output: {postfix} | Actual Stack: {stack}")

    print()
    postfix = postfix.replace('∘', '')
    return postfix

def main():
    filename = input("Enter the path to the text file: ")
    lines = txtreader(filename)

    for line in lines:
        print(f"Processing line: {line}")
        print("-" * 100)
        postfix = infixToPostfix(line)
        print("-" * 100)
        print(f"Postfix notation: {postfix}")
        print("=" * 100 + "\n")


main()
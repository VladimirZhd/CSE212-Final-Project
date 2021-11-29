def isValid(s):
    # Declare a stack
    stack = []
    # If starting parentheses is encountered, then append it to the stack
    for char in s:
        if char in ['(', '[', '{']:
            stack.append(char)
        # If starting parentheses is not encountered, then return False
        else:
            if not stack:
                return False
            # Match pair of parentheses to pop out if end parentheses is encountered
            current_char = stack.pop()
            if current_char == '(':
                if char != ")":
                    return False
            if current_char == '{':
                if char != "}":
                    return False
            if current_char == '[':
                if char != "]":
                    return False
    # If stack is empty
    if stack:
        return False
    return True


print('Test 1')
print(isValid("[{{()}}]"))  # Will return true
print('Test 2')
print(isValid("{{()}"))  # Will return false
print('Test 3')
print(isValid("((((({)))))"))  # Will return false

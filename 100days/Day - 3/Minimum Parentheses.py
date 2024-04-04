def minimumParentheses(pattern):
    # Return the minimum number of parentheses required.

    l_count = 0
    r_count = 0 
    added = 0

    for char in pattern:
        if char == "(":
            l_count +=1
        else:
            if l_count > r_count:
                r_count += 1
            else:
                added += 1
    added += l_count - r_count

    return added
    


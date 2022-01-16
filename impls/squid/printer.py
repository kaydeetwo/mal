def pr_str(tokens):
    pr_string = '('
    for token in tokens:
        if isinstance(token, int):
            pr_string += (str(token) + " ")
        elif isinstance(token, str):
            pr_string += (token + " ")
        elif isinstance(token, list):
            pr_string += (pr_str(token) + " ")
        else:
            assert False, "Invalid input string."

    pr_string = pr_string[:len(pr_string)-1] + ")"
    return pr_string

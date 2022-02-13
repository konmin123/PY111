def check_brackets(brackets_row: str) -> bool:
    """
    Check whether input string is a valid bracket sequence
    Valid examples: "", "()", "()()(()())", invalid: "(", ")", ")("
    :param brackets_row: input string to be checked
    :return: True if valid, False otherwise
    """
    list_brackets = []
    for brackets in brackets_row:
        if brackets == "(":
            list_brackets.append(brackets)
        if brackets == ")":
            if list_brackets:
                list_brackets.remove("(")
            else:
                list_brackets.append("brackets_no_valid")
                break
    if list_brackets:
        return False
    else:
        return True

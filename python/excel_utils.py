def sanitize_for_excel(val):
    """
    Sanitize string data to prevent Formula/CSV Injection in Excel.
    Prepends a single quote (') to values starting with =, +, -, @, \t, \r.
    """
    if isinstance(val, str):
        if val and val[0] in ('=', '+', '-', '@', '\t', '\r', '\n'):
            return "'" + val
    return val

def sanitize_for_excel(val):
    """
    Sanitize string data to prevent Formula/CSV Injection in Excel.
    Prepends a single quote to values starting with special execution characters.
    """
    if isinstance(val, str) and val and val[0] in ('=', '+', '-', '@', '\t', '\r'):
        return "'" + val
    return val

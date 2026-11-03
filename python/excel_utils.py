def sanitize_for_excel(val):
    """
    Sanitize string data to prevent Formula/CSV Injection when exporting to Excel formats.
    """
    if isinstance(val, str) and val.startswith(('=', '+', '-', '@', '\t', '\r')):
        return "'" + val
    return val

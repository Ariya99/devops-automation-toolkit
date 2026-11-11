def sanitize_for_excel(val):
    """Sanitize strings to prevent CSV/Formula injection in Excel."""
    if isinstance(val, str) and val.startswith(('=', '+', '-', '@', '\t', '\r')):
        return "'" + val
    return val

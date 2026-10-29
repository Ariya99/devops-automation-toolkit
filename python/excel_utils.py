def sanitize_for_excel(val):
    """
    Sanitize string values to prevent CSV/Formula injection.
    Prepends a single quote to values starting with special execution characters.
    """
    if isinstance(val, str) and val.startswith(('=', '+', '-', '@', '\t', '\r')):
        return "'" + val
    return val

def sanitize_dataframe(df):
    """Sanitize an entire DataFrame against Formula Injection."""
    if hasattr(df, 'map'):
        return df.map(sanitize_for_excel)
    else:
        return df.applymap(sanitize_for_excel)

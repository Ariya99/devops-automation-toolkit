def sanitize_for_excel(val):
    """Sanitize string values to prevent CSV/Formula injection in Excel."""
    if isinstance(val, str) and val.startswith(('=', '+', '-', '@', '\t', '\r')):
        return f"'{val}"
    return val

def sanitize_dataframe(df):
    """Sanitize DataFrame headers and values against Formula Injection."""
    df = df.rename(columns=lambda x: sanitize_for_excel(x) if isinstance(x, str) else x)
    if hasattr(df, 'map'):
        df = df.map(sanitize_for_excel)
    else:
        df = df.applymap(sanitize_for_excel)
    return df

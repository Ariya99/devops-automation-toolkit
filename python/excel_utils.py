def sanitize_for_excel(val):
    """Sanitize string data to prevent Formula/CSV Injection in Excel exports."""
    if isinstance(val, str) and val and val[0] in ('=', '+', '-', '@', '\t', '\r'):
        return "'" + val
    return val

def sanitize_dataframe(df):
    """Sanitize DataFrame cell values and column headers against Formula Injection."""
    df = df.map(sanitize_for_excel)
    df = df.rename(columns=lambda x: sanitize_for_excel(x) if isinstance(x, str) else x)
    return df

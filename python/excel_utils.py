import pandas as pd

def sanitize_for_excel(val):
    """Sanitize string values to prevent Formula/CSV Injection in Excel."""
    if isinstance(val, str) and val and val[0] in ('=', '+', '-', '@', '\t', '\r'):
        return "'" + val
    return val

def sanitize_dataframe(df: pd.DataFrame) -> pd.DataFrame:
    """Sanitize DataFrame headers and values for Excel export to prevent Formula/CSV Injection."""
    df = df.map(sanitize_for_excel)
    df = df.rename(columns=lambda x: sanitize_for_excel(x) if isinstance(x, str) else x)
    return df

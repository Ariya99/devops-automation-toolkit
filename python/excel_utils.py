import pandas as pd

def sanitize_for_excel(val):
    """Sanitize strings to prevent Formula/CSV Injection in Excel."""
    if isinstance(val, str) and val.startswith(('=', '+', '-', '@', '\t', '\r')):
        return "'" + val
    return val

def sanitize_dataframe(df: pd.DataFrame) -> pd.DataFrame:
    """Apply formula injection sanitization to a DataFrame's values and columns."""
    df_sanitized = df.map(sanitize_for_excel)
    df_sanitized = df_sanitized.rename(columns=lambda x: sanitize_for_excel(x) if isinstance(x, str) else x)
    return df_sanitized

import pandas as pd

def sanitize_for_excel(val):
    """Sanitizes a value to prevent formula/CSV injection in Excel."""
    if isinstance(val, str) and val.startswith(('=', '+', '-', '@', '\t', '\r')):
        return "'" + val
    return val

def sanitize_dataframe_for_excel(df: pd.DataFrame) -> pd.DataFrame:
    """Sanitizes all string data and column headers in a dataframe to prevent formula/CSV injection."""
    sanitized_df = df.map(sanitize_for_excel)
    sanitized_df = sanitized_df.rename(columns=lambda x: sanitize_for_excel(x))
    return sanitized_df

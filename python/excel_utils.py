import pandas as pd

def sanitize_for_excel(val):
    """Sanitize string values to prevent CSV/Formula injection in Excel."""
    if isinstance(val, str) and val and val[0] in ('=', '+', '-', '@', '\t', '\r'):
        return "'" + val
    return val

def sanitize_dataframe(df: pd.DataFrame) -> pd.DataFrame:
    """Apply formula injection sanitization to all string columns in a DataFrame."""
    for col in df.select_dtypes(include=['object', 'string']).columns:
        df[col] = df[col].map(sanitize_for_excel)
    return df

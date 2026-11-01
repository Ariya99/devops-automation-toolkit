import pandas as pd

def sanitize_for_excel(val):
    """
    Sanitize strings to prevent CSV/Formula injection in Excel.
    Prepends a single quote to strings starting with execution characters.
    """
    if isinstance(val, str) and val.startswith(('=', '+', '-', '@', '\t', '\r', '\n')):
        return "'" + val
    return val

def sanitize_dataframe(df):
    """
    Applies the sanitize_for_excel function to all elements in a DataFrame.
    """
    if hasattr(df, 'map'):
        return df.map(sanitize_for_excel)
    else:
        return df.applymap(sanitize_for_excel)

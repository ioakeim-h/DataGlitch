from rapidfuzz import process, fuzz
import pandas as pd


def column_search(df, col, score_cutoff=80):
    """
    col argument should be of type str
    """
    if not isinstance(df, pd.DataFrame):
        raise TypeError(f"{df} should be a Pandas DataFrame")

    column_to_match = col
    options = df.columns

    result = process.extract(query=column_to_match, choices=options,
                             limit=None, score_cutoff=score_cutoff)
    print(result)


def value_search(col, value):
    if not isinstance(col, pd.Series):
        raise TypeError(f"{col} should be a Pandas Series")
    if not isinstance(value, str):
        raise TypeError(f"{value} should be of type str")
    
    result = process.extractOne(value, col, scorer=fuzz.ratio)
    print(result)

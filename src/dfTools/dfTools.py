import pandas as pd

def select_by_colvals(df, col_val_dict):
    """Selects rows of a dataframe by column values.
    Args:
        df (DataFrame): the input dataframe.
        col_dict (dict): dictionary of column names (dict keys) and values (dict values), values
        can be non-list (numbers, string, etc.) or any list-like data type.
    Returns:
        (DataFrame) a dataframe with the rows from the input dataframe filtered by the given values 
        of the selected columns.
    """
    mask = pd.Series([True]*len(df.index))
    for name, values in col_val_dict.items():
        try:
            mask = mask & (df[name].isin(values))
        except TypeError:
            mask = mask & (df[name] == values)

    return df[mask]

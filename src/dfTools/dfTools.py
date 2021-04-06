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

def rename_columns(df, colnames_dict, inplace=False):
    """Renames columns in a dataframe. Uses 'pandas.DataFrame.rename'.

    Args:
        df (DataFrame): the input dataframe.
        colnames_dict (dict): dictionary of existing column names as keys and new names as values.
        inplace (bool): whether or not rename columns inplace.
    Returns:
        (DataFrame) if inplace is True the input dataframe is modified, otherwise a new dataframe is 
        returned with new column names.
    """
    if inplace:
        df.rename(colnames_dict, axis='columns', inplace=True)
        return "Warning: the input DataFrame has been modified!"
    else:
        df_out = df.rename(colnames_dict, axis='columns', inplace=False)
        return df_out

def delete_columns(df, colnames_list, inplace=False):
    """Deletes columns from a dataframe. Uses 'pandas.DataFrame.drop'.

    Args:
        df (DataFrame): the input dataframe.
        colnames_list (list of string): list of column names to be deleted.
        inplace (bool): whether or not delete columns inplace.
    Returns:
        (DataFrame) if inplace is True the input dataframe is modified, otherwise a new dataframe is 
        returned without the specified columns.
    """
    if inplace:
        df.drop(colnames_list, axis='columns', inplace=True)
        return "Warning: the input DataFrame has been modified!"
    else:
        df_out = df.drop(colnames_list, axis='columns', inplace=False)
        return df_out

def add_columns(df, columns_dict):
    """Adds columns to a dataframe. Uses 'pandas.DataFrame.insert'.

    Args:
        df (DataFrame): the input dataframe.
        columns_dict (dict): dictionary of the columns to be added. keys are locations (indices), values
        are tuples of length 2, the first element is the column name, the second element is a list containing 
        the column data.
    Returns:
        (DataFrame) the input dataframe with new columns.
    """
    for loc, (name, values) in columns_dict.items():
        df.insert(loc, name, values, allow_duplicates=False)
    return "Warning! new columns have been added to the input DataFrame!"

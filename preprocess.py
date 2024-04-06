import pandas as pd
from constants import MAPPING_DICT


def fix_data_columns(column_names, df):
    """
    process real world data issues with column names and entry
    
    Parameters:
    column_names (list[str]): columns of data.
    df (DataFrame): input dataFrame
    
    Returns:
    column_mapping: cleaned column names mapped to old ones
    """
      
    for i,c in enumerate(column_names):
        if c in MAPPING_DICT:
            column_names[i] = MAPPING_DICT[c]
        
    for i,c in enumerate(column_names):
        if " :" in c:
            column_names[i] = column_names[i].split(" :")[0] 
        if " " in c:
            column_names[i] = '_'.join(column_names[i].split(" "))

    column_mapping = dict(zip(df.columns.tolist(), column_names))

    return column_mapping

def preprocess_data(csv_file):
    """
    Read CSV file and preprocess the data.
    
    Parameters:
    csv_file (str): Path to the CSV file.
    
    Returns:
    pandas.DataFrame: Preprocessed DataFrame.
    """
    # Read CSV file
    df = pd.read_csv(csv_file)
    
    column_names = df.columns.tolist()
    column_names = [c.strip() for c in column_names]


    column_mapping = fix_data_columns(column_names, df)
    df = df.rename(columns=column_mapping)
    
    return df

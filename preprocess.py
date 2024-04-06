import pandas as pd

def preprocess_data(csv_file):
    """
    Read CSV file and preprocess the data.
    
    Parameters:
    csv_file (str): Path to the CSV file.
    
    Returns:
    pandas.DataFrame: Preprocessed DataFrame.
    """
    # Read CSV file
    data = pd.read_csv(csv_file)
    
    # Filtering unwanted columns (to be implemented by the user)
    # Example: data = data.drop(['unwanted_column1', 'unwanted_column2'], axis=1)
    
    # Combine answers from selected columns into a joint string
    data['joint_answers'] = data['column1'] + ' ' + data['column2'] + ' ' + data['column3']
    
    return data

import os
import sys

import torch
import numpy as np
import pandas as pd

from preprocess import preprocess_data
from plotting import plot_data

def generate_embeddings(data):
    """
    Generate embeddings for the processed data using BERT.
    
    Parameters:
    data (pandas.DataFrame): Processed DataFrame.
    
    Returns:
    list: List of embeddings.
    """
    # Placeholder function for BERT embedding generation
    # User should implement BERT embedding generation logic here
    embeddings = []
    return embeddings

def calculate_cosine_similarity(embeddings):
    """
    Calculate cosine similarity between embeddings.
    
    Parameters:
    embeddings (list): List of embeddings.
    
    Returns:
    pandas.DataFrame: DataFrame containing cosine similarity scores.
    """
    # Calculate cosine similarity
    similarity_matrix = cosine_similarity(embeddings, embeddings)
    
    # Convert similarity matrix to DataFrame
    similarity_df = pd.DataFrame(similarity_matrix)
    
    return similarity_df


def main(csv_file):
    # Preprocess the data
    processed_data = preprocessing.preprocess_data(csv_file)
    
    # Generate embeddings
    embeddings = embedding.generate_embeddings(processed_data)
    
    # Calculate cosine similarity
    similarity_df = cosine_similarity.calculate_cosine_similarity(embeddings)
    
    # Store the similarity scores in another CSV
    similarity_df.to_csv('similarity_scores.csv', index=False)
    
    # Plot relevant data
    plot_data(processed_data)

if __name__ == "__main__":
    # Path to the CSV file
    csv_file = 'data/student perception-Data-Form-Responses.csv'
    
    # Call the main function
    main(csv_file)

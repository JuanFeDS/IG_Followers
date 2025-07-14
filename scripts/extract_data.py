# extract_data.py
import os
import zipfile

def extract_data(data_path: str, month: int):
    """Extract data from a zip file.
    
    Args:
        data_path (str): Path to the data directory.
    """
    original_path = f'{data_path}raw/juanfeds-{month}.zip'

    destination_path = f'{data_path}processed/{month}'
    os.makedirs(destination_path, exist_ok=True)

    with zipfile.ZipFile(original_path, 'r') as zip_ref:
        zip_ref.extractall(destination_path)

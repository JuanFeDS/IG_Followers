# read_data.py
import pandas as pd
from bs4 import BeautifulSoup

def read_data(path: str, category: str) -> pd.DataFrame:
    """Build a DataFrame from a HTML file.
    
    Args:
        path (str): Path to the HTML file.
        category (str): Category of the data.
    
    Returns:
        pd.DataFrame: DataFrame with the data.
    """

    # Read the HTML file
    with open(path, 'r', encoding='utf-8') as file:
        content = file.read()

    # Parse the HTML content
    soup = BeautifulSoup(content, 'html.parser')
    data_raw = soup.select('div._a705 > main > div')

    data_list = []
    url_list = []

    for item in data_raw:
        final_item = item.get_text(separator=' ', strip=True)
        url = item.find('a')['href']

        data_list.append(final_item)
        url_list.append(url)

    user = [i.split(' ')[0] for i in data_list]
    year = [i.split(' ')[3] for i in data_list]
    month = [i.split(' ')[1] for i in data_list]
    day = [i.split(' ')[2].replace(',', '') for i in data_list]

    df = pd.DataFrame({
        f'{category}_username': user,
        f'{category}_url': url_list,
        f'{category}_year': year,
        f'{category}_month': month,
        f'{category}_day': day
    })

    return df

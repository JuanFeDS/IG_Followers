# run.py
import os
import json
from datetime import datetime

from scripts.extract_data import extract_data
from scripts.read_data import read_data
from scripts.unfollowers import unfollowers

# Load config
with open('config/config.json', 'r', encoding='utf-8') as f:
    config = json.load(f)

# Global variables
MONTH = int(str(datetime.now()).replace('-', '')[:6])
DATA_PATH = config['paths']['data']
DESTINATION_PATH = f'{DATA_PATH}/processed/{MONTH}'

def main(): 
    """Main function."""
    extract_data(data_path=DATA_PATH, month=MONTH)

    # Following
    following_path = config['categories']['following']['path']
    following_path = os.path.join(DESTINATION_PATH, following_path)

    following_df = read_data(following_path, category='following')

    # Followers
    followers_path = config['categories']['followers']['path']
    followers_path = os.path.join(DESTINATION_PATH, followers_path)

    followers_df = read_data(followers_path, category='followers')

    # Unfollowers
    df_unfollowers = unfollowers(following_df, followers_df)

    # Save unfollowers
    download_path = os.path.join(DATA_PATH, f'clean/unfollowers_{MONTH}.csv')
    df_unfollowers.to_csv(download_path, index=False)

if __name__ == "__main__":
    main()

# unfollowers.py
import pandas as pd

def unfollowers(
    df_following: pd.DataFrame, 
    df_followers: pd.DataFrame
) -> pd.DataFrame:
    """Find the unfollowers between two DataFrames.
    
    Args:
        df_following (pd.DataFrame): DataFrame with the following data.
        df_followers (pd.DataFrame): DataFrame with the followers data.
    
    Returns:
        pd.DataFrame: DataFrame with the unfollowers data.
    """

    df_final = pd.merge(
        df_following,
        df_followers,
        how='outer',
        left_on='following_username',
        right_on='followers_username'
    )

    df_unfollowers = df_final[df_final['followers_username'].isna()]
    df_unfollowers = df_unfollowers[['following_username', 'following_url']]
    df_unfollowers.reset_index(drop=True, inplace=True)

    return df_unfollowers

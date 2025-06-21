import pandas as pd
import numpy as np 
import ast 
from datetime import datetime

def load_data():
    movies = pd.read_csv('data/raw/tmdb_5000_movies.csv')
    credits = pd.read_csv('data/raw/tmdb_5000_credits.csv')
    df = movies.merge(credits,on='title')
    return df

def preprocess(df):
    df['release_date'] = pd.to_datetime(df['release_date'],errors='coerce')
    df['release_month'] = df['release_date'].dt.month
    df['release_year'] = df['release_date'].dt.year
    
    df['genres_list'] = df['genres'].apply(lambda x:[i['name'] for i in ast.literal_eval(x)] if pd.notnull(x) else [])
    df['genre_count'] = df['genres_list'].apply(len)
    
    df.loc[:, 'runtime'] = df['runtime'].fillna(df['runtime'].median())

    df = df[df['budget'] > 0].copy()

    df['log_budget'] = np.log1p(df['budget'])
    
    df = df[df['revenue'] > 0 ].copy()
    df['log_revenue'] = np.log1p(df['revenue'])
    
    df_final = df[['title','log_budget','popularity','runtime','release_month','release_year','genre_count','log_revenue']]
    return df_final

def save_data(df):
    df.to_csv('data/processed/final_movies.csv',index=False)
    
if __name__ == "__main__":
    print("Loading raw data....")
    raw_df = load_data()
    
    print("Preprocessing...")
    final_df= preprocess(raw_df)
    
    print("Saving cleaned data....")
    save_data(final_df)
    
    print("Done ")
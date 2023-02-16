import pandas as pd
from dagster import job, asset


@asset
def split_url():
    df = pd.read_csv('pipelines/data/data.csv')
    df['domain_of_url'] = df['url'].str.extract('//(?:www\.)?(.*?)/')
    df.to_csv('pipelines/data/result.csv', index=False)
    return df


@job
def dagster():
    split_url()

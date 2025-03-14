import pandas as pd


def read_parquet():
    # Replace this with the path to your parquet file
    parquet_file = 'data/budget_tracker_daily.parquet'

    # Read the parquet file
    df = pd.read_parquet(parquet_file)

    # Print the contents of the parquet file
    print(df)


if __name__ == '__main__':
    read_parquet()

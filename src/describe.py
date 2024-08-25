import argparse
import pandas as pd

def describe(filename):
    """
    Uses Pandas read_csv function to read a CSV file as a dataframe and describe it.

    Args:
        filename (string): CSV filename to be read by Pandas.

    Returns:
        DataFrame produced by the Pandas describe method.
    """
    df = pd.read_csv(filename)
    return df.describe()

def main():
    """
    Uses argparse to set up a simple CLI, with only one required argument: the CSV filename.
    """
    parser = argparse.ArgumentParser(
                    prog='describe',
                    description='Uses Pandas to describe a CSV file')
    parser.add_argument('filename')
    args = parser.parse_args()
    filename = args.filename
    print(describe(filename))

if __name__ == '__main__':
    main()
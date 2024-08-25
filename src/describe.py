import argparse
import pandas as pd

def describe(filename):
    df = pd.read_csv(filename)
    return df.describe()

def main():
    parser = argparse.ArgumentParser(
                    prog='describe',
                    description='Uses Pandas to describe a CSV file')
    parser.add_argument('filename')
    args = parser.parse_args()
    filename = args.filename
    print(f'Processing {filename}...')
    print(describe(filename))

if __name__ == '__main__':
    main()
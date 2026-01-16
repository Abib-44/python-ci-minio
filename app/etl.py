import pandas as pd

def transform_data(input_file, output_file):
    df = pd.read_csv(input_file)
    if 'col1' in df.columns and 'col2' in df.columns:
        df['sum'] = df['col1'] + df['col2']
    df.to_csv(output_file, index=False)
    return df

if __name__ == "__main__":
    import sys
    transform_data(sys.argv[1], sys.argv[2])

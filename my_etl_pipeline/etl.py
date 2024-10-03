import pandas as pd

def extract(file_path):
    print('Extracting data...')
    print('hello')
    df = pd.DataFrame()
    {
        'column1': [1, 2, 3],
        'column2': ['A', 'B', 'C']
    }
    return df

def transform(data):
    # Here you can add transformation logic
    print(data)
    return data

def load(data, output_path):
    data.to_csv(output_path, index=False)

def run_etl(input_file, output_file):
    data = extract(input_file)
    transformed_data = transform(data)
    load(transformed_data, output_file)

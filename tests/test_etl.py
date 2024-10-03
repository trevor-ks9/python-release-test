import pandas as pd
from my_etl_pipeline.etl import extract, transform, load

def test_etl():
    # Create a sample CSV file
    input_data = pd.DataFrame({'column1': [1, 2], 'column2': ['a', 'b']})
    input_data.to_csv('test_input.csv', index=False)

    # Run the ETL process
    data = extract('test_input.csv')
    assert not data.empty  # Check that data is not empty

    transformed_data = transform(data)
    assert 'column1' in transformed_data.columns  # Check transformation

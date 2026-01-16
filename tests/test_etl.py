from app.etl import transform_data
import pandas as pd

def test_transform_data(tmp_path):
    input_file = tmp_path / "input.csv"
    input_file.write_text("col1,col2\n1,2\n3,4")
    output_file = tmp_path / "output.csv"
    df = transform_data(input_file, output_file)
    assert 'sum' in df.columns
    assert df['sum'].tolist() == [3, 7]

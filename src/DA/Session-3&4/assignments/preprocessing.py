import pandas as pd

def Read_data_file(file_path):
    try:
        df = pd.read_csv(file_path)
        return df
    except FileNotFoundError:
        print(f"Error: The file was not found at path: {file_path}")
        return None
    except Exception as e:
        print(f"Error: Could not read the file. Details: {e}")
        return None


def Drop_unnecessary_features(df, cols_to_drop):
    df = df.drop(columns=cols_to_drop, errors='ignore')
    return df

def Check_data_type(df):
    report = pd.DataFrame({
        'Datatype': df.dtypes,
        'Unique_Values': df.nunique()
    })
    return report.T

df = Read_data_file('data/raw/titanic.csv')   

if df is not None:
    print(df.head())
    print(df.tail())

    df = Drop_unnecessary_features(df, ['PassengerId', 'Name', 'Ticket'])
    print(df.head())

    print(Check_data_type(df))
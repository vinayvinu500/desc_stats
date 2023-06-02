import os
import pandas as pd
from pathlib import Path

parent = Path(__file__).resolve().parent.parent
os.chdir(parent.joinpath('src'))
print(os.listdir())

# import desc_stats
# # from desc_stats import desc_stats

# def test_mean(df, num):
#     """Checking mean for the file extensions having '.CSV' & '.XLSX'"""
#     assert desc_stats(df, num).iloc[0,0] == df[num].mean()[0]


if __name__ == '__main__':
    cfgFileDirectory='config'
    BASE_DIR=Path(__file__).resolve().parent.parent

    files = [i for i in os.listdir(BASE_DIR.joinpath(cfgFileDirectory))]
    print(os.listdir())
    for file in files:
        ext = str(file).split('.')[1]
        if ext == 'xlsx':
            df = pd.read_excel(BASE_DIR.joinpath(cfgFileDirectory).joinpath(file))
            num = df.select_dtypes(include=['int64', 'float64'])
            
        elif ext == 'csv':
            df = pd.read_csv(BASE_DIR.joinpath(cfgFileDirectory).joinpath(file))
            num = df.select_dtypes(include=['int64', 'float64'])
        
    # function calling
    # print(test_mean(df, num))
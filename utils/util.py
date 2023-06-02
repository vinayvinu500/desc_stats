import os
import pandas as pd
from pathlib import Path

def get_data(files):
    for file in files:
        ext = str(file).split('.')[1]
        if ext == 'xlsx':
            df = pd.read_excel(parent.joinpath(cfgFileDirectory).joinpath(file))
            
        elif ext == 'csv':
            df = pd.read_csv(parent.joinpath(cfgFileDirectory).joinpath(file))
        
        return df


if __name__ == '__main__':
    parent = Path(__file__).resolve().parent.parent
    cfgFileDirectory='config'
    files = [i for i in os.listdir(parent.joinpath(cfgFileDirectory))]
    x,y = get_data(files)
    print(x.head(2), y[:2])
    
        

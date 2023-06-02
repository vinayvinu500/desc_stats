import pytest
from utils.util import get_data
from src.desc_stats import desc_stats
from pathlib import Path
import os


# checking the data files of different formats
@pytest.mark.parametrize('df', get_data)
def test_mean(df):
    print(df)
#     num = df.select_dtypes(include=['int64', 'float64']).columns.to_list()
#     print(num)
#     assert desc_stats(df, num).iloc[0,0] == df[num].mean()[0]

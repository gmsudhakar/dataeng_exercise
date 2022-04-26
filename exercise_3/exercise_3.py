# from {your-package-name} import analytics
import boto3
import pandas as pd

def read_parquet(bucket: str = 'cmc-bds-de', object: str = 'wishes/you/good/luck.parquet') -> pd.DataFrame:
    """Reads a parquet file from an S3 bucket object into a pandas dataframe.

    Args:
        bucket (str, optional): The S3 bucket. Defaults to 'cmc-bds-de'.
        object (str, optional): The S3 bucket object. Defaults to 'wishes/you/good/luck.parquet'.

    Returns:
        pd.DataFrame: The S3 bucket object data.

    Examples:

    ```python
    >>> data = read_parquet()
    >>> data
       A  B    C        D
    0  a  A  1.0   djasd8
    1  b  B  NaN   7123hy
    2  a  C  3.0   h6as7d
    3  a  A  4.0     None
    4  b  B  5.0  dashd77
    5  b  C  6.0  mdas7gg
    ```
    """
    df: pd.DataFrame

    session = boto3.session(profile='exercise')
    s3 = session.client(service_name='s3', region_name="eu-central-1")

    # your code here

    return df


def write_parquet(data: pd.DataFrame, bucket: str = 'cmc-bds-de', object: str = None) -> None:
    """Writes a parquet file to an S3 bucket object.

    Args:
        bucket (str, optional): The S3 bucket. Defaults to 'cmc-bds-de'.
        object (str): The S3 bucket object.

    Raises:
        Exception: It is required to provide an obect name, i.e., the name of your parquet file to be copied to the S3 bucket.

    Examples:

    ```python
    >>> write_parquet(data, object='your/name/of/choice.parquet')
    ```
    """
    if not object:
        raise Exception('Please provide an object name of your choice.')

    # your code here


data = read_parquet()

# expected:
#
#    A  B    C        D
# 0  a  A  1.0   djasd8
# 2  a  C  3.0   h6as7d
# 4  b  B  5.0  dashd77
# 5  b  C  6.0  mdas7gg
data_non_null = analytics.Ops.dropna(data)

data = None
if not data_non_null:
    raise Exception('Please return a clone instead of the original dataframe.')

# expected:
#
# B     A          B     C
# A                       
# a  13.0    4.41332  3.40
# b  54.0  123.12000  6.12
data_pivot = analytics.Ops.pivot(data_non_null)

data = write_parquet(data_pivot, object='your/name/of/choice.parquet')
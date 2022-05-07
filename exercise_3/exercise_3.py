from example_package import analytics
import io
import boto3
import pandas as pd


# use the s3 client to fetch/write data from/to the S3 service
# suggestion: s3.get_object/s3.put_object
session = boto3.Session(profile_name='exercise')
s3 = session.client(service_name='s3', region_name="eu-central-1")


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
       A     B          C           D
    0  a   AXA   13.00000      djasd8
    1  b   BZB  123.12000      7123hy
    2  a   CYC    3.40000      h6as7d
    3  a   BZB    4.41332   Naisd871a
    4  b   AXA   54.00000     dashd77
    5  b   CYC    6.12000     mdas7gg
    6  b  None  612.10000     masf7gg
    7  a   AXA        NaN  jdasd765ad
    ```
    """
    df: pd.DataFrame = pd.DataFrame(columns=['A', 'B', 'C', 'D'])

    # your code here
    # hint: use the s3 api
    
    response = s3.get_object(Bucket=bucket, Key=object)
    df = pd.read_parquet(io.BytesIO(response['Body'].read()))    

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
    # hint: use the s3 api
    
    out_buffer = io.BytesIO()
    data.to_parquet(out_buffer, index=False)

    s3.put_object(Bucket=bucket, Key=object, Body=out_buffer.getvalue())


data = read_parquet()

# expected:
#
#    A    B          C          D
# 0  a  AXA   13.00000     djasd8
# 1  b  BZB  123.12000     7123hy
# 2  a  CYC    3.40000     h6as7d
# 3  a  BZB    4.41332  Naisd871a
# 4  b  AXA   54.00000    dashd77
# 5  b  CYC    6.12000    mdas7gg
analytics.Ops.remove_null_values(data)

# expected:
#
# B   AXA        BZB   CYC
# A                       
# a  13.0    4.41332  3.40
# b  54.0  123.12000  6.12
rotated = analytics.Ops.rotate(data, xx='A', yy='B', scalars='C')

write_parquet(rotated, object='your/name/of/choice.parquet')

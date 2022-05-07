import pandas as pd
import numpy as np

class Ops():
  
    @staticmethod
    def remove_null_values(df: pd.DataFrame) -> pd.DataFrame:
        """Removes all rows containing null values in the dataframe.
        Args:
            df (pd.DataFrame): Dataframe
        Returns:
            pd.DataFrame: Dataframe without any null values.
        """
        
        return data.dropna()
      
    @staticmethod
    def rotate(df: pd.DataFrame, xx: str, yy: str, scalars: str) -> pd.DataFrame:
        """Rotate the dataframe using the pivot function.
        Args:
            df (pd.DataFrame): Dataframe.
            xx (str): The column to be rotated as index.
            yy (str): The column to be roated to new column.
            scalars (str): Column to use for index.
        Returns:
            pd.DataFrame: reshaped dataframe.
        """
        
        return df.pivot(index=xx, columns=yy, values=scalars)

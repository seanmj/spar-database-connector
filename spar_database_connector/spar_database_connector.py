import pandas as pd
import sqlalchemy as sa
from .query_engine.query_engine import query_engine

class DatabaseConnector:
    def __init__(self, provider:str, database:str, schema:str):
        '''
        provider = ['snowflake', 'mysql']
        '''
        self.provider = provider
        self.database = database
        self.schema = schema
        self.query_engine = query_engine(provider,database,schema)

    def query_select(self, sql_string:str) -> pd.DataFrame:
        """
        provider = ['snowflake', 'mysql']
        """
        with self.query_engine.connect() as conn:
            return pd.DataFrame(conn.execute(sa.text(sql_string)))

    def query_upload(self, data: pd.DataFrame, table: str, how: str):
        """
        how = ['append', 'replace']
        provider = ['snowflake', 'mysql']
        """
        if len(data) > 0:
            with self.query_engine.begin() as connection:
                data.to_sql(name=table, con=connection, if_exists=how, index=False)
            print(f"Data uploaded to {table}... \n")
        else:
            print(f"No data to upload to {table}... \n")

    def query_update(self, sql_string:str):
        """
        provider = ['snowflake', 'mysql']
        """
        with self.query_engine.begin() as conn:
            conn.execute(sa.text(sql_string))
        
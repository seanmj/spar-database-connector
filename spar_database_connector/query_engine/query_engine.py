import os
import sqlalchemy as sa
from snowflake.sqlalchemy import URL
from dotenv import load_dotenv

def check_required_envs(provider:str):
    if provider == 'snowflake':
        reqd_envs = [
            'SNOWFLAKE_HOST',
            'SNOWFLAKE_USER',
            'SNOWFLAKE_PASSWORD'
            'SNOWFLAKE_ACCOUNT',
            'SNOWFLAKE_WAREHOUSE',
            'SNOWFLAKE_ROLE'
        ]
    elif provider == 'mysql':
        reqd_envs = [
            'OMNI_HOST',
            'ANALYTICS_HOST',
            'MYSQL_USER',
            'MYSQL_PASSWORD'
        ]
    missing_env = []
    for reqd_env in reqd_envs:
        if reqd_env not in os.environ:
            missing_env.append(reqd_env)
    if len(missing_env) > 0:
        insert_str = '", "'.join(missing_env)
        raise EnvironmentError(f'Env var "{insert_str}" missing.')

def query_engine(provider: str, database: str, schema: str):
    '''
    provider = ['snowflake', 'mysql']
    '''
    load_dotenv()

    provider_options = ['snowflake', 'mysql']
    if provider not in provider_options:
        raise ValueError(f'Value "{provider}" not a valid provider.')
    
    elif provider == 'snowflake':
        check_required_envs(provider)
        
        snowflake_host = os.getenv('SNOWFLAKE_HOST')
        snowflake_user = os.getenv('SNOWFLAKE_USER')
        snowflake_password = os.getenv('SNOWFLAKE_PASSWORD')
        snowflake_account = os.getenv('SNOWFLAKE_ACCOUNT')
        snowflake_warehouse = os.getenv('SNOWFLAKE_WAREHOUSE')
        snowflake_role = os.getenv('SNOWFLAKE_ROLE')
        con = URL(
            host=snowflake_host,
            user=snowflake_user,
            password=snowflake_password,
            account=snowflake_account,
            warehouse=snowflake_warehouse,
            database=database,
            schema=schema,
            role=snowflake_role,
        )

        return sa.create_engine(con)
    elif provider == 'mysql':
        check_required_envs(provider)
        
        if database == 'omni_database':
            host = os.getenv('OMNI_HOST')
        elif database == 'analytics_database':
            host = os.getenv('ANALYTICS_HOST')
        user = os.getenv('MYSQL_USER')
        password = os.getenv('MYSQL_PASSWORD')
        return sa.create_engine(f'mysql+pymysql://{user}:{password}@{host}/{schema}')

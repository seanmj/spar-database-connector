## Pip Install

> pip install git+https://github.com/seanmj/spar-database-connector.git

## Requirements

Environment variables required for connection.
Attempts to load ".env" in root folder.
Variables only needed if connecting to said providers.
1. snowflake
    1. SNOWFLAKE_HOST
    2. SNOWFLAKE_USER
    3. SNOWFLAKE_PASSWORD
    4. SNOWFLAKE_ACCOUNT
    5. SNOWFLAKE_WAREHOUSE
    6. SNOWFLAKE_ROLE
2. mysql
    1. OMNI_HOST
    2. ANALYTICS_HOST
    3. MYSQL_USER
    4. MYSQL_PASSWORD

## Basic Use

#### Querying a table...

``` 
from spar_database_connector.spar_database_connector import DatabaseConnector

OmniConnector = DatabaseConnector('mysql','omni_database','omni_production')

response_df = OmniConnector.query_select('SELECT * FROM assets LIMIT 10;') 
```

#### Appending/Loading dataframe to a table...

```
AnalyticsConnector = DatabaseConnector('mysql','analytics_database','spar_analytics')

test_df = pd.DataFrame({'a':[1,2,3],'b':[4,5,6]})

AnalyticsConnector.query_upload(test_df,'test_table','replace')
```

#### Updates/Insert/etc. queries...

```
update_query = "UPDATE test_table SET 'b' = 9 WHERE 'a' = 3;"

insert_query = "INSERT INTO test_table ('a','b') VALUES (7,8);"

AnalyticsConnector.query_update(update_query)

AnalyticsConnector.query_update(insert_query)
```
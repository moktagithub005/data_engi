import pandas as pd 
from sqlalchemy import create_engine

mysql_engine = create_engine("mysql+pymysql://root:MacMYSQL005@localhost/retail_oltp")

query= "SELECT * FROM online_retail"

df = pd.read_sql(query, mysql_engine)
print(df.head())


import duckdb
#duck_conn =  duckdb.connect("retail_analytics.duckdb")
duck_conn =  duckdb.connect("md:")


# load data into duckdb 

duck_conn.execute( """

     CREATE TABLE IF NOT EXISTS olap_retail AS
     SELECT *  FROM df 

""")

# verify data inside duckdb 

result = duck_conn.execute( """
      SELECT *
      FROM olap_retrail
      LIMIT 5

""").fetchdf()

print(result)

## create cloud database 




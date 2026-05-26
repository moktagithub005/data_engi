import pandas as pd 
from sqlalchemy import create_engine

mysql_engine = create_engine(

    "mysql+pymysql://root:YOUR_PASSWORD@localhost/retail_oltp"
)
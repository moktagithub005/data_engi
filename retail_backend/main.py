from fastapi import FastAPI
from db import cursor

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Retail Intelligence Platform API Running"}


@app.get("/orders")
def get_orders():
    cursor.execute("SELECT * FROM online_retail LIMIT 10")
    results = cursor.fetchall()
    return results

@app.get("/top-countries")
def top_countries():

    query = """
     SELECT 
     country,
     ROUND(SUM(Quantity * UnitPrice),2) AS revenue

     FROM online_retail
     WHERE Quantity > 0
     GROUP BY country
     ORDER BY revenue DESC
     LIMIT 10

     """
    cursor.execute(query)
    results = cursor.fetchall() 
    return results

# top product ....
@app.get("/top-products")
def top_product():
    query = """
    SELECT 
    Description,
    SUM(Quantity)  AS total_quantity
    FROM online_retail
    WHERE Quantity > 0
    GRUOP BY Description
    ORDER BY total_qantity DESC
    LIMIT 10

    """

    cursor.execute(query)

    result = cursor.fetchall()

    return result


## top customers 

@app.get("/top-customers")

def top_customers():
    query= """
    SELECT 
    CustomerID,
    ROUND(SUM(Quantity * UnitPrice),2) AS  total_spent
    FROM online_retail
    WHWRE Quantity > 0  AND CustomerID  IS NOT NULL
    GROUP BY  CustomerID
    ORDER BY total_spent DESC
    LIMIT 10

"""

    cursor.execute(query)

    result = cursor.fetchall()

    return result

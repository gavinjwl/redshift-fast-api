from typing import Optional

from fastapi import FastAPI
import redshift_connector

app = FastAPI()

conn = redshift_connector.connect(
    iam=True,
    cluster_identifier='my-redshift-cluster',
    port=5439,
    database='dev',
    db_user='fast_api',
    user='',
    password='',
    region='ap-northeast-1',
)
conn.rollback()
conn.autocommit = True

@app.get("/")
def read_root():
    with conn.cursor() as cursor:
        cursor.execute('SELECT * FROM "dev"."tpcds_100gb"."item" LIMIT 10;')
        result: tuple = cursor.fetchall()
    return result


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

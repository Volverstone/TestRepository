import sqlite3
from db import queries

db = sqlite3.connect('db/db.sqlite3')
cursor = db.cursor()


async def sql_create():
    if db:
        print("База данных SQLite3 подключена!")
    cursor.execute(queries.CREATE_TABLE_PRODUCTS)
    db.commit()

async def sql_insert_products(name, size, price,category, id_product, photo):
    cursor.execute(queries.INSERT_PRODUCTS, (
        name,
        size,
        price,
        category,
        id_product,
        photo
    ))
    db.commit()
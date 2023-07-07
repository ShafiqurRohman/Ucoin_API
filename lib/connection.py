# # https://www.psycopg.org/docs/usage.html
# import psycopg2

# # Connect to existing database
# conn = psycopg2.connect(
#     database="UcoinDB",
#     user="Shafiq",
#     password="password",
#     host="0.0.0.0"
# )

# # Open cursor to perform database operation
# cur = conn.cursor()

# # Query the database 
# cur.execute("SELECT * FROM login_info_table")
# rows = cur.fetchall()
# for row in rows:
#     print(row)

# # Close communications with database
# cur.close()
# conn.close()


# from UCS API Example


import json
import os
from venv import logger
import boto3
import psycopg2
import logging
from botocore.exceptions import ClientError
from psycopg2 import Error, connect

def db_connection(db_host, db_info, dbname):
   
    return psycopg2.connect(
        host=db_host,
        user=db_info['username'],
        password=db_info['password'],
        dbname=dbname)
# conn = psycopg2.connect(
#     database="UcoinDB",
#     user="Shafiq",
#     password="password",
#     host="0.0.0.0"
# )

def query(db_conn, sql):
    logger.info("query start")
    try:
        cursor = db_conn.cursor()
        cursor.execute(sql)
        row = cursor.fetchall()
        cursor.close()
        return row

    except psycopg2.Error as e:
        logger.error(e)
        logger.error(f'psycopg2.Error occurred:{e.pgerror}, '
                     f'{e.diag.message_detail}')
        cursor.rollback()
        raise(e)
    finally:
        logger.info("query end")

        
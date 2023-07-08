import json
from psycopg2 import Error, connect
from lib import connection as connect
from datetime import datetime
from lib import constraints as CONST

def lambda_handler(event, context):
         
    try:
        db_host = CONST.host
        db_info = CONST.host_info
        db_name = 'UcoinDB'
       

        with connect.db_connection(db_host,db_info,db_name) as conn:
           # print("db_connection成功")
            with conn.cursor() as cur:

                try:
                    # ユーザー情報マスタ取得
                    sql = "SELECT * FROM t_login_info WHERE user_id = '1';"
                    
                    for result in connect.query(conn, sql):
                        # ログイン種別が正か確認
                        #print(result)
                        return responseData(result)
                        
                except(Exception, Error) as error:
                    print("ユーザー情報マスタ取得エラー", error)
                    body = json.dumps({"statusCode": 500001})
                    return responseData(body)

                

                

            cur.close
            conn.close
            print("i am here")
            return responseData(json.dumps({"statusCode": 1}))  
                
    except(Exception, Error) as error:
        print("エラー発生", error)
        body = json.dumps({"statusCode": 500001})
        return responseData(body)
    #finally:
    

def responseData(body):
   # print(body)
    return {
        "headers": {
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Methods": "GET"
        },
        "body": body,
    }


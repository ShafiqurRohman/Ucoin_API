from api import login 


if __name__ == '__main__':
    login.lambda_handler({"headers": {"accessToken": "12345"},"body":{"userId": "taro.yamada", "loginType": "0"}},{})
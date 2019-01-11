import requests
def use_params_requests():
    params={'params1':'Hello','params2':'World'}

    response=requests.get('http://127.0.0.1:8000/ip',params=params)
    print(response.status_code,response.reason)
    print(response.headers)
    print(response.json())
    print(response.text)

if __name__ == '__main__':
    use_params_requests()
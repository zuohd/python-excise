from requests import Request,Session

def hard_request():
    s=Session()
    headers={'User_Agent':'fake2.2'}
    req=Request('GET','https://zuohd.github.io/',headers=headers)
    prepped=req.prepare()
    print('request header>>',prepped.headers)

    resp=s.send(prepped)
    print(resp.status_code)
    print(resp.request.headers)
    print(resp.text)

if __name__ == '__main__':
    hard_request()

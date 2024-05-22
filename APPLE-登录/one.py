import requests
import subprocess
from functools import partial
subprocess.Popen = partial(subprocess.Popen, encoding="utf-8")
import execjs

with open('APPLE-登录/get_key.js', 'rb') as f:
    content = f.read()
    js = content.decode('utf-8')
ctx = execjs.compile(js)
get_key=ctx.call('get_KEY', '1111')

cookies = {
    'dssf': '1',
    'dssid2': 'e4107826-01a6-4f92-86cf-b689e0af390d',
    'pxro': '1',
    'as_sfa': 'Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE',
    'POD': 'us~en',
    'as_dc': 'ucp3',
    'as_pcts': 'CbJ9fSH:X-oLQoTJqjWF4bN3mmgcMBh_4K:OoST145P7MUyH6eGSfaq:UzhMydkNMKo4l64Z_2mIKku6xlRPz6PWbY5wPcha6ZWvoNE:NJ1nP6ea-U7PTkUfr9EtqfGWKHvxq1gHNdLrhl49DjERRuh5B3r+LNP8SHePr+zlM82T-PU-r1EJOUqy',
    'geo': 'CN',
    's_fid': '258F2AD2B1DB7DC5-3A3CB7EACD784BFD',
    's_cc': 'true',
    's_vi': '[CS]v1|3326BEE1F9192AEB-40000C7E402110DF[CE]',
    'as_rumid': 'b6d0bc5f-d86d-4523-9075-2a7de6522755',
    'dslang': 'US-EN',
    'site': 'USA',
    'aasp': '47538DC0AA90ED5048984D72FC4E148AE1F6D3EF1B22CE3D8AA539B74B2683AA13C8E5E49BE07FEEB9A1FA7AB5F6896D653238050AA987EBC69A709FE547F9481869F3624035C7C00D0980A2036675013F87356125C004833B9B11868309E5F8A6209A1D68C87E6C85FCFA633BD5A3FEECD3A02B80BBC972',
    's_sq': 'applestoreww%3D%2526c.%2526a.%2526activitymap.%2526page%253DAOS%25253A%252520orders%25252Forder_signin%2526link%253D%252528inner%252520text%252529%252520%25257C%252520no%252520href%252520%25257C%252520body%2526region%253Dbody%2526pageIDType%253D1%2526.activitymap%2526.a%2526.c%2526pid%253DAOS%25253A%252520orders%25252Forder_signin%2526pidt%253D1%2526oid%253Dfunctionkd%252528%252529%25257B%25257D%2526oidt%253D2%2526ot%253DDIV',
    'aa': '914ADE5757E9F1D31EB4F70C0BB3D858',
}
headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    # 'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    # 'Cache-Control': 'no-cache',
    # 'Connection': 'keep-alive',
    # 'Content-Type': 'application/json',
    # 'Cookie': 'dssf=1; dssid2=e4107826-01a6-4f92-86cf-b689e0af390d; pxro=1; as_sfa=Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE; POD=us~en; as_dc=ucp3; as_pcts=CbJ9fSH:X-oLQoTJqjWF4bN3mmgcMBh_4K:OoST145P7MUyH6eGSfaq:UzhMydkNMKo4l64Z_2mIKku6xlRPz6PWbY5wPcha6ZWvoNE:NJ1nP6ea-U7PTkUfr9EtqfGWKHvxq1gHNdLrhl49DjERRuh5B3r+LNP8SHePr+zlM82T-PU-r1EJOUqy; geo=CN; s_fid=258F2AD2B1DB7DC5-3A3CB7EACD784BFD; s_cc=true; s_vi=[CS]v1|3326BEE1F9192AEB-40000C7E402110DF[CE]; as_rumid=b6d0bc5f-d86d-4523-9075-2a7de6522755; dslang=US-EN; site=USA; aasp=47538DC0AA90ED5048984D72FC4E148AE1F6D3EF1B22CE3D8AA539B74B2683AA13C8E5E49BE07FEEB9A1FA7AB5F6896D653238050AA987EBC69A709FE547F9481869F3624035C7C00D0980A2036675013F87356125C004833B9B11868309E5F8A6209A1D68C87E6C85FCFA633BD5A3FEECD3A02B80BBC972; s_sq=applestoreww%3D%2526c.%2526a.%2526activitymap.%2526page%253DAOS%25253A%252520orders%25252Forder_signin%2526link%253D%252528inner%252520text%252529%252520%25257C%252520no%252520href%252520%25257C%252520body%2526region%253Dbody%2526pageIDType%253D1%2526.activitymap%2526.a%2526.c%2526pid%253DAOS%25253A%252520orders%25252Forder_signin%2526pidt%253D1%2526oid%253Dfunctionkd%252528%252529%25257B%25257D%2526oidt%253D2%2526ot%253DDIV; aa=914ADE5757E9F1D31EB4F70C0BB3D858',
    # 'Origin': 'https://idmsa.apple.com',
    # 'Pragma': 'no-cache',
    # 'Referer': 'https://idmsa.apple.com/',
    # 'Sec-Fetch-Dest': 'empty',
    # 'Sec-Fetch-Mode': 'cors',
    # 'Sec-Fetch-Site': 'same-origin',
    # 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
    # 'X-Apple-Auth-Attributes': '8y7B7t8EepIPbfgiSI0HmgCm9LJok1cixT6FtCMYFgIQzMoKgUX7ssEdX8c/QjLqab+IRfhIGTQCQmmLFocKc1ebUqazejPpCeWFMKBhgZTMuxvTnLvKpNgTe0skPxZT9gi8EQH7RkFBtDFgR3G3XLoaOjBNt0R9nCeNGB8ubyby/D0D7gU8QA1MJBv40opVBtif/PAe/VnzSFSTdYJNYjhrXOTgZFPUIDVsSEQLEbb5O4TQT26rqjh88gGUlyE/N+gqxss1BCOhnEYADoyoZv0T7A==',
    # 'X-Apple-Domain-Id': '35',
    # 'X-Apple-Frame-Id': 'auth-i3r74d9t-x5fp-mj84-tfci-tvvqkqzj',
    # 'X-Apple-I-FD-Client-Info': '{"U":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36","L":"zh-CN","Z":"GMT+08:00","V":"1.1","F":"Fla44j1e3NlY5BNlY5BSmHACVZXnNA9J1I5Kp.beLzLu_dYV6Hycfx9MsFY5CKw.Tf5.EKWJ9Vb5DJfmdUe9zJ.NlY5BNp55BNlan0Os5Apw.80m"}',
    # 'X-Apple-Locale': 'en_US',
    # 'X-Apple-OAuth-Client-Id': 'a797929d224abb1cc663bb187bbcd02f7172ca3a84df470380522a7c6092118b',
    # 'X-Apple-OAuth-Client-Type': 'firstPartyAuth',
    # 'X-Apple-OAuth-Redirect-URI': 'https://secure6.store.apple.com',
    # 'X-Apple-OAuth-Response-Mode': 'web_message',
    # 'X-Apple-OAuth-Response-Type': 'code',
    # 'X-Apple-OAuth-State': 'auth-i3r74d9t-x5fp-mj84-tfci-tvvqkqzj',
    # 'X-Apple-Widget-Key': 'a797929d224abb1cc663bb187bbcd02f7172ca3a84df470380522a7c6092118b',
    # 'X-Requested-With': 'XMLHttpRequest',
    # 'scnt': 'AAAA-jQ3NTM4REMwQUE5MEVENTA0ODk4NEQ3MkZDNEUxNDhBRTFGNkQzRUYxQjIyQ0UzRDhBQTUzOUI3NEIyNjgzQUExM0M4RTVFNDlCRTA3RkVFQjlBMUZBN0FCNUY2ODk2RDY1MzIzODA1MEFBOTg3RUJDNjlBNzA5RkU1NDdGOTQ4MTg2OUYzNjI0MDM1QzdDMDBEMDk4MEEyMDM2Njc1MDEzRjg3MzU2MTI1QzAwNDgzM0I5QjExODY4MzA5RTVGOEE2MjA5QTFENjhDODdFNkM4NUZDRkE2MzNCRDVBM0ZFRUNEM0EwMkI4MEJCQzk3MnwzAAABj57M8J1J3KFrvyGKwqkFE5fWGHv-xNbpsrBIdT6OW5d7e5Cdg9tdK-r3La9SACk0wry58b87-F1z1LJ1IgSgUYyPvA4UFf-nqA6MPmhtM-6vCmA53Q',
    # 'sec-ch-ua': '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
    # 'sec-ch-ua-mobile': '?0',
    # 'sec-ch-ua-platform': '"Windows"',
}

json_data = {
    'a': get_key,
    'accountName': '13131121',
    'protocols': [
        's2k',
        's2k_fo',
    ],
}

response = requests.post('https://idmsa.apple.com/appleauth/auth/signin/init', headers=headers, json=json_data)
print(response.text)
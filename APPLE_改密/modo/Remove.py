import requests,re,logging


logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s\n',
    datefmt='%Y-%m-%d %H:%M:%S',
    handlers=[
        logging.StreamHandler()
    ]
)
# ------------------------------------------------------------------------------------------------------------------------------------
cookies = {
    'dssid2': 'c71e8b00-8802-4176-aec7-02d1e369f1d3',
    'dssf': '1',
}

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'DNT': '1',
    'Pragma': 'no-cache',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0',
    'sec-ch-ua': '"Not)A;Brand";v="99", "Microsoft Edge";v="127", "Chromium";v="127"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

response_1 = requests.get('https://appleid.apple.com/', cookies=cookies, headers=headers)
aidsp_1 = response_1.cookies.get('aidsp')
logging.info(f'aidsp_1----{aidsp_1}')



headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json',
    'DNT': '1',
    'Pragma': 'no-cache',
    'Referer': 'https://appleid.apple.com/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0',
    'X-Apple-I-FD-Client-Info': '{"U":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0","L":"zh-CN","Z":"GMT+08:00","V":"1.1","F":".la44j1e3NlY5BNlY5BSmHACVZXnNA9dHHavS3eFMurJhBR.uMp4UdHz13NldjV2pNk0ug9WJ3uJtBE_HzWBzu0Y5BNlYJNNlY5QB4bVNjMk.CLJ"}',
    'X-Apple-I-Request-Context': 'ca',
    'X-Apple-I-TimeZone': 'Asia/Shanghai',
    'sec-ch-ua': '"Not)A;Brand";v="99", "Microsoft Edge";v="127", "Chromium";v="127"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}
response_2 = requests.get('https://appleid.apple.com/bootstrap/portal', headers=headers)
aidsp_2 = response_2.cookies.get('aidsp')#没用上
serviceKey = response_2.json()['serviceKey']#用上了
logging.info(f'aidsp_2----{aidsp_2}')
logging.info(f'serviceKey----{serviceKey}')


# 用aidsp_1,
headers = {
    "Host": "appleid.apple.com",
    "Connection": "keep-alive",
    "sec-ch-ua": "\"Not)A;Brand\";v=\"99\", \"Google Chrome\";v=\"127\", \"Chromium\";v=\"127\"",
    "X-Apple-I-FD-Client-Info": "{\"U\":\"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36\",\"L\":\"zh-CN\",\"Z\":\"GMT+08:00\",\"V\":\"1.1\",\"F\":\"7la44j1e3NlY5BNlY5BSmHACVZXnNA9dMGAqBfg.CyhpAI6.D_xGMuJjkW5BOQs.xLB.Tf1cK0D_DI2tFEp5UaJBNlY5BPY25BNnOVgw24uy.Cbz\"}",
    "X-Apple-I-Request-Context": "ca",
    "sec-ch-ua-mobile": "?0",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36",
    "Content-Type": "application/json",
    "Accept": "application/json, text/plain, */*",
    "X-Apple-I-TimeZone": "Asia/Shanghai",
    "sec-ch-ua-platform": "\"Windows\"",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Dest": "empty",
    "Referer": "https://appleid.apple.com/",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Cookie": f"idclient=web; dslang=CN-ZH; site=CHN; aidsp={aidsp_1}; geo=CN"
}
response = requests.get('https://appleid.apple.com/account/manage/gs/ws/token', headers=headers)
scnt = response.headers["scnt"]
X_Apple_I_Request_ID = response.headers["X-Apple-I-Request-ID"]
logging.info(f'scnt----{scnt}')
logging.info(f'X_Apple_I_Request_ID----{X_Apple_I_Request_ID}')




url = 'https://appleid.apple.com/jslog'
headers ={
    "Host": "appleid.apple.com",
    "Connection": "keep-alive",
    "Content-Length": "88",
    "sec-ch-ua": "\"Not)A;Brand\";v=\"99\", \"Google Chrome\";v=\"127\", \"Chromium\";v=\"127\"",
    "scnt":scnt,
    "X-Apple-I-FD-Client-Info": "{\"U\":\"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36\",\"L\":\"zh-CN\",\"Z\":\"GMT+08:00\",\"V\":\"1.1\",\"F\":\"Fla44j1e3NlY5BNlY5BSmHACVZXnNA9dMGAqBZB7AxQeLaD.SAuXjodUW1BNmWjV2pNk0ug9WJ3uJtBE_.zJOyO7lY5BNleBBNlYCa1nkBMfs.ELl\"}",
    "X-Apple-I-Request-Context": "ca",
    "sec-ch-ua-mobile": "?0",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36",
    "Content-Type": "application/json",
    "Accept": "application/json, text/plain, */*",
    "X-Apple-I-TimeZone": "Asia/Shanghai",
    "sec-ch-ua-platform": "\"Windows\"",
    "Origin": "https://appleid.apple.com",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Dest": "empty",
    "Referer": "https://appleid.apple.com/",
    # "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Cookie": f"idclient=web; dslang=CN-ZH; site=CHN; aidsp={aidsp_1}; geo=CN"
}
data = {"title":"ROUTE CHANGED","type":"INFO","messageMap":{"ACTION":"FE_INFO"},"details":"{}"}
response = requests.post(url, headers=headers,data=data)
aid_1 = response.cookies.get('aid')
logging.info(f'aid_1----{aid_1}')


# X-Apple-ID-Session-Id和aid_2同一个
url = 'https://appleid.apple.com/jslog'
headers ={
    "Host": "appleid.apple.com",
    "Connection": "keep-alive",
    "Content-Length": "108",
    "sec-ch-ua": "\"Not)A;Brand\";v=\"99\", \"Google Chrome\";v=\"127\", \"Chromium\";v=\"127\"",
    "scnt": scnt,
    "X-Apple-I-FD-Client-Info": "{\"U\":\"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36\",\"L\":\"zh-CN\",\"Z\":\"GMT+08:00\",\"V\":\"1.1\",\"F\":\"7la44j1e3NlY5BNlY5BSmHACVZXnNA9dMGAqB0J9QxQeLaD.SAuXjodUW1BNpMk0ugN.xL4Fe1S9Ra6mVUeBzB.NlY5BNp55BNlan0Os5Apw.1_d\"}",
    "X-Apple-I-Request-Context": "ca",
    "sec-ch-ua-mobile": "?0",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36",
    "Content-Type": "application/json",
    "Accept": "application/json, text/plain, */*",
    "X-Apple-I-TimeZone": "Asia/Shanghai",
    "sec-ch-ua-platform": "\"Windows\"",
    "Origin": "https://appleid.apple.com",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Dest": "empty",
    "Referer": "https://appleid.apple.com/",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Cookie": f"idclient=web; dslang=CN-ZH; site=CHN; aidsp={aidsp_1}; geo=CN; aid={aid_1}"
}
data = {"message":"sign-in","title":"ROUTE CHANGED","type":"INFO","messageMap":{"ACTION":"FE_INFO"},"details":"{}"}
response = requests.post(url, headers=headers,data=data)
aid_2 = response.cookies.get('aid')
logging.info(f'aid_2----{aid_2}')




# 他也会返回scnt，但是没用到
url = f'https://idmsa.apple.com/appleauth/auth/authorize/signin?frame_id=auth-xgo22dgf-qlc6-e2kq-uw0c-4z1vnc57&skVersion=7&iframeId=auth-xgo22dgf-qlc6-e2kq-uw0c-4z1vnc57&client_id={serviceKey}&redirect_uri=https://appleid.apple.com&response_type=code&response_mode=web_message&state=auth-xgo22dgf-qlc6-e2kq-uw0c-4z1vnc57&authVersion=latest'
headers = {
    "Host": "idmsa.apple.com",
    "Connection": "keep-alive",
    "sec-ch-ua": "\"Not)A;Brand\";v=\"99\", \"Google Chrome\";v=\"127\", \"Chromium\";v=\"127\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Sec-Fetch-Site": "same-site",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-User": "?1",
    "Sec-Fetch-Dest": "iframe",
    "Referer": "https://appleid.apple.com/",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Cookie": "dslang=CN-ZH; site=CHN; geo=CN"
}
response = requests.get(url, headers=headers)
X_Apple_Auth_Attributes = response.headers["X-Apple-Auth-Attributes"]
X_Apple_HC_Challenge = response.headers["X-Apple-HC-Challenge"]
aasp = response.cookies.get('aasp')
logging.info(f'X_Apple_Auth_Attributes----{X_Apple_Auth_Attributes}')
logging.info(f'X_Apple_HC_Challenge----{X_Apple_HC_Challenge}')
logging.info(f'aasp----{aasp}')



url = 'https://idmsa.apple.com/appleauth/jslog'
headers = {
    "Host": "idmsa.apple.com",
    "Connection": "keep-alive",
    "Content-Length": "154",
    "sec-ch-ua": "\"Not)A;Brand\";v=\"99\", \"Google Chrome\";v=\"127\", \"Chromium\";v=\"127\"",
    "scnt": "",
    "x-csrf-token": "",
    "sec-ch-ua-mobile": "?0",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36",
    "Content-type": "application/json",
    "Accept": "application/json",
    "sec-ch-ua-platform": "\"Windows\"",
    "Origin": "https://idmsa.apple.com",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Dest": "empty",
    "Referer": "https://idmsa.apple.com/",
    # "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Cookie": f"dslang=CN-ZH; site=CHN; geo=CN; aasp={aasp}"
}
data = {"title":"Hashcash generation","type":"INFO","message":"APPLE ID : Performace - 0.027300000000046565 s","details":"{\"pageVisibilityState\":\"visible\"}"}
response = requests.post(url, headers=headers,data=data)
aa = response.cookies.get('aa')
logging.info(f'aa----{aa}')



name = 'sophiab2022@gmail.com'
url = "https://env-00jxgsqva6td.dev-hz.cloudbasefunction.cn/A1?type=1"
payload = {f"email": {name}}
Key = requests.post(url=url, data=payload).json()


combined_headers_and_cookies = {
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0",
}
json_data = {
    "a": Key["r"],
    "accountName": name,
    "protocols": [
        "s2k",
        "s2k_fo",
    ],
}
response_2 = requests.post(
    url="https://idmsa.apple.com/appleauth/auth/signin/init",
    headers=combined_headers_and_cookies,
    json=json_data,
)
scnt_1 = response_2.headers['scnt']
logging.info(f'scnt_1----{scnt_1}')



url = "https://env-00jxgsqva6td.dev-hz.cloudbasefunction.cn/A1?type=2"
payload = {
    "email": name,
    "iterations": response_2.json()["iteration"],
    "Value": response_2.json()["b"],
    "salt": response_2.json()["salt"],
    "password": "Aa147369",
    "protocol": response_2.json()["protocol"],
    "privateHexValue": Key["privateHexValue"],
    "publicHexValue": Key["publicHexValue"],
}
response_3 = requests.post(url=url, json=payload
).json()



headers = {
    "Host": "idmsa.apple.com",
    "Connection": "keep-alive",
    "Content-Length": "214",
    "sec-ch-ua": "\"Not)A;Brand\";v=\"99\", \"Google Chrome\";v=\"127\", \"Chromium\";v=\"127\"",
    "scnt": scnt_1,
    "X-Apple-Widget-Key": "af1139274f266b22b68c2a3e7ad932cb3c0bbe854e13a79af78dcc73136882c3",
    "X-Apple-Frame-Id": "auth-xgo22dgf-qlc6-e2kq-uw0c-4z1vnc57",
    "X-Apple-I-FD-Client-Info": "{\"U\":\"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36\",\"L\":\"zh-CN\",\"Z\":\"GMT+08:00\",\"V\":\"1.1\",\"F\":\"7la44j1e3NlY5BNlY5BSmHACVZXnNA9dMGAq.bfpCUfSHolk2dUJKy_Aw7GY5ey.EKY.6eke4FIdIZkyJ2xF6w9GY5BNlYJNNlY5QB4bVNjMk.4sL\"}",
    "X-Apple-OAuth-Redirect-URI": "https://appleid.apple.com",
    "X-Apple-OAuth-Client-Id": "af1139274f266b22b68c2a3e7ad932cb3c0bbe854e13a79af78dcc73136882c3",
    "X-Apple-OAuth-Client-Type": "firstPartyAuth",
    "X-Requested-With": "XMLHttpRequest",
    "X-APPLE-HC": "1:10:20240730082557:2dd9c513daab667bdef7632eca3caed3::697",
    "sec-ch-ua-platform": "\"Windows\"",
    "X-Apple-Auth-Attributes": X_Apple_Auth_Attributes,
    "sec-ch-ua-mobile": "?0",
    "X-Apple-OAuth-Response-Type": "code",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36",
    "X-Apple-OAuth-Response-Mode": "web_message",
    "Content-Type": "application/json",
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "X-Apple-Domain-Id": "1",
    "X-Apple-OAuth-State": "auth-xgo22dgf-qlc6-e2kq-uw0c-4z1vnc57",
    "Origin": "https://idmsa.apple.com",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Dest": "empty",
    "Referer": "https://idmsa.apple.com/",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Cookie": f"dslang=CN-ZH; site=CHN; geo=CN; aasp={aasp}; aa={aa}"
}
json_data = {
    "accountName": name,
    "rememberMe": False,
    "m1": response_3["M1"],
    "c": response_2.json()["c"],
    "m2": response_3["M2"],
}
response_4 =  requests.post(
    url="https://idmsa.apple.com/appleauth/auth/signin/complete?isRememberMeEnabled=true",
    headers=headers,
    json=json_data,
)
# CK = response_4.headers.get("Set-Cookie")
# myacinfo_pattern = re.compile(r"myacinfo=([^;]+)")
# myacinfo_match = myacinfo_pattern.search(CK).group(1)
scnt_2 = response_4.headers["scnt"]
X_Apple_ID_Session_Id = response_4.headers['X-Apple-ID-Session-Id']
X_Apple_Auth_Attributes = response_4.headers['X-Apple-Auth-Attributes']
logging.info(f'scnt_2----{scnt_2}')
logging.info(f'X_Apple_ID_Session_Id----{X_Apple_ID_Session_Id}')
logging.info(f'X_Apple_Auth_Attributes----{X_Apple_Auth_Attributes}')


url = 'https://idmsa.apple.com/appleauth/auth'
headers = {
    "Host": "idmsa.apple.com",
    "Connection": "keep-alive",
    "sec-ch-ua": "\"Not)A;Brand\";v=\"99\", \"Google Chrome\";v=\"127\", \"Chromium\";v=\"127\"",
    "scnt": scnt_2,
    "X-Apple-Widget-Key": "af1139274f266b22b68c2a3e7ad932cb3c0bbe854e13a79af78dcc73136882c3",
    "X-Apple-Frame-Id": "auth-xgo22dgf-qlc6-e2kq-uw0c-4z1vnc57",
    "X-Apple-I-FD-Client-Info": "{\"U\":\"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36\",\"L\":\"zh-CN\",\"Z\":\"GMT+08:00\",\"V\":\"1.1\",\"F\":\"7la44j1e3NlY5BNlY5BSmHACVZXnNA9dMGAq.4H_MurJhBR.uMp4UdHz13NlejV2pNk0ug9WJ3uJtBE_.zJ0z13NlY5BNp55BNlan0Os5Apw.3Ol\"}",
    "X-Apple-OAuth-Redirect-URI": "https://appleid.apple.com",
    "X-Apple-OAuth-Client-Id": "af1139274f266b22b68c2a3e7ad932cb3c0bbe854e13a79af78dcc73136882c3",
    "X-Apple-OAuth-Client-Type": "firstPartyAuth",
    "X-Requested-With": "XMLHttpRequest",
    "sec-ch-ua-platform": "\"Windows\"",
    "X-Apple-ID-Session-Id": aasp,
    "X-Apple-Auth-Attributes": X_Apple_Auth_Attributes,
    "sec-ch-ua-mobile": "?0",
    "X-Apple-OAuth-Response-Type": "code",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36",
    "X-Apple-OAuth-Response-Mode": "web_message",
    "Content-Type": "application/json",
    "Accept": "text/html",
    "X-Apple-Domain-Id": "1",
    "X-Apple-OAuth-State": "auth-xgo22dgf-qlc6-e2kq-uw0c-4z1vnc57",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Dest": "empty",
    "Referer": "https://idmsa.apple.com/",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Cookie": f"dslang=CN-ZH; site=CHN; geo=CN; aasp={aasp}; aa={aa}"
}
response =  requests.get(
    url=url,
    headers=headers,
)
scnt_3 = response.headers["scnt"]
X_Apple_Auth_Attributes = response.headers["X-Apple-Auth-Attributes"]
logging.info(f'scnt_3----{scnt_3}')
logging.info(f'X_Apple_Auth_Attributes----{X_Apple_Auth_Attributes}')
logging.info(f'X_Apple_Auth_Attributes----{response.text}')



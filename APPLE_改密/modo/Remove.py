import requests,re,logging


logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s\n',
    datefmt='%Y-%m-%d %H:%M:%S',
    handlers=[
        logging.StreamHandler()
    ]
)
# # --------------------------------------------------------------------------------------------------------------
# name = 'sophiab2022@gmail.com'

# url = "https://env-00jxgsqva6td.dev-hz.cloudbasefunction.cn/A1?type=1"
# payload = {f"email": {name}}
# Key = requests.post(url=url, data=payload).json()
# # ------------------------------------------------------------------------------
# combined_headers_and_cookies = {
#     "Accept": "application/json, text/javascript, */*; q=0.01",
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0",
# }
# json_data = {
#     "a": Key["r"],
#     "accountName": name,
#     "protocols": [
#         "s2k",
#         "s2k_fo",
#     ],
# }
# response_2 = requests.post(
#     url="https://idmsa.apple.com/appleauth/auth/signin/init",
#     headers=combined_headers_and_cookies,
#     json=json_data,
# ).json()
# # -------------------------------------------------------------------------------
# url = "https://env-00jxgsqva6td.dev-hz.cloudbasefunction.cn/A1?type=2"
# payload = {
#     "email": name,
#     "iterations": response_2["iteration"],
#     "Value": response_2["b"],
#     "salt": response_2["salt"],
#     "password": "Aa147369",
#     "protocol": response_2["protocol"],
#     "privateHexValue": Key["privateHexValue"],
#     "publicHexValue": Key["publicHexValue"],
# }
# response_3 = requests.post(url=url, json=payload
# ).json()
# # -----------------------------------------------------------------------------
# cookies = {
#     "as_rumid": "9f9a7e8708ebbde2daf02b478473eccd",
#     "dssf": "1",
#     "as_sfa": "Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE",
#     "geo": "CN",
#     "pxro": "1",
#     "s_fid": "6323376718433557-371662D1A66E1B14",
#     "s_cc": "true",
#     "s_vi": "[CS]v1|332AA8C7A36C871F-40000E40A15E97D6[CE]",
#     "dslang": "US-EN",
#     "site": "USA",
#     "aa": "1B99A552487EA314F1CE4E8E4291BC46",
# }

# headers = {
#     "Accept": "application/json, text/javascript, */*; q=0.01",
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0",
#     "X-Apple-Widget-Key": "a797929d224abb1cc663bb187bbcd02f7172ca3a84df470380522a7c6092118b",
# }
# json_data = {
#     "accountName": name,
#     "rememberMe": False,
#     "m1": response_3["M1"],
#     "c": response_2["c"],
#     "m2": response_3["M2"],
# }
# response_4 =  requests.post(
#     url="https://idmsa.apple.com/appleauth/auth/signin/complete",
#     headers=headers,
#     json=json_data,
#     cookies=cookies,
# )
# CK = response_4.headers.get("Set-Cookie")
# myacinfo_pattern = re.compile(r"myacinfo=([^;]+)")
# myacinfo_match = myacinfo_pattern.search(CK).group(1)



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
aidsp_2 = response_2.cookies.get('aidsp')
serviceKey = response_2.json()['serviceKey']
logging.info(f'aidsp_2----{aidsp_2}')
logging.info(f'serviceKey----{serviceKey}')


# 用aidsp_1,
cookies = {
    'dssid2': 'c71e8b00-8802-4176-aec7-02d1e369f1d3',
    'dssf': '1',
    'idclient': 'web',
    'dslang': 'CN-ZH',
    'site': 'CHN',
    'aidsp': aidsp_1,
    'geo': 'CN',
}
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
    'X-Apple-I-FD-Client-Info': '{"U":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0","L":"zh-CN","Z":"GMT+08:00","V":"1.1","F":"Fla44j1e3NlY5BNlY5BSmHACVZXnNA9dHHav8HZrLzLu_dYV6Hycfx9MsFY5CKw.Tf5.EKWJ9VbHb8WweMw8buJY5BNlY5cklY5BqNAE.lTjV.Do6"}',
    'X-Apple-I-Request-Context': 'ca',
    'X-Apple-I-TimeZone': 'Asia/Shanghai',
    'sec-ch-ua': '"Not)A;Brand";v="99", "Microsoft Edge";v="127", "Chromium";v="127"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}
response = requests.get('https://appleid.apple.com/account/manage/gs/ws/token', cookies=cookies, headers=headers)
scnt = response.headers["scnt"]
logging.info(f'scnt----{scnt}')




cookies = {
    'dssid2': 'c71e8b00-8802-4176-aec7-02d1e369f1d3',
    'dssf': '1',
    'dslang': 'CN-ZH',
    'site': 'CHN',
    'geo': 'CN',
}

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    # 'Cookie': 'dssid2=c71e8b00-8802-4176-aec7-02d1e369f1d3; dssf=1; dslang=CN-ZH; site=CHN; geo=CN',
    'DNT': '1',
    'Pragma': 'no-cache',
    'Referer': 'https://appleid.apple.com/',
    'Sec-Fetch-Dest': 'iframe',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-site',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0',
    'sec-ch-ua': '"Not)A;Brand";v="99", "Microsoft Edge";v="127", "Chromium";v="127"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

response = requests.get(
    'https://idmsa.apple.com/appleauth/auth/authorize/signin?frame_id=auth-v5so9kto-e0ad-pysh-ednn-w1m8x9bl&skVersion=7&iframeId=auth-v5so9kto-e0ad-pysh-ednn-w1m8x9bl&client_id=af1139274f266b22b68c2a3e7ad932cb3c0bbe854e13a79af78dcc73136882c3&redirect_uri=https://appleid.apple.com&response_type=code&response_mode=web_message&state=auth-v5so9kto-e0ad-pysh-ednn-w1m8x9bl&authVersion=latest',
    cookies=cookies,
    headers=headers,
)
scnt_2 = response.headers["scnt"]
aasp =  response.cookies.get('aasp')
X_Apple_Auth_Attributes =  response.headers['X-Apple-Auth-Attributes']
logging.info(f'scnt_2----{scnt_2}')
logging.info(f'aasp----{aasp}')
logging.info(f'X_Apple_Auth_Attributes----{X_Apple_Auth_Attributes}')


# 缺两个gs





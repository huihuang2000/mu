import requests
import re
import logging
logging.basicConfig(level=logging.INFO)
# -------------------------------开头的307请求重定向----------------------------------------------
cookies = {
    'as_rumid': '713659ab-5b7d-4a99-ab37-caddb52fb928',
    'pt-dm': 'v1~x~tgu4kwv1~m~3',
}

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'no-cache',
    # 'cookie': 'as_rumid=713659ab-5b7d-4a99-ab37-caddb52fb928; pt-dm=v1~x~tgu4kwv1~m~3',
    'pragma': 'no-cache',
    'priority': 'u=0, i',
    'sec-ch-ua': '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
}

response_1 = requests.get('https://secure8.store.apple.com/shop/account/home', cookies=cookies, headers=headers, allow_redirects=False)
x_shred = response_1.headers['x-shred']
logging.info(x_shred)
logging.info(f'第一步只返回了个x_shred'+("-"*200))
# -------------------------------这一步取出来的ssi没用-----------------------------------------------------

cookies = {
    'as_rumid': '713659ab-5b7d-4a99-ab37-caddb52fb928',
    'pt-dm': 'v1~x~tgu4kwv1~m~3',
}

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'no-cache',
    # 'cookie': 'as_rumid=713659ab-5b7d-4a99-ab37-caddb52fb928; pt-dm=v1~x~tgu4kwv1~m~3',
    'pragma': 'no-cache',
    'priority': 'u=0, i',
    'sec-ch-ua': '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
}

response_2 = requests.get('https://secure.store.apple.com/shop/account/home', cookies=cookies, headers=headers, allow_redirects=False)

CK = response_2.headers.get('Set-Cookie')
dssid2_match = re.search(r"dssid2=([a-z0-9\-]+);", CK)
as_pcts_match = re.search(r"as_pcts=([^;]+);", CK)

dssid2 = dssid2_match.group(1)
as_pcts = as_pcts_match.group(1)
# ssi = response_2.headers['Location']
logging.info(dssid2)
logging.info(as_pcts)
# logging.info(ssi)
logging.info(f'第二步返回dssid2,,as_pcts'+('-'*200))

# ------------------------------------第三步返回dssid2,,ssi----------------------------------------------------------------------------------------------

cookies = {
    'as_rumid': '713659ab-5b7d-4a99-ab37-caddb52fb928',
    'pt-dm': 'v1~x~tgu4kwv1~m~3',
    'dssid2': dssid2,
    'dssf': '1',
    'as_pcts': as_pcts,
    'as_dc': 'ucp3',
}

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'no-cache',
    # 'cookie': 'as_rumid=713659ab-5b7d-4a99-ab37-caddb52fb928; pt-dm=v1~x~tgu4kwv1~m~3; dssid2=3f1742da-9200-43bf-9fc3-5b516e1d112b; dssf=1; as_pcts=GKnuwS9zgCkVw7tNZXfZCOFLOBRmYmGaivs3:Aek7do_sxLivxKUo5dNDGviGybS:tL7-pn6D0femWhe-OzHUWpRY3CvEp3uc7q-KOkHvOzG_-M_yvq-S2axBghxDkNC5qmUNBhN9YGzNXTPHMh291VfN5D8WVT6aPIWhuQ_6EFyfeRXPSt; as_dc=ucp3',
    'pragma': 'no-cache',
    'priority': 'u=0, i',
    'sec-ch-ua': '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
}

response_3 = requests.get('https://secure6.store.apple.com/shop/account/home', cookies=cookies, headers=headers, allow_redirects=False)
CK = response_3.headers.get('Set-Cookie')
dssid2_match = re.search(r"dssid2=([a-z0-9\-]+);", CK)

dssid2 = dssid2_match.group(1)
ssi = response_3.headers['Location']
logging.info(dssid2)
logging.info(ssi)
logging.info(f'第三步返回dssid2,,ssi'+('-'*200))

# ---------------------------------第四步返回dssid2--x_aos_stk-----------------------------------------------------------------------------------------------

cookies = {
    'as_rumid': '713659ab-5b7d-4a99-ab37-caddb52fb928',
    'pt-dm': 'v1~x~tgu4kwv1~m~3',
    'dssid2': dssid2,
    'dssf': '1',
    'as_pcts': as_pcts,
    'as_dc': 'ucp3',
}

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'no-cache',
    # 'cookie': 'as_rumid=713659ab-5b7d-4a99-ab37-caddb52fb928; pt-dm=v1~x~tgu4kwv1~m~3; dssid2=3f1742da-9200-43bf-9fc3-5b516e1d112b; dssf=1; as_pcts=GKnuwS9zgCkVw7tNZXfZCOFLOBRmYmGaivs3:Aek7do_sxLivxKUo5dNDGviGybS:tL7-pn6D0femWhe-OzHUWpRY3CvEp3uc7q-KOkHvOzG_-M_yvq-S2axBghxDkNC5qmUNBhN9YGzNXTPHMh291VfN5D8WVT6aPIWhuQ_6EFyfeRXPSt; as_dc=ucp3',
    'pragma': 'no-cache',
    'priority': 'u=0, i',
    'sec-ch-ua': '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
}

response_4 = requests.get(ssi, cookies=cookies, headers=headers)
CK = response_4.headers.get('Set-Cookie')
x_aos_stk_value = re.search(r'"x-aos-stk":"([^"]+)"', response_4.text)
dssid2_match = re.search(r"dssid2=([a-z0-9\-]+);", CK)
x_aos_stk = x_aos_stk_value.group(1)
dssid2 = dssid2_match.group(1)
logging.info(dssid2)
logging.info(x_aos_stk)
logging.info(f'第四步返回dssid2,,x_aos_stk'+('-'*200))
# ---------------------------------第五步请求了个很可疑的403---------------------------------------------------------------------------------------------------

cookies = {
    'as_rumid': '713659ab-5b7d-4a99-ab37-caddb52fb928',
    'dssid2': dssid2,
    'dssf': '1',
    'as_pcts': as_pcts,
    'as_dc': 'ucp3',
    'as_sfa': 'Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE',#此处的是个问题点
    'geo': 'CN',
    'pxro': '1',
}

headers = {
    'accept': '*/*',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'no-cache',
    # 'cookie': 'as_rumid=713659ab-5b7d-4a99-ab37-caddb52fb928; dssid2=3f1742da-9200-43bf-9fc3-5b516e1d112b; dssf=1; as_pcts=GKnuwS9zgCkVw7tNZXfZCOFLOBRmYmGaivs3:Aek7do_sxLivxKUo5dNDGviGybS:tL7-pn6D0femWhe-OzHUWpRY3CvEp3uc7q-KOkHvOzG_-M_yvq-S2axBghxDkNC5qmUNBhN9YGzNXTPHMh291VfN5D8WVT6aPIWhuQ_6EFyfeRXPSt; as_dc=ucp3; as_sfa=Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE; geo=CN; pxro=1',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': ssi,
    'sec-ch-ua': '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
}

params = {
    'src': 'globalnav',
    'locale': 'en_US',
}

response_5 = requests.get(
    'https://secure6.store.apple.com/search-services/suggestions/defaultlinks/',
    params=params,
    cookies=cookies,
    headers=headers,
)
logging.info(response_5)
logging.info(f'第五步403'+('-'*200))

# ---------------------------------第六步拿了个aasp----X_Apple_Auth_Attributes---scnt-------------------------------------------------------------------------------------


cookies = {
    'as_rumid': '713659ab-5b7d-4a99-ab37-caddb52fb928',
    'dssid2': dssid2,
    'dssf': '1',
    'as_pcts': as_pcts,
    'as_dc': 'ucp3',
    'as_sfa': 'Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE',
    'geo': 'CN',
    'pxro': '1',
    's_fid': '6323376718433557-371662D1A66E1B14',
    's_cc': 'true',
}

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    # 'Cookie': 'as_rumid=713659ab-5b7d-4a99-ab37-caddb52fb928; dssid2=3f1742da-9200-43bf-9fc3-5b516e1d112b; dssf=1; as_pcts=GKnuwS9zgCkVw7tNZXfZCOFLOBRmYmGaivs3:Aek7do_sxLivxKUo5dNDGviGybS:tL7-pn6D0femWhe-OzHUWpRY3CvEp3uc7q-KOkHvOzG_-M_yvq-S2axBghxDkNC5qmUNBhN9YGzNXTPHMh291VfN5D8WVT6aPIWhuQ_6EFyfeRXPSt; as_dc=ucp3; as_sfa=Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE; geo=CN; pxro=1; s_fid=6323376718433557-371662D1A66E1B14; s_cc=true',
    'Pragma': 'no-cache',
    'Referer': 'https://secure6.store.apple.com/',
    'Sec-Fetch-Dest': 'iframe',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-site',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

response_6 = requests.get(
    'https://idmsa.apple.com/appleauth/auth/authorize/signin?frame_id=auth-sb36y35c-nirc-wgmc-2kzu-mdiax2hg&language=en_US&skVersion=7&iframeId=auth-sb36y35c-nirc-wgmc-2kzu-mdiax2hg&client_id=a797929d224abb1cc663bb187bbcd02f7172ca3a84df470380522a7c6092118b&redirect_uri=https://secure6.store.apple.com&response_type=code&response_mode=web_message&state=auth-sb36y35c-nirc-wgmc-2kzu-mdiax2hg&authVersion=latest',
    cookies=cookies,
    headers=headers,
)

CK = response_6.headers.get('Set-Cookie')
aasp = re.search(r"aasp=([a-zA-Z0-9\-]+);", CK)
aasp = aasp.group(1)

X_Apple_Auth_Attributes = response_6.headers.get('X-Apple-Auth-Attributes')
scnt = response_6.headers['scnt']
logging.info(aasp)
logging.info(X_Apple_Auth_Attributes)
logging.info(scnt)

# --------------------------------------------第七步叠加登录取myacinfo-----------------------------------------------------------------------------------------------------------
name = "freesia.e-fpb@softbank.ne.jp"
pwd = "Aa147369"

# 
url = "https://env-00jxgsqva6td.dev-hz.cloudbasefunction.cn/A1?type=1"
payload = {f"email": {name}}
Key = requests.request("POST", url, data=payload).json()
print("1-生成key---", Key)
print("*" * 100)
# =========================================================================================================================================
cookies = {
    'as_rumid': '713659ab-5b7d-4a99-ab37-caddb52fb928',
    'dssid2': dssid2,
    'dssf': '1',
    'as_pcts': as_pcts,
    'as_dc': 'ucp3',
    'as_sfa': 'Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE',
    'geo': 'CN',
    'pxro': '1',
    's_fid': '6323376718433557-371662D1A66E1B14',
    's_cc': 'true',
    's_vi': '[CS]v1|332AA8C7A36C871F-40000E40A15E97D6[CE]',
    'dslang': 'US-EN',
    'site': 'USA',
    'aasp': aasp,
    'aa': '1B99A552487EA314F1CE4E8E4291BC46',
}
headers = {"Accept": "application/json, text/javascript, */*; q=0.01"}
json_data = {
    "a": Key["r"],
    "accountName": name,
    "protocols": [
        "s2k",
        "s2k_fo",
    ],
}
response_2 = requests.post(
    "https://idmsa.apple.com/appleauth/auth/signin/init",
    headers=headers,
    json=json_data,
    cookies=cookies
).json()
print("2-获取key---", response_2)
print("*" * 100)
# =========================================================================================================================================
url = "https://env-00jxgsqva6td.dev-hz.cloudbasefunction.cn/A1?type=2"
payload = {
    "email": name,
    "iterations": response_2["iteration"],
    "Value": response_2["b"],
    "salt": response_2["salt"],
    "password": pwd,
    "protocol": response_2["protocol"],
    "privateHexValue": Key["privateHexValue"],
    "publicHexValue": Key["publicHexValue"],
}
response_3 = requests.request("POST", url, json=payload).json()
print("3-加密所有加密参数---", response_3)
print("*" * 100)
# =========================================================================================================================================
cookies = {
    'as_rumid': '713659ab-5b7d-4a99-ab37-caddb52fb928',
    'dssid2': dssid2,
    'dssf': '1',
    'as_pcts': as_pcts,
    'as_dc': 'ucp3',
    'as_sfa': 'Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE',
    'geo': 'CN',
    'pxro': '1',
    's_fid': '6323376718433557-371662D1A66E1B14',
    's_cc': 'true',
    's_vi': '[CS]v1|332AA8C7A36C871F-40000E40A15E97D6[CE]',
    'dslang': 'US-EN',
    'site': 'USA',
    'aasp': aasp,
    'aa': '1B99A552487EA314F1CE4E8E4291BC46',
}

headers = {
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "X-Apple-OAuth-Client-Id": "a797929d224abb1cc663bb187bbcd02f7172ca3a84df470380522a7c6092118b",
    "X-Apple-OAuth-Redirect-URI": "https://secure6.store.apple.com",
    "X-Apple-OAuth-Response-Type": "code",
}
json_data = {
    "accountName": name,
    "rememberMe": False,
    "m1": response_3["M1"],
    "c": response_2["c"],
    "m2": response_3["M2"],
}
response_4 = requests.post(
    "https://idmsa.apple.com/appleauth/auth/signin/complete",
    headers=headers,
    json=json_data,
    cookies=cookies
)
CK = response_4.headers.get('Set-Cookie')
myacinfo_pattern = re.compile(r"myacinfo=([^;]+)")
myacinfo_match = myacinfo_pattern.search(CK)
myacinfo = myacinfo_match.group(1)
# -------------------------------------------第八步-----------------------------------------------------------------------------------------------


extracted_part = ssi.split('shop/signIn/account?ssi=')[1]
cookies = {
    'as_rumid': '713659ab-5b7d-4a99-ab37-caddb52fb928',
    'dssid2': dssid2,
    'dssf': '1',
    'as_pcts': as_pcts,
    'as_dc': 'ucp3',
    'as_sfa': 'Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE',
    'geo': 'CN',
    'pxro': '1',
    's_fid': '6323376718433557-371662D1A66E1B14',
    's_cc': 'true',
    's_vi': '[CS]v1|332AA8C7A36C871F-40000E40A15E97D6[CE]',
    'dslang': 'US-EN',
    'site': 'USA',
    'myacinfo': myacinfo,
}

headers = {
    'accept': '*/*',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'no-cache',
    'content-type': 'application/x-www-form-urlencoded',
    # 'cookie': 'as_rumid=713659ab-5b7d-4a99-ab37-caddb52fb928; dssid2=3f1742da-9200-43bf-9fc3-5b516e1d112b; dssf=1; as_pcts=GKnuwS9zgCkVw7tNZXfZCOFLOBRmYmGaivs3:Aek7do_sxLivxKUo5dNDGviGybS:tL7-pn6D0femWhe-OzHUWpRY3CvEp3uc7q-KOkHvOzG_-M_yvq-S2axBghxDkNC5qmUNBhN9YGzNXTPHMh291VfN5D8WVT6aPIWhuQ_6EFyfeRXPSt; as_dc=ucp3; as_sfa=Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE; geo=CN; pxro=1; s_fid=6323376718433557-371662D1A66E1B14; s_cc=true; s_vi=[CS]v1|332AA8C7A36C871F-40000E40A15E97D6[CE]; dslang=US-EN; site=USA; myacinfo=DAWTKNV323952cf8084a204fb20ab2508441a07d02d37c69aef65d485a43bbb3d0aa4d589f0dc0abcfa0bfc59f8e36b20c34a1fc1e70d3adf31dac3ee471af55cdee2e5bf945bf61ba5499c9194ae74a80afd75697a09222cc7ec782e90c960209ae74528cfd315d0a302c92bb369076b13a9bdef89dc0695eb0aacb547f57fa9328b03fbf8e99879a0c22dc1f96557221d83e6de254fb37e16925e2e06e28e6aed25b2995cea2d9a6888f2abb63a6ba1ffdceb84b826b0eedcee3ebe12e305709fc837d037d4e5a6afb4391a26c957d32f9d8ca5ed310bd0258bf0f8904fff36c246888990c552f2d2862bc0f00086e4b27488be36a6b9aa9222874db44c9c7b3783f8fd55939cc8d084e7cda991beff0cbec32414360124492e432580e3c423d13adc2a90b52bbff24622cb74c333db53bbd696579c97c0eb4efd7afa075064940c44d630842ebddad91b67456bdf6826456196099e9bdc0de4bca9c1f5d9e84d79b688f5359bd270ab4ca98bbced70a679a6c29c8fb9ff668191c9cd7ec697fd2aee2619d7f202cdd80eccac2b2a1acee602224086d73869a9e27142f17c81f6cfd8ad0d10ccff5133e5dbf64ef610930ecd2070ec499a3204b7382df5a7eab03be5142a09a5fbe92bf705edd9eb89ad3249086d106730ac740d46f142c750a99e0e519e1473ed3f7d4438f60f961c213d383484b585a47V3',
    'modelversion': 'v2',
    'origin': 'https://secure6.store.apple.com',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': ssi,
    'sec-ch-ua': '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'syntax': 'graviton',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
    'x-aos-model-page': 'idmsSignInPage',
    'x-aos-stk': x_aos_stk,
    'x-requested-with': 'Fetch',
}

params = {
    'ssi': extracted_part,
}

data = {
    'deviceID': 'TF1;015;;;;;;;;;;;;;;;;;;;;;;Mozilla;Netscape;5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit/537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome/124.0.0.0%20Safari/537.36;20030107;undefined;true;;true;Win32;undefined;Mozilla/5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit/537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome/124.0.0.0%20Safari/537.36;zh-CN;undefined;secure6.store.apple.com;undefined;undefined;undefined;undefined;false;false;1716867481875;8;2005/6/7%2021%3A33%3A44;1920;1080;;;;;;;;-480;-480;2024/5/28%2011%3A38%3A01;24;1920;1032;0;0;;;;;;;;;;;;;;;;;;;25;',
    'grantCode': '',
}

response_8 = requests.post(
    'https://secure6.store.apple.com/shop/signIn/idms/authx',
    params=params,
    cookies=cookies,
    headers=headers,
    data=data,
)
set_cookie_header = response_8.headers.get('Set-Cookie', '')
dssid2_match = re.search(r"dssid2=([a-zA-Z0-9\-]+)", set_cookie_header)
as_cn_match = re.search(r"as_cn=(.+?);", set_cookie_header)
as_disa_match = re.search(r"as_disa=(.+?);", set_cookie_header)
as_ltn_us_match = re.search(r"as_ltn_us=(.+?);", set_cookie_header)
as_rec_match = re.search(r"as_rec=(.+?);", set_cookie_header)

dssid2 = dssid2_match.group(1) if dssid2_match else None
as_cn = as_cn_match.group(1) if as_cn_match else None
as_disa = as_disa_match.group(1) if as_disa_match else None
as_ltn_us_1 = as_ltn_us_match.group(1) if as_ltn_us_match else None
as_rec = as_rec_match.group(1) if as_rec_match else None

logging.info(f"dssid2_2: {dssid2}")
logging.info(f"as_cn: {as_cn}")
logging.info(f"as_disa: {as_disa}")
logging.info(f"as_ltn_us: {as_ltn_us_1}")
logging.info(f"as_rec: {as_rec}")
logging.info('-'*200)



# ---------------------------------------第九步拿上面的开始转换第一次---------------------------------------------------------------------------------------

cookies = {
    'as_rumid': '713659ab-5b7d-4a99-ab37-caddb52fb928',
    'dssid2': dssid2,
    'dssf': '1',
    'as_pcts': as_pcts,
    'as_dc': 'ucp3',
    'as_sfa': 'Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE',
    'geo': 'CN',
    'pxro': '1',
    's_fid': '6323376718433557-371662D1A66E1B14',
    's_cc': 'true',
    's_vi': '[CS]v1|332AA8C7A36C871F-40000E40A15E97D6[CE]',
    'dslang': 'US-EN',
    'site': 'USA',
    'as_cn': as_cn,
    'as_disa': as_disa,
    'as_ltn_us': as_ltn_us_1,
    'as_rec': as_rec,
    'pt-dm': 'v1~x~tgu4kwv1~m~3~n~AOS%3A%20Checkout%20Sign%20In~r~aos%3Aaccount',
}

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'no-cache',
    # 'cookie': 'as_rumid=713659ab-5b7d-4a99-ab37-caddb52fb928; dssid2=3f1742da-9200-43bf-9fc3-5b516e1d112b; dssf=1; as_pcts=GKnuwS9zgCkVw7tNZXfZCOFLOBRmYmGaivs3:Aek7do_sxLivxKUo5dNDGviGybS:tL7-pn6D0femWhe-OzHUWpRY3CvEp3uc7q-KOkHvOzG_-M_yvq-S2axBghxDkNC5qmUNBhN9YGzNXTPHMh291VfN5D8WVT6aPIWhuQ_6EFyfeRXPSt; as_dc=ucp3; as_sfa=Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE; geo=CN; pxro=1; s_fid=6323376718433557-371662D1A66E1B14; s_cc=true; s_vi=[CS]v1|332AA8C7A36C871F-40000E40A15E97D6[CE]; dslang=US-EN; site=USA; as_cn=~o64i6uZb4PuY27kIPLY3lh6XZD-jepmeS9EPzQFZZPM=; as_disa=AAAjAAABB70hXJVUL-660b8UPj220WS1tuvryuPcxlWLVSCS8nDC4YGhJ2gTDfJ2vMeDHSLlAAIB851deBiNzcfmem3_mMiYl8Dey3kuVOBxica3eM1t9ZM=; as_ltn_us=AAQEAMKJLZW5pKfoKiKOOOTwF2xa164mMMSuroB-utAy7N1qsFiMarBxBVDj4ULggLnRjbxRhxKlh4UcfSL0DSUzS5vUqHdrqfQ; as_rec=cbbe13d4421486187cedcc78d8b8a00ffcca98e351e82d721be410449961e5b6839d1341120593db4a446210b7c6004cf4635238904a6d8ec97c021203cea6f444ee39972eba8939ca4519e34deb490e; pt-dm=v1~x~tgu4kwv1~m~3~n~AOS%3A%20Checkout%20Sign%20In~r~aos%3Aaccount',
    'pragma': 'no-cache',
    'priority': 'u=0, i',
    'referer': ssi,
    'sec-ch-ua': '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
}

response_9 = requests.get('https://secure6.store.apple.com/shop/account/home', cookies=cookies, headers=headers)
set_cookie_header = response_9.headers.get('Set-Cookie', '')
dssid2_match = re.search(r"dssid2=([a-zA-Z0-9\-]+)", set_cookie_header)
as_ltn_us_match = re.search(r"as_ltn_us=(.+?);", set_cookie_header)
dssid2 = dssid2_match.group(1) if dssid2_match else None
as_ltn_us_2 = as_ltn_us_match.group(1) if as_ltn_us_match else None

logging.info(f"dssid2_2: {dssid2}")
logging.info(f"home_as_ltn_us: {as_ltn_us_2}")
logging.info('-'*200)

# -----------------------------------------第十步估计是过检测-----------------------------------------------------------------------------------------------

cookies = {
    'xp_aostkn': 'xVXefVuS8R-_X6o783kD98LxrdT3Y8LxrdT3YwA',#此处怀疑
    'as_rumid': '713659ab-5b7d-4a99-ab37-caddb52fb928',
    'dssid2': dssid2,
    'dssf': '1',
    'as_pcts': as_pcts,
    'as_sfa': 'Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE',
    'geo': 'CN',
    'pxro': '1',
    's_cc': 'true',
    'dslang': 'US-EN',
    'site': 'USA',
    'as_cn': as_cn,
    's_fid': '6CDDD52C21065486-3346E9DAB52C8CE9',
    's_vi': '[CS]v1|332ABCD5F8E1638B-400017842FB7A4DE[CE]',
    'as_dc': 'ucp4',
    's_sq': '%5B%5BB%5D%5D',
    'as_disa': as_disa,
    'as_rec': as_rec,
    'as_ltn_us': as_ltn_us_2,
}

headers = {
    'accept': '*/*',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'no-cache',
    # 'content-length': '4531',
    'content-type': 'application/json; charset=utf-8',
    # 'cookie': 'xp_aostkn=xVXefVuS8R-_X6o783kD98LxrdT3Y8LxrdT3YwA; as_rumid=713659ab-5b7d-4a99-ab37-caddb52fb928; dssid2=3f1742da-9200-43bf-9fc3-5b516e1d112b; dssf=1; as_pcts=GKnuwS9zgCkVw7tNZXfZCOFLOBRmYmGaivs3:Aek7do_sxLivxKUo5dNDGviGybS:tL7-pn6D0femWhe-OzHUWpRY3CvEp3uc7q-KOkHvOzG_-M_yvq-S2axBghxDkNC5qmUNBhN9YGzNXTPHMh291VfN5D8WVT6aPIWhuQ_6EFyfeRXPSt; as_sfa=Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE; geo=CN; pxro=1; s_cc=true; dslang=US-EN; site=USA; as_cn=~o64i6uZb4PuY27kIPLY3lh6XZD-jepmeS9EPzQFZZPM=; s_fid=6CDDD52C21065486-3346E9DAB52C8CE9; s_vi=[CS]v1|332ABCD5F8E1638B-400017842FB7A4DE[CE]; as_dc=ucp4; s_sq=%5B%5BB%5D%5D; as_disa=AAAjAAAB4B0xQPa0UWRJi2Nf80ssPodQFWp7cTAfGMBkCzHygoYyeMROHNSi6YFP1g9B9NGEAAIBB-t7mxwy_ZWgcSlfWS0NCnzul8tg7tq3zuwtLzrFeo8=; as_rec=cdf1980926bda61948e0bc5ad0933f6963dca330370e674479a63781c91767de877bed41430ecdec2a6669796e23757f84a76bfbb4a662d40ce25b2c2df0b76c81f972e862e9c391005db0be9b4443db; as_ltn_us=AAQEAMOqkJ6QzrELg5EgH1lFtDbvCYnTpEuKi350zsKVEl0WfFiMarBxBVDj4ULggLnRjbxTus6CXkBmuLii_ot-GG3oq_ZkY4Q',
    'origin': 'https://secure7.store.apple.com',
    'pragma': 'no-cache',
    'priority': 'u=4, i',
    'referer': 'https://secure7.store.apple.com/',
    'sec-ch-ua': '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
}

response_10 = requests.post('https://xp.apple.com/report/2/xp_aos_clientperf', cookies=cookies, headers=headers)

# --------------------------------------404再过一遍-----------------------------------------------------------------------------------------------------------
cookies = {
    'as_rumid': '713659ab-5b7d-4a99-ab37-caddb52fb928',
    'dssid2': dssid2,
    'dssf': '1',
    'as_pcts': as_pcts,
    'as_sfa': 'Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE',
    'geo': 'CN',
    'pxro': '1',
    's_cc': 'true',
    'dslang': 'US-EN',
    'site': 'USA',
    'as_cn': as_cn,
    's_fid': '6CDDD52C21065486-3346E9DAB52C8CE9',
    's_vi': '[CS]v1|332ABCD5F8E1638B-400017842FB7A4DE[CE]',
    'as_dc': 'ucp4',
    's_sq': '%5B%5BB%5D%5D',
    'as_disa': as_disa,
    'as_rec': as_rec,
    'as_ltn_us': as_ltn_us_2,
}

headers = {
    'accept': '*/*',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'no-cache',
    # 'cookie': 'as_rumid=713659ab-5b7d-4a99-ab37-caddb52fb928; dssid2=3f1742da-9200-43bf-9fc3-5b516e1d112b; dssf=1; as_pcts=GKnuwS9zgCkVw7tNZXfZCOFLOBRmYmGaivs3:Aek7do_sxLivxKUo5dNDGviGybS:tL7-pn6D0femWhe-OzHUWpRY3CvEp3uc7q-KOkHvOzG_-M_yvq-S2axBghxDkNC5qmUNBhN9YGzNXTPHMh291VfN5D8WVT6aPIWhuQ_6EFyfeRXPSt; as_sfa=Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE; geo=CN; pxro=1; s_cc=true; dslang=US-EN; site=USA; as_cn=~o64i6uZb4PuY27kIPLY3lh6XZD-jepmeS9EPzQFZZPM=; s_fid=6CDDD52C21065486-3346E9DAB52C8CE9; s_vi=[CS]v1|332ABCD5F8E1638B-400017842FB7A4DE[CE]; as_dc=ucp4; s_sq=%5B%5BB%5D%5D; as_disa=AAAjAAAB4B0xQPa0UWRJi2Nf80ssPodQFWp7cTAfGMBkCzHygoYyeMROHNSi6YFP1g9B9NGEAAIBB-t7mxwy_ZWgcSlfWS0NCnzul8tg7tq3zuwtLzrFeo8=; as_rec=cdf1980926bda61948e0bc5ad0933f6963dca330370e674479a63781c91767de877bed41430ecdec2a6669796e23757f84a76bfbb4a662d40ce25b2c2df0b76c81f972e862e9c391005db0be9b4443db; as_ltn_us=AAQEAMOqkJ6QzrELg5EgH1lFtDbvCYnTpEuKi350zsKVEl0WfFiMarBxBVDj4ULggLnRjbxTus6CXkBmuLii_ot-GG3oq_ZkY4Q',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://secure7.store.apple.com/shop/account/home',
    'sec-ch-ua': '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
}

params = {
    'src': 'globalnav',
    'locale': 'en_US',
}

response = requests.get(
    'https://secure7.store.apple.com/search-services/suggestions/defaultlinks/',
    params=params,
    cookies=cookies,
    headers=headers,
)

# ---------------------------------------第十一步开始转换第一次-------------------------------------------------------------------------------------------

cookies = {
    'as_rumid': '713659ab-5b7d-4a99-ab37-caddb52fb928',
    'dssid2': dssid2,
    'dssf': '1',
    'as_pcts': as_pcts,
    'as_sfa': 'Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE',
    'geo': 'CN',
    'pxro': '1',
    's_cc': 'true',
    'dslang': 'US-EN',
    'site': 'USA',
    'as_cn': as_cn,
    's_fid': '6CDDD52C21065486-3346E9DAB52C8CE9',
    's_vi': '[CS]v1|332AC4C3C85BFB44-40001D14E2C77ABD[CE]',
    'as_dc': 'ucp3',
    's_sq': '%5B%5BB%5D%5D',
    'as_disa': as_disa,
    'as_rec': as_rec,
    'as_ltn_us': as_ltn_us_2,
}

headers = {
    'accept': '*/*',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'no-cache',
    # 'content-length': '0',
    'content-type': 'application/x-www-form-urlencoded',
    # 'cookie': 'as_rumid=713659ab-5b7d-4a99-ab37-caddb52fb928; dssid2=3f1742da-9200-43bf-9fc3-5b516e1d112b; dssf=1; as_pcts=GKnuwS9zgCkVw7tNZXfZCOFLOBRmYmGaivs3:Aek7do_sxLivxKUo5dNDGviGybS:tL7-pn6D0femWhe-OzHUWpRY3CvEp3uc7q-KOkHvOzG_-M_yvq-S2axBghxDkNC5qmUNBhN9YGzNXTPHMh291VfN5D8WVT6aPIWhuQ_6EFyfeRXPSt; as_sfa=Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE; geo=CN; pxro=1; s_cc=true; dslang=US-EN; site=USA; as_cn=~o64i6uZb4PuY27kIPLY3lh6XZD-jepmeS9EPzQFZZPM=; s_fid=6CDDD52C21065486-3346E9DAB52C8CE9; s_vi=[CS]v1|332AC4C3C85BFB44-40001D14E2C77ABD[CE]; as_dc=ucp3; s_sq=%5B%5BB%5D%5D; as_disa=AAAjAAABESl6Gelh5qYHenmDlrY9SFtnHPCjoM3awfyeMx2LQ5vJKvrm4l1ytrvMb6fx4hAPAAIBQ6A6QR_WXf60INAUYrvdgVlFMIfMhT9_Mw5AzECMaqc=; as_rec=139b9689928d9577ac9e902fce9e7d174635cbf81191a2d24a08be282a0f1cc821018d2df815e39f32b46ebfdcbc42c37f1fc0cf67f09ad6f1ec1a3e230e414124cd3b0a06faa9cf370868fdf8d9416b; as_ltn_us=AAQEAMK5nzlVZLGKRQDonKU56DdjiHj5d2HOci9j3wE_wiFFWFiMarBxBVDj4ULggLnRjbxRAetqkjGkX05P4DsSeIqPnwvWCMw',
    'modelversion': 'v2',
    'origin': 'https://secure6.store.apple.com',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://secure6.store.apple.com/shop/account/home',
    'sec-ch-ua': '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'syntax': 'graviton',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
    'x-aos-model-page': 'RetailHome',
    'x-aos-stk': x_aos_stk,
    'x-requested-with': 'Fetch',
}

params = {
    '_a': 'fetchDashboard',
    '_m': 'home.dashboards',
}

response_11 = requests.post('https://secure6.store.apple.com/shop/accounthomex', params=params, cookies=cookies, headers=headers)

set_cookie_header = response_11.headers.get('Set-Cookie', '')
dssid2_match = re.search(r"dssid2=([a-zA-Z0-9\-]+)", set_cookie_header)
as_ltn_us_match = re.search(r"as_ltn_us=(.+?);", set_cookie_header)
dssid2 = dssid2_match.group(1) if dssid2_match else None
as_ltn_us_3 = as_ltn_us_match.group(1) if as_ltn_us_match else None

logging.info(f"dssid2: {dssid2}")
logging.info(f"fetchDashboard: {as_ltn_us_3}")
logging.info('-'*200)

# ---------------------------------------第十二步开始转换第二次,此处估计是检测，生成但是不用-------------------------------------------------------------------------------------------

cookies = {
    'as_rumid': '713659ab-5b7d-4a99-ab37-caddb52fb928',
    'dssid2': dssid2,
    'dssf': '1',
    'as_pcts': as_pcts,
    'as_sfa': 'Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE',
    'geo': 'CN',
    'pxro': '1',
    's_cc': 'true',
    'dslang': 'US-EN',
    'site': 'USA',
    'as_cn': as_cn,
    's_fid': '6CDDD52C21065486-3346E9DAB52C8CE9',
    's_vi': '[CS]v1|332AC4C3C85BFB44-40001D14E2C77ABD[CE]',
    'as_dc': 'ucp3',
    's_sq': '%5B%5BB%5D%5D',
    'as_disa': as_disa,
    'as_rec': as_rec,
    'as_ltn_us': as_ltn_us_2,
}

headers = {
    'accept': '*/*',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'no-cache',
    # 'content-length': '0',
    'content-type': 'application/x-www-form-urlencoded',
    # 'cookie': 'as_rumid=713659ab-5b7d-4a99-ab37-caddb52fb928; dssid2=3f1742da-9200-43bf-9fc3-5b516e1d112b; dssf=1; as_pcts=GKnuwS9zgCkVw7tNZXfZCOFLOBRmYmGaivs3:Aek7do_sxLivxKUo5dNDGviGybS:tL7-pn6D0femWhe-OzHUWpRY3CvEp3uc7q-KOkHvOzG_-M_yvq-S2axBghxDkNC5qmUNBhN9YGzNXTPHMh291VfN5D8WVT6aPIWhuQ_6EFyfeRXPSt; as_sfa=Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE; geo=CN; pxro=1; s_cc=true; dslang=US-EN; site=USA; as_cn=~o64i6uZb4PuY27kIPLY3lh6XZD-jepmeS9EPzQFZZPM=; s_fid=6CDDD52C21065486-3346E9DAB52C8CE9; s_vi=[CS]v1|332AC4C3C85BFB44-40001D14E2C77ABD[CE]; as_dc=ucp3; s_sq=%5B%5BB%5D%5D; as_disa=AAAjAAABESl6Gelh5qYHenmDlrY9SFtnHPCjoM3awfyeMx2LQ5vJKvrm4l1ytrvMb6fx4hAPAAIBQ6A6QR_WXf60INAUYrvdgVlFMIfMhT9_Mw5AzECMaqc=; as_rec=139b9689928d9577ac9e902fce9e7d174635cbf81191a2d24a08be282a0f1cc821018d2df815e39f32b46ebfdcbc42c37f1fc0cf67f09ad6f1ec1a3e230e414124cd3b0a06faa9cf370868fdf8d9416b; as_ltn_us=AAQEAMK5nzlVZLGKRQDonKU56DdjiHj5d2HOci9j3wE_wiFFWFiMarBxBVDj4ULggLnRjbxRAetqkjGkX05P4DsSeIqPnwvWCMw',
    'modelversion': 'v2',
    'origin': 'https://secure6.store.apple.com',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://secure6.store.apple.com/shop/account/home',
    'sec-ch-ua': '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'syntax': 'graviton',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
    'x-aos-model-page': 'RetailHome',
    'x-aos-stk': x_aos_stk,
    'x-requested-with': 'Fetch',
}

params = {
    '_a': 'fetchDevices',
    '_m': 'home.devices',
}

response_12 = requests.post('https://secure6.store.apple.com/shop/accounthomex', params=params, cookies=cookies, headers=headers)
# logging.info(response_12.headers)

# ---------------------------------------第十三步开始转换第三次-------------------------------------------------------------------------------------------
cookies = {
    'as_rumid': '713659ab-5b7d-4a99-ab37-caddb52fb928',
    'dssid2': dssid2,
    'dssf': '1',
    'as_pcts': as_pcts,
    'as_sfa': 'Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE',
    'geo': 'CN',
    'pxro': '1',
    's_cc': 'true',
    'dslang': 'US-EN',
    'site': 'USA',
    'as_cn': as_cn,
    's_fid': '6CDDD52C21065486-3346E9DAB52C8CE9',
    's_vi': '[CS]v1|332AC4C3C85BFB44-40001D14E2C77ABD[CE]',
    'as_dc': 'ucp3',
    'as_disa': as_disa,
    'as_rec': as_rec,
    'as_ltn_us': as_ltn_us_3,
    's_sq': 'applestoreww%3D%2526c.%2526a.%2526activitymap.%2526page%253DAOS%25253A%252520account%25252Fhome%2526link%253Deditedit%252520shipping%252520address%252520%252528inner%252520text%252529%252520%25257C%252520no%252520href%252520%25257C%252520body%2526region%253Dbody%2526pageIDType%253D1%2526.activitymap%2526.a%2526.c%2526pid%253DAOS%25253A%252520account%25252Fhome%2526pidt%253D1%2526oid%253Dfunctionkd%252528%252529%25257B%25257D%2526oidt%253D2%2526ot%253DBUTTON',
}

headers = {
    'accept': '*/*',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'no-cache',
    # 'content-length': '0',
    'content-type': 'application/x-www-form-urlencoded',
    # 'cookie': 'as_rumid=713659ab-5b7d-4a99-ab37-caddb52fb928; dssid2=3f1742da-9200-43bf-9fc3-5b516e1d112b; dssf=1; as_pcts=GKnuwS9zgCkVw7tNZXfZCOFLOBRmYmGaivs3:Aek7do_sxLivxKUo5dNDGviGybS:tL7-pn6D0femWhe-OzHUWpRY3CvEp3uc7q-KOkHvOzG_-M_yvq-S2axBghxDkNC5qmUNBhN9YGzNXTPHMh291VfN5D8WVT6aPIWhuQ_6EFyfeRXPSt; as_sfa=Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE; geo=CN; pxro=1; s_cc=true; dslang=US-EN; site=USA; as_cn=~o64i6uZb4PuY27kIPLY3lh6XZD-jepmeS9EPzQFZZPM=; s_fid=6CDDD52C21065486-3346E9DAB52C8CE9; s_vi=[CS]v1|332AC4C3C85BFB44-40001D14E2C77ABD[CE]; as_dc=ucp3; as_disa=AAAjAAABESl6Gelh5qYHenmDlrY9SFtnHPCjoM3awfyeMx2LQ5vJKvrm4l1ytrvMb6fx4hAPAAIBQ6A6QR_WXf60INAUYrvdgVlFMIfMhT9_Mw5AzECMaqc=; as_rec=139b9689928d9577ac9e902fce9e7d174635cbf81191a2d24a08be282a0f1cc821018d2df815e39f32b46ebfdcbc42c37f1fc0cf67f09ad6f1ec1a3e230e414124cd3b0a06faa9cf370868fdf8d9416b; as_ltn_us=AAQEAMK5nzlVZLGKRQDonKU56DdjdInGST0N_zx9hvsoNOmEkFiMarBxBVDj4ULggLnRjbxRIv-TTJiI5LTlQhhCiXPtPQ5UpeQ; s_sq=applestoreww%3D%2526c.%2526a.%2526activitymap.%2526page%253DAOS%25253A%252520account%25252Fhome%2526link%253Deditedit%252520shipping%252520address%252520%252528inner%252520text%252529%252520%25257C%252520no%252520href%252520%25257C%252520body%2526region%253Dbody%2526pageIDType%253D1%2526.activitymap%2526.a%2526.c%2526pid%253DAOS%25253A%252520account%25252Fhome%2526pidt%253D1%2526oid%253Dfunctionkd%252528%252529%25257B%25257D%2526oidt%253D2%2526ot%253DBUTTON',
    'modelversion': 'v2',
    'origin': 'https://secure6.store.apple.com',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://secure6.store.apple.com/shop/account/home',
    'sec-ch-ua': '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'syntax': 'graviton',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
    'x-aos-model-page': 'RetailHome',
    'x-aos-stk': x_aos_stk,
    'x-requested-with': 'Fetch',
}

params = {
    '_a': 'editAddress',
    '_m': 'home.customerAccount.shippingInfo.shippingAddress',
}

response_13 = requests.post('https://secure6.store.apple.com/shop/accounthomex', params=params, cookies=cookies, headers=headers)
set_cookie_header = response_13.headers.get('Set-Cookie', '')
dssid2_match = re.search(r"dssid2=([a-zA-Z0-9\-]+)", set_cookie_header)
as_ltn_us_match = re.search(r"as_ltn_us=(.+?);", set_cookie_header)
dssid2 = dssid2_match.group(1) if dssid2_match else None
as_ltn_us_4 = as_ltn_us_match.group(1) if as_ltn_us_match else None

logging.info(f"dssid2: {dssid2}")
logging.info(f"editAddress: {as_ltn_us_4}")
logging.info('-'*200)

# --------------------------------第十四步开始转换第四次-这个转出来直接提交-----------------------------------------------------------------------------------------------------------

cookies = {
    'as_rumid': '713659ab-5b7d-4a99-ab37-caddb52fb928',
    'dssid2': dssid2,
    'dssf': '1',
    'as_pcts': as_pcts,
    'as_sfa': 'Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE',
    'geo': 'CN',
    'pxro': '1',
    's_cc': 'true',
    'dslang': 'US-EN',
    'site': 'USA',
    'as_cn': as_cn,
    's_fid': '6CDDD52C21065486-3346E9DAB52C8CE9',
    's_vi': '[CS]v1|332AC4C3C85BFB44-40001D14E2C77ABD[CE]',
    'as_dc': 'ucp3',
    'as_disa': as_disa,
    'as_rec': as_rec,
    's_sq': '%5B%5BB%5D%5D',
    'as_ltn_us': as_ltn_us_4,
}

headers = {
    'accept': '*/*',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'no-cache',
    # 'content-length': '0',
    'content-type': 'application/x-www-form-urlencoded',
    # 'cookie': 'as_rumid=713659ab-5b7d-4a99-ab37-caddb52fb928; dssid2=3f1742da-9200-43bf-9fc3-5b516e1d112b; dssf=1; as_pcts=GKnuwS9zgCkVw7tNZXfZCOFLOBRmYmGaivs3:Aek7do_sxLivxKUo5dNDGviGybS:tL7-pn6D0femWhe-OzHUWpRY3CvEp3uc7q-KOkHvOzG_-M_yvq-S2axBghxDkNC5qmUNBhN9YGzNXTPHMh291VfN5D8WVT6aPIWhuQ_6EFyfeRXPSt; as_sfa=Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE; geo=CN; pxro=1; s_cc=true; dslang=US-EN; site=USA; as_cn=~o64i6uZb4PuY27kIPLY3lh6XZD-jepmeS9EPzQFZZPM=; s_fid=6CDDD52C21065486-3346E9DAB52C8CE9; s_vi=[CS]v1|332AC4C3C85BFB44-40001D14E2C77ABD[CE]; as_dc=ucp3; as_disa=AAAjAAABESl6Gelh5qYHenmDlrY9SFtnHPCjoM3awfyeMx2LQ5vJKvrm4l1ytrvMb6fx4hAPAAIBQ6A6QR_WXf60INAUYrvdgVlFMIfMhT9_Mw5AzECMaqc=; as_rec=139b9689928d9577ac9e902fce9e7d174635cbf81191a2d24a08be282a0f1cc821018d2df815e39f32b46ebfdcbc42c37f1fc0cf67f09ad6f1ec1a3e230e414124cd3b0a06faa9cf370868fdf8d9416b; s_sq=%5B%5BB%5D%5D; as_ltn_us=AAQEAMK5nzlVZLGKRQDonKU56Ddg6dpHwPUuUqMH88oVBKnnKFiMarBxBVDj4ULggLnRjbxQ7D2mnanQjAqS2Gkw10t8CKWQcsQ',
    'modelversion': 'v2',
    'origin': 'https://secure6.store.apple.com',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://secure6.store.apple.com/shop/account/home',
    'sec-ch-ua': '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'syntax': 'graviton',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
    'x-aos-model-page': 'RetailHome',
    'x-aos-stk': x_aos_stk,
    'x-requested-with': 'Fetch',
}

params = {
    '_a': 'fetchDashboard',
    '_m': 'home.dashboards',
}

response_14 = requests.post('https://secure6.store.apple.com/shop/accounthomex', params=params, cookies=cookies, headers=headers)
set_cookie_header = response_14.headers.get('Set-Cookie', '')
dssid2_match = re.search(r"dssid2=([a-zA-Z0-9\-]+)", set_cookie_header)
as_ltn_us_match = re.search(r"as_ltn_us=(.+?);", set_cookie_header)
dssid2 = dssid2_match.group(1) if dssid2_match else None
as_ltn_us_5 = as_ltn_us_match.group(1) if as_ltn_us_match else None

logging.info(f"dssid2: {dssid2}")
logging.info(f"editAddress: {as_ltn_us_5}")
logging.info('-'*200)


# -------------------------------------------提交--------------------------------------------------------------------------------------------------

cookies = {
    'as_rumid': '713659ab-5b7d-4a99-ab37-caddb52fb928',
    'dssid2': dssid2,
    'dssf': '1',
    'as_pcts': as_pcts,
    'as_sfa': 'Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE',
    'geo': 'CN',
    'pxro': '1',
    's_cc': 'true',
    'dslang': 'US-EN',
    'site': 'USA',
    'as_cn': as_cn,
    's_fid': '6CDDD52C21065486-3346E9DAB52C8CE9',
    's_vi': '[CS]v1|332AC4C3C85BFB44-40001D14E2C77ABD[CE]',
    'as_dc': 'ucp3',
    'as_disa': as_disa,
    'as_rec': as_rec,
    'as_ltn_us': "AAQEAMF5INEOBnF-gjqHy2IIn4b3hwRK6pSBEyZOH19w6zbIPFiMarBxBVDj4ULggLnRjbxRGQYOlBN_ygSs5WU8jw0mWJP9v-A",
    's_sq': '%5B%5BB%5D%5D',
}

headers = {
    'accept': '*/*',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'no-cache',
    'content-type': 'application/x-www-form-urlencoded',
    # 'cookie': 'as_rumid=713659ab-5b7d-4a99-ab37-caddb52fb928; dssid2=3f1742da-9200-43bf-9fc3-5b516e1d112b; dssf=1; as_pcts=GKnuwS9zgCkVw7tNZXfZCOFLOBRmYmGaivs3:Aek7do_sxLivxKUo5dNDGviGybS:tL7-pn6D0femWhe-OzHUWpRY3CvEp3uc7q-KOkHvOzG_-M_yvq-S2axBghxDkNC5qmUNBhN9YGzNXTPHMh291VfN5D8WVT6aPIWhuQ_6EFyfeRXPSt; as_sfa=Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE; geo=CN; pxro=1; s_cc=true; dslang=US-EN; site=USA; as_cn=~o64i6uZb4PuY27kIPLY3lh6XZD-jepmeS9EPzQFZZPM=; s_fid=6CDDD52C21065486-3346E9DAB52C8CE9; s_vi=[CS]v1|332AC4C3C85BFB44-40001D14E2C77ABD[CE]; as_dc=ucp3; as_disa=AAAjAAABESl6Gelh5qYHenmDlrY9SFtnHPCjoM3awfyeMx2LQ5vJKvrm4l1ytrvMb6fx4hAPAAIBQ6A6QR_WXf60INAUYrvdgVlFMIfMhT9_Mw5AzECMaqc=; as_rec=139b9689928d9577ac9e902fce9e7d174635cbf81191a2d24a08be282a0f1cc821018d2df815e39f32b46ebfdcbc42c37f1fc0cf67f09ad6f1ec1a3e230e414124cd3b0a06faa9cf370868fdf8d9416b; as_ltn_us=AAQEAMK5nzlVZLGKRQDonKU56DdjjIv6R367lFfriEaYUXB2UFiMarBxBVDj4ULggLnRjbxTqHuR5uF7Ig23URWYTGsj1u6pKWA; s_sq=%5B%5BB%5D%5D',
    'modelversion': 'v2',
    'origin': 'https://secure6.store.apple.com',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://secure6.store.apple.com/shop/account/home',
    'sec-ch-ua': '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'syntax': 'graviton',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
    'x-aos-model-page': 'RetailHome',
    'x-aos-stk': x_aos_stk,
    'x-requested-with': 'Fetch',
}

params = {
    '_a': 'address-submit',
    '_m': 'home.customerAccount.shippingInfo.shippingAddress.editShippingAddress.editAddress',
}

data = 'home.customerAccount.shippingInfo.shippingAddress.editShippingAddress.editAddress.fullDaytimePhone=(861)%20111-7777&home.customerAccount.shippingInfo.shippingAddress.editShippingAddress.editAddress.street2=212231312&home.customerAccount.shippingInfo.shippingAddress.editShippingAddress.editAddress.lastName=lllll3333&home.customerAccount.shippingInfo.shippingAddress.editShippingAddress.editAddress.firstName=hhhjjj11166666&home.customerAccount.shippingInfo.shippingAddress.editShippingAddress.editAddress.companyName=122332&home.customerAccount.shippingInfo.shippingAddress.editShippingAddress.editAddress.street=88888888888&home.customerAccount.shippingInfo.shippingAddress.editShippingAddress.editAddress.zipLookup.city=Albany&home.customerAccount.shippingInfo.shippingAddress.editShippingAddress.editAddress.zipLookup.state=NY&home.customerAccount.shippingInfo.shippingAddress.editShippingAddress.editAddress.zipLookup.postalCode=11111-4444&home.customerAccount.shippingInfo.shippingAddress.editShippingAddress.editAddress.zipLookup.countryCode=US'

response = requests.post(
    'https://secure6.store.apple.com/shop/accounthomex',
    params=params,
    cookies=cookies,
    headers=headers,
    data=data,
)
logging.info(response.headers)
import requests
import re

# # ===========================================================================================================================================
name = "freesia.e-fpb@softbank.ne.jp"
pwd = "Aa147369"
# # ===========================================================================================================================================
url = "https://env-00jxgsqva6td.dev-hz.cloudbasefunction.cn/A1?type=1"
payload = {f"email": {name}}
Key = requests.request("POST", url, data=payload).json()
print("1-生成key---", Key)
print("*" * 100)
# # =========================================================================================================================================
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
).json()
print("2-获取key---", response_2)
print("*" * 100)
# # =========================================================================================================================================
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
# # =========================================================================================================================================
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
)

set_cookie_header = response_4.headers.get('Set-Cookie')
match = re.search(r'myacinfo=([^;]+)', set_cookie_header)
myacinfo_value = match.group(1)

print("4-myacinfo_value---", myacinfo_value)
print("*" * 100)
# #======================================================================
"""
取ssi链接
"""
response = requests.get(
    "https://secure6.store.apple.com/shop/account/home", allow_redirects=False
)
ssi = response.headers["Location"]
print("5-ssi链接---", ssi)
print("*" * 100)
# =========================================================================================================================================
"""
拿as_disa,  as_ltn_us, 

"""
cookies = {
    "dssid2": "3c76019f-d1c3-412c-becd-51617ae5822b",
    "dssf": "1",
    "myacinfo": myacinfo_value,
}

headers = {
    "accept": "*/*",
    "referer": ssi,
    "x-aos-stk": x_aos_stk_value,
    "x-requested-with": "Fetch",
}

params = {
    "ssi": "1AAABj67qXUAg_m2SCkQnbKgldue2wzKuQB9tw7rH0WQ80xU4t8SO63wAAAAzaHR0cHM6Ly9zZWN1cmU2LnN0b3JlLmFwcGxlLmNvbS9zaG9wL2FjY291bnQvaG9tZXx8AAIBXLK9tOoydUGosx3RAtxKIT4txDgzKk-9PUD7Pkbf4zU",
}

data = {
    "deviceID": "TF1;015;;;;;;;;;;;;;;;;;;;;;;Mozilla;Netscape;5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit/537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome/125.0.0.0%20Safari/537.36%20Edg/125.0.0.0;20030107;undefined;true;;true;Win32;undefined;Mozilla/5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit/537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome/125.0.0.0%20Safari/537.36%20Edg/125.0.0.0;zh-CN;undefined;secure6.store.apple.com;undefined;undefined;undefined;undefined;false;false;1716626572003;8;2005/6/7%2021%3A33%3A44;1920;1080;;;;;;;;-480;-480;2024/5/25%2016%3A42%3A52;24;1920;1032;0;0;;;;;;;;;;;;;;;;;;;25;",
    "grantCode": "",
}

response = requests.post(
    "https://secure6.store.apple.com/shop/signIn/idms/authx",
    params=params,
    cookies=cookies,
    headers=headers,
    data=data,
)
print("7-x_aos_stk_value---", response.headers)




set_cookie_header = response.headers.get('Set-Cookie')
if set_cookie_header:
    as_disa_match = re.search(r'as_disa=([^;]+)', set_cookie_header)
    as_ltn_us_match = re.search(r'as_ltn_us=([^;]+)', set_cookie_header)

as_disa = as_disa_match.group(1)
as_ltn_us = as_ltn_us_match.group(1)

print("*" * 100)

# ============================================================================================================================================

"""
那ssi链当Referer
"""

url = "https://secure6.store.apple.com/shop/account/home"

headers = {
    # "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    # "accept-language": "zh-CN,zh;q=0.9",
    # "cache-control": "no-cache",
    # "dnt": "1",
    # "pragma": "no-cache",
    # "priority": "u=0, i",
    "referer": ssi,
    # "sec-fetch-dest": "document",
    # "sec-fetch-mode": "navigate",
    # "sec-fetch-site": "same-origin",
    # "sec-fetch-user": "?1",
    # "upgrade-insecure-requests": "1",
    # "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0",
    "Cookie": "dssid2=3c76019f-d1c3-412c-becd-51617ae5822b; as_disa=AAAjAAABp2MJttRYpk2tYJ7roqdhfGJExv0fTemjPSNFxml-_vnSBEk9a9k4SWwowrUvVfu4AAIBT4Pm2GB1f_EAraS6WO-Efw-n6JBDCQOCIQj3MS7jQc0=; as_rec=970b7aaa96759d2a383188a9c653851f6774c268ed7d21880b3ce1126738bc52ac37cf302e205f61d7f708a427f3a968e3ea0180e099d72cc48305153e45c7cf5c60193a8110c69638996b1d333a9d62; as_ltn_us=AAQEAMKyKZaTcxh5MoRJQZxamIoxo-YvK0XdMx7iZFVxPwyiRFiMarBxBVDj4ULggLnRjbxRtyCn348dbIBJNFYnQIIuqLiFwJQ; pt-dm=v1~x~ejkf9q1s~m~3~n~AOS: account/home~r~aos:account"
}

response = requests.request("GET", url, headers=headers)


print(response.headers)
match = re.search(r'"x-aos-stk":"([^"]+)"', response.text)
x_aos_stk_value = match.group(1)
print("6-x_aos_stk_value---", x_aos_stk_value)
print("*" * 100)

# ======================================================================

# ===========================================================================
"""
最终的更改资料
"""
# cookies = {
#     'dssid2': "3c76019f-d1c3-412c-becd-51617ae5822b",
#     'dssf': '1',
#     'as_disa': as_disa,
#     'as_ltn_us': as_ltn_us,
# }

# headers = {
#     'x-aos-stk': x_aos_stk_value,
#     'x-requested-with': 'Fetch',
# }

# params = {
#     '_a': 'address-submit',
#     '_m': 'home.customerAccount.shippingInfo.shippingAddress.editShippingAddress.editAddress',
# }

# data = 'home.customerAccount.shippingInfo.shippingAddress.editShippingAddress.editAddress.fullDaytimePhone=(861)%11111-9873&home.customerAccount.shippingInfo.shippingAddress.editShippingAddress.editAddress.street2=6666666&home.customerAccount.shippingInfo.shippingAddress.editShippingAddress.editAddress.lastName=lllll3333&home.customerAccount.shippingInfo.shippingAddress.editShippingAddress.editAddress.firstName=hhhjjj11111111&home.customerAccount.shippingInfo.shippingAddress.editShippingAddress.editAddress.companyName=122332&home.customerAccount.shippingInfo.shippingAddress.editShippingAddress.editAddress.street=33333333333&home.customerAccount.shippingInfo.shippingAddress.editShippingAddress.editAddress.zipLookup.city=Albany&home.customerAccount.shippingInfo.shippingAddress.editShippingAddress.editAddress.zipLookup.state=NY&home.customerAccount.shippingInfo.shippingAddress.editShippingAddress.editAddress.zipLookup.postalCode=12234&home.customerAccount.shippingInfo.shippingAddress.editShippingAddress.editAddress.zipLookup.countryCode=US'

# response = requests.post(
#     'https://secure6.store.apple.com/shop/accounthomex',
#     params=params,
#     cookies=cookies,
#     headers=headers,
#     data=data,
# )
# print(response.text)









# ======================================================================================================================

import requests

cookies = {
    'dssid2': '3c76019f-d1c3-412c-becd-51617ae5822b',
    'dssf': '1',
    # 'as_pcts': 'wVefwk3fAtaMhI0uxIbShIDrgGkRRNu06ZIoZThu6wdlZjmPQquuXByrITcLOKUTO3efPD5dG6wZpwIYClhl1XBxgp01GC2_3VC3wXr_pqp46aswrvKs7N80c_yQyJ9nAYNHaKDsQugMfmp_ijoHlDLhlcE1LVC00GxG6:Mnte8PpPtnryL',
    # 'as_sfa': 'Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE',
    # 'geo': 'CN',
    # 's_cc': 'true',
    # 'as_rumid': '45119418-d117-4bea-a135-095a202f1528',
    # 'pxro': '1',
    # 'dslang': 'US-EN',
    # 'site': 'USA',
    # 'at_check': 'true',
    # 'as_cn': '~yssISysoRYLTGHdV-nqslI7aA35Y8W5N91dY81VaOJc=',
    # 'as_dc': 'ucp3',
    # 's_fid': '05ABCEBA483F1FD9-0C8615B6715BF63E',
    # 's_vi': '[CS]v1|3328E1C2262DEB4E-400002262B4956CA[CE]',
    'as_disa': as_disa,
    # 'as_rec': 'c845bbdd7f5080e33b5b030b3b2ebcb1140b2e6283978bb9b48a6bece853b9b56e0c7046bbed30e740f9901c2dbc2e86eca65173e3aecda6bee4383c5775c12508fb31b35bea3140d6fe304da5122eed',
    'as_ltn_us': 'AAQEAMKyKZaTcxh5MoRJQZxamIow_-j5ldOT-zNr6XPRgLZ5GFiMarBxBVDj4ULggLnRjbxTzECa8mWU2Dn-lT-S8QuRHD8Wjlw',
    # 's_sq': '%5B%5BB%5D%5D',
}

headers = {
    # 'accept': '*/*',
    # 'accept-language': 'zh-CN,zh;q=0.9',
    # 'cache-control': 'no-cache',
    'content-type': 'application/x-www-form-urlencoded',
    # 'cookie': 'dssid2=3c76019f-d1c3-412c-becd-51617ae5822b; dssf=1; as_pcts=wVefwk3fAtaMhI0uxIbShIDrgGkRRNu06ZIoZThu6wdlZjmPQquuXByrITcLOKUTO3efPD5dG6wZpwIYClhl1XBxgp01GC2_3VC3wXr_pqp46aswrvKs7N80c_yQyJ9nAYNHaKDsQugMfmp_ijoHlDLhlcE1LVC00GxG6:Mnte8PpPtnryL; as_sfa=Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE; geo=CN; s_cc=true; as_rumid=45119418-d117-4bea-a135-095a202f1528; pxro=1; dslang=US-EN; site=USA; at_check=true; as_cn=~yssISysoRYLTGHdV-nqslI7aA35Y8W5N91dY81VaOJc=; as_dc=ucp3; s_fid=05ABCEBA483F1FD9-0C8615B6715BF63E; s_vi=[CS]v1|3328E1C2262DEB4E-400002262B4956CA[CE]; as_disa=AAAjAAABIv31ClLYR4RdQE8G65cFnd2RQ9PStywvHtlyY46kBjmhg2T95dqRW88HbTy74OQTAAIBZF5z5KL_8gdNVfzfZRYnZ05CcMq6j0IAcJ-R38poJG0=; as_rec=c845bbdd7f5080e33b5b030b3b2ebcb1140b2e6283978bb9b48a6bece853b9b56e0c7046bbed30e740f9901c2dbc2e86eca65173e3aecda6bee4383c5775c12508fb31b35bea3140d6fe304da5122eed; as_ltn_us=AAQEAMJBWtWMz4CehbUB_YjdBhcXCPsa8aR9RXIvPubsLj9GMFiMarBxBVDj4ULggLnRjbxT-dvNwB-Fnjo1KGkT3vu9RKG_TMA; s_sq=%5B%5BB%5D%5D',
    # 'dnt': '1',
    # 'modelversion': 'v2',
    # 'origin': 'https://secure6.store.apple.com',
    # 'pragma': 'no-cache',
    # 'priority': 'u=1, i',
    # 'referer': 'https://secure6.store.apple.com/shop/account/home',
    # 'sec-ch-ua': '"Microsoft Edge";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
    # 'sec-ch-ua-mobile': '?0',
    # 'sec-ch-ua-platform': '"Windows"',
    # 'sec-fetch-dest': 'empty',
    # 'sec-fetch-mode': 'cors',
    # 'sec-fetch-site': 'same-origin',
    # 'syntax': 'graviton',
    # 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0',
    # 'x-aos-model-page': 'RetailHome',
    'x-aos-stk': x_aos_stk_value,
    'x-requested-with': 'Fetch',
}

params = {
    '_a': 'address-submit',
    '_m': 'home.customerAccount.shippingInfo.shippingAddress.editShippingAddress.editAddress',
}

data = 'home.customerAccount.shippingInfo.shippingAddress.editShippingAddress.editAddress.fullDaytimePhone=(861)%11111-1243&home.customerAccount.shippingInfo.shippingAddress.editShippingAddress.editAddress.street2=212231312&home.customerAccount.shippingInfo.shippingAddress.editShippingAddress.editAddress.lastName=lllll3333&home.customerAccount.shippingInfo.shippingAddress.editShippingAddress.editAddress.firstName=hhhjjj1111111&home.customerAccount.shippingInfo.shippingAddress.editShippingAddress.editAddress.companyName=122332&home.customerAccount.shippingInfo.shippingAddress.editShippingAddress.editAddress.street=88888888888&home.customerAccount.shippingInfo.shippingAddress.editShippingAddress.editAddress.zipLookup.city=Albany&home.customerAccount.shippingInfo.shippingAddress.editShippingAddress.editAddress.zipLookup.state=NY&home.customerAccount.shippingInfo.shippingAddress.editShippingAddress.editAddress.zipLookup.postalCode=12234&home.customerAccount.shippingInfo.shippingAddress.editShippingAddress.editAddress.zipLookup.countryCode=US'

response = requests.post(
    'https://secure6.store.apple.com/shop/accounthomex',
    params=params,
    cookies=cookies,
    headers=headers,
    data=data,
)
print(response.text)
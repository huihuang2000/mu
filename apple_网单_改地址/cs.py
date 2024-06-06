import requests,re

cookies = {
    'dssid2': '9f8a1375-fe4a-4dd8-b092-b901b14c70f2',
    'dssf': '1',
    'as_dc': 'ucp4',
    'as_pcts': 'wKzq1VVoj8tWNtdR4pFOA-iroduUOgKwfFNXr+v7r2ZWBatYP-oTbKaQ4orj0fqj1hZ46H+h7z:HVfMT-QgEovuoz4-22pg_Z8_dgt2cvSzWQfGcsF4x7Kn1LZX+6qIk-vrLRLbVw:j4OpDnWIO4yzh+YtnyPy400mW5UnzS6bkV3b-NyJzMB:7O',
    'as_sfa': 'Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE',
    'geo': 'CN',
    's_fid': '5DCB07D277DD9855-0E6BBED71DA9D505',
    's_cc': 'true',
    's_vi': '[CS]v1|3330EF22F1DF4A5E-400010501790B29E[CE]',
    'as_rumid': '9a867f65-f7f0-4d8c-89de-1642443834e4',
    's_sq': '%5B%5BB%5D%5D',
    'pxro': '1',
    'dslang': 'US-EN',
    'site': 'USA',
    'myacinfo': 'DAWTKNV323952cf8084a204fb20ab2508441a07d02d3c41be3a700cd5d9a82c64a22b2b567588636af6a52a2927d8848c53ef6cf0a36764bfc76a903adf21188932616f447f8c5adaa22c062d6611da93b9f44dbb1d96d5d1bab69da973044172c35495abb5b4275ccf46f1510a25fa2ffe1b431149c10196893541516a8d170cac09229218157480f190795d04a84ee388dff6e7a5ccf9f6e054101bd2430d9d1a2234848de3942ba741a66aa2df7d4550dc78f41e59fb03278bf668f1d45687e60e5af86a711ff1e1ab6662c8faf61319e923fe25cfd26bdbcbe77493167f1a9635412a8f1491ba18c939dc2d457838dd54ed51a5b084d6491eb9dc03628f41c40625e5ea221bf2661c5df0d34ebe848fe81fefc0d2f38ce2c2a7ec7cbb92418320457cdb2b142c0932d1ae5009ab8c852b7fcead7b2036b784bf8c818b98e2e94223c4ec43ba7df1fde432e17854b9b4b32de0256b27a73ec2ff6d79f4420d79e811d376bbcafdf1533119985e88b2f33009d1b3a9e9ceb9d389c7bc8fc792a65ffb23acb9a5920a7197c33c76ecfec58dac6c2d46c8d8e39a263f1aa8b95be734d8e9f060adb04351439bee3667108e88851fef1fd08783faa6d807f2f8dd5a9fdeaed776da457dceb0a23a59ad604477d6be70b37a4b8ed827e56279e70b389af99ce54f21f25106420112d54aba303d11f6e23585a47V3',
}

headers = {
    'accept': '*/*',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'no-cache',
    'content-type': 'application/x-www-form-urlencoded',
    # 'cookie': 'dssid2=9f8a1375-fe4a-4dd8-b092-b901b14c70f2; dssf=1; as_dc=ucp4; as_pcts=wKzq1VVoj8tWNtdR4pFOA-iroduUOgKwfFNXr+v7r2ZWBatYP-oTbKaQ4orj0fqj1hZ46H+h7z:HVfMT-QgEovuoz4-22pg_Z8_dgt2cvSzWQfGcsF4x7Kn1LZX+6qIk-vrLRLbVw:j4OpDnWIO4yzh+YtnyPy400mW5UnzS6bkV3b-NyJzMB:7O; as_sfa=Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE; geo=CN; s_fid=5DCB07D277DD9855-0E6BBED71DA9D505; s_cc=true; s_vi=[CS]v1|3330EF22F1DF4A5E-400010501790B29E[CE]; as_rumid=9a867f65-f7f0-4d8c-89de-1642443834e4; s_sq=%5B%5BB%5D%5D; pxro=1; dslang=US-EN; site=USA; myacinfo=DAWTKNV323952cf8084a204fb20ab2508441a07d02d3c41be3a700cd5d9a82c64a22b2b567588636af6a52a2927d8848c53ef6cf0a36764bfc76a903adf21188932616f447f8c5adaa22c062d6611da93b9f44dbb1d96d5d1bab69da973044172c35495abb5b4275ccf46f1510a25fa2ffe1b431149c10196893541516a8d170cac09229218157480f190795d04a84ee388dff6e7a5ccf9f6e054101bd2430d9d1a2234848de3942ba741a66aa2df7d4550dc78f41e59fb03278bf668f1d45687e60e5af86a711ff1e1ab6662c8faf61319e923fe25cfd26bdbcbe77493167f1a9635412a8f1491ba18c939dc2d457838dd54ed51a5b084d6491eb9dc03628f41c40625e5ea221bf2661c5df0d34ebe848fe81fefc0d2f38ce2c2a7ec7cbb92418320457cdb2b142c0932d1ae5009ab8c852b7fcead7b2036b784bf8c818b98e2e94223c4ec43ba7df1fde432e17854b9b4b32de0256b27a73ec2ff6d79f4420d79e811d376bbcafdf1533119985e88b2f33009d1b3a9e9ceb9d389c7bc8fc792a65ffb23acb9a5920a7197c33c76ecfec58dac6c2d46c8d8e39a263f1aa8b95be734d8e9f060adb04351439bee3667108e88851fef1fd08783faa6d807f2f8dd5a9fdeaed776da457dceb0a23a59ad604477d6be70b37a4b8ed827e56279e70b389af99ce54f21f25106420112d54aba303d11f6e23585a47V3',
    'dnt': '1',
    'modelversion': 'v2',
    'origin': 'https://secure7.store.apple.com',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://secure7.store.apple.com/shop/signIn/orders?hgl=t&ssi=1AAABj-5MRQ4gROGHv2Gipb8U59vcQaOMOym98_8vkjiWuqSUsgkXzXsAAABFaHR0cHM6Ly9zZWN1cmU3LnN0b3JlLmFwcGxlLmNvbS9zaG9wL29yZGVyL2RldGFpbC8xMDA3OC9XMTA0NzAwMTM2Mnx8AAIBDK6mh8XdiXTLa0SKsQ1eTJP4dzDnk2rRsyDo6HM1rx0',
    'sec-ch-ua': '"Microsoft Edge";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'syntax': 'graviton',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0',
    'x-aos-model-page': 'olssSignInPage',
    'x-aos-stk': 'YbPANeULtyMvwiFg13tS58SBaaYozY4fjdN81pJnrXk',
    'x-requested-with': 'Fetch',
}

params = {
    'ssi': '1AAABj-5MRQ4gROGHv2Gipb8U59vcQaOMOym98_8vkjiWuqSUsgkXzXsAAABFaHR0cHM6Ly9zZWN1cmU3LnN0b3JlLmFwcGxlLmNvbS9zaG9wL29yZGVyL2RldGFpbC8xMDA3OC9XMTA0NzAwMTM2Mnx8AAIBDK6mh8XdiXTLa0SKsQ1eTJP4dzDnk2rRsyDo6HM1rx0',
}

data = {
    'deviceID': 'TF1;015;;;;;;;;;;;;;;;;;;;;;;Mozilla;Netscape;5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit/537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome/125.0.0.0%20Safari/537.36%20Edg/125.0.0.0;20030107;undefined;true;;true;Win32;undefined;Mozilla/5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit/537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome/125.0.0.0%20Safari/537.36%20Edg/125.0.0.0;zh-CN;undefined;secure7.store.apple.com;undefined;undefined;undefined;undefined;false;false;1717689939649;8;2005/6/7%2021%3A33%3A44;1920;1080;;;;;;;;-480;-480;2024/6/7%2000%3A05%3A39;24;1920;1032;0;0;;;;;;;;;;;;;;;;;;;25;',
    'grantCode': '',
}

response = requests.post(
    'https://secure7.store.apple.com/shop/signIn/idms/authx',
    params=params,
    cookies=cookies,
    headers=headers,
    data=data,
)
set_cookie_header = response.headers.get("Set-Cookie", "")
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
print(f"dssid2_2: {dssid2}")
print(f"as_cn: {as_cn}")
print(f"as_disa: {as_disa}")
print(f"as_ltn_us: {as_ltn_us_1}")
print(f"as_rec: {as_rec}")
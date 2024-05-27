import requests
import re
import logging
#------------------------------
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
# -----------------------------------------------------------------------------------------------------------------------------
headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'DNT': '1',
    'Pragma': 'no-cache',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0',
    'sec-ch-ua': '"Microsoft Edge";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

response = requests.get('https://secure8.store.apple.com/shop/account/home', headers=headers, allow_redirects=False)

dssid2_pattern = r"dssid2=([a-z0-9\-]+);"
as_pcts_pattern = r"as_pcts=([^;]+);"

CK = response.headers.get('Set-Cookie')
dssid2_match = re.search(dssid2_pattern, CK)
as_pcts_match = re.search(as_pcts_pattern, CK)

dssid2_match = dssid2_match.group(1)
as_pcts_match = as_pcts_match.group(1)

ssi = response.headers['Location']

logging.info(f"dssid2: {dssid2_match}")
logging.info(f"as_pcts: {as_pcts_match}")
logging.info(f"ssi: {ssi}")
logging.info('-'*200)
# -------------------------------------------------------------------------------------------------------------------------------------

cookies = {
    'dssid2': dssid2_match,
    'dssf': '1',
    'as_pcts': as_pcts_match,
    'as_dc': 'ucp5',
}
headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    # 'Cookie': 'dssid2=9e7f53ef-1683-47d7-994a-26471c9e5f17; dssf=1; as_pcts=KLYIVPNazOZt:5M9yfOcgypngw9YrIMHMUD2KJgMDEZ58egA-owNzg2CBVmhB6eRjrSz6uNqdYnAL57xhM5gLjGL+mTgIszOTBgku35VL:GqZSvWohf:F6QcJl+1I22makrJ1rX5EfIE9wcLFdRMafdFX6YhucfeKSz-qwU9AlusF-ee7L4; as_dc=ucp5',
    'DNT': '1',
    'Pragma': 'no-cache',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0',
    'sec-ch-ua': '"Microsoft Edge";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

response = requests.get(ssi, cookies=cookies, headers=headers)

CK = response.headers.get('Set-Cookie')
dssid2_match = re.search(dssid2_pattern, CK)
dssid2_match = dssid2_match.group(1)

match = re.search(r'"x-aos-stk":"([^"]+)"', response.text)
x_aos_stk_value = match.group(1)

logging.info(f"dssid2_2: {dssid2_match}")
logging.info(f"x-aos-stk: {x_aos_stk_value}")
logging.info('-'*200)

# ------------------------------------------------------------------------------------------------------
extracted_part = ssi.split('shop/signIn/account?ssi=')[1]

cookies = {
    'dssid2': dssid2_match,
    'dssf': '1',
    'as_pcts': as_pcts_match,
    'as_dc': 'ucp5',
    'as_sfa': 'Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE',
    'geo': 'CN',
    'pxro': '1',
    's_fid': '22A68F50E3445E2D-0B08E505DA15764C',
    's_cc': 'true',
    's_vi': '[CS]v1|3329F7A9AA590FDA-40000A75B8C5D059[CE]',
    'dslang': 'US-EN',
    'site': 'USA',
    'as_rumid': '719045a8-955d-47e5-8d54-ceda7aea0529',
    'myacinfo': 'DAWTKNV323952cf8084a204fb20ab2508441a07d02d3c7d71978bc409cc4ffece5c89b717b07ca5e08256b880344d15ed60cd37bc0473321bc3685f390893c25a5ac1b16b686ba780889737810c55fa41aaa6e4c00354722937564063a046b274d3fe374e015a5b1ebc556cca0a8806aad57a1cec19ce61f20f45437b662245fd14d122d2d16ab55bbd68402f96c4eb225bb2587c09833b081387f9c57bcd32e7cd58d26fc4501a4f89cf64c81a98c58106f247c5faf3c56e8a7a62e64ef061a709e0d425b0deb8761f4d9a324eb3a7977ed498522c84bb9ff881650f2f22a0c6da2e0f67a3214219c667622cbee90ee27ac779ada23476d7e391f8a72f59e4094163930b6ec33b7650484ceb4379f47958bed803fddf4ada8c95584def3add8a852758faf3bc9477a0ce5015fcd091e1af680d1011bd3308576b050b9911c827f2c034d989e25bd41cdeda3822d35c436e8dd35c98568e088bc3faacaf7169c1f7aa2e3c42e1cc09934ce4afcb3f54b484e8be5279e729b8a9b66dbce43882d15ae9a774758b0f1cbb29c68e33f46a8230be944be852e4ab759bba524c20faa73c4195f236735135c3c5c1df1eea412b94781247a1737eed8d98b9bbde2b9d01d8d6f3d0731e3ea82cbb440c1cc2d0a4f3e7ff1ad4ae0c425c1d8cf0c0d2f40c87515834971e8fd861586c35ae759404c558f9427f8585a47V3',
}

headers = {
    'Accept': '*/*',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded',
    # 'Cookie': 'dssid2=9e7f53ef-1683-47d7-994a-26471c9e5f17; dssf=1; as_pcts=KLYIVPNazOZt:5M9yfOcgypngw9YrIMHMUD2KJgMDEZ58egA-owNzg2CBVmhB6eRjrSz6uNqdYnAL57xhM5gLjGL+mTgIszOTBgku35VL:GqZSvWohf:F6QcJl+1I22makrJ1rX5EfIE9wcLFdRMafdFX6YhucfeKSz-qwU9AlusF-ee7L4; as_dc=ucp5; as_sfa=Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE; geo=CN; pxro=1; s_fid=22A68F50E3445E2D-0B08E505DA15764C; s_cc=true; s_vi=[CS]v1|3329F7A9AA590FDA-40000A75B8C5D059[CE]; dslang=US-EN; site=USA; as_rumid=719045a8-955d-47e5-8d54-ceda7aea0529; myacinfo=DAWTKNV323952cf8084a204fb20ab2508441a07d02d3d6284851fcceaaee43cadf2307771a2949b15634eb12ca693db0332aa7c7bc03d2078e75bc584b6446120ea315358ae69b5ccbe6909fa44692ee2a19571cd2d3f9045c8e2ec56b05ae02ec75627cca119429e841cd823cd36b2d32c66a9d6b00049baef4365c6f4309553c5319ef83c2eec91c980c8cadd562014ae539d6922e3ad46dcce1ccd98fbbb823915092ca6b44ae96f6fb76a94805d8d6d56e310ee665945a7c6be0743ebd579d640dcfd67d5362587780b6273de7f2a688541c9aca8ca9b62a7e777ddab5a96f0d722e74a96a23a49ffeb7b6c01fe120ca6db3b48dc39561f0ba61271b673ff080ad5029326c72309b560410d489c214f6b35fa7a60785888cdc56765d79269eded9c47a1b486f7bfebe7ed2306a9aa96177e640063990c542f52135a6e39af6a2b75fe788855030a57a3da63a43f3d918b3614aef3cd034215e058ada26e20c3838d136b0ddd3e8bbc8cbd5c3607df3ce4294bd91e2b68930a7e72ba445434ff0e8bd608ac07a1a5b76293b1fc1070e721f80fcd00cd3c82201a1437d80c2a37abdc91fea54dfdf2420528d5b1ba586e36a77b91d1ac7d721ad8c32a27f6ec99b3d6f8fb7bbdb1377b93db2f315cac5bb41d82000f10b3bbc60b09480ccbbeefb28cdff764edff008dc1a3a1d9a69294884d34f47585a47V3',
    'DNT': '1',
    'Origin': 'https://secure8.store.apple.com',
    'Pragma': 'no-cache',
    'Referer': 'https://secure8.store.apple.com/shop/signIn/account?ssi=1AAABj7fe1-0gIonDWEhE3m91ymjGbBGrkdhh5TlCMdzwQMOEnsBWszEAAAAzaHR0cHM6Ly9zZWN1cmU4LnN0b3JlLmFwcGxlLmNvbS9zaG9wL2FjY291bnQvaG9tZXx8AAIBYDtWVxomHxk4s1c0H_sjRPBh-56GWaM9KXdktiAqrE0',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0',
    'X-Requested-With': 'Fetch',
    'modelVersion': 'v2',
    'sec-ch-ua': '"Microsoft Edge";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'syntax': 'graviton',
    'x-aos-model-page': 'idmsSignInPage',
    'x-aos-stk': x_aos_stk_value,
}

params = {
    'ssi': extracted_part,
}

data = {
    'deviceID': 'TF1;015;;;;;;;;;;;;;;;;;;;;;;Mozilla;Netscape;5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit/537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome/125.0.0.0%20Safari/537.36%20Edg/125.0.0.0;20030107;undefined;true;;true;Win32;undefined;Mozilla/5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit/537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome/125.0.0.0%20Safari/537.36%20Edg/125.0.0.0;zh-CN;undefined;secure8.store.apple.com;undefined;undefined;undefined;undefined;false;false;1716776801637;8;2005/6/7%2021%3A33%3A44;1920;1080;;;;;;;;-480;-480;2024/5/27%2010%3A26%3A41;24;1920;1032;0;0;;;;;;;;;;;;;;;;;;;25;',
    'grantCode': '',
}

response = requests.post(
    'https://secure8.store.apple.com/shop/signIn/idms/authx',
    params=params,
    cookies=cookies,
    headers=headers,
    data=data,
)
set_cookie_header = response.headers.get('Set-Cookie', '')
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
# ----------------------------------------------------------------------------------------------

cookies = {
    'dssid2': dssid2,
    'dssf': '1',
    'as_pcts': as_pcts_match,
    'as_dc': 'ucp5',
    'as_sfa': 'Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE',
    'geo': 'CN',
    'pxro': '1',
    's_cc': 'true',
    'dslang': 'US-EN',
    'site': 'USA',
    'as_rumid': '719045a8-955d-47e5-8d54-ceda7aea0529',
    'as_cn': as_cn,
    's_fid': '0C03C3941EF76CB8-2D4BC8F9C5ABD04F',
    's_sq': '%5B%5BB%5D%5D',
    's_vi': '[CS]v1|332A0324B56BF7F2-40000482215C9807[CE]',
    'as_disa': as_disa,
    'as_ltn_us': as_ltn_us_1,
    'as_rec': as_rec,
    'pt-dm': 'v1~x~z8iftd63~m~3~n~AOS%3A%20Checkout%20Sign%20In~r~aos%3Aaccount',
}

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'no-cache',
    # 'cookie': 'dssid2=9e7f53ef-1683-47d7-994a-26471c9e5f17; dssf=1; as_pcts=KLYIVPNazOZt:5M9yfOcgypngw9YrIMHMUD2KJgMDEZ58egA-owNzg2CBVmhB6eRjrSz6uNqdYnAL57xhM5gLjGL+mTgIszOTBgku35VL:GqZSvWohf:F6QcJl+1I22makrJ1rX5EfIE9wcLFdRMafdFX6YhucfeKSz-qwU9AlusF-ee7L4; as_dc=ucp5; as_sfa=Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE; geo=CN; pxro=1; s_cc=true; dslang=US-EN; site=USA; as_rumid=719045a8-955d-47e5-8d54-ceda7aea0529; as_cn=~o64i6uZb4PuY27kIPLY3lh6XZD-jepmeS9EPzQFZZPM=; s_fid=0C03C3941EF76CB8-2D4BC8F9C5ABD04F; s_sq=%5B%5BB%5D%5D; s_vi=[CS]v1|332A0324B56BF7F2-40000482215C9807[CE]; as_disa=AAAjAAABKWTOmbezbcnVaOIq-LKFIQJAFD5zkyzTCVEEoa9SUa--cTqCFgwdaGPelTgh3f2FAAIBV7T63YkcQHrHm6t6KLoaH5_LPtD4H-DlasE1jpoLbIU=; as_ltn_us=AAQEAMGioaqAVYLRQ4wp_MhwqIsnKpPvijGHX6r6fAKFgbHZRFiMarBxBVDj4ULggLnRjbxTCKqAK7GFkI9-t01ZP-D0Ml2RsWA; as_rec=d278f5e92d5c97e8dfb0375ba78318c4a38806e8d69bba04ce353e0a20edfdbda2482fecc9c6a1e7ef64241a9de8bf4d267b6f3339c9deba392ea047ea76b3623dc1789999faca835b8d968e2e9cae1b; pt-dm=v1~x~z8iftd63~m~3~n~AOS%3A%20Checkout%20Sign%20In~r~aos%3Aaccount',
    'dnt': '1',
    'pragma': 'no-cache',
    'priority': 'u=0, i',
    'referer': 'https://secure8.store.apple.com/shop/signIn/account?ssi=1AAABj7g5ElYgf8JVLq2FxksgK0WdPkxjd9cZzIsEwvdRkX2TN0dzUFEAAAAzaHR0cHM6Ly9zZWN1cmU4LnN0b3JlLmFwcGxlLmNvbS9zaG9wL2FjY291bnQvaG9tZXx8AAIBVSTR3m9wxFYGBUcy0uzgvSSpclg1A5cHSmgmtQIjJ8Q',
    'sec-ch-ua': '"Microsoft Edge";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0',
}

response = requests.get('https://secure8.store.apple.com/shop/account/home', cookies=cookies, headers=headers)
set_cookie_header = response.headers.get('Set-Cookie', '')
dssid2_match = re.search(r"dssid2=([a-zA-Z0-9\-]+)", set_cookie_header)
as_ltn_us_match = re.search(r"as_ltn_us=(.+?);", set_cookie_header)
dssid2 = dssid2_match.group(1) if dssid2_match else None
as_ltn_us_2 = as_ltn_us_match.group(1) if as_ltn_us_match else None

logging.info(f"dssid2_2: {dssid2}")
logging.info(f"home_as_ltn_us: {as_ltn_us_2}")
logging.info('-'*200)

# -------------------------------------------------------------------------------------------------------------------
# 第一次转
cookies = {
    'dssid2': dssid2,
    'dssf': '1',
    'as_pcts': as_pcts_match,
    'as_dc': 'ucp5',
    'as_sfa': 'Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE',
    'geo': 'CN',
    'pxro': '1',
    's_cc': 'true',
    'dslang': 'US-EN',
    'site': 'USA',
    'as_rumid': '719045a8-955d-47e5-8d54-ceda7aea0529',
    'as_cn': as_cn,
    's_fid': '66B279F5376900CA-2D0D3DE6A70B315C',
    's_sq': '%5B%5BB%5D%5D',
    's_vi': '[CS]v1|332A075DF8E107B2-40001784269E3B83[CE]',
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
    # 'cookie': 'dssid2=9e7f53ef-1683-47d7-994a-26471c9e5f17; dssf=1; as_pcts=KLYIVPNazOZt:5M9yfOcgypngw9YrIMHMUD2KJgMDEZ58egA-owNzg2CBVmhB6eRjrSz6uNqdYnAL57xhM5gLjGL+mTgIszOTBgku35VL:GqZSvWohf:F6QcJl+1I22makrJ1rX5EfIE9wcLFdRMafdFX6YhucfeKSz-qwU9AlusF-ee7L4; as_dc=ucp5; as_sfa=Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE; geo=CN; pxro=1; s_cc=true; dslang=US-EN; site=USA; as_rumid=719045a8-955d-47e5-8d54-ceda7aea0529; as_cn=~o64i6uZb4PuY27kIPLY3lh6XZD-jepmeS9EPzQFZZPM=; s_fid=66B279F5376900CA-2D0D3DE6A70B315C; s_sq=%5B%5BB%5D%5D; s_vi=[CS]v1|332A075DF8E107B2-40001784269E3B83[CE]; as_disa=AAAjAAABIsUqyQfvFHqyREBFs83QFej8WNaxyFE2mYbZ9x2ZDtzld8ILlGp0Zdqj0I7JYtpuAAIBCpth-UGOC2eUdCmib4qdFEuRVKdyc10kAXo68O-376Q=; as_rec=2d4be1fe7f1c438cf58a3fa2f5f62fa340004646a5f8e0727b0aeec9d10a37b7f6b4bc75a1a221960719d66d5f8a99f901426e8268ee1dc3a5112dc275515f94da439ad3dcab42f9c3a5410ff0ca5296; as_ltn_us=AAQEAMM8Zk4r2hiiP4KY6rPDmmEtSNzSDyfRZ4cgyhhCtQWGUFiMarBxBVDj4ULggLnRjbxTMn67RyNGx3rjoUjhg1HETyBIf-Q',
    'dnt': '1',
    'modelversion': 'v2',
    'origin': 'https://secure8.store.apple.com',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://secure8.store.apple.com/shop/account/home',
    'sec-ch-ua': '"Microsoft Edge";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'syntax': 'graviton',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0',
    'x-aos-model-page': 'RetailHome',
    'x-aos-stk': x_aos_stk_value,
    'x-requested-with': 'Fetch',
}

params = {
    '_a': 'fetchDashboard',
    '_m': 'home.dashboards',
}

response = requests.post('https://secure8.store.apple.com/shop/accounthomex', params=params, cookies=cookies, headers=headers)

set_cookie_header = response.headers.get('Set-Cookie', '')
dssid2_match = re.search(r"dssid2=([a-zA-Z0-9\-]+)", set_cookie_header)
as_ltn_us_match = re.search(r"as_ltn_us=(.+?);", set_cookie_header)
dssid2 = dssid2_match.group(1) if dssid2_match else None
as_ltn_us_3 = as_ltn_us_match.group(1) if as_ltn_us_match else None

logging.info(f"dssid2_2: {dssid2}")
logging.info(f"fetchDashboard_1: {as_ltn_us_3}")
logging.info('-'*200)
# ------------------------------------------------------------------------------------------------

# 第二次转
cookies = {
    'dssid2': dssid2,
    'dssf': '1',
    'as_pcts': as_pcts_match,
    'as_dc': 'ucp5',
    'as_sfa': 'Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE',
    'geo': 'CN',
    'pxro': '1',
    's_cc': 'true',
    'dslang': 'US-EN',
    'site': 'USA',
    'as_rumid': '719045a8-955d-47e5-8d54-ceda7aea0529',
    'as_cn': as_cn,
    's_fid': '66B279F5376900CA-2D0D3DE6A70B315C',
    's_sq': '%5B%5BB%5D%5D',
    's_vi': '[CS]v1|332A075DF8E107B2-40001784269E3B83[CE]',
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
    # 'cookie': 'dssid2=9e7f53ef-1683-47d7-994a-26471c9e5f17; dssf=1; as_pcts=KLYIVPNazOZt:5M9yfOcgypngw9YrIMHMUD2KJgMDEZ58egA-owNzg2CBVmhB6eRjrSz6uNqdYnAL57xhM5gLjGL+mTgIszOTBgku35VL:GqZSvWohf:F6QcJl+1I22makrJ1rX5EfIE9wcLFdRMafdFX6YhucfeKSz-qwU9AlusF-ee7L4; as_dc=ucp5; as_sfa=Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE; geo=CN; pxro=1; s_cc=true; dslang=US-EN; site=USA; as_rumid=719045a8-955d-47e5-8d54-ceda7aea0529; as_cn=~o64i6uZb4PuY27kIPLY3lh6XZD-jepmeS9EPzQFZZPM=; s_fid=66B279F5376900CA-2D0D3DE6A70B315C; s_sq=%5B%5BB%5D%5D; s_vi=[CS]v1|332A075DF8E107B2-40001784269E3B83[CE]; as_disa=AAAjAAABIsUqyQfvFHqyREBFs83QFej8WNaxyFE2mYbZ9x2ZDtzld8ILlGp0Zdqj0I7JYtpuAAIBCpth-UGOC2eUdCmib4qdFEuRVKdyc10kAXo68O-376Q=; as_rec=2d4be1fe7f1c438cf58a3fa2f5f62fa340004646a5f8e0727b0aeec9d10a37b7f6b4bc75a1a221960719d66d5f8a99f901426e8268ee1dc3a5112dc275515f94da439ad3dcab42f9c3a5410ff0ca5296; as_ltn_us=AAQEAMM8Zk4r2hiiP4KY6rPDmmEtSNzSDyfRZ4cgyhhCtQWGUFiMarBxBVDj4ULggLnRjbxTMn67RyNGx3rjoUjhg1HETyBIf-Q',
    'dnt': '1',
    'modelversion': 'v2',
    'origin': 'https://secure8.store.apple.com',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://secure8.store.apple.com/shop/account/home',
    'sec-ch-ua': '"Microsoft Edge";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'syntax': 'graviton',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0',
    'x-aos-model-page': 'RetailHome',
    'x-aos-stk': x_aos_stk_value,
    'x-requested-with': 'Fetch',
}

params = {
    '_a': 'fetchDevices',
    '_m': 'home.devices',
}

response = requests.post('https://secure8.store.apple.com/shop/accounthomex', params=params, cookies=cookies, headers=headers)

set_cookie_header = response.headers.get('Set-Cookie', '')
dssid2_match = re.search(r"dssid2=([a-zA-Z0-9\-]+)", set_cookie_header)
as_ltn_us_match = re.search(r"as_ltn_us=(.+?);", set_cookie_header)
dssid2 = dssid2_match.group(1) if dssid2_match else None
as_ltn_us_4 = as_ltn_us_match.group(1) if as_ltn_us_match else None

logging.info(f"dssid2_2: {dssid2}")
logging.info(f"fetchDevices: {as_ltn_us_4}")
logging.info('-'*200)

# ----------------------------------------------------------------------------------------------
# 第三次转

cookies = {
    'dssid2': '888d1e0d-f7f3-448c-8c3e-767fd4afff74',
    'dssf': '1',
    'as_pcts': 'ZJ_L-d0ARHPi9MEixtp7ZfCPQ2ZOwAItuT7RN2jydmWVAAFaW4q_krqS3FZTfS4cp3M2:c6Cp9QYcmVS:BaaqTxgT435tUahz89bwHaPITv0NDEYv-hVEiOlS4CcLZl0lZBTHsTrRm+63jYO0JD:lUiwnPCx8bSsf8+2X:w+7ERjCUDvZN6',
    'as_dc': 'ucp3',
    'as_sfa': 'Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE',
    'geo': 'CN',
    's_fid': '1734BD72CAB684C2-2F460012A8259460',
    's_cc': 'true',
    'pxro': '1',
    's_vi': '[CS]v1|332A1858BF37119D-600004F0E086E007[CE]',
    'dslang': 'US-EN',
    'site': 'USA',
    'as_rumid': 'c20dc5ca-19fb-429a-b074-c36db4eccd54',
    'as_cn': '~o64i6uZb4PuY27kIPLY3lh6XZD-jepmeS9EPzQFZZPM=',
    'as_disa': 'AAAjAAABht7Qum9pYB4UMXkLbvPEtuwIUVoxcXMhZyIbu_vzNYw_vIGluX8typQ7vUBbCBJRAAIBZ9uq3f71sNo_1c4jEq2FIL33CSYpFczBtkFnWyxgszk=',
    'as_rec': '1f197c5c77d611e4b10f782772172a4ada18d4beaa869a590b3233c77ff8e0797c6e344991ee1e0eac79375fc8694044123ed6e609fc9a71e1ff72d053ab91a803d1f587e2223c0ec93d9508114c218b',
    'as_ltn_us': 'AAQEAMOztWEUr4ejXJG2xWyfIbE1Tu3LQ8tx7twMu3psrKCUUFiMarBxBVDj4ULggLnRjbxRDL8MpC0YFdgwxYWfpDv6Gye_iwQ',
    's_sq': 'applestoreww%3D%2526c.%2526a.%2526activitymap.%2526page%253DAOS%25253A%252520account%25252Fhome%2526link%253Deditedit%252520shipping%252520address%252520%252528inner%252520text%252529%252520%25257C%252520no%252520href%252520%25257C%252520body%2526region%253Dbody%2526pageIDType%253D1%2526.activitymap%2526.a%2526.c%2526pid%253DAOS%25253A%252520account%25252Fhome%2526pidt%253D1%2526oid%253Dfunctionkd%252528%252529%25257B%25257D%2526oidt%253D2%2526ot%253DBUTTON',
}

headers = {
    'accept': '*/*',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'no-cache',
    # 'content-length': '0',
    'content-type': 'application/x-www-form-urlencoded',
    # 'cookie': 'dssid2=888d1e0d-f7f3-448c-8c3e-767fd4afff74; dssf=1; as_pcts=ZJ_L-d0ARHPi9MEixtp7ZfCPQ2ZOwAItuT7RN2jydmWVAAFaW4q_krqS3FZTfS4cp3M2:c6Cp9QYcmVS:BaaqTxgT435tUahz89bwHaPITv0NDEYv-hVEiOlS4CcLZl0lZBTHsTrRm+63jYO0JD:lUiwnPCx8bSsf8+2X:w+7ERjCUDvZN6; as_dc=ucp3; as_sfa=Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE; geo=CN; s_fid=1734BD72CAB684C2-2F460012A8259460; s_cc=true; pxro=1; s_vi=[CS]v1|332A1858BF37119D-600004F0E086E007[CE]; dslang=US-EN; site=USA; as_rumid=c20dc5ca-19fb-429a-b074-c36db4eccd54; as_cn=~o64i6uZb4PuY27kIPLY3lh6XZD-jepmeS9EPzQFZZPM=; as_disa=AAAjAAABht7Qum9pYB4UMXkLbvPEtuwIUVoxcXMhZyIbu_vzNYw_vIGluX8typQ7vUBbCBJRAAIBZ9uq3f71sNo_1c4jEq2FIL33CSYpFczBtkFnWyxgszk=; as_rec=1f197c5c77d611e4b10f782772172a4ada18d4beaa869a590b3233c77ff8e0797c6e344991ee1e0eac79375fc8694044123ed6e609fc9a71e1ff72d053ab91a803d1f587e2223c0ec93d9508114c218b; as_ltn_us=AAQEAMOztWEUr4ejXJG2xWyfIbE1Tu3LQ8tx7twMu3psrKCUUFiMarBxBVDj4ULggLnRjbxRDL8MpC0YFdgwxYWfpDv6Gye_iwQ; s_sq=applestoreww%3D%2526c.%2526a.%2526activitymap.%2526page%253DAOS%25253A%252520account%25252Fhome%2526link%253Deditedit%252520shipping%252520address%252520%252528inner%252520text%252529%252520%25257C%252520no%252520href%252520%25257C%252520body%2526region%253Dbody%2526pageIDType%253D1%2526.activitymap%2526.a%2526.c%2526pid%253DAOS%25253A%252520account%25252Fhome%2526pidt%253D1%2526oid%253Dfunctionkd%252528%252529%25257B%25257D%2526oidt%253D2%2526ot%253DBUTTON',
    'dnt': '1',
    'modelversion': 'v2',
    'origin': 'https://secure6.store.apple.com',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://secure6.store.apple.com/shop/account/home',
    'sec-ch-ua': '"Microsoft Edge";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'syntax': 'graviton',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0',
    'x-aos-model-page': 'RetailHome',
    'x-aos-stk': 'OZ9QHQnM6slaE2GRrkHbhXOd-DV1zfxJ1B2cb6P_6uY',
    'x-requested-with': 'Fetch',
}

params = {
    '_a': 'editAddress',
    '_m': 'home.customerAccount.shippingInfo.shippingAddress',
}

response = requests.post('https://secure6.store.apple.com/shop/accounthomex', params=params, cookies=cookies, headers=headers)



set_cookie_header = response.headers.get('Set-Cookie', '')
dssid2_match = re.search(r"dssid2=([a-zA-Z0-9\-]+)", set_cookie_header)
as_ltn_us_match = re.search(r"as_ltn_us=(.+?);", set_cookie_header)
dssid2 = dssid2_match.group(1) if dssid2_match else None
as_ltn_us_5 = as_ltn_us_match.group(1) if as_ltn_us_match else None

logging.info(f"dssid2_2: {dssid2}")
logging.info(f"editAddress: {as_ltn_us_5}")
logging.info('-'*200)
logging.info('-'*200)
# ------------------------------------------------------------------------------------------------
# 第四次转
cookies = {
    'dssid2': dssid2,
    'dssf': '1',
    'as_pcts': as_pcts_match,
    'as_dc': 'ucp5',
    'as_sfa': 'Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE',
    'geo': 'CN',
    'pxro': '1',
    's_cc': 'true',
    'dslang': 'US-EN',
    'site': 'USA',
    'as_rumid': '719045a8-955d-47e5-8d54-ceda7aea0529',
    'as_cn': as_cn,
    's_fid': '66B279F5376900CA-2D0D3DE6A70B315C',
    's_sq': '%5B%5BB%5D%5D',
    's_vi': '[CS]v1|332A075DF8E107B2-40001784269E3B83[CE]',
    'as_disa': as_disa,
    'as_rec': as_rec,
    'as_ltn_us': as_ltn_us_3,
}

headers = {
    'accept': '*/*',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'no-cache',
    # 'content-length': '0',
    'content-type': 'application/x-www-form-urlencoded',
    # 'cookie': 'dssid2=9e7f53ef-1683-47d7-994a-26471c9e5f17; dssf=1; as_pcts=KLYIVPNazOZt:5M9yfOcgypngw9YrIMHMUD2KJgMDEZ58egA-owNzg2CBVmhB6eRjrSz6uNqdYnAL57xhM5gLjGL+mTgIszOTBgku35VL:GqZSvWohf:F6QcJl+1I22makrJ1rX5EfIE9wcLFdRMafdFX6YhucfeKSz-qwU9AlusF-ee7L4; as_dc=ucp5; as_sfa=Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE; geo=CN; pxro=1; s_cc=true; dslang=US-EN; site=USA; as_rumid=719045a8-955d-47e5-8d54-ceda7aea0529; as_cn=~o64i6uZb4PuY27kIPLY3lh6XZD-jepmeS9EPzQFZZPM=; s_fid=66B279F5376900CA-2D0D3DE6A70B315C; s_sq=%5B%5BB%5D%5D; s_vi=[CS]v1|332A075DF8E107B2-40001784269E3B83[CE]; as_disa=AAAjAAABIsUqyQfvFHqyREBFs83QFej8WNaxyFE2mYbZ9x2ZDtzld8ILlGp0Zdqj0I7JYtpuAAIBCpth-UGOC2eUdCmib4qdFEuRVKdyc10kAXo68O-376Q=; as_rec=2d4be1fe7f1c438cf58a3fa2f5f62fa340004646a5f8e0727b0aeec9d10a37b7f6b4bc75a1a221960719d66d5f8a99f901426e8268ee1dc3a5112dc275515f94da439ad3dcab42f9c3a5410ff0ca5296; as_ltn_us=AAQEAMM8Zk4r2hiiP4KY6rPDmmEvBhfY9X8EaEVITOk2dAITjFiMarBxBVDj4ULggLnRjbxSBj_2fZwIAtn2bGBarwL0sCW-6gw',
    'dnt': '1',
    'modelversion': 'v2',
    'origin': 'https://secure8.store.apple.com',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://secure8.store.apple.com/shop/account/home',
    'sec-ch-ua': '"Microsoft Edge";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'syntax': 'graviton',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0',
    'x-aos-model-page': 'RetailHome',
    'x-aos-stk': x_aos_stk_value,
    'x-requested-with': 'Fetch',
}

params = {
    '_a': 'fetchDashboard',
    '_m': 'home.dashboards',
}

response = requests.post('https://secure8.store.apple.com/shop/accounthomex', params=params, cookies=cookies, headers=headers)
set_cookie_header = response.headers.get('Set-Cookie', '')
dssid2_match = re.search(r"dssid2=([a-zA-Z0-9\-]+)", set_cookie_header)
as_ltn_us_match = re.search(r"as_ltn_us=(.+?);", set_cookie_header)
dssid2 = dssid2_match.group(1) if dssid2_match else None
as_ltn_us_6 = as_ltn_us_match.group(1) if as_ltn_us_match else None

logging.info(f"dssid2_2: {dssid2}")
logging.info(f"fetchDashboard_2: {as_ltn_us_6}")
logging.info('-'*200)

# ---------------------------------------------------------------------------------------------------------------------------------
# 最终提交
cookies = {
    'dssid2': dssid2,
    'dssf': '1',
    'as_pcts': as_pcts_match,
    'as_dc': 'ucp5',
    'as_sfa': 'Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE',
    'geo': 'CN',
    'pxro': '1',
    's_cc': 'true',
    'dslang': 'US-EN',
    'site': 'USA',
    'as_rumid': '719045a8-955d-47e5-8d54-ceda7aea0529',
    'as_cn': as_cn,
    's_fid': '67ECE61270D0DC81-097D5D1C97370A24',
    's_vi': '[CS]v1|332A0E30F91954D8-60000C7E49A20526[CE]',
    'as_disa': as_disa,
    'as_rec': as_rec,
    'as_ltn_us': as_ltn_us_6,
    's_sq': '%5B%5BB%5D%5D',
}

headers = {
    'accept': '*/*',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'no-cache',
    'content-type': 'application/x-www-form-urlencoded',
    # 'cookie': 'dssid2=9e7f53ef-1683-47d7-994a-26471c9e5f17; dssf=1; as_pcts=KLYIVPNazOZt:5M9yfOcgypngw9YrIMHMUD2KJgMDEZ58egA-owNzg2CBVmhB6eRjrSz6uNqdYnAL57xhM5gLjGL+mTgIszOTBgku35VL:GqZSvWohf:F6QcJl+1I22makrJ1rX5EfIE9wcLFdRMafdFX6YhucfeKSz-qwU9AlusF-ee7L4; as_dc=ucp5; as_sfa=Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE; geo=CN; pxro=1; s_cc=true; dslang=US-EN; site=USA; as_rumid=719045a8-955d-47e5-8d54-ceda7aea0529; as_cn=~o64i6uZb4PuY27kIPLY3lh6XZD-jepmeS9EPzQFZZPM=; s_fid=67ECE61270D0DC81-097D5D1C97370A24; s_vi=[CS]v1|332A0E30F91954D8-60000C7E49A20526[CE]; as_disa=AAAjAAABdtzuZYTnHOL8DNOtGLEj9iMnJPf0k5nHbctcPDgpAkPePt3lE3qV8h6tnp2P5sJBAAIBQ78dIOPeNnxvWmsf9K6IyyIxf0RpHxh8lrkUwN40SHg=; as_rec=e643dec40f700524256928c8234750a6c4e9ea771ffc17c527476a794c398420da110f4f432a50e462b85181a4067b590a600d28547eabb3d140867392cdf05f765e6b13cab68cbeb26b277053098306; as_ltn_us=AAQEAMKf6Pe3MfD2vW9lnQONk2ifWXBQExIDFZavbPZLJyU9sFiMarBxBVDj4ULggLnRjbxS0SGEIfd1u3yjiJD-oFQ6V9HCbfw; s_sq=%5B%5BB%5D%5D',
    'dnt': '1',
    'modelversion': 'v2',
    'origin': 'https://secure8.store.apple.com',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://secure8.store.apple.com/shop/account/home',
    'sec-ch-ua': '"Microsoft Edge";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'syntax': 'graviton',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0',
    'x-aos-model-page': 'RetailHome',
    'x-aos-stk': x_aos_stk_value,
    'x-requested-with': 'Fetch',
}

params = {
    '_a': 'address-submit',
    '_m': 'home.customerAccount.shippingInfo.shippingAddress.editShippingAddress.editAddress',
}

data = 'home.customerAccount.shippingInfo.shippingAddress.editShippingAddress.editAddress.fullDaytimePhone=(861)%20111-1111&home.customerAccount.shippingInfo.shippingAddress.editShippingAddress.editAddress.street2=212231312&home.customerAccount.shippingInfo.shippingAddress.editShippingAddress.editAddress.lastName=lllll3333&home.customerAccount.shippingInfo.shippingAddress.editShippingAddress.editAddress.firstName=hhhjjj11166666&home.customerAccount.shippingInfo.shippingAddress.editShippingAddress.editAddress.companyName=122332&home.customerAccount.shippingInfo.shippingAddress.editShippingAddress.editAddress.street=88888888888&home.customerAccount.shippingInfo.shippingAddress.editShippingAddress.editAddress.zipLookup.city=Albany&home.customerAccount.shippingInfo.shippingAddress.editShippingAddress.editAddress.zipLookup.state=NY&home.customerAccount.shippingInfo.shippingAddress.editShippingAddress.editAddress.zipLookup.postalCode=11111-4444&home.customerAccount.shippingInfo.shippingAddress.editShippingAddress.editAddress.zipLookup.countryCode=US'

response = requests.post(
    'https://secure8.store.apple.com/shop/accounthomex',
    params=params,
    cookies=cookies,
    headers=headers,
    data=data,
)
logging.info(response.text)
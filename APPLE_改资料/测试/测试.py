import requests,re


name = "freesia.e-fpb@softbank.ne.jp"
pwd = "Aa147369"

# -------------------------------------------------------------------------------------------------------------------------------------------------
url = "https://secure8.store.apple.com/shop/account/home"
headers = {"Cookie": "myacinfo=DAWTKNV323952cf8084a204fb20ab2508441a07d02d367245a870606eb217bb73e04a705faf9ace0cf85af38259cedb9093af5aee68bbb56fd292e5d905206a6fdb1f69c9820669883c365936092ce8ff3a8d5dc2d4c090e5309bf69db302d2202f46c9b4fa7a264958ebcca5a581114e194d44b77fcdc6699d87692a7bfeba9546707d556a140b982355ad73b16f3cfa209a6d7e1a26aecf36396d9ca7551dda823c93e2462f3e4ea694704e764ba3bc1e0912e291a0ad343bdec3ffa335aa4f7f40886ef382ed883972b3c71e1a1e949fdc159cd67c7f085fc7b9ee726e30e45f45cff05a694421e9291ee8e6f3b75f41dcf13d115deafe9c5076ca9252357204d0ef515b74c51f5f3fcca7258a6c00e2f36035a23e3014f0438ae8126795a0fea43e5dc5f5796a5264d024df5ac43a92a422d5e69e7f7192e98456336b26cf5302eee226e66c3e5d39ee6e06b224213e7a881eab63b8abaa16a53b0ce266ae96e27b67a2c7a221d1e9e8eca3c878c186420479f097d56886cfbe1ab385a563463c5f8bce8438f99c6e7e41f10d885a8b82a1ace388774866517f07f9816b6572af188eb767a8dbed85e72101fc0da9bab07ee3b7c2b38fe49cf639d04cc3ee52daa6b12f794c02760239d0c390392329466d61b7102cfac7ac9d13c307488c90826d669a5b78fafb23555d5fc8c2e92199c821903585a47V3;"}
response = requests.request("GET", url, headers=headers, allow_redirects=False)

ssi = response.headers["Location"]
headers_str = str(response.headers)
dssid2_pattern = r"dssid2=([a-z0-9\-]+)"
as_pcts_pattern = r"as_pcts=([^;]+)"
dssid2_match = re.search(dssid2_pattern, headers_str, re.IGNORECASE)
as_pcts_match = re.search(as_pcts_pattern, headers_str, re.IGNORECASE)
dssid2 = dssid2_match.group(1)
as_pcts =  as_pcts_match.group(1)

# -------------------------------------用ssi链接取x_aos_stk_value-------------------------------------------------------------------------------------------------
cookies = {
    'dssid2': dssid2,
    'dssf': '1',
    'as_pcts': as_pcts
}
response_2 = requests.get(ssi, cookies=cookies)
match = re.search(r'"x-aos-stk":"([^"]+)"', response_2.text)
x_aos_stk_value = match.group(1)
# -------------------------------------用ssi链接取其余的-------------------------------------------------------------------------------------------------


cookies = {
    # 'as_rumid': '71785f21-fee2-4dcc-a146-f1e99cbc2341',
    # 'dslang': 'US-EN',
    # 'site': 'USA',
    # 'myacinfo': 'DAWTKNV323952cf8084a204fb20ab2508441a07d02d367245a870606eb217bb73e04a705faf9ace0cf85af38259cedb9093af5aee68bbb56fd292e5d905206a6fdb1f69c9820669883c365936092ce8ff3a8d5dc2d4c090e5309bf69db302d2202f46c9b4fa7a264958ebcca5a581114e194d44b77fcdc6699d87692a7bfeba9546707d556a140b982355ad73b16f3cfa209a6d7e1a26aecf36396d9ca7551dda823c93e2462f3e4ea694704e764ba3bc1e0912e291a0ad343bdec3ffa335aa4f7f40886ef382ed883972b3c71e1a1e949fdc159cd67c7f085fc7b9ee726e30e45f45cff05a694421e9291ee8e6f3b75f41dcf13d115deafe9c5076ca9252357204d0ef515b74c51f5f3fcca7258a6c00e2f36035a23e3014f0438ae8126795a0fea43e5dc5f5796a5264d024df5ac43a92a422d5e69e7f7192e98456336b26cf5302eee226e66c3e5d39ee6e06b224213e7a881eab63b8abaa16a53b0ce266ae96e27b67a2c7a221d1e9e8eca3c878c186420479f097d56886cfbe1ab385a563463c5f8bce8438f99c6e7e41f10d885a8b82a1ace388774866517f07f9816b6572af188eb767a8dbed85e72101fc0da9bab07ee3b7c2b38fe49cf639d04cc3ee52daa6b12f794c02760239d0c390392329466d61b7102cfac7ac9d13c307488c90826d669a5b78fafb23555d5fc8c2e92199c821903585a47V3',
    # 's_fid': '48E177C3D2DDE9DC-26432B49CC5C48BB',
    # 'pt-dm': 'v1~x~5bhzghse~m~3',
    'dssid2': dssid2,
    # 'dssf': '1',
    'as_pcts': as_pcts,
    'as_dc': 'ucp5',
}

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'no-cache',
    # 'cookie': 'as_rumid=71785f21-fee2-4dcc-a146-f1e99cbc2341; dslang=US-EN; site=USA; myacinfo=DAWTKNV323952cf8084a204fb20ab2508441a07d02d367245a870606eb217bb73e04a705faf9ace0cf85af38259cedb9093af5aee68bbb56fd292e5d905206a6fdb1f69c9820669883c365936092ce8ff3a8d5dc2d4c090e5309bf69db302d2202f46c9b4fa7a264958ebcca5a581114e194d44b77fcdc6699d87692a7bfeba9546707d556a140b982355ad73b16f3cfa209a6d7e1a26aecf36396d9ca7551dda823c93e2462f3e4ea694704e764ba3bc1e0912e291a0ad343bdec3ffa335aa4f7f40886ef382ed883972b3c71e1a1e949fdc159cd67c7f085fc7b9ee726e30e45f45cff05a694421e9291ee8e6f3b75f41dcf13d115deafe9c5076ca9252357204d0ef515b74c51f5f3fcca7258a6c00e2f36035a23e3014f0438ae8126795a0fea43e5dc5f5796a5264d024df5ac43a92a422d5e69e7f7192e98456336b26cf5302eee226e66c3e5d39ee6e06b224213e7a881eab63b8abaa16a53b0ce266ae96e27b67a2c7a221d1e9e8eca3c878c186420479f097d56886cfbe1ab385a563463c5f8bce8438f99c6e7e41f10d885a8b82a1ace388774866517f07f9816b6572af188eb767a8dbed85e72101fc0da9bab07ee3b7c2b38fe49cf639d04cc3ee52daa6b12f794c02760239d0c390392329466d61b7102cfac7ac9d13c307488c90826d669a5b78fafb23555d5fc8c2e92199c821903585a47V3; s_fid=48E177C3D2DDE9DC-26432B49CC5C48BB; pt-dm=v1~x~5bhzghse~m~3; dssid2=9746c9a4-0082-49b5-a01e-43bd6296e8a4; dssf=1; as_pcts=7YnlLK6Gm92hT1r-rRyeg:fGmVxyCBjX3yXa8FW8BP91SDhWb7pESqTRiXgVUG9QHBm7Xxv4QiKNC5TGuALwhjW1fd+3UREo89B1i1smwOTsls5x5fdPXaHplQo8-j+PoqgeW8YBt-a87uXruFE:jQyfDk2GbqsFWf6tgNNCcPAPu-j6NG7; as_dc=ucp5',
    'dnt': '1',
    'pragma': 'no-cache',
    'priority': 'u=0, i',
    'sec-ch-ua': '"Microsoft Edge";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0',
}

params = {
    'ssi': '1AAABj7Ro4KEgxGEnmY05tgaflOgLQOSs7fXiCaxn6zTXVbTjqH8sVrwAAAAzaHR0cHM6Ly9zZWN1cmU4LnN0b3JlLmFwcGxlLmNvbS9zaG9wL2FjY291bnQvaG9tZXx8AAIBMuQzSVHutjZfDcYwOI2WHAJnadc-Jyt0aafTCjbPxQo',
}

response1 = requests.get('https://secure8.store.apple.com/shop/signIn/account', params=params, cookies=cookies, headers=headers)

print(response1.headers)
pass



# # -----------------------------------------------------------------------------------------------------------------------------------------------


url = "https://secure8.store.apple.com/shop/signIn/idms/authx"
# !!!
querystring = {"ssi":"1AAABj7Ro4KEgxGEnmY05tgaflOgLQOSs7fXiCaxn6zTXVbTjqH8sVrwAAAAzaHR0cHM6Ly9zZWN1cmU4LnN0b3JlLmFwcGxlLmNvbS9zaG9wL2FjY291bnQvaG9tZXx8AAIBMuQzSVHutjZfDcYwOI2WHAJnadc-Jyt0aafTCjbPxQo"}

payload = "deviceID=TF1;015;;;;;;;;;;;;;;;;;;;;;;Mozilla;Netscape;5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit/537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome/125.0.0.0%20Safari/537.36%20Edg/125.0.0.0;20030107;undefined;true;;true;Win32;undefined;Mozilla/5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit/537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome/125.0.0.0%20Safari/537.36%20Edg/125.0.0.0;zh-CN;undefined;secure8.store.apple.com;undefined;undefined;undefined;undefined;false;false;1716718742250;8;2005/6/7%2021%3A33%3A44;1920;1080;;;;;;;;-480;-480;2024/5/26%2018%3A19%3A02;24;1920;1032;0;0;;;;;;;;;;;;;;;;;;;25;&grantCode="
headers = {
    "accept": "*/*",
    "accept-language": "zh-CN,zh;q=0.9",
    "cache-control": "no-cache",
    "content-type": "application/x-www-form-urlencoded",
    "dnt": "1",
    "modelversion": "v2",
    "origin": "https://secure8.store.apple.com",
    "pragma": "no-cache",
    "priority": "u=1, i",
    "referer": "https://secure8.store.apple.com/shop/signIn/account?ssi=1AAABj7Ro4KEgxGEnmY05tgaflOgLQOSs7fXiCaxn6zTXVbTjqH8sVrwAAAAzaHR0cHM6Ly9zZWN1cmU4LnN0b3JlLmFwcGxlLmNvbS9zaG9wL2FjY291bnQvaG9tZXx8AAIBMuQzSVHutjZfDcYwOI2WHAJnadc-Jyt0aafTCjbPxQo",
    "sec-ch-ua-mobile": "?0",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "syntax": "graviton",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0",
    "x-aos-model-page": "idmsSignInPage",
    "x-aos-stk": "UqZOrOBggyJdZVUrSr29wqV0kAXyI7kx5aqo_mjaO5c",
    "x-requested-with": "Fetch",
    "Cookie": f"dssid2=9746c9a4-0082-49b5-a01e-43bd6296e8a4; dssf=1;  myacinfo=DAWTKNV323952cf8084a204fb20ab2508441a07d02d3efa865d051be1b76db7833cd16490ec7bf9bc9f677b6632ec5803283b86c90bfbb5cb7d0f06a419abf1bf641b15003d9baab98846c497c2512db8bfcccb778f25b2d5befe94d0084273f900b7963924c822ff9fbd252f259e418dfe31ca21b908db371de8e3d32e73705ce04b2d268da2c9cd7a516e7055e7ab87c04e56e5e8c7672e5b05379aabd1db3521b4515d94488d99c891b295289471bea67276ed35b49b4aec6ab7d5ec6230ed8d1f1baa2436a79de969a0806edc94e3300c81f83f2cbbef19b625280e90c1564bab1226abba02478a724be26be13f7a54143b2065b0b354365cb2e4a4df87ada34a0a78e05fe4e2f5a1647f139527f5b40a6a1e340ec83e3026fd14259bdd2d88b71a3617363a93345afd637bd831d348db8b9ebeb68e2c6b14739d460f9560446b426b6c3a935db5ad26e8abffd92b31060e36e07bc0710cf643d1755707cfaaa7f7991eb7250691f3c8a8bfd3c5fc30aa381e208aa3bb2212cb55babed007e249fa69cf36123017cbb94fb0e7eaf026c082e4a810f6c4e54f2cb74e7bd9747dba0a43279cdea22e47c2aae241dbedaf7b82074ff7dd6905d1aa18caff094e2fba9b58c684edef8746f92173a721919527055e8a219a1faad77c0c84bec80d41f434abe736b1e783fae39198d4ce020d6c93457ac585a47V3"
}

response = requests.request("POST", url, data=payload, headers=headers, params=querystring)

print(response.headers)

pass















# ---------------------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------------------
# --------------------------------------------------经过这个转换才能用在最后面-----------------------------------------------------------------------
# https://secure8.store.apple.com/shop/accounthomex?_a=fetchDashboard&_m=home.dashboards

cookies = {
    'dssid2': dssid2,
    'dssf': '1',
    'as_pcts': as_pcts,
    'as_ltn_us': 'AAQEAMEfjW6aQ-WVoeOKB651sk91QN_c4z9zFtYZJjhr7OnAoFiMarBxBVDj4ULggLnRjbxSMbok0uIrlRL5MtHV1keEVpM7g_A',
}

headers = {
    'accept': '*/*',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'no-cache',
    'dnt': '1',
    'x-aos-stk': x_aos_stk_value,
    'x-requested-with': 'Fetch',
}

params = {
    '_a': 'fetchDevices',
    '_m': 'home.devices',
}

response = requests.post('https://secure8.store.apple.com/shop/accounthomex', params=params, cookies=cookies, headers=headers)

print(response.headers)
pass

# --------------------------------------------------最终的提交，不能只过这一遍，此处的as_ltn_us必须经过上面的转换-------------------------------------------------------------------------
# https://secure8.store.apple.com/shop/accounthomex?_a=fetchDevices&_m=home.devices
cookies = {
    'dssid2': dssid2,
    'dssf': '1',
    'as_disa': 'AAAjAAABcurOfWkBunbB_vJ1wvZHfWcY90_X6M3c5ZNC2XZxuTZly7uSFUhRLZh96xajK4NMAAIBfW7bIpiCgS02gdhsJErcjZTXpyTDdsK9mhyJmITJD3U=',
    'as_ltn_us': "AAQEAMEfjW6aQ-WVoeOKB651sk93ye4LXjRBgg7niLhXzyLwCFiMarBxBVDj4ULggLnRjbxRgA-cZAjLtLN2eGVGclupIi30c_A",
}

headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
    'X-Requested-With': 'Fetch',
    'x-aos-stk': x_aos_stk_value,
}

params = {
    '_a': 'address-submit',
    '_m': 'home.customerAccount.shippingInfo.shippingAddress.editShippingAddress.editAddress',
}

data = 'home.customerAccount.shippingInfo.shippingAddress.editShippingAddress.editAddress.fullDaytimePhone=(861)%20111-77777&home.customerAccount.shippingInfo.shippingAddress.editShippingAddress.editAddress.street2=212231312&home.customerAccount.shippingInfo.shippingAddress.editShippingAddress.editAddress.lastName=lllll3333&home.customerAccount.shippingInfo.shippingAddress.editShippingAddress.editAddress.firstName=hhhjjj11166666&home.customerAccount.shippingInfo.shippingAddress.editShippingAddress.editAddress.companyName=122332&home.customerAccount.shippingInfo.shippingAddress.editShippingAddress.editAddress.street=88888888888&home.customerAccount.shippingInfo.shippingAddress.editShippingAddress.editAddress.zipLookup.city=Albany&home.customerAccount.shippingInfo.shippingAddress.editShippingAddress.editAddress.zipLookup.state=NY&home.customerAccount.shippingInfo.shippingAddress.editShippingAddress.editAddress.zipLookup.postalCode=11111-1111&home.customerAccount.shippingInfo.shippingAddress.editShippingAddress.editAddress.zipLookup.zipLookupCityState=Other&home.customerAccount.shippingInfo.shippingAddress.editShippingAddress.editAddress.zipLookup.countryCode=US'

response = requests.post(
    'https://secure8.store.apple.com/shop/accounthomex',
    params=params,
    cookies=cookies,
    headers=headers,
    data=data,
)
print(response.text)



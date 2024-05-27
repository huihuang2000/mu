import http.client

conn = http.client.HTTPSConnection('secure6.store.apple.com')
headers = {
    'accept': '*/*',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'cache-control': 'no-cache',
    'content-type': 'application/x-www-form-urlencoded',
    'cookie': 'dssid2=f973fd53-41ab-424a-a195-5849a8a4fff6; dssf=1; pxro=1; as_tex=~1~|553217:1:1717311540:USA|Xe8mplIBUKk0Ae/AbNai0aNGmOkWL3AL6gZsBoys+T8; POD=cn~zh; as_sfa=Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE; as_dc=ucp3; as_pcts=L6wkraI51K_Pt8CA0woyKhlFGevdqqd1LZdanM6EmUw0h-5lLVu9KDlU2dMBKzywG+b-lI:yAIat1j8GM0m0RGQnFFyG6BfxtFmhEj-ORHjs1hL+0_7X+MxRxnP_J6-ZUmJa1hy0DAGaAgcTkHmUovnywudJ_1hrFYgAelESQkZKdlOi:feIiUAl; geo=CN; s_fid=742FDBF5DF160AE1-33BAD36812B156C0; s_cc=true; s_vi=[CS]v1|332A411AF79120DD-40000B8568405D37[CE]; as_rumid=fd968e4a-6955-4607-87ed-0d5492dea43b; dslang=US-EN; site=USA; as_cn=~o64i6uZb4PuY27kIPLY3lh6XZD-jepmeS9EPzQFZZPM=; as_rec=535f029c76436a69bd83e6db17ed4f579cc9d6226acd795e89aa2251b92c2f1cf421764f9b0273021100854b69a2211b546859f5ff7a2f129ab508883f25036150be5c75dac389d69771f874d323b808; as_ltn_us=AAQEAMPJvfXkcaJJ3eU22wGFdYf_v97BOJ6p5TBTmx_JU1DPBUe4c26VeuELC7Pkmeiq31BR4VbS1CJ3vzfepCmOVqgjqlGHdBw; s_sq=%5B%5BB%5D%5D; myacinfo=DAWTKNV323952cf8084a204fb20ab2508441a07d02d3a6c0614d991522a9967de6c0213aa6afd530198efcfa6eba0b49a4424a495fc0d3dcbca87634c0281ba24b84ccfbae42fcc8599f793529e1dc1cbad8df1211605de65fc34c85f850081a16931a5763e45344119aac1cea236d4fa7b0bad3241b0b6c37e13e1df6726960d97c89696272622a7eefde7578a319da1dbcde3d27e1c87b83d86447398a430ce46d8af6f73861cbd6519556a2ad0ed46a28ccd6cb1818df4c8da76d6d77d814b64b584df2b759b42dc7398ba28d04b9ee34d9bf420272089eb77bb6e3a5d7d8ff0ad6353e291bea1095514d09f2c79c0b2df2a6bb04371e5d49f9a5a57d5f22d49c35f1717d25f49e53dd8d9d0b119e6a631872cc4916d648ceddb2579e9e7ac5a14f07f07c70592c0d0f3eb5523b8e6f6c2c70d7a88bf626c37886b7b32fffb826b31322b01bd82c77e948cbc55041f061e880d1e9fccbb79031f7c675947d0d44e4a8069ee44b0bbcc82f735f4f9ae170c07877dbe8a3e5c2a8e224bbb9567da8d321fa20e0c2f4c3b99b1a7eaf0acfb8edd962f169d409802e93592f5d2ffa7bf0a5a664c6177657003d2465cc0d68ceb8bb19ccad5cad98c541e0e8880c41e0ddc11e9b2e8963e0142ca65f2d54d934f594b10b55f4e55fd8346a1711aba9c1645eeb5bc985e8dc3931d94e74c7b0ccf22dfa75585a47V3',
    'dnt': '1',
    'modelversion': 'v2',
    'origin': 'https://secure6.store.apple.com',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://secure6.store.apple.com/shop/signIn/account?ssi=1AAABj7odVSUgkscQfLmHyU-qX49pFigvhvScyNh-2bhl2w3QG9e7sTkAAAAzaHR0cHM6Ly9zZWN1cmU2LnN0b3JlLmFwcGxlLmNvbS9zaG9wL2FjY291bnQvaG9tZXx8AAIBk2rA1NeW-_61v3YxSJtCDh76CZHae5Heb5HUEyNd1k8',
    'sec-ch-ua': '"Microsoft Edge";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'syntax': 'graviton',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0',
    'x-aos-model-page': 'idmsSignInPage',
    'x-aos-stk': 'kJC3HqDzUWdcqesDO6tCcO6nsEKO0uROVJAQzRTNpi0',
    'x-requested-with': 'Fetch',
}
conn.request(
    'POST',
    '/shop/signIn/idms/authx?ssi=1AAABj7odVSUgkscQfLmHyU-qX49pFigvhvScyNh-2bhl2w3QG9e7sTkAAAAzaHR0cHM6Ly9zZWN1cmU2LnN0b3JlLmFwcGxlLmNvbS9zaG9wL2FjY291bnQvaG9tZXx8AAIBk2rA1NeW-_61v3YxSJtCDh76CZHae5Heb5HUEyNd1k8',
    'deviceID=TF1%3B015%3B%3B%3B%3B%3B%3B%3B%3B%3B%3B%3B%3B%3B%3B%3B%3B%3B%3B%3B%3B%3B%3BMozilla%3BNetscape%3B5.0%2520%2528Windows%2520NT%252010.0%253B%2520Win64%253B%2520x64%2529%2520AppleWebKit%2F537.36%2520%2528KHTML%252C%2520like%2520Gecko%2529%2520Chrome%2F125.0.0.0%2520Safari%2F537.36%2520Edg%2F125.0.0.0%3B20030107%3Bundefined%3Btrue%3B%3Btrue%3BWin32%3Bundefined%3BMozilla%2F5.0%2520%2528Windows%2520NT%252010.0%253B%2520Win64%253B%2520x64%2529%2520AppleWebKit%2F537.36%2520%2528KHTML%252C%2520like%2520Gecko%2529%2520Chrome%2F125.0.0.0%2520Safari%2F537.36%2520Edg%2F125.0.0.0%3Bzh-CN%3Bundefined%3Bsecure6.store.apple.com%3Bundefined%3Bundefined%3Bundefined%3Bundefined%3Bfalse%3Bfalse%3B1716814454772%3B8%3B2005%2F6%2F7%252021%253A33%253A44%3B1920%3B1080%3B%3B%3B%3B%3B%3B%3B%3B-480%3B-480%3B2024%2F5%2F27%252020%253A54%253A14%3B24%3B1920%3B1032%3B0%3B0%3B%3B%3B%3B%3B%3B%3B%3B%3B%3B%3B%3B%3B%3B%3B%3B%3B%3B%3B25%3B&grantCode=',
    headers
)
response = conn.getresponse()
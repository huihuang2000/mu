# https://appleid.apple.com/
# {"账号": "aidenclrob@hotmail.com", "密码": "Aa147369"},
# {"账号": "my_hero.hero@softbank.ne.jp", "密码": "Aa147369"},
# {"账号": "yohtaydarv11@gmail.com", "密码": "Aa147369"},
# {"账号": "jacobgordon6s@hotmail.com", "密码": "Aa147369"},
# {"账号": "lovejessi06@gmail.com", "密码": "Aa147369"},
# {"账号": "sophiab2022@gmail.com", "密码": "Aa147369"},


import requests,re

# --------------------------------------------------------------------------------------------------------------
name = 'sophiab2022@gmail.com'

url = "https://env-00jxgsqva6td.dev-hz.cloudbasefunction.cn/A1?type=1"
payload = {f"email": {name}}
Key = requests.post(url=url, data=payload).json()
# ------------------------------------------------------------------------------
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
).json()
# -------------------------------------------------------------------------------
url = "https://env-00jxgsqva6td.dev-hz.cloudbasefunction.cn/A1?type=2"
payload = {
    "email": name,
    "iterations": response_2["iteration"],
    "Value": response_2["b"],
    "salt": response_2["salt"],
    "password": "Aa147369",
    "protocol": response_2["protocol"],
    "privateHexValue": Key["privateHexValue"],
    "publicHexValue": Key["publicHexValue"],
}
response_3 = requests.post(url=url, json=payload
).json()
# -----------------------------------------------------------------------------
cookies = {
    "as_rumid": "9f9a7e8708ebbde2daf02b478473eccd",
    "dssf": "1",
    "as_sfa": "Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE",
    "geo": "CN",
    "pxro": "1",
    "s_fid": "6323376718433557-371662D1A66E1B14",
    "s_cc": "true",
    "s_vi": "[CS]v1|332AA8C7A36C871F-40000E40A15E97D6[CE]",
    "dslang": "US-EN",
    "site": "USA",
    "aa": "1B99A552487EA314F1CE4E8E4291BC46",
}

headers = {
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0",
    "X-Apple-Widget-Key": "a797929d224abb1cc663bb187bbcd02f7172ca3a84df470380522a7c6092118b",
}
json_data = {
    "accountName": name,
    "rememberMe": False,
    "m1": response_3["M1"],
    "c": response_2["c"],
    "m2": response_3["M2"],
}
response_4 =  requests.post(
    url="https://idmsa.apple.com/appleauth/auth/signin/complete",
    headers=headers,
    json=json_data,
    cookies=cookies,
)
CK = response_4.headers.get("Set-Cookie")
myacinfo_pattern = re.compile(r"myacinfo=([^;]+)")
myacinfo_match = myacinfo_pattern.search(CK).group(1)






# ------------------------------------------------------------------------------------------------------------------------------------
# 开头第一个包获取的
headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}
response = requests.get('https://appleid.apple.com/', headers=headers)
aidsp = response.cookies.get('aidsp')
print(aidsp)
print('第一个包'+"----"*100)
# ------------------------------------------------------------------------------------------------------------------------------------
cookies = {
    'idclient': 'web',
    'dslang': 'CN-ZH',
    'site': 'CHN',
    'aidsp': aidsp,
    'geo': 'CN',
    'aid': 'B730C6C42F0611EB5B1CE65AC895679C',
}
headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive',
    'Referer': 'https://idmsa.apple.com/',
    'Sec-Fetch-Dest': 'iframe',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-site',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}
params = {
    'widgetKey': 'af1139274f266b22b68c2a3e7ad932cb3c0bbe854e13a79af78dcc73136882c3',
    'rv': '1',
    'language': 'zh_CN_CHN',
}
response = requests.get('https://appleid.apple.com/widget/account/repair', params=params, cookies=cookies, headers=headers)
print(response.headers)
print('第二个包'+"----"*100)
# ------------------------------------------------------------------------------------------------------------------------------------
url = 'https://appleid.apple.com/account/manage/gs/ws/token'
headers = {
    "Host": "appleid.apple.com",
    "Connection": "keep-alive",
    "sec-ch-ua": "\"Not)A;Brand\";v=\"99\", \"Google Chrome\";v=\"127\", \"Chromium\";v=\"127\"",
    "scnt": "AAAA-kVDODU1RTBCQzVERURDNkQwM0MyQzQ5NjkxOTUwNDJCRDA3NkM0ODU1RTQyQUY0MThGNjMwNkYyQUE2MkRBMEQxMDY4ODg3OTUxRTZGOTRDMjUzNzg0MzdCODlCNzM0NkQ4QTUzQUQwMjk5NTcxQ0IxMjM1NUQ3NUMxRjBENUUxN0E1QTYxRjI5NjYxM0UwREZFMTUzOTFFQjYxNDA1QjZGRkIzRUUwNEMyMjUxMDEzREQ4OENCRkIxRTBGRTc1MzFFNjkwRkRFODM1OEU5OTVEQkM1MkIyQzNFQjI0RkVCODM1QkVERjM1NzE5NTFGQnwyAAABkPkhEV6rkuTozg4Q0eSAw7S_DsSHQiXLKdOfJYgB4-2RJkgAyPoleUGNzxerAD3ZRUEkcZLYW660Nii7X1ItRCRDrhfFElOIjNve6DLp9SpKCH9KWw",
    "X-Apple-I-FD-Client-Info": "{\"U\":\"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36\",\"L\":\"zh-CN\",\"Z\":\"GMT+08:00\",\"V\":\"1.1\",\"F\":\"7la44j1e3NlY5BNlY5BSmHACVZXnNA9dGF5_uDeJrurJhBR.uMp4UdHz13NlejV2pNk0ug9WJ3uJtMMmxbu_Eme5BNlY5CGWY5BOgkLT0XxU..8GI\"}",
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
    "Cookie": f"idclient=web; dslang=CN-ZH; site=CHN; aidsp={aidsp} myacinfo={myacinfo_match}"
}
response2 = requests.get(url, cookies=cookies, headers=headers)
aidsp2 = response2.cookies.get('aidsp')
print(aidsp2)
print('第三个包'+"----"*100)

cookies = {
    'idclient': 'web',
    'dslang': 'CN-ZH',
    'site': 'CHN',
    'geo': 'CN',
    'aid': '5AAAA50572D3634A9DEF7F39B3F7788A',
    'aidsp': aidsp2,
}
headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json',
    # 'Cookie': 'idclient=web; dslang=CN-ZH; site=CHN; geo=CN; aid=5AAAA50572D3634A9DEF7F39B3F7788A; aidsp=5C674FC4E1C3CCD7B0C0F9C2615DEF13E4063BB36CF433179CE3356F82D4399985EAC01D72C32451AFEBF798B723EB8090BD83B2DA3A7D505A858C3E1B17FBCBFCFC0D59D61F540058B5E737AD1709DC16549EEA9CA364ACE42CC57D178F52BE33DDBFE6129EB6A6C9F9F6ECCEE5F82CDE2A2A99E715AAE7',
    'Referer': 'https://appleid.apple.com/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
    'X-Apple-I-FD-Client-Info': '{"U":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36","L":"zh-CN","Z":"GMT+08:00","V":"1.1","F":"7la44j1e3NlY5BNlY5BSmHACVZXnNA9dGOHavFmxaDhpAI6.D_xGMuJjkW5BPfs.xLB.Tf1cK0D_DKpxJAwrOyP3NlY5BNp55BNlan0Os5Apw.BfI"}',
    'X-Apple-I-TimeZone': 'Asia/Shanghai',

    'X-Apple-Session-Token': '12ZAaTlhPvB9hoBpwvTFXdci+NEGi3Kf0DlyRuE6N2MQYb91rU3SISnPMpthG51AsOfH9jXCwaMDk8/Z8ZUg+OHGUJetwhpHGJlTuev7uHqNR0xlHL8i/YBqshmq7VHBlyZ2DNkaRFGB6Uvm5375TVzsG8cKYf7hDuoiTfQqPcKGp8dW5bOj/M5klC4zz28Us3NRkWygvZg39IoCFWS3dwRQ4kNBtRNMVlBjxF7uzlhfkszK0GJv3zOgvW64agqc8tQxMJGC350X2zaFZC1TdjcdpsBVF38j7MBodQOkggqynwic33Txs6NudpHqbbcOCGJN8ft+/p1iG/PfFbHrKDa0ZzCYgxawcBJksJm1yEY2+nwb+dZXTQWtKFKRvlSRQwVTl0uWniQgpz4yFZq5a+suqgET+MkCYyAXbszFTU4xAlnKfS8kuQDgv7SngJWWOTneDZB1jZU/n/kcwH4bwGru8XxABkeffY8YKTc71M/ky6Y+uvW0WedE0nOJpCNzIJvjtrwAHkpUFK3g95PerZLet2pgoNkKANlUexCuvOVuVw+tBtnjVFalRAMHEZR7uNnqpRFNRYayAXUrJbyuNb/Sh0AtK8OqnnxCzyNn+vuH4Y2BT3y7UgC6zmHfVIJQcO5bvx0wn2DWGkxG1N3Yho266yQ12modiZNcbBsucwqnGLuaCkANp8nea9XNe6C+19Z9J7ihRSqKWxa+6Hjhv6b89OwMG4xOHyAyiIpxeb5O9pLy4oqU2MS9jbXAPz526ClyLWiM9z9ZK8AixDE7PcIGar5lAJ8KFO5rpalHdotoAm+jX08uYFEKJX+liVoRw67sVTzxdre0TkzHHLc/JhDxr1KdmmtUbRPepQqwKJ0wg6wr8172HpsGCz2hUCu5exops/8bAS3/PiDF0DDBbjBxuHROdn6eMS2HHLzHPJm8p24g2MAxigjfqWcs9NmOJ+0AIzLne9nH7Q==',
    'X-Apple-Skip-Repair-Attributes': '["hsa2_enrollment"]',
    'X-Apple-Widget-Key': 'af1139274f266b22b68c2a3e7ad932cb3c0bbe854e13a79af78dcc73136882c3',
    'X-Requested-With': 'XMLHttpRequest',
    'scnt': 'AAAA-jVDNjc0RkM0RTFDM0NDRDdCMEMwRjlDMjYxNURFRjEzRTQwNjNCQjM2Q0Y0MzMxNzlDRTMzNTZGODJENDM5OTk4NUVBQzAxRDcyQzMyNDUxQUZFQkY3OThCNzIzRUI4MDkwQkQ4M0IyREEzQTdENTA1QTg1OEMzRTFCMTdGQkNCRkNGQzBENTlENjFGNTQwMDU4QjVFNzM3QUQxNzA5REMxNjU0OUVFQTlDQTM2NEFDRTQyQ0M1N0QxNzhGNTJCRTMzRERCRkU2MTI5RUI2QTZDOUY5RjZFQ0NFRTVGODJDREUyQTJBOTlFNzE1QUFFN3wyAAABkPl6-BWZRirDB0rPGpDGmIVYP20KD2wF90H-P_aSeTvTsiI6sy4NIuETfTS4AD3emZ-7MDnSS_jXf40z1WFUoYwmxSqhl3mqXEQk1eoVhankFl-peg',
    'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}
response = requests.get('https://appleid.apple.com/account/manage/repair/options', cookies=cookies, headers=headers)
print(response.text)
print('第四个包'+"----"*100)



cookies = {
    'idclient': 'web',
    'dslang': 'CN-ZH',
    'site': 'CHN',
    'geo': 'CN',
    'aid': '5AAAA50572D3634A9DEF7F39B3F7788A',
    'aidsp': aidsp,
}

headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json',
    # 'Cookie': 'idclient=web; dslang=CN-ZH; site=CHN; geo=CN; aid=5AAAA50572D3634A9DEF7F39B3F7788A; aidsp=5C674FC4E1C3CCD7B0C0F9C2615DEF13E4063BB36CF433179CE3356F82D4399985EAC01D72C32451AFEBF798B723EB8090BD83B2DA3A7D505A858C3E1B17FBCBFCFC0D59D61F540058B5E737AD1709DC16549EEA9CA364ACE42CC57D178F52BE33DDBFE6129EB6A6C9F9F6ECCEE5F82CDE2A2A99E715AAE7',
    'Referer': 'https://appleid.apple.com/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
    'X-Apple-I-FD-Client-Info': '{"U":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36","L":"zh-CN","Z":"GMT+08:00","V":"1.1","F":"7la44j1e3NlY5BNlY5BSmHACVZXnNA9dGOHavFmxaDhpAI6.D_xGMuJjkW5BPfs.xLB.Tf1cK0D_DKpxJAwrOyP3NlY5BNp55BNlan0Os5Apw.BfI"}',
    'X-Apple-I-TimeZone': 'Asia/Shanghai',
    'X-Apple-ID-Session-Id': '5C674FC4E1C3CCD7B0C0F9C2615DEF13E4063BB36CF433179CE3356F82D4399985EAC01D72C32451AFEBF798B723EB8090BD83B2DA3A7D505A858C3E1B17FBCBFCFC0D59D61F540058B5E737AD1709DC16549EEA9CA364ACE42CC57D178F52BE33DDBFE6129EB6A6C9F9F6ECCEE5F82CDE2A2A99E715AAE7',
    'X-Apple-OAuth-Context': '3qm2p+fWhs3t6tcSJel4c1q0d+AsjzjObdoa4TSsv8iPlqoGGp/ROeY9c4ohfEZVPb/ZxIuTPYNmZdDnm64PkFdlqdMhkgTM76hnDJ3OtK3qSRYempL1+WQpmoqwhyhPdQKiR6Wm4YmM5xgqhfPP+pkV4YLuc8vjVdGO81guYmbdTj+YcWTMMeSbqU0zQrXdt/h2pRT//ny8UOyd4P1ybRReAB3jwNaTMfs=',
    'X-Apple-Session-Token': '12ZAaTlhPvB9hoBpwvTFXdci+NEGi3Kf0DlyRuE6N2MQYb91rU3SISnPMpthG51AsOfH9jXCwaMDk8/Z8ZUg+OHGUJetwhpHGJlTuev7uHqNR0xlHL8i/YBqshmq7VHBlyZ2DNkaRFGB6Uvm5375TVzsG8cKYf7hDuoiTfQqPcKGp8dW5bOj/M5klC4zz28Us3NRkWygvZg39IoCFWS3dwRQ4kNBtRNMVlBjxF7uzlhfkszK0GJv3zOgvW64agqc8tQxMJGC350X2zaFZC1TdjcdpsBVF38j7MBodQOkggqynwic33Txs6NudpHqbbcOCGJN8ft+/p1iG/PfFbHrKDa0ZzCYgxawcBJksJm1yEY2+nwb+dZXTQWtKFKRvlSRQwVTl0uWniQgpz4yFZq5a+suqgET+MkCYyAXbszFTU4xAlnKfS8kuQDgv7SngJWWOTneDZB1jZU/n/kcwH4bwGru8XxABkeffY8YKTc71M/ky6Y+uvW0WedE0nOJpCNzIJvjtrwAHkpUFK3g95PerZLet2pgoNkKANlUexCuvOVuVw+tBtnjVFalRAMHEZR7uNnqpRFNRYayAXUrJbyuNb/Sh0AtK8OqnnxCzyNn+vuH4Y2BT3y7UgC6zmHfVIJQcO5bvx0wn2DWGkxG1N3Yho266yQ12modiZNcbBsucwqnGLuaCkANp8nea9XNe6C+19Z9J7ihRSqKWxa+6Hjhv6b89OwMG4xOHyAyiIpxeb5O9pLy4oqU2MS9jbXAPz526ClyLWiM9z9ZK8AixDE7PcIGar5lAJ8KFO5rpalHdotoAm+jX08uYFEKJX+liVoRw67sVTzxdre0TkzHHLc/JhDxr1KdmmtUbRPepQqwKJ0wg6wr8172HpsGCz2hUCu5exops/8bAS3/PiDF0DDBbjBxuHROdn6eMS2HHLzHPJm8p24g2MAxigjfqWcs9NmOJ+0AIzLne9nH7Q==',
    'X-Apple-Skip-Repair-Attributes': '[]',
    'X-Apple-Widget-Key': 'af1139274f266b22b68c2a3e7ad932cb3c0bbe854e13a79af78dcc73136882c3',
    'X-Requested-With': 'XMLHttpRequest',
    'scnt': 'AAAA-jVDNjc0RkM0RTFDM0NDRDdCMEMwRjlDMjYxNURFRjEzRTQwNjNCQjM2Q0Y0MzMxNzlDRTMzNTZGODJENDM5OTk4NUVBQzAxRDcyQzMyNDUxQUZFQkY3OThCNzIzRUI4MDkwQkQ4M0IyREEzQTdENTA1QTg1OEMzRTFCMTdGQkNCRkNGQzBENTlENjFGNTQwMDU4QjVFNzM3QUQxNzA5REMxNjU0OUVFQTlDQTM2NEFDRTQyQ0M1N0QxNzhGNTJCRTMzRERCRkU2MTI5RUI2QTZDOUY5RjZFQ0NFRTVGODJDREUyQTJBOTlFNzE1QUFFN3wyAAABkPl6-BWZRirDB0rPGpDGmIVYP20KD2wF90H-P_aSeTvTsiI6sy4NIuETfTS4AD3emZ-7MDnSS_jXf40z1WFUoYwmxSqhl3mqXEQk1eoVhankFl-peg',
    'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

response = requests.get('https://appleid.apple.com/account/security/upgrade', cookies=cookies, headers=headers)
print(response.json())
print('第五个包'+"----"*100)




# --------------------------------------------------------------------------------------------------
# cookies = {
#     'aidsp':aidsp2,
# }

# headers = {
#     'Accept': 'application/json, text/plain, */*',
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0'
# }
# response = requests.get('https://appleid.apple.com/account/manage/security/devices', cookies=cookies, headers=headers)
# print(response.json())
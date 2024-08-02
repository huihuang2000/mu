import requests, re, logging, json

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s\n",
    datefmt="%Y-%m-%d %H:%M:%S",
    handlers=[logging.StreamHandler()],
)

name = "jacobgordon6s@hotmail.com"
passs = "Aa147369"

question_one = "你少年时代最好的朋友叫什么名字？"
answer_one = "py1234"
question_two = "你的理想工作是什么？"
answer_two = "gz1234"
question_three = "你的父母是在哪里认识的？"
answer_three = "fm1234"
# ------------------------------------------------------------------------------------------------------------------------------------
# one
cookies = {
    "dssid2": "c71e8b00-8802-4176-aec7-02d1e369f1d3",
    "dssf": "1",
}
headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "DNT": "1",
    "Pragma": "no-cache",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "none",
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0",
    "sec-ch-ua": '"Not)A;Brand";v="99", "Microsoft Edge";v="127", "Chromium";v="127"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
}
response_1 = requests.get(
    "https://appleid.apple.com/", cookies=cookies, headers=headers
)
aidsp_1 = response_1.cookies.get("aidsp")
scnt_7 = response_1.headers["scnt"]
logging.info(f"aidsp_1----{aidsp_1}")
logging.info(f"scnt_7----{scnt_7}")

# two
headers = {
    "Accept": "application/json, text/plain, */*",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Content-Type": "application/json",
    "DNT": "1",
    "Pragma": "no-cache",
    "Referer": "https://appleid.apple.com/",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0",
    "X-Apple-I-FD-Client-Info": '{"U":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0","L":"zh-CN","Z":"GMT+08:00","V":"1.1","F":".la44j1e3NlY5BNlY5BSmHACVZXnNA9dHHavS3eFMurJhBR.uMp4UdHz13NldjV2pNk0ug9WJ3uJtBE_HzWBzu0Y5BNlYJNNlY5QB4bVNjMk.CLJ"}',
    "X-Apple-I-Request-Context": "ca",
    "X-Apple-I-TimeZone": "Asia/Shanghai",
    "sec-ch-ua": '"Not)A;Brand";v="99", "Microsoft Edge";v="127", "Chromium";v="127"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
}
response_2 = requests.get("https://appleid.apple.com/bootstrap/portal", headers=headers)
aidsp_2 = response_2.cookies.get("aidsp")  # 没用上
serviceKey = response_2.json()["serviceKey"]  # 用上了
logging.info(f"aidsp_2----{aidsp_2}")
logging.info(f"serviceKey----{serviceKey}")

# 用aidsp_1,
# three
headers = {
    "Host": "appleid.apple.com",
    "Connection": "keep-alive",
    "sec-ch-ua": '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    "X-Apple-I-FD-Client-Info": '{"U":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36","L":"zh-CN","Z":"GMT+08:00","V":"1.1","F":"7la44j1e3NlY5BNlY5BSmHACVZXnNA9dMGAqBfg.CyhpAI6.D_xGMuJjkW5BOQs.xLB.Tf1cK0D_DI2tFEp5UaJBNlY5BPY25BNnOVgw24uy.Cbz"}',
    "X-Apple-I-Request-Context": "ca",
    "sec-ch-ua-mobile": "?0",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36",
    "Content-Type": "application/json",
    "Accept": "application/json, text/plain, */*",
    "X-Apple-I-TimeZone": "Asia/Shanghai",
    "sec-ch-ua-platform": '"Windows"',
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Dest": "empty",
    "Referer": "https://appleid.apple.com/",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Cookie": f"idclient=web; dslang=CN-ZH; site=CHN; aidsp={aidsp_1}; geo=CN",
}
response = requests.get(
    "https://appleid.apple.com/account/manage/gs/ws/token", headers=headers
)
scnt = response.headers["scnt"]
X_Apple_I_Request_ID = response.headers["X-Apple-I-Request-ID"]
logging.info(f"scnt----{scnt}")
logging.info(f"X_Apple_I_Request_ID----{X_Apple_I_Request_ID}")

# four
url = "https://appleid.apple.com/jslog"
headers = {
    "Host": "appleid.apple.com",
    "Connection": "keep-alive",
    "Content-Length": "88",
    "sec-ch-ua": '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    "scnt": scnt,
    "X-Apple-I-FD-Client-Info": '{"U":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36","L":"zh-CN","Z":"GMT+08:00","V":"1.1","F":"Fla44j1e3NlY5BNlY5BSmHACVZXnNA9dMGAqBZB7AxQeLaD.SAuXjodUW1BNmWjV2pNk0ug9WJ3uJtBE_.zJOyO7lY5BNleBBNlYCa1nkBMfs.ELl"}',
    "X-Apple-I-Request-Context": "ca",
    "sec-ch-ua-mobile": "?0",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36",
    "Content-Type": "application/json",
    "Accept": "application/json, text/plain, */*",
    "X-Apple-I-TimeZone": "Asia/Shanghai",
    "sec-ch-ua-platform": '"Windows"',
    "Origin": "https://appleid.apple.com",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Dest": "empty",
    "Referer": "https://appleid.apple.com/",
    # "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Cookie": f"idclient=web; dslang=CN-ZH; site=CHN; aidsp={aidsp_1}; geo=CN",
}
data = {
    "title": "ROUTE CHANGED",
    "type": "INFO",
    "messageMap": {"ACTION": "FE_INFO"},
    "details": "{}",
}
response = requests.post(url, headers=headers, data=data)
aid_1 = response.cookies.get("aid")
logging.info(f"aid_1----{aid_1}")

# X-Apple-ID-Session-Id和aid_2同一个
# five
url = "https://appleid.apple.com/jslog"
headers = {
    "Host": "appleid.apple.com",
    "Connection": "keep-alive",
    "Content-Length": "108",
    "sec-ch-ua": '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    "scnt": scnt,
    "X-Apple-I-FD-Client-Info": '{"U":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36","L":"zh-CN","Z":"GMT+08:00","V":"1.1","F":"7la44j1e3NlY5BNlY5BSmHACVZXnNA9dMGAqB0J9QxQeLaD.SAuXjodUW1BNpMk0ugN.xL4Fe1S9Ra6mVUeBzB.NlY5BNp55BNlan0Os5Apw.1_d"}',
    "X-Apple-I-Request-Context": "ca",
    "sec-ch-ua-mobile": "?0",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36",
    "Content-Type": "application/json",
    "Accept": "application/json, text/plain, */*",
    "X-Apple-I-TimeZone": "Asia/Shanghai",
    "sec-ch-ua-platform": '"Windows"',
    "Origin": "https://appleid.apple.com",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Dest": "empty",
    "Referer": "https://appleid.apple.com/",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Cookie": f"idclient=web; dslang=CN-ZH; site=CHN; aidsp={aidsp_1}; geo=CN; aid={aid_1}",
}
data = {
    "message": "sign-in",
    "title": "ROUTE CHANGED",
    "type": "INFO",
    "messageMap": {"ACTION": "FE_INFO"},
    "details": "{}",
}
response = requests.post(url, headers=headers, data=data)
aid_2 = response.cookies.get("aid")
logging.info(f"aid_2----{aid_2}")

# 他也会返回scnt，但是没用到
# six
url = f"https://idmsa.apple.com/appleauth/auth/authorize/signin?frame_id=auth-xgo22dgf-qlc6-e2kq-uw0c-4z1vnc57&skVersion=7&iframeId=auth-xgo22dgf-qlc6-e2kq-uw0c-4z1vnc57&client_id={serviceKey}&redirect_uri=https://appleid.apple.com&response_type=code&response_mode=web_message&state=auth-xgo22dgf-qlc6-e2kq-uw0c-4z1vnc57&authVersion=latest"
headers = {
    "Host": "idmsa.apple.com",
    "Connection": "keep-alive",
    "sec-ch-ua": '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
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
    "Cookie": "dslang=CN-ZH; site=CHN; geo=CN",
}
response = requests.get(url, headers=headers)
X_Apple_Auth_Attributes = response.headers["X-Apple-Auth-Attributes"]
X_Apple_HC_Challenge = response.headers["X-Apple-HC-Challenge"]
aasp = response.cookies.get("aasp")
logging.info(f"X_Apple_Auth_Attributes----{X_Apple_Auth_Attributes}")
logging.info(f"X_Apple_HC_Challenge----{X_Apple_HC_Challenge}")
logging.info(f"aasp----{aasp}")

# seven
url = "https://idmsa.apple.com/appleauth/jslog"
headers = {
    "Host": "idmsa.apple.com",
    "Connection": "keep-alive",
    "Content-Length": "154",
    "sec-ch-ua": '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    "scnt": "",
    "x-csrf-token": "",
    "sec-ch-ua-mobile": "?0",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36",
    "Content-type": "application/json",
    "Accept": "application/json",
    "sec-ch-ua-platform": '"Windows"',
    "Origin": "https://idmsa.apple.com",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Dest": "empty",
    "Referer": "https://idmsa.apple.com/",
    # "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Cookie": f"dslang=CN-ZH; site=CHN; geo=CN; aasp={aasp}",
}
data = {
    "title": "Hashcash generation",
    "type": "INFO",
    "message": "APPLE ID : Performace - 0.027300000000046565 s",
    "details": '{"pageVisibilityState":"visible"}',
}
response = requests.post(url, headers=headers, data=data)
aa = response.cookies.get("aa")
logging.info(f"aa----{aa}")

# eight
url = "https://env-00jxgsqva6td.dev-hz.cloudbasefunction.cn/A1?type=1"
payload = {f"email": {name}}
Key = requests.post(url=url, data=payload).json()

# nine
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
scnt_1 = response_2.headers["scnt"]
logging.info(f"scnt_1----{scnt_1}")

# ten
url = "https://env-00jxgsqva6td.dev-hz.cloudbasefunction.cn/A1?type=2"
payload = {
    "email": name,
    "iterations": response_2.json()["iteration"],
    "Value": response_2.json()["b"],
    "salt": response_2.json()["salt"],
    "password": passs,
    "protocol": response_2.json()["protocol"],
    "privateHexValue": Key["privateHexValue"],
    "publicHexValue": Key["publicHexValue"],
}
response_3 = requests.post(url=url, json=payload).json()

# eleven
headers = {
    "Host": "idmsa.apple.com",
    "Connection": "keep-alive",
    "Content-Length": "214",
    "sec-ch-ua": '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    "scnt": scnt_1,
    "X-Apple-Widget-Key": "af1139274f266b22b68c2a3e7ad932cb3c0bbe854e13a79af78dcc73136882c3",
    "X-Apple-Frame-Id": "auth-xgo22dgf-qlc6-e2kq-uw0c-4z1vnc57",
    "X-Apple-I-FD-Client-Info": '{"U":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36","L":"zh-CN","Z":"GMT+08:00","V":"1.1","F":"7la44j1e3NlY5BNlY5BSmHACVZXnNA9dMGAq.bfpCUfSHolk2dUJKy_Aw7GY5ey.EKY.6eke4FIdIZkyJ2xF6w9GY5BNlYJNNlY5QB4bVNjMk.4sL"}',
    "X-Apple-OAuth-Redirect-URI": "https://appleid.apple.com",
    "X-Apple-OAuth-Client-Id": "af1139274f266b22b68c2a3e7ad932cb3c0bbe854e13a79af78dcc73136882c3",
    "X-Apple-OAuth-Client-Type": "firstPartyAuth",
    "X-Requested-With": "XMLHttpRequest",
    "X-APPLE-HC": "1:10:20240730082557:2dd9c513daab667bdef7632eca3caed3::697",
    "sec-ch-ua-platform": '"Windows"',
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
    "Cookie": f"dslang=CN-ZH; site=CHN; geo=CN; aasp={aasp}; aa={aa}",
}
json_data = {
    "accountName": name,
    "rememberMe": False,
    "m1": response_3["M1"],
    "c": response_2.json()["c"],
    "m2": response_3["M2"],
}
response_4 = requests.post(
    url="https://idmsa.apple.com/appleauth/auth/signin/complete?isRememberMeEnabled=true",
    headers=headers,
    json=json_data,
)
# CK = response_4.headers.get("Set-Cookie")
# myacinfo_pattern = re.compile(r"myacinfo=([^;]+)")
# myacinfo_match = myacinfo_pattern.search(CK).group(1)
scnt_2 = response_4.headers["scnt"]
X_Apple_ID_Session_Id = response_4.headers["X-Apple-ID-Session-Id"]
X_Apple_Auth_Attributes = response_4.headers["X-Apple-Auth-Attributes"]
logging.info(f"scnt_2----{scnt_2}")
logging.info(f"X_Apple_ID_Session_Id----{X_Apple_ID_Session_Id}")
logging.info(f"X_Apple_Auth_Attributes----{X_Apple_Auth_Attributes}")

# twelve
url = "https://idmsa.apple.com/appleauth/auth"
headers = {
    "Host": "idmsa.apple.com",
    "Connection": "keep-alive",
    "sec-ch-ua": '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    "scnt": scnt_2,
    "X-Apple-Widget-Key": "af1139274f266b22b68c2a3e7ad932cb3c0bbe854e13a79af78dcc73136882c3",
    "X-Apple-Frame-Id": "auth-xgo22dgf-qlc6-e2kq-uw0c-4z1vnc57",
    "X-Apple-I-FD-Client-Info": '{"U":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36","L":"zh-CN","Z":"GMT+08:00","V":"1.1","F":"7la44j1e3NlY5BNlY5BSmHACVZXnNA9dMGAq.4H_MurJhBR.uMp4UdHz13NlejV2pNk0ug9WJ3uJtBE_.zJ0z13NlY5BNp55BNlan0Os5Apw.3Ol"}',
    "X-Apple-OAuth-Redirect-URI": "https://appleid.apple.com",
    "X-Apple-OAuth-Client-Id": "af1139274f266b22b68c2a3e7ad932cb3c0bbe854e13a79af78dcc73136882c3",
    "X-Apple-OAuth-Client-Type": "firstPartyAuth",
    "X-Requested-With": "XMLHttpRequest",
    "sec-ch-ua-platform": '"Windows"',
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
    "Cookie": f"dslang=CN-ZH; site=CHN; geo=CN; aasp={aasp}; aa={aa}",
}
response = requests.get(
    url=url,
    headers=headers,
)
scnt_3 = response.headers["scnt"]
X_Apple_Auth_Attributes = response.headers["X-Apple-Auth-Attributes"]

regex_pattern = r'"securityQuestions":\s*(\{(?:[^{}]|\{(?:[^{}]|\{.*?\})*\})*\})'
match = re.search(regex_pattern, response.text, re.DOTALL)
if match:
    json_str = match.group(1)
    try:
        security_questions_data = json.loads(json_str)
        print("Security Questions Data:", security_questions_data)
        # questions_answers = {
        #     self.question_one: self.answer_one,
        #     self.question_two: self.answer_two,
        #     self.question_three: self.answer_three,
        # }
        questions_answers = {
            question_one: answer_one,
            question_two: answer_two,
            question_three: answer_three,
        }
        answers = []
        questions = security_questions_data["questions"]
        for question in questions:
            if question["question"] == question_one:
                answer = questions_answers.get(question_one)
            elif question["question"] == question_two:
                answer = questions_answers.get(question_two)
            elif question["question"] == question_three:
                answer = questions_answers.get(question_three)
            else:
                answer = ""

            answers.append(
                {
                    "question": question["question"],
                    "answer": answer,
                    "number": question["number"],
                    "id": question["id"],
                }
            )

    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")
else:
    print("No securityQuestions data found.")

logging.info(f"scnt_3----{scnt_3}")
logging.info(f"X_Apple_Auth_Attributes----{X_Apple_Auth_Attributes}")
# logging.info(f"X_Apple_Auth_Attributes----{response.text}")

# thirteen
url = "https://idmsa.apple.com/appleauth/jslog"
headers = {
    "Host": "idmsa.apple.com",
    "Connection": "keep-alive",
    "Content-Length": "518",
    "sec-ch-ua": '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    "scnt": scnt_2,
    "x-csrf-token": "",
    "sec-ch-ua-mobile": "?0",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36",
    "Content-type": "application/json",
    "Accept": "application/json",
    "sec-ch-ua-platform": '"Windows"',
    "Origin": "https://idmsa.apple.com",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Dest": "empty",
    "Referer": "https://idmsa.apple.com/",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Cookie": f"dslang=CN-ZH; site=CHN; geo=CN; aasp={aasp}; aa={aa}",
}
data = {
    "type": "INFO",
    "title": "AppleAuthFFPerf-2",
    "message": 'APPLE ID : {"data":{"showPasswordField":{"federatedCalled":{"duration":361},"duration":1101},"init":{"initData":{"duration":17.699999999953434},"initCalled":{"duration":284.5}},"complete":{"completeData":{"duration":24}},"authFirstFactor":{"errorPasswordCalled":{"duration":336.5999999999767}}},"order":["showPasswordField"]}',
    "iframeId": "auth-xgo22dgf-qlc6-e2kq-uw0c-4z1vnc57",
    "details": '{"pageVisibilityState":"visible"}',
}
response = requests.post(url, headers=headers, data=data)
aa_2 = response.cookies.get("aa")
logging.info(f"aa_2----{aa_2}")

# fourteen
url = "https://idmsa.apple.com/appleauth/jslog"
headers = {
    "Host": "idmsa.apple.com",
    "Connection": "keep-alive",
    "Content-Length": "218",
    "sec-ch-ua": '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    "scnt": scnt_3,
    "x-csrf-token": "",
    "sec-ch-ua-mobile": "?0",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36",
    "Content-type": "application/json",
    "Accept": "application/json",
    "sec-ch-ua-platform": '"Windows"',
    "Origin": "https://idmsa.apple.com",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Dest": "empty",
    "Referer": "https://idmsa.apple.com/",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Cookie": f"dslang=CN-ZH; site=CHN; geo=CN; aasp={aasp}; aa={aa_2}",
}
data = {
    "type": "INFO",
    "title": "Second Factor setup",
    "message": "APPLE ID : Will start second factor setup for sa auth type.",
    "iframeId": "auth-xgo22dgf-qlc6-e2kq-uw0c-4z1vnc57",
    "details": '{"pageVisibilityState":"visible"}',
}
response = requests.post(url, headers=headers, data=data)
aa_3 = response.cookies.get("aa")
logging.info(f"aa_3----{aa_3}")

# fifteen
url = "https://idmsa.apple.com/appleauth/auth/verify/questions"
headers = {
    "Host": "idmsa.apple.com",
    "Connection": "keep-alive",
    "Content-Length": "201",
    "sec-ch-ua": '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    "scnt": scnt_3,
    "X-Apple-Widget-Key": serviceKey,
    "X-Apple-Frame-Id": "auth-xgo22dgf-qlc6-e2kq-uw0c-4z1vnc57",
    "X-Apple-I-FD-Client-Info": '{"U":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36","L":"zh-CN","Z":"GMT+08:00","V":"1.1","F":"7la44j1e3NlY5BNlY5BSmHACVZXnNA9dMGAqueBKKyhpAI6.D_xGMuJjkW5BPfs.xLB.Tf1cK0D_DI2tFEp.UeJBNlY5BPY25BNnOVgw24uy.CkO"}',
    "X-Apple-OAuth-Redirect-URI": "https://appleid.apple.com",
    "X-Apple-OAuth-Client-Id": serviceKey,
    "X-Apple-OAuth-Client-Type": "firstPartyAuth",
    "sec-ch-ua-platform": '"Windows"',
    "X-Apple-App-Id": serviceKey,
    "X-Apple-ID-Session-Id": aasp,
    "X-Apple-Auth-Attributes": X_Apple_Auth_Attributes,
    "sec-ch-ua-mobile": "?0",
    "X-Apple-OAuth-Response-Type": "code",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36",
    "X-Apple-OAuth-Response-Mode": "web_message",
    "Content-Type": "application/json",
    "Accept": "application/json, text/plain, */*",
    "X-Apple-Domain-Id": "1",
    "X-Apple-OAuth-State": "auth-xgo22dgf-qlc6-e2kq-uw0c-4z1vnc57",
    "Origin": "https://idmsa.apple.com",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Dest": "empty",
    "Referer": "https://idmsa.apple.com/",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Cookie": f"dslang=CN-ZH; site=CHN; geo=CN; aasp={aasp}; aa={aa_3}",
}
data = {"questions": answers}
response = requests.post(url, headers=headers, json=data)
scnt_4 = response.headers["scnt"]
X_Apple_Repair_Session_Token = response.headers["X-Apple-Repair-Session-Token"]
X_Apple_OAuth_Context = response.headers["X-Apple-OAuth-Context"]
Location = response.headers["Location"]
logging.info(f"scnt_4----{scnt_4}")
logging.info(f"X_Apple_Repair_Session_Token----{X_Apple_Repair_Session_Token}")
logging.info(f"X_Apple_OAuth_Context----{X_Apple_OAuth_Context}")
logging.info(f"Location----{Location}")

# sixteen
url = "https://appleid.apple.com/widget/account/repair?widgetKey=af1139274f266b22b68c2a3e7ad932cb3c0bbe854e13a79af78dcc73136882c3&rv=1&language=zh_CN_CHN"
headers = {
    "Host": "appleid.apple.com",
    "Connection": "keep-alive",
    "sec-ch-ua": '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Sec-Fetch-Site": "same-site",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-User": "?1",
    "Sec-Fetch-Dest": "iframe",
    "Referer": "https://idmsa.apple.com/",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Cookie": f"idclient=web; dslang=CN-ZH; site=CHN; aidsp={aidsp_1}; geo=CN; aid={aid_2}",
}
response = requests.get(
    url=url,
    headers=headers,
)
scnt_5 = response.headers["scnt"]
logging.info(f"scnt_5----{scnt_5}")

# seventeen
url = "https://appleid.apple.com/account/manage/repair/options"
headers = {
    "Host": "appleid.apple.com",
    "Connection": "keep-alive",
    "X-Apple-ID-Session-Id": aidsp_1,
    "scnt": scnt_5,
    "X-Apple-Widget-Key": serviceKey,
    "sec-ch-ua": '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    "X-Apple-I-FD-Client-Info": '{"U":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36","L":"zh-CN","Z":"GMT+08:00","V":"1.1","F":"7la44j1e3NlY5BNlY5BSmHACVZXnNA9dMGAquW9dCyhpAI6.D_xGMuJjkW5BPfs.xLB.Tf1cK0D_DI2tFEp.Ue1BNlY5BPY25BNnOVgw24uy.AOX"}',
    "sec-ch-ua-mobile": "?0",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36",
    "Content-Type": "application/json",
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "X-Apple-OAuth-Context": X_Apple_OAuth_Context,
    "X-Requested-With": "XMLHttpRequest",
    "X-Apple-Session-Token": X_Apple_Repair_Session_Token,
    "X-Apple-I-TimeZone": "Asia/Shanghai",
    "X-Apple-Skip-Repair-Attributes": "[]",
    "sec-ch-ua-platform": '"Windows"',
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Dest": "empty",
    "Referer": "https://appleid.apple.com/",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Cookie": f"idclient=web; dslang=CN-ZH; site=CHN; aidsp={aidsp_1}; geo=CN; aid={aid_2}",
}
response = requests.get(
    url=url,
    headers=headers,
)
scnt_6 = response.headers["scnt"]
X_Apple_Session_Token = response.headers["X-Apple-Session-Token"]
logging.info(f"scnt_6----{scnt_6}")
logging.info(f"X_Apple_Session_Token----{X_Apple_Session_Token}")

# eighteen
url = "https://appleid.apple.com/account/security/upgrade"
headers = {
    "Host": "appleid.apple.com",
    "Connection": "keep-alive",
    "X-Apple-ID-Session-Id": aidsp_1,
    "scnt": scnt_6,
    "X-Apple-Widget-Key": serviceKey,
    "sec-ch-ua": '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    "X-Apple-I-FD-Client-Info": '{"U":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36","L":"zh-CN","Z":"GMT+08:00","V":"1.1","F":"7la44j1e3NlY5BNlY5BSmHACVZXnNA9dMGAquW9dCyhpAI6.D_xGMuJjkW5BPfs.xLB.Tf1cK0D_DI2tFEp.Ue1BNlY5BPY25BNnOVgw24uy.AOX"}',
    "sec-ch-ua-mobile": "?0",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36",
    "Content-Type": "application/json",
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "X-Apple-OAuth-Context": X_Apple_OAuth_Context,
    "X-Requested-With": "XMLHttpRequest",
    "X-Apple-Session-Token": X_Apple_Session_Token,
    "X-Apple-I-TimeZone": "Asia/Shanghai",
    "X-Apple-Skip-Repair-Attributes": "[]",
    "sec-ch-ua-platform": '"Windows"',
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Dest": "empty",
    "Referer": "https://appleid.apple.com/",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Cookie": f"idclient=web; dslang=CN-ZH; site=CHN; aidsp={aidsp_1}; geo=CN; aid={aid_2}",
}
response = requests.get(
    url=url,
    headers=headers,
)
X_Apple_Session_Token_2 = response.headers["X-Apple-Session-Token"]
logging.info(f"X_Apple_Session_Token_2----{X_Apple_Session_Token_2}")
# logging.info(f'response----{response.text}')

# nineteen
url = "https://appleid.apple.com/account/security/upgrade/setuplater"
headers = {
    "Host": "appleid.apple.com",
    "Connection": "keep-alive",
    "X-Apple-ID-Session-Id": aidsp_1,
    "scnt": scnt_6,
    "X-Apple-Widget-Key": serviceKey,
    "sec-ch-ua": '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    "X-Apple-I-FD-Client-Info": '{"U":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36","L":"zh-CN","Z":"GMT+08:00","V":"1.1","F":"7la44j1e3NlY5BNlY5BSmHACVZXnNA9dMGAquW9dCyhpAI6.D_xGMuJjkW5BPfs.xLB.Tf1cK0D_DI2tFEp.Ue1BNlY5BPY25BNnOVgw24uy.AOX"}',
    "sec-ch-ua-mobile": "?0",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36",
    "Content-Type": "application/json",
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "X-Apple-OAuth-Context": X_Apple_OAuth_Context,
    "X-Requested-With": "XMLHttpRequest",
    "X-Apple-Session-Token": X_Apple_Session_Token_2,
    "X-Apple-I-TimeZone": "Asia/Shanghai",
    "X-Apple-Skip-Repair-Attributes": "[]",
    "sec-ch-ua-platform": '"Windows"',
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Dest": "empty",
    "Referer": "https://appleid.apple.com/",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Cookie": f"idclient=web; dslang=CN-ZH; site=CHN; aidsp={aidsp_1}; geo=CN; aid={aid_2}",
}
response = requests.get(
    url=url,
    headers=headers,
)
X_Apple_Session_Token_3 = response.headers["X-Apple-Session-Token"]
logging.info(f"X_Apple_Session_Token_3----{X_Apple_Session_Token_3}")

# twenty
url = "https://appleid.apple.com/account/manage/repair/options"
headers = {
    "Host": "appleid.apple.com",
    "Connection": "keep-alive",
    "X-Apple-ID-Session-Id": aidsp_1,
    "scnt": scnt_6,
    "X-Apple-Widget-Key": serviceKey,
    "sec-ch-ua": '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    "X-Apple-I-FD-Client-Info": '{"U":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36","L":"zh-CN","Z":"GMT+08:00","V":"1.1","F":"7la44j1e3NlY5BNlY5BSmHACVZXnNA9dMGAquW9dCyhpAI6.D_xGMuJjkW5BPfs.xLB.Tf1cK0D_DI2tFEp.Ue1BNlY5BPY25BNnOVgw24uy.AOX"}',
    "sec-ch-ua-mobile": "?0",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36",
    "Content-Type": "application/json",
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "X-Apple-OAuth-Context": X_Apple_OAuth_Context,
    "X-Requested-With": "XMLHttpRequest",
    "X-Apple-Session-Token": X_Apple_Session_Token_3,
    "X-Apple-I-TimeZone": "Asia/Shanghai",
    "X-Apple-Skip-Repair-Attributes": '["hsa2_enrollment"]',
    "sec-ch-ua-platform": '"Windows"',
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Dest": "empty",
    "Referer": "https://appleid.apple.com/",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Cookie": f"idclient=web; dslang=CN-ZH; site=CHN; aidsp={aidsp_1}; geo=CN; aid={aid_2}",
}
response = requests.get(
    url=url,
    headers=headers,
)
X_Apple_Session_Token_4 = response.headers["X-Apple-Session-Token"]
logging.info(f"X_Apple_Session_Token_4----{X_Apple_Session_Token_4}")

# twenty-one
url = "https://idmsa.apple.com/appleauth/auth/repair/complete"
headers = {
    "Host": "idmsa.apple.com",
    "Connection": "keep-alive",
    "Content-Length": "0",
    "X-Apple-Repair-Session-Token": X_Apple_Session_Token_4,
    "scnt": scnt_2,
    "X-Apple-Widget-Key": serviceKey,
    "X-Apple-Frame-Id": "auth-xgo22dgf-qlc6-e2kq-uw0c-4z1vnc57",
    "sec-ch-ua": '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    "X-Apple-I-FD-Client-Info": '{"U":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36","L":"zh-CN","Z":"GMT+08:00","V":"1.1","F":"7la44j1e3NlY5BNlY5BSmHACVZXnNA9dMGAquxTmdQxQeLaD.SAuXjodUW1BNork0ugN.xL4Fe1S9Ra6mVUe.zKp5BNlY5CGWY5BOgkLT0XxU..Bco"}',
    "X-Apple-OAuth-Redirect-URI": "https://appleid.apple.com",
    "X-Apple-OAuth-Client-Id": serviceKey,
    "X-Apple-OAuth-Client-Type": "firstPartyAuth",
    "X-Requested-With": "XMLHttpRequest",
    "sec-ch-ua-platform": '"Windows"',
    "X-Apple-ID-Session-Id": aasp,
    "X-Apple-Auth-Attributes": X_Apple_Auth_Attributes,
    "sec-ch-ua-mobile": "?0",
    "X-Apple-OAuth-Response-Type": "code",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36",
    "X-Apple-OAuth-Response-Mode": "web_message",
    "Content-Type": "application/json",
    "Accept": "application/json;charset=utf-8",
    "X-Apple-Domain-Id": "1",
    "X-Apple-OAuth-State": "auth-xgo22dgf-qlc6-e2kq-uw0c-4z1vnc57",
    "Origin": "https://idmsa.apple.com",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Dest": "empty",
    "Referer": "https://idmsa.apple.com/",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Cookie": f"dslang=CN-ZH; site=CHN; geo=CN; aasp={aasp}; aa={aa_3}",
}
data = ""
response = requests.post(url, headers=headers, data=data)
myacinfo = response.cookies.get("myacinfo")
logging.info(f"myacinfo----{myacinfo}")

# twenty-two
url = "https://appleid.apple.com/account/manage/gs/ws/token"
headers = {
    "Host": "appleid.apple.com",
    "Connection": "keep-alive",
    "sec-ch-ua": '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    "scnt": scnt_7,
    "X-Apple-I-FD-Client-Info": '{"U":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36","L":"zh-CN","Z":"GMT+08:00","V":"1.1","F":"7la44j1e3NlY5BNlY5BSmHACVZXnNA9dMGAquxZkxfxQeLaD.SAuXjodUW1BNpMk0ugN.xL4Fe1S9Ra6mVUe.zKq5BNlY5CGWY5BOgkLT0XxU...m1"}',
    "X-Apple-I-Request-Context": "ca",
    "sec-ch-ua-mobile": "?0",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36",
    "Content-Type": "application/json",
    "Accept": "application/json, text/plain, */*",
    "X-Apple-I-TimeZone": "Asia/Shanghai",
    "sec-ch-ua-platform": '"Windows"',
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Dest": "empty",
    "Referer": "https://appleid.apple.com/",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Cookie": f"idclient=web; dslang=CN-ZH; site=CHN; aidsp={aidsp_1}; geo=CN; aid={aa_3}; myacinfo={myacinfo}",
}
response = requests.get(
    url=url,
    headers=headers,
)
X_Apple_I_Request_ID = response.headers["X-Apple-I-Request-ID"]
scnt_8 = response.headers["scnt"]
awat = response.cookies.get("awat")
caw = response.cookies.get("caw")
caw_at = response.cookies.get("caw-at")
aidsp_2 = response.cookies.get("aidsp")
logging.info(f"X_Apple_I_Request_ID----{X_Apple_I_Request_ID}")
logging.info(f"scnt_8----{scnt_8}")
logging.info(f"awat----{awat}")
logging.info(f"caw----{caw}")
logging.info(f"caw_at----{caw_at}")
logging.info(f"aidsp_2----{aidsp_2}")

# twenty-three
url = "https://appleid.apple.com/account/manage/profile/avatar"
headers = {
    "Host": "appleid.apple.com",
    "Connection": "keep-alive",
    "sec-ch-ua": '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    "scnt": scnt_8,
    "X-Apple-I-FD-Client-Info": '{"U":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36","L":"zh-CN","Z":"GMT+08:00","V":"1.1","F":"7la44j1e3NlY5BNlY5BSmHACVZXnNA9dMGAquxdTmQxQeLaD.SAuXjodUW1BNmrk0ugN.xL4Fe1S9Ra6mVUe.zKq5BNlY5CGWY5BOgkLT0XxU..BXr"}',
    "X-Apple-I-Request-Context": "ca",
    "sec-ch-ua-mobile": "?0",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36",
    "Content-Type": "application/json",
    "Accept": "application/json, text/plain, */*",
    "X-Apple-I-TimeZone": "Asia/Shanghai",
    "sec-ch-ua-platform": '"Windows"',
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Dest": "empty",
    "Referer": "https://appleid.apple.com/",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Cookie": f"idclient=web; dslang=CN-ZH; site=CHN; geo=CN; aid={aa_3}; myacinfo={myacinfo}; awat={awat}; caw={caw}; caw-at={caw_at}; aidsp={aidsp_2}",
}
response = requests.get(
    url=url,
    headers=headers,
)
caw_at_2 = response.cookies.get("caw-at")
logging.info(f"caw_at_2----{caw_at_2}")

# twenty-four
url = "https://appleid.apple.com/account/manage"
headers = {
    "Host": "appleid.apple.com",
    "Connection": "keep-alive",
    "sec-ch-ua": '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    "scnt": scnt_8,
    "X-Apple-I-FD-Client-Info": '{"U":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36","L":"zh-CN","Z":"GMT+08:00","V":"1.1","F":"7la44j1e3NlY5BNlY5BSmHACVZXnNA9dMGAquxdTlfxQeLaD.SAuXjodUW1BNmrk0ugN.xL4Fe1S9Ra6mVUe.zKq5BNlY5CGWY5BOgkLT0XxU..4Cc"}',
    "X-Apple-I-Request-Context": "ca",
    "sec-ch-ua-mobile": "?0",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36",
    "Content-Type": "application/json",
    "Accept": "application/json, text/plain, */*",
    "X-Apple-I-TimeZone": "Asia/Shanghai",
    "sec-ch-ua-platform": '"Windows"',
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Dest": "empty",
    "Referer": "https://appleid.apple.com/",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Cookie": f"idclient=web; dslang=CN-ZH; site=CHN; geo=CN; aid={aa_3}; myacinfo={myacinfo}; awat={awat}; caw={caw}; caw-at={caw_at}; aidsp={aidsp_2}",
}
response = requests.get(
    url=url,
    headers=headers,
)
scnt_9 = response.headers["scnt"]
awat_2 = response.cookies.get("awat")
dat = response.cookies.get("dat")
logging.info(f"scnt_9----{scnt_9}")
logging.info(f"awat_2----{awat_2}")
logging.info(f"dat----{dat}")

# twenty-five
url = "https://appleid.apple.com/account/manage/profile/avatar"
headers = {
    "Host": "appleid.apple.com",
    "Connection": "keep-alive",
    "sec-ch-ua": '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    "scnt": scnt_8,
    "X-Apple-I-FD-Client-Info": '{"U":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36","L":"zh-CN","Z":"GMT+08:00","V":"1.1","F":"7la44j1e3NlY5BNlY5BSmHACVZXnNA9dMGAqv49ZCyhpAI6.D_xGMuJjkW5BPfs.xLB.Tf1cK0D_DI2tFEp.Ud9BNlY5BPY25BNnOVgw24uy.6v5"}',
    "X-Apple-I-Request-Context": "ca",
    "sec-ch-ua-mobile": "?0",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36",
    "Content-Type": "application/json",
    "Accept": "application/json, text/plain, */*",
    "X-Apple-I-TimeZone": "Asia/Shanghai",
    "X-Apple-Api-Key": "cbf64fd6843ee630b463f358ea0b707b",  # 可能有问题
    "sec-ch-ua-platform": '"Windows"',
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Dest": "empty",
    "Referer": "https://appleid.apple.com/",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Cookie": f"idclient=web; dslang=CN-ZH; site=CHN; geo=CN; aid={aa_3}; myacinfo={myacinfo}; caw={caw}; aidsp={aidsp_2}; caw-at={caw_at}; awat={awat_2}; dat={dat}",
}
response = requests.get(
    url=url,
    headers=headers,
)
scnt_10 = response.headers["scnt"]
caw_at_3 = response.cookies.get("caw-at")
awat_5 = response.cookies.get("awat")
logging.info(f"scnt_10----{scnt_10}")
logging.info(f"caw_at_3----{caw_at_3}")
logging.info(f"awat_5----{awat_5}")

# twenty-six
url = "https://appleid.apple.com/account/manage/payment"
headers = {
    "Host": "appleid.apple.com",
    "Connection": "keep-alive",
    "sec-ch-ua": '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    "scnt": scnt_8,
    "X-Apple-I-FD-Client-Info": '{"U":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36","L":"zh-CN","Z":"GMT+08:00","V":"1.1","F":"7la44j1e3NlY5BNlY5BSmHACVZXnNA9dMGAqv49Z4yhpAI6.D_xGMuJjkW5BOQs.xLB.Tf1cK0D_DI2tFEp.Ud9BNlY5BPY25BNnOVgw24uy.7iu"}',
    "X-Apple-I-Request-Context": "ca",
    "sec-ch-ua-mobile": "?0",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36",
    "Content-Type": "application/json",
    "Accept": "application/json, text/plain, */*",
    "X-Apple-I-TimeZone": "Asia/Shanghai",
    "X-Apple-Api-Key": "cbf64fd6843ee630b463f358ea0b707b",
    "sec-ch-ua-platform": '"Windows"',
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Dest": "empty",
    "Referer": "https://appleid.apple.com/",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Cookie": f"idclient=web; dslang=CN-ZH; site=CHN; geo=CN; aid={aa_3}; myacinfo={myacinfo}; caw={caw}; aidsp={aidsp_2}; caw-at={caw_at}; awat={awat_2}; dat={dat}",
}
response = requests.get(
    url=url,
    headers=headers,
)
awat_7 = response.cookies.get("awat")
logging.info(f"awat_7----{awat_7}")

# 显示所有设备!!!
# twenty-seven
url = "https://appleid.apple.com/account/manage/security/devices"
headers = {
    "Host": "appleid.apple.com",
    "Connection": "keep-alive",
    "sec-ch-ua": '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    "scnt": scnt_8,
    "X-Apple-I-FD-Client-Info": '{"U":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36","L":"zh-CN","Z":"GMT+08:00","V":"1.1","F":"7la44j1e3NlY5BNlY5BSmHACVZXnNA9dMGAqv49bfUfSHolk2dUJKy_Aw7GY5ey.EKY.6eke4FIdIZkyJ2xF6uHY5BNlY5cklY5BqNAE.lTjV.4_O"}',
    "X-Apple-I-Request-Context": "ca",
    "sec-ch-ua-mobile": "?0",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36",
    "Content-Type": "application/json",
    "Accept": "application/json, text/plain, */*",
    "X-Apple-I-TimeZone": "Asia/Shanghai",
    "X-Apple-Api-Key": "cbf64fd6843ee630b463f358ea0b707b",
    "sec-ch-ua-platform": '"Windows"',
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Dest": "empty",
    "Referer": "https://appleid.apple.com/",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Cookie": f"idclient=web; dslang=CN-ZH; site=CHN; geo=CN; aid={aa_3}; myacinfo={myacinfo}; caw={caw}; aidsp={aidsp_2}; caw-at={caw_at}; awat={awat_2}; dat={dat}",
}
response = requests.get(
    url=url,
    headers=headers,
)
scnt_11 = response.headers["scnt"]
awat_6 = response.cookies.get("awat")
id_list = [device["id"] for device in response.json()["devices"]]
logging.info(f"devices----{id_list}")
logging.info(f"response----{response.json()}")
logging.info(f"scnt_11----{scnt_11}")
logging.info(f"awat_6----{awat_6}")

# twenty-eight
url = "https://appleid.apple.com/jslog"
headers = {
    "Host": "appleid.apple.com",
    "Connection": "keep-alive",
    "Content-Length": "115",
    "sec-ch-ua": '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    "scnt": scnt_8,
    "X-Apple-I-FD-Client-Info": '{"U":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36","L":"zh-CN","Z":"GMT+08:00","V":"1.1","F":"7la44j1e3NlY5BNlY5BSmHACVZXnNA9dFTocTk1e0UfSHolk2dUJKy_Aw7GY5ey.EKY.6eke4FIidlU9OyZfx70Y5BNlYJNNlY5QB4bVNjMk.1bU"}',
    "X-Apple-I-Request-Context": "ca",
    "sec-ch-ua-mobile": "?0",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36",
    "Content-Type": "application/json",
    "Accept": "application/json, text/plain, */*",
    "X-Apple-I-TimeZone": "Asia/Shanghai",
    "X-Apple-Api-Key": "cbf64fd6843ee630b463f358ea0b707b",
    "sec-ch-ua-platform": '"Windows"',
    "Origin": "https://appleid.apple.com",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Dest": "empty",
    "Referer": "https://appleid.apple.com/",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
    "Cookie": f"dssid2=b99cb946-5068-4333-b0bb-11d6b876874b; dssf=1; as_sfa=Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE; pltvcid=undefined; pldfltcid=f123ec0ccd59486f8ffee8e4e2c0f00e060; idclient=web; dslang=CN-ZH; site=CHN; geo=CN; aid={aa_3}; myacinfo={myacinfo}; caw={caw}; aidsp={aidsp_2}; caw-at={caw_at}; awat={awat_2}; dat={dat}",
}
data = {
    "message": "account/manage",
    "title": "ROUTE CHANGED",
    "type": "INFO",
    "messageMap": {"ACTION": "FE_INFO"},
    "details": "{}",
}
response = requests.post(url, headers=headers, json=data)

# twenty-nine
url = "https://appleid.apple.com/jslog"
headers = {
    "Host": "appleid.apple.com",
    "Connection": "keep-alive",
    "Content-Length": "226",
    "sec-ch-ua": '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    "scnt": scnt_8,
    "X-Apple-I-FD-Client-Info": '{"U":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36","L":"zh-CN","Z":"GMT+08:00","V":"1.1","F":"7la44j1e3NlY5BNlY5BSmHACVZXnNA9dFTocTk.FxfxQeLaD.SAuXjodUW1BNpMk0ugN.xL4Fe1SpDAtIEo_Ud.BNlY5BPY25BNnOVgw24uy..bi"}',
    "X-Apple-I-Request-Context": "ca",
    "sec-ch-ua-mobile": "?0",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36",
    "Content-Type": "application/json",
    "Accept": "application/json, text/plain, */*",
    "X-Apple-I-TimeZone": "Asia/Shanghai",
    "X-Apple-Api-Key": "cbf64fd6843ee630b463f358ea0b707b",
    "sec-ch-ua-platform": '"Windows"',
    "Origin": "https://appleid.apple.com",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Dest": "empty",
    "Referer": "https://appleid.apple.com/",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
    "Cookie": f"dssid2=b99cb946-5068-4333-b0bb-11d6b876874b; dssf=1; as_sfa=Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE; pltvcid=undefined; pldfltcid=f123ec0ccd59486f8ffee8e4e2c0f00e060; idclient=web; dslang=CN-ZH; site=CHN; geo=CN; aid={aa_3}; myacinfo={myacinfo}; caw={caw}; aidsp={aidsp_2}; dat={dat}; caw-at={caw_at}; awat={awat_5}",
}
data = {
    "message": "Attempting to connect to module.",
    "title": "MODULE CONNECTING",
    "type": "INFO",
    "messageMap": {"ACTION": "FE_INFO"},
    "details": '{"name":"family-section","wid":"4e50560c-57c3-4c8f-83ca-b48e334fc262","time":505}',
}
response = requests.post(url, headers=headers, json=data)
# logging.info(f'scnt_11----{response.headers}')
# logging.info(f'scnt_11----{response.status_code}')

# thirty
url = "https://appleid.apple.com/jslog"
headers = {
    "Host": "appleid.apple.com",
    "Connection": "keep-alive",
    "Content-Length": "226",
    "sec-ch-ua": '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    "scnt": scnt_8,
    "X-Apple-I-FD-Client-Info": '{"U":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36","L":"zh-CN","Z":"GMT+08:00","V":"1.1","F":"7la44j1e3NlY5BNlY5BSmHACVZXnNA9dFTocTk.FxfxQeLaD.SAuXjodUW1BNpMk0ugN.xL4Fe1SpDAtIEo_Ud.BNlY5BPY25BNnOVgw24uy..bi"}',
    "X-Apple-I-Request-Context": "ca",
    "sec-ch-ua-mobile": "?0",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36",
    "Content-Type": "application/json",
    "Accept": "application/json, text/plain, */*",
    "X-Apple-I-TimeZone": "Asia/Shanghai",
    "X-Apple-Api-Key": "cbf64fd6843ee630b463f358ea0b707b",
    "sec-ch-ua-platform": '"Windows"',
    "Origin": "https://appleid.apple.com",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Dest": "empty",
    "Referer": "https://appleid.apple.com/",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
    "Cookie": f"dssid2=b99cb946-5068-4333-b0bb-11d6b876874b; dssf=1; as_sfa=Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE; pltvcid=undefined; pldfltcid=f123ec0ccd59486f8ffee8e4e2c0f00e060; idclient=web; dslang=CN-ZH; site=CHN; geo=CN; aid={aa_3}; myacinfo={myacinfo}; caw={caw}; aidsp={aidsp_2}; dat={dat}; caw-at={caw_at}; awat={awat_5}",
}
data = {
    "message": "Module connected successfully.",
    "title": "MODULE CONNECTED",
    "type": "INFO",
    "messageMap": {"ACTION": "FE_INFO"},
    "details": '{"name":"family-section","wid":"4e50560c-57c3-4c8f-83ca-b48e334fc262","time":663,"version":"unknown"}',
}
response = requests.post(url, headers=headers, json=data)
# logging.info(f'scnt_11----{response.headers}')
# logging.info(f'scnt_11----{response.status_code}')

# thirty-one
url = "https://familyws.icloud.apple.com/api/i18n"
headers = {
    "Host": "familyws.icloud.apple.com",
    "Connection": "keep-alive",
    "sec-ch-ua": '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    "sec-ch-ua-mobile": "?0",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36",
    "sec-ch-ua-platform": '"Windows"',
    "Accept": "*/*",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Dest": "empty",
    "Referer": "https://familyws.icloud.apple.com/members?wid=4e50560c-57c3-4c8f-83ca-b48e334fc262&env=idms_prod&theme=light&locale=zh_CN",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
    "Cookie": f"dssid2=b99cb946-5068-4333-b0bb-11d6b876874b; dssf=1; as_sfa=Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE; pltvcid=undefined; pldfltcid=f123ec0ccd59486f8ffee8e4e2c0f00e060; dslang=CN-ZH; site=CHN; geo=CN; myacinfo={myacinfo}; caw={caw}; caw-at={caw_at}",
}
response = requests.get(
    url=url,
    headers=headers,
)
# logging.info(f'scnt_11----{response.text}')

# thirty-two
url = "https://familyws.icloud.apple.com/api/member-photos"
Header = {
    "Host": "familyws.icloud.apple.com",
    "Connection": "keep-alive",
    "sec-ch-ua": '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    "sec-ch-ua-mobile": "?0",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36",
    "sec-ch-ua-platform": '"Windows"',
    "Accept": "*/*",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Dest": "empty",
    "Referer": "https://familyws.icloud.apple.com/members?wid=4e50560c-57c3-4c8f-83ca-b48e334fc262&env=idms_prod&theme=light&locale=zh_CN",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
    "Cookie": f"dssid2=b99cb946-5068-4333-b0bb-11d6b876874b; dssf=1; as_sfa=Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE; pltvcid=undefined; pldfltcid=f123ec0ccd59486f8ffee8e4e2c0f00e060; dslang=CN-ZH; site=CHN; geo=CN; myacinfo={myacinfo}; caw={caw}; caw-at={caw_at}",
}
response = requests.get(
    url=url,
    headers=headers,
)
# logging.info(f'scnt_11----{response.text}')

# thirty-three
url = "https://appleid.apple.com/jslog"
headers = {
    "Host": "appleid.apple.com",
    "Connection": "keep-alive",
    "Content-Length": "217",
    "sec-ch-ua": '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    "scnt": scnt_8,
    "X-Apple-I-FD-Client-Info": '{"U":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36","L":"zh-CN","Z":"GMT+08:00","V":"1.1","F":"7la44j1e3NlY5BNlY5BSmHACVZXnNA9dFTocTog7DpyhpAI6.D_xGMuJjkW5BPfs.xLB.Tf1cK0Dub4wdbuHjomY5BNlY5cklY5BqNAE.lTjV.5_U"}',
    "X-Apple-I-Request-Context": "ca",
    "sec-ch-ua-mobile": "?0",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36",
    "Content-Type": "application/json",
    "Accept": "application/json, text/plain, */*",
    "X-Apple-I-TimeZone": "Asia/Shanghai",
    "X-Apple-Api-Key": "cbf64fd6843ee630b463f358ea0b707b",
    "sec-ch-ua-platform": '"Windows"',
    "Origin": "https://appleid.apple.com",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Dest": "empty",
    "Referer": "https://appleid.apple.com/",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
    "Cookie": f"dssid2=b99cb946-5068-4333-b0bb-11d6b876874b; dssf=1; as_sfa=Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE; pltvcid=undefined; pldfltcid=f123ec0ccd59486f8ffee8e4e2c0f00e060; idclient=web; dslang=CN-ZH; site=CHN; geo=CN; myacinfo={myacinfo}; caw={caw}; aidsp={aidsp_2}; dat={dat}; caw-at={caw_at}; awat={awat_6}; aid={aa_3}",
}
data = {
    "message": "Module is ready to be shown.",
    "title": "MODULE READY",
    "type": "INFO",
    "messageMap": {"ACTION": "FE_INFO"},
    "details": '{"name":"family-section","wid":"4e50560c-57c3-4c8f-83ca-b48e334fc262","time":965}',
}
response = requests.post(url, headers=headers, json=data)
# logging.info(f'scnt_11----{response.headers}')

# thirty-four
url = "https://appleid.apple.com/jslog"
headers = {
    "Host": "appleid.apple.com",
    "Connection": "keep-alive",
    "Content-Length": "224",
    "sec-ch-ua": '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    "scnt": scnt_8,
    "X-Apple-I-FD-Client-Info": '{"U":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36","L":"zh-CN","Z":"GMT+08:00","V":"1.1","F":"7la44j1e3NlY5BNlY5BSmHACVZXnNA9dFTocTogBdQxQeLaD.SAuXjodUW1BNpMk0ugN.xL4Fe1SpDAtIEo_Ud_5BNlY5CGWY5BOgkLT0XxU..7e4"}',
    "X-Apple-I-Request-Context": "ca",
    "sec-ch-ua-mobile": "?0",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36",
    "Content-Type": "application/json",
    "Accept": "application/json, text/plain, */*",
    "X-Apple-I-TimeZone": "Asia/Shanghai",
    "X-Apple-Api-Key": "cbf64fd6843ee630b463f358ea0b707b",
    "sec-ch-ua-platform": '"Windows"',
    "Origin": "https://appleid.apple.com",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Dest": "empty",
    "Referer": "https://appleid.apple.com/",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
    "Cookie": f"dssid2=b99cb946-5068-4333-b0bb-11d6b876874b; dssf=1; as_sfa=Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE; pltvcid=undefined; pldfltcid=f123ec0ccd59486f8ffee8e4e2c0f00e060; idclient=web; dslang=CN-ZH; site=CHN; geo=CN; myacinfo={myacinfo}; caw={caw}; aidsp={aidsp_2}; dat={dat}; caw-at={caw_at}; awat={awat_6}; aid={aa_3}",
}
data = {
    "message": "Module should be shown",
    "title": "MODULE WILL SHOW RESOLVED",
    "type": "INFO",
    "messageMap": {"ACTION": "FE_INFO"},
    "details": '{"name":"family-section","wid":"4e50560c-57c3-4c8f-83ca-b48e334fc262","time":965}',
}
response = requests.post(url, headers=headers, json=data)
aid_3 = response.cookies.get("aid")
X_Apple_ID_Session_Id = response.headers["X-Apple-ID-Session-Id"]
logging.info(f"aid_3----{aid_3}")
logging.info(f"X_Apple_ID_Session_Id----{X_Apple_ID_Session_Id}")

# thirty-five
url = "https://appleid.apple.com/jslog"
headers = {
    "Host": "appleid.apple.com",
    "Connection": "keep-alive",
    "Content-Length": "131",
    "sec-ch-ua": '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    "scnt": scnt_8,
    "X-Apple-I-FD-Client-Info": '{"U":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36","L":"zh-CN","Z":"GMT+08:00","V":"1.1","F":"7la44j1e3NlY5BNlY5BSmHACVZXnNA9dFTocTrMebhUfSHolk2dUJKy_Aw7GY55y.EKY.6eke4FIidlU9OyZfxEJNlY5BNp55BNlan0Os5Apw.A1F"}',
    "X-Apple-I-Request-Context": "ca",
    "sec-ch-ua-mobile": "?0",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36",
    "Content-Type": "application/json",
    "Accept": "application/json, text/plain, */*",
    "X-Apple-I-TimeZone": "Asia/Shanghai",
    "X-Apple-Api-Key": "cbf64fd6843ee630b463f358ea0b707b",
    "sec-ch-ua-platform": '"Windows"',
    "Origin": "https://appleid.apple.com",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Dest": "empty",
    "Referer": "https://appleid.apple.com/",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
    "Cookie": f"dssid2=b99cb946-5068-4333-b0bb-11d6b876874b; dssf=1; as_sfa=Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE; pltvcid=undefined; pldfltcid=f123ec0ccd59486f8ffee8e4e2c0f00e060; idclient=web; dslang=CN-ZH; site=CHN; geo=CN; myacinfo={myacinfo}; caw={caw}; aidsp={aidsp_2}; dat={dat}; aid={aid_3}; itspod=16; caw-at={caw_at}; awat={awat_7}",
}
data = {
    "message": "account/manage/section/devices",
    "title": "ROUTE CHANGED",
    "type": "INFO",
    "messageMap": {"ACTION": "FE_INFO"},
    "details": "{}",
}
response = requests.post(url, headers=headers, json=data)
aid_4 = response.cookies.get("aid")
X_Apple_ID_Session_Id_3 = response.headers["X-Apple-ID-Session-Id"]


for device_id in id_list[:]:
    url = f"https://appleid.apple.com/account/manage/security/devices/{device_id}"
    headers = {
        "Host": "appleid.apple.com",
        "Connection": "keep-alive",
        "sec-ch-ua": '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
        "scnt": scnt_8,
        "X-Apple-I-FD-Client-Info": '{"U":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36","L":"zh-CN","Z":"GMT+08:00","V":"1.1","F":".la44j1e3NlY5BNlY5BSmHACVZXnNA9dFTodcJa_NurJhBR.uMp4UdHz13NldjV2pNk0ug9WJ3veRMmaUd9z1ZNlY5BNp55BNlan0Os5Apw.BGt"}',
        "X-Apple-I-Request-Context": "ca",
        "sec-ch-ua-mobile": "?0",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36",
        "Content-Type": "application/json",
        "Accept": "application/json, text/plain, */*",
        "X-Apple-I-TimeZone": "Asia/Shanghai",
        "X-Apple-Api-Key": "cbf64fd6843ee630b463f358ea0b707b",
        "sec-ch-ua-platform": '"Windows"',
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Referer": "https://appleid.apple.com/",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
        "Cookie": f"dssid2=b99cb946-5068-4333-b0bb-11d6b876874b; dssf=1; as_sfa=Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE; pltvcid=undefined; pldfltcid=f123ec0ccd59486f8ffee8e4e2c0f00e060; idclient=web; dslang=CN-ZH; site=CHN; geo=CN; myacinfo={myacinfo}; caw={caw}; aidsp={aidsp_2}; dat={dat}; itspod=16; caw-at={caw_at}; awat={awat_7}; aid={aid_4}",
    }
    response = requests.get(
        url=url,
        headers=headers,
    )
    caw_at_4 = response.cookies.get("caw-at")
    awat_8 = response.cookies.get("awat")
    scnt_12 = response.headers["scnt"]
    logging.info(f"caw_at_4----{caw_at_4}")
    logging.info(f"awat_8----{awat_8}")
    logging.info(f"scnt_12----{scnt_12}")

    url = f"https://appleid.apple.com/account/manage/security/devices/{device_id}"
    headers = {
        "Host": "appleid.apple.com",
        "Connection": "keep-alive",
        "sec-ch-ua": '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
        "scnt": scnt_8,
        "X-Apple-I-FD-Client-Info": '{"U":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36","L":"zh-CN","Z":"GMT+08:00","V":"1.1","F":"7la44j1e3NlY5BNlY5BSmHACVZXnNA9dFTodcTeVSfxQeLaD.SAuXjodUW1BNork0ugN.xL4Fe1SpDAtIEo_UWuY5BNlY5cklY5BqNAE.lTjV.8Ez"}',
        "X-Apple-I-Request-Context": "ca",
        "sec-ch-ua-mobile": "?0",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36",
        "Content-Type": "application/json",
        "Accept": "application/json, text/plain, */*",
        "X-Apple-I-TimeZone": "Asia/Shanghai",
        "X-Apple-Api-Key": "cbf64fd6843ee630b463f358ea0b707b",
        "sec-ch-ua-platform": '"Windows"',
        "Origin": "https://appleid.apple.com",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Referer": "https://appleid.apple.com/",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
        "Cookie": f"dssid2=b99cb946-5068-4333-b0bb-11d6b876874b; dssf=1; as_sfa=Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE; pltvcid=undefined; pldfltcid=f123ec0ccd59486f8ffee8e4e2c0f00e060; idclient=web; dslang=CN-ZH; site=CHN; geo=CN; myacinfo={myacinfo}; caw={caw}; aidsp={aidsp_2}; dat={dat}; itspod=16; aid={aid_4}; caw-at={caw_at}; awat={awat_8}",
    }
    response = requests.delete(
        url=url,
        headers=headers,
    )
    logging.info(f"caw_at_4----{response.text}")

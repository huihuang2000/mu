import requests, re, logging, json
from retry import retry

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s\n",
    datefmt="%Y-%m-%d %H:%M:%S",
)


# ------------------------------------------------------------------------------------------------------------------------------------
class APPLE_Remove:
    def __init__(self, **kwargs) -> None:
        self.username = kwargs.get("username")
        self.password = kwargs.get("password")
        self.question_one = kwargs.get("Question_one")
        self.answer_one = kwargs.get("Answer_one")
        self.question_two = kwargs.get("Question_two")
        self.answer_two = kwargs.get("Answer_two")
        self.question_three = kwargs.get("Question_three")
        self.answer_three = kwargs.get("Answer_three")

        self.DL = {
            "http": "http://usera1:pwdword2@tunnel1.docip.net:18199",
            "https": "http://usera1:pwdword2@tunnel1.docip.net:18199",
        }
        self.time = (3, 5)

    @retry(tries=20)
    def one(self):
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
            "https://appleid.apple.com/",
            cookies=cookies,
            headers=headers,
            proxies=self.DL,
            timeout=self.time,
        )
        self.aidsp_1 = response_1.cookies.get("aidsp")
        self.scnt_7 = response_1.headers["scnt"]
        logging.info(f"aidsp_1----{self.aidsp_1}")
        logging.info(f"scnt_7----{self.scnt_7}")
        return self

    @retry(tries=20)
    def two(self):
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
        response_2 = requests.get(
            "https://appleid.apple.com/bootstrap/portal",
            headers=headers,
            proxies=self.DL,
            timeout=self.time,
        )
        self.aidsp_2 = response_2.cookies.get("aidsp")  # 没用上
        self.serviceKey = response_2.json()["serviceKey"]  # 用上了
        logging.info(f"aidsp_2----{self.aidsp_2}")
        logging.info(f"serviceKey----{self.serviceKey}")
        return self

    @retry(tries=20)
    def three(self):
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
            "Cookie": f"idclient=web; dslang=CN-ZH; site=CHN; aidsp={self.aidsp_1}; geo=CN",
        }
        response = requests.get(
            "https://appleid.apple.com/account/manage/gs/ws/token",
            headers=headers,
            proxies=self.DL,
            timeout=self.time,
        )
        self.scnt = response.headers["scnt"]
        self.X_Apple_I_Request_ID = response.headers["X-Apple-I-Request-ID"]
        logging.info(f"scnt----{self.scnt}")
        logging.info(f"X_Apple_I_Request_ID----{self.X_Apple_I_Request_ID}")
        return self

    @retry(tries=20)
    def four(self):
        url = "https://appleid.apple.com/jslog"
        headers = {
            "Host": "appleid.apple.com",
            "Connection": "keep-alive",
            "Content-Length": "88",
            "sec-ch-ua": '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
            "scnt": self.scnt,
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
            "Cookie": f"idclient=web; dslang=CN-ZH; site=CHN; aidsp={self.aidsp_1}; geo=CN",
        }
        data = {
            "title": "ROUTE CHANGED",
            "type": "INFO",
            "messageMap": {"ACTION": "FE_INFO"},
            "details": "{}",
        }
        response = requests.post(
            url,
            headers=headers,
            data=data,
            proxies=self.DL,
            timeout=self.time,
        )
        self.aid_1 = response.cookies.get("aid")
        logging.info(f"aid_1----{self.aid_1}")
        return self

    @retry(tries=20)
    def six(self):
        url = f"https://idmsa.apple.com/appleauth/auth/authorize/signin?frame_id=auth-xgo22dgf-qlc6-e2kq-uw0c-4z1vnc57&skVersion=7&iframeId=auth-xgo22dgf-qlc6-e2kq-uw0c-4z1vnc57&client_id={self.serviceKey}&redirect_uri=https://appleid.apple.com&response_type=code&response_mode=web_message&state=auth-xgo22dgf-qlc6-e2kq-uw0c-4z1vnc57&authVersion=latest"
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
        response = requests.get(
            url,
            headers=headers,
            proxies=self.DL,
            timeout=self.time,
        )
        self.X_Apple_Auth_Attributes = response.headers["X-Apple-Auth-Attributes"]
        self.X_Apple_HC_Challenge = response.headers["X-Apple-HC-Challenge"]
        self.aasp = response.cookies.get("aasp")
        logging.info(f"X_Apple_Auth_Attributes----{self.X_Apple_Auth_Attributes}")
        logging.info(f"X_Apple_HC_Challenge----{self.X_Apple_HC_Challenge}")
        logging.info(f"aasp----{self.aasp}")
        return self

    @retry(tries=20)
    def eight(self):
        url = "https://env-00jxgsqva6td.dev-hz.cloudbasefunction.cn/A1?type=1"
        payload = {f"email": {self.username}}
        self.Key = requests.post(
            url=url,
            data=payload,
            proxies=self.DL,
            timeout=self.time,
        ).json()
        return self

    @retry(tries=20)
    def nine(self):
        combined_headers_and_cookies = {
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0",
        }
        json_data = {
            "a": self.Key["r"],
            "accountName": self.username,
            "protocols": [
                "s2k",
                "s2k_fo",
            ],
        }
        self.response_2 = requests.post(
            url="https://idmsa.apple.com/appleauth/auth/signin/init",
            headers=combined_headers_and_cookies,
            json=json_data,
            proxies=self.DL,
            timeout=self.time,
        )
        self.scnt_1 = self.response_2.headers["scnt"]
        logging.info(f"scnt_1----{self.scnt_1}")
        return self

    @retry(tries=20)
    def ten(self):
        url = "https://env-00jxgsqva6td.dev-hz.cloudbasefunction.cn/A1?type=2"
        payload = {
            "email": self.username,
            "iterations": self.response_2.json()["iteration"],
            "Value": self.response_2.json()["b"],
            "salt": self.response_2.json()["salt"],
            "password": self.password,
            "protocol": self.response_2.json()["protocol"],
            "privateHexValue": self.Key["privateHexValue"],
            "publicHexValue": self.Key["publicHexValue"],
        }
        self.response_3 = requests.post(
            url=url,
            json=payload,
            proxies=self.DL,
            timeout=self.time,
        ).json()
        return self

    @retry(tries=20)
    def eleven(self):
        headers = {
            "Host": "idmsa.apple.com",
            "Connection": "keep-alive",
            "Content-Length": "214",
            "sec-ch-ua": '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
            "scnt": self.scnt_1,
            "X-Apple-Widget-Key": "af1139274f266b22b68c2a3e7ad932cb3c0bbe854e13a79af78dcc73136882c3",
            "X-Apple-Frame-Id": "auth-xgo22dgf-qlc6-e2kq-uw0c-4z1vnc57",
            "X-Apple-I-FD-Client-Info": '{"U":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36","L":"zh-CN","Z":"GMT+08:00","V":"1.1","F":"7la44j1e3NlY5BNlY5BSmHACVZXnNA9dMGAq.bfpCUfSHolk2dUJKy_Aw7GY5ey.EKY.6eke4FIdIZkyJ2xF6w9GY5BNlYJNNlY5QB4bVNjMk.4sL"}',
            "X-Apple-OAuth-Redirect-URI": "https://appleid.apple.com",
            "X-Apple-OAuth-Client-Id": "af1139274f266b22b68c2a3e7ad932cb3c0bbe854e13a79af78dcc73136882c3",
            "X-Apple-OAuth-Client-Type": "firstPartyAuth",
            "X-Requested-With": "XMLHttpRequest",
            "X-APPLE-HC": "1:10:20240730082557:2dd9c513daab667bdef7632eca3caed3::697",
            "sec-ch-ua-platform": '"Windows"',
            "X-Apple-Auth-Attributes": self.X_Apple_Auth_Attributes,
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
            "Cookie": f"dslang=CN-ZH; site=CHN; geo=CN; aasp={self.aasp};",
        }
        json_data = {
            "accountName": self.username,
            "rememberMe": False,
            "m1": self.response_3["M1"],
            "c": self.response_2.json()["c"],
            "m2": self.response_3["M2"],
        }
        response_4 = requests.post(
            url="https://idmsa.apple.com/appleauth/auth/signin/complete?isRememberMeEnabled=true",
            headers=headers,
            json=json_data,
            proxies=self.DL,
            timeout=self.time,
        )
        # CK = response_4.headers.get("Set-Cookie")
        # myacinfo_pattern = re.compile(r"myacinfo=([^;]+)")
        # myacinfo_match = myacinfo_pattern.search(CK).group(1)
        self.scnt_2 = response_4.headers["scnt"]
        self.X_Apple_ID_Session_Id = response_4.headers["X-Apple-ID-Session-Id"]
        self.X_Apple_Auth_Attributes = response_4.headers["X-Apple-Auth-Attributes"]
        logging.info(f"scnt_2----{self.scnt_2}")
        logging.info(f"X_Apple_ID_Session_Id----{self.X_Apple_ID_Session_Id}")
        logging.info(f"X_Apple_Auth_Attributes----{self.X_Apple_Auth_Attributes}")
        return self

    # 此处需要修改密保
    @retry(tries=20)
    def twelve(self):
        url = "https://idmsa.apple.com/appleauth/auth"
        headers = {
            "Host": "idmsa.apple.com",
            "Connection": "keep-alive",
            "sec-ch-ua": '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
            "scnt": self.scnt_2,
            "X-Apple-Widget-Key": "af1139274f266b22b68c2a3e7ad932cb3c0bbe854e13a79af78dcc73136882c3",
            "X-Apple-Frame-Id": "auth-xgo22dgf-qlc6-e2kq-uw0c-4z1vnc57",
            "X-Apple-I-FD-Client-Info": '{"U":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36","L":"zh-CN","Z":"GMT+08:00","V":"1.1","F":"7la44j1e3NlY5BNlY5BSmHACVZXnNA9dMGAq.4H_MurJhBR.uMp4UdHz13NlejV2pNk0ug9WJ3uJtBE_.zJ0z13NlY5BNp55BNlan0Os5Apw.3Ol"}',
            "X-Apple-OAuth-Redirect-URI": "https://appleid.apple.com",
            "X-Apple-OAuth-Client-Id": "af1139274f266b22b68c2a3e7ad932cb3c0bbe854e13a79af78dcc73136882c3",
            "X-Apple-OAuth-Client-Type": "firstPartyAuth",
            "X-Requested-With": "XMLHttpRequest",
            "sec-ch-ua-platform": '"Windows"',
            "X-Apple-ID-Session-Id": self.aasp,
            "X-Apple-Auth-Attributes": self.X_Apple_Auth_Attributes,
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
            "Cookie": f"dslang=CN-ZH; site=CHN; geo=CN; aasp={self.aasp};",
        }
        response = requests.get(
            url=url,
            headers=headers,
            proxies=self.DL,
            timeout=self.time,
        )
        self.scnt_3 = response.headers["scnt"]
        self.X_Apple_Auth_Attributes = response.headers["X-Apple-Auth-Attributes"]

        regex_pattern = (
            r'"securityQuestions":\s*(\{(?:[^{}]|\{(?:[^{}]|\{.*?\})*\})*\})'
        )
        match = re.search(regex_pattern, response.text, re.DOTALL)
        if match:
            json_str = match.group(1)
            try:
                security_questions_data = json.loads(json_str)
                print("Security Questions Data:", security_questions_data)
                questions_answers = {
                    self.question_one: self.answer_one,
                    self.question_two: self.answer_two,
                    self.question_three: self.answer_three,
                }
                self.answers = []
                questions = security_questions_data["questions"]
                for question in questions:
                    if question["question"] == self.question_one:
                        answer = questions_answers.get(self.question_one)
                    elif question["question"] == self.question_two:
                        answer = questions_answers.get(self.question_two)
                    elif question["question"] == self.question_three:
                        answer = questions_answers.get(self.question_three)
                    else:
                        answer = ""

                    self.answers.append(
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

        logging.info(f"scnt_3----{self.scnt_3}")
        logging.info(f"X_Apple_Auth_Attributes----{self.X_Apple_Auth_Attributes}")
        # logging.info(f"X_Apple_Auth_Attributes----{response.text}")
        return self

    @retry(tries=20)
    def fifteen(self):
        url = "https://idmsa.apple.com/appleauth/auth/verify/questions"
        headers = {
            "Host": "idmsa.apple.com",
            "Connection": "keep-alive",
            "Content-Length": "201",
            "sec-ch-ua": '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
            "scnt": self.scnt_3,
            "X-Apple-Widget-Key": self.serviceKey,
            "X-Apple-Frame-Id": "auth-xgo22dgf-qlc6-e2kq-uw0c-4z1vnc57",
            "X-Apple-I-FD-Client-Info": '{"U":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36","L":"zh-CN","Z":"GMT+08:00","V":"1.1","F":"7la44j1e3NlY5BNlY5BSmHACVZXnNA9dMGAqueBKKyhpAI6.D_xGMuJjkW5BPfs.xLB.Tf1cK0D_DI2tFEp.UeJBNlY5BPY25BNnOVgw24uy.CkO"}',
            "X-Apple-OAuth-Redirect-URI": "https://appleid.apple.com",
            "X-Apple-OAuth-Client-Id": self.serviceKey,
            "X-Apple-OAuth-Client-Type": "firstPartyAuth",
            "sec-ch-ua-platform": '"Windows"',
            "X-Apple-App-Id": self.serviceKey,
            "X-Apple-ID-Session-Id": self.aasp,
            "X-Apple-Auth-Attributes": self.X_Apple_Auth_Attributes,
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
            "Cookie": f"dslang=CN-ZH; site=CHN; geo=CN; aasp={self.aasp};",
        }
        data = {"questions": self.answers}
        response = requests.post(
            url,
            headers=headers,
            json=data,
            proxies=self.DL,
            timeout=self.time,
        )
        self.scnt_4 = response.headers["scnt"]
        self.X_Apple_Repair_Session_Token = response.headers[
            "X-Apple-Repair-Session-Token"
        ]
        self.X_Apple_OAuth_Context = response.headers["X-Apple-OAuth-Context"]
        self.Location = response.headers["Location"]
        logging.info(f"scnt_4----{self.scnt_4}")
        logging.info(
            f"X_Apple_Repair_Session_Token----{self.X_Apple_Repair_Session_Token}"
        )
        logging.info(f"X_Apple_OAuth_Context----{self.X_Apple_OAuth_Context}")
        logging.info(f"Location----{self.Location}")
        return self

    @retry(tries=20)
    def sixteen(self):
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
            "Cookie": f"idclient=web; dslang=CN-ZH; site=CHN; aidsp={self.aidsp_1}; geo=CN;",
        }
        response = requests.get(
            url=url,
            headers=headers,
            proxies=self.DL,
            timeout=self.time,
        )
        self.scnt_5 = response.headers["scnt"]
        logging.info(f"scnt_5----{self.scnt_5}")
        return self

    @retry(tries=20)
    def seventeen(self):
        url = "https://appleid.apple.com/account/manage/repair/options"
        headers = {
            "Host": "appleid.apple.com",
            "Connection": "keep-alive",
            "X-Apple-ID-Session-Id": self.aidsp_1,
            "scnt": self.scnt_5,
            "X-Apple-Widget-Key": self.serviceKey,
            "sec-ch-ua": '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
            "X-Apple-I-FD-Client-Info": '{"U":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36","L":"zh-CN","Z":"GMT+08:00","V":"1.1","F":"7la44j1e3NlY5BNlY5BSmHACVZXnNA9dMGAquW9dCyhpAI6.D_xGMuJjkW5BPfs.xLB.Tf1cK0D_DI2tFEp.Ue1BNlY5BPY25BNnOVgw24uy.AOX"}',
            "sec-ch-ua-mobile": "?0",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36",
            "Content-Type": "application/json",
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "X-Apple-OAuth-Context": self.X_Apple_OAuth_Context,
            "X-Requested-With": "XMLHttpRequest",
            "X-Apple-Session-Token": self.X_Apple_Repair_Session_Token,
            "X-Apple-I-TimeZone": "Asia/Shanghai",
            "X-Apple-Skip-Repair-Attributes": "[]",
            "sec-ch-ua-platform": '"Windows"',
            "Sec-Fetch-Site": "same-origin",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Dest": "empty",
            "Referer": "https://appleid.apple.com/",
            "Accept-Encoding": "gzip, deflate, br, zstd",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Cookie": f"idclient=web; dslang=CN-ZH; site=CHN; aidsp={self.aidsp_1}; geo=CN;",
        }
        response = requests.get(
            url=url,
            headers=headers,
            proxies=self.DL,
            timeout=self.time,
        )
        self.scnt_6 = response.headers["scnt"]
        self.X_Apple_Session_Token = response.headers["X-Apple-Session-Token"]
        logging.info(f"scnt_6----{self.scnt_6}")
        logging.info(f"X_Apple_Session_Token----{self.X_Apple_Session_Token}")
        return self

    @retry(tries=20)
    def eighteen(self):
        url = "https://appleid.apple.com/account/security/upgrade"
        headers = {
            "Host": "appleid.apple.com",
            "Connection": "keep-alive",
            "X-Apple-ID-Session-Id": self.aidsp_1,
            "scnt": self.scnt_6,
            "X-Apple-Widget-Key": self.serviceKey,
            "sec-ch-ua": '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
            "X-Apple-I-FD-Client-Info": '{"U":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36","L":"zh-CN","Z":"GMT+08:00","V":"1.1","F":"7la44j1e3NlY5BNlY5BSmHACVZXnNA9dMGAquW9dCyhpAI6.D_xGMuJjkW5BPfs.xLB.Tf1cK0D_DI2tFEp.Ue1BNlY5BPY25BNnOVgw24uy.AOX"}',
            "sec-ch-ua-mobile": "?0",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36",
            "Content-Type": "application/json",
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "X-Apple-OAuth-Context": self.X_Apple_OAuth_Context,
            "X-Requested-With": "XMLHttpRequest",
            "X-Apple-Session-Token": self.X_Apple_Session_Token,
            "X-Apple-I-TimeZone": "Asia/Shanghai",
            "X-Apple-Skip-Repair-Attributes": "[]",
            "sec-ch-ua-platform": '"Windows"',
            "Sec-Fetch-Site": "same-origin",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Dest": "empty",
            "Referer": "https://appleid.apple.com/",
            "Accept-Encoding": "gzip, deflate, br, zstd",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Cookie": f"idclient=web; dslang=CN-ZH; site=CHN; aidsp={self.aidsp_1}; geo=CN;",
        }
        response = requests.get(
            url=url,
            headers=headers,
            proxies=self.DL,
            timeout=self.time,
        )
        self.X_Apple_Session_Token_2 = response.headers["X-Apple-Session-Token"]
        logging.info(f"X_Apple_Session_Token_2----{self.X_Apple_Session_Token_2}")
        # logging.info(f'response----{response.text}')
        return self

    @retry(tries=20)
    def nineteen(self):
        url = "https://appleid.apple.com/account/security/upgrade/setuplater"
        headers = {
            "Host": "appleid.apple.com",
            "Connection": "keep-alive",
            "X-Apple-ID-Session-Id": self.aidsp_1,
            "scnt": self.scnt_6,
            "X-Apple-Widget-Key": self.serviceKey,
            "sec-ch-ua": '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
            "X-Apple-I-FD-Client-Info": '{"U":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36","L":"zh-CN","Z":"GMT+08:00","V":"1.1","F":"7la44j1e3NlY5BNlY5BSmHACVZXnNA9dMGAquW9dCyhpAI6.D_xGMuJjkW5BPfs.xLB.Tf1cK0D_DI2tFEp.Ue1BNlY5BPY25BNnOVgw24uy.AOX"}',
            "sec-ch-ua-mobile": "?0",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36",
            "Content-Type": "application/json",
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "X-Apple-OAuth-Context": self.X_Apple_OAuth_Context,
            "X-Requested-With": "XMLHttpRequest",
            "X-Apple-Session-Token": self.X_Apple_Session_Token_2,
            "X-Apple-I-TimeZone": "Asia/Shanghai",
            "X-Apple-Skip-Repair-Attributes": "[]",
            "sec-ch-ua-platform": '"Windows"',
            "Sec-Fetch-Site": "same-origin",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Dest": "empty",
            "Referer": "https://appleid.apple.com/",
            "Accept-Encoding": "gzip, deflate, br, zstd",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Cookie": f"idclient=web; dslang=CN-ZH; site=CHN; aidsp={self.aidsp_1}; geo=CN;",
        }
        response = requests.get(
            url=url,
            headers=headers,
            proxies=self.DL,
            timeout=self.time,
        )
        self.X_Apple_Session_Token_3 = response.headers["X-Apple-Session-Token"]
        logging.info(f"X_Apple_Session_Token_3----{self.X_Apple_Session_Token_3}")
        return self

    @retry(tries=20)
    def twenty(self):
        url = "https://appleid.apple.com/account/manage/repair/options"
        headers = {
            "Host": "appleid.apple.com",
            "Connection": "keep-alive",
            "X-Apple-ID-Session-Id": self.aidsp_1,
            "scnt": self.scnt_6,
            "X-Apple-Widget-Key": self.serviceKey,
            "sec-ch-ua": '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
            "X-Apple-I-FD-Client-Info": '{"U":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36","L":"zh-CN","Z":"GMT+08:00","V":"1.1","F":"7la44j1e3NlY5BNlY5BSmHACVZXnNA9dMGAquW9dCyhpAI6.D_xGMuJjkW5BPfs.xLB.Tf1cK0D_DI2tFEp.Ue1BNlY5BPY25BNnOVgw24uy.AOX"}',
            "sec-ch-ua-mobile": "?0",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36",
            "Content-Type": "application/json",
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "X-Apple-OAuth-Context": self.X_Apple_OAuth_Context,
            "X-Requested-With": "XMLHttpRequest",
            "X-Apple-Session-Token": self.X_Apple_Session_Token_3,
            "X-Apple-I-TimeZone": "Asia/Shanghai",
            "X-Apple-Skip-Repair-Attributes": '["hsa2_enrollment"]',
            "sec-ch-ua-platform": '"Windows"',
            "Sec-Fetch-Site": "same-origin",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Dest": "empty",
            "Referer": "https://appleid.apple.com/",
            "Accept-Encoding": "gzip, deflate, br, zstd",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Cookie": f"idclient=web; dslang=CN-ZH; site=CHN; aidsp={self.aidsp_1}; geo=CN; ",
        }
        response = requests.get(
            url=url,
            headers=headers,
            proxies=self.DL,
            timeout=self.time,
        )
        self.X_Apple_Session_Token_4 = response.headers["X-Apple-Session-Token"]
        logging.info(f"X_Apple_Session_Token_4----{self.X_Apple_Session_Token_4}")
        return self

    @retry(tries=20)
    def twenty_one(self):
        url = "https://idmsa.apple.com/appleauth/auth/repair/complete"
        headers = {
            "Host": "idmsa.apple.com",
            "Connection": "keep-alive",
            "Content-Length": "0",
            "X-Apple-Repair-Session-Token": self.X_Apple_Session_Token_4,
            "scnt": self.scnt_2,
            "X-Apple-Widget-Key": self.serviceKey,
            "X-Apple-Frame-Id": "auth-xgo22dgf-qlc6-e2kq-uw0c-4z1vnc57",
            "sec-ch-ua": '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
            "X-Apple-I-FD-Client-Info": '{"U":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36","L":"zh-CN","Z":"GMT+08:00","V":"1.1","F":"7la44j1e3NlY5BNlY5BSmHACVZXnNA9dMGAquxTmdQxQeLaD.SAuXjodUW1BNork0ugN.xL4Fe1S9Ra6mVUe.zKp5BNlY5CGWY5BOgkLT0XxU..Bco"}',
            "X-Apple-OAuth-Redirect-URI": "https://appleid.apple.com",
            "X-Apple-OAuth-Client-Id": self.serviceKey,
            "X-Apple-OAuth-Client-Type": "firstPartyAuth",
            "X-Requested-With": "XMLHttpRequest",
            "sec-ch-ua-platform": '"Windows"',
            "X-Apple-ID-Session-Id": self.aasp,
            "X-Apple-Auth-Attributes": self.X_Apple_Auth_Attributes,
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
            "Cookie": f"dslang=CN-ZH; site=CHN; geo=CN; aasp={self.aasp};",
        }
        data = ""
        response = requests.post(
            url,
            headers=headers,
            data=data,
            proxies=self.DL,
            timeout=self.time,
        )
        self.myacinfo = response.cookies.get("myacinfo")
        logging.info(f"myacinfo----{self.myacinfo}")
        return self

    @retry(tries=20)
    def twenty_two(self):
        url = "https://appleid.apple.com/account/manage/gs/ws/token"
        headers = {
            "Host": "appleid.apple.com",
            "Connection": "keep-alive",
            "sec-ch-ua": '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
            "scnt": self.scnt_7,
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
            "Cookie": f"idclient=web; dslang=CN-ZH; site=CHN; aidsp={self.aidsp_1}; geo=CN;myacinfo={self.myacinfo}",
        }
        response = requests.get(
            url=url,
            headers=headers,
            proxies=self.DL,
            timeout=self.time,
        )
        self.X_Apple_I_Request_ID = response.headers["X-Apple-I-Request-ID"]
        self.scnt_8 = response.headers["scnt"]
        self.awat = response.cookies.get("awat")
        self.caw = response.cookies.get("caw")
        self.caw_at = response.cookies.get("caw-at")
        self.aidsp_2 = response.cookies.get("aidsp")
        logging.info(f"X_Apple_I_Request_ID----{self.X_Apple_I_Request_ID}")
        logging.info(f"scnt_8----{self.scnt_8}")
        logging.info(f"awat----{self.awat}")
        logging.info(f"caw----{self.caw}")
        logging.info(f"caw_at----{self.caw_at}")
        logging.info(f"aidsp_2----{self.aidsp_2}")
        return self

    @retry(tries=20)
    def twenty_three(self):
        url = "https://appleid.apple.com/account/manage/profile/avatar"
        headers = {
            "Host": "appleid.apple.com",
            "Connection": "keep-alive",
            "sec-ch-ua": '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
            "scnt": self.scnt_8,
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
            "Cookie": f"idclient=web; dslang=CN-ZH; site=CHN; geo=CN;myacinfo={self.myacinfo}; awat={self.awat}; caw={self.caw}; caw-at={self.caw_at}; aidsp={self.aidsp_2}",
        }
        response = requests.get(
            url=url,
            headers=headers,
            proxies=self.DL,
            timeout=self.time,
        )
        self.caw_at_2 = response.cookies.get("caw-at")
        logging.info(f"caw_at_2----{self.caw_at_2}")
        return self

    @retry(tries=20)
    def twenty_four(self):
        url = "https://appleid.apple.com/account/manage"
        headers = {
            "Host": "appleid.apple.com",
            "Connection": "keep-alive",
            "sec-ch-ua": '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
            "scnt": self.scnt_8,
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
            "Cookie": f"idclient=web; dslang=CN-ZH; site=CHN; geo=CN;myacinfo={self.myacinfo}; awat={self.awat}; caw={self.caw}; caw-at={self.caw_at}; aidsp={self.aidsp_2}",
        }
        response = requests.get(
            url=url,
            headers=headers,
            proxies=self.DL,
            timeout=self.time,
        )
        self.scnt_9 = response.headers["scnt"]
        self.awat_2 = response.cookies.get("awat")
        self.dat = response.cookies.get("dat")
        logging.info(f"scnt_9----{self.scnt_9}")
        logging.info(f"awat_2----{self.awat_2}")
        logging.info(f"dat----{self.dat}")
        return self

    @retry(tries=20)
    def twenty_five(self):
        url = "https://appleid.apple.com/account/manage/profile/avatar"
        headers = {
            "Host": "appleid.apple.com",
            "Connection": "keep-alive",
            "sec-ch-ua": '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
            "scnt": self.scnt_8,
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
            "Cookie": f"idclient=web; dslang=CN-ZH; site=CHN; geo=CN;myacinfo={self.myacinfo}; caw={self.caw}; aidsp={self.aidsp_2}; caw-at={self.caw_at}; awat={self.awat_2}; dat={self.dat}",
        }
        response = requests.get(
            url=url,
            headers=headers,
            proxies=self.DL,
            timeout=self.time,
        )
        self.scnt_10 = response.headers["scnt"]
        self.caw_at_3 = response.cookies.get("caw-at")
        self.awat_5 = response.cookies.get("awat")
        logging.info(f"scnt_10----{self.scnt_10}")
        logging.info(f"caw_at_3----{self.caw_at_3}")
        logging.info(f"awat_5----{self.awat_5}")
        return self

    @retry(tries=20)
    def twenty_six(self):
        url = "https://appleid.apple.com/account/manage/payment"
        headers = {
            "Host": "appleid.apple.com",
            "Connection": "keep-alive",
            "sec-ch-ua": '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
            "scnt": self.scnt_8,
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
            "Cookie": f"idclient=web; dslang=CN-ZH; site=CHN; geo=CN; myacinfo={self.myacinfo}; caw={self.caw}; aidsp={self.aidsp_2}; caw-at={self.caw_at}; awat={self.awat_2}; dat={self.dat}",
        }
        response = requests.get(
            url=url,
            headers=headers,
            proxies=self.DL,
            timeout=self.time,
        )
        self.awat_7 = response.cookies.get("awat")
        logging.info(f"awat_7----{self.awat_7}")
        return self

    # 设备目录
    @retry(tries=20)
    def twenty_seven(self):
        url = "https://appleid.apple.com/account/manage/security/devices"
        headers = {
            "Host": "appleid.apple.com",
            "Connection": "keep-alive",
            "sec-ch-ua": '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
            "scnt": self.scnt_8,
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
            "Cookie": f"idclient=web; dslang=CN-ZH; site=CHN; geo=CN; myacinfo={self.myacinfo}; caw={self.caw}; aidsp={self.aidsp_2}; caw-at={self.caw_at}; awat={self.awat_2}; dat={self.dat}",
        }
        response = requests.get(
            url=url,
            headers=headers,
            proxies=self.DL,
            timeout=self.time,
        )
        self.scnt_11 = response.headers["scnt"]
        self.awat_6 = response.cookies.get("awat")
        self.id_list = [device["id"] for device in response.json()["devices"]]
        logging.info(f"devices----{self.id_list}")
        logging.info(f"response----{response.json()}")
        logging.info(f"scnt_11----{self.scnt_11}")
        logging.info(f"awat_6----{self.awat_6}")
        return self

    @retry(tries=20)
    def thirty_one(self):
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
            "Cookie": f"dssid2=b99cb946-5068-4333-b0bb-11d6b876874b; dssf=1; as_sfa=Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE; pltvcid=undefined; pldfltcid=f123ec0ccd59486f8ffee8e4e2c0f00e060; dslang=CN-ZH; site=CHN; geo=CN; myacinfo={self.myacinfo}; caw={self.caw}; caw-at={self.caw_at}",
        }
        response = requests.get(
            url=url,
            headers=headers,
            proxies=self.DL,
            timeout=self.time,
        )
        # logging.info(f'scnt_11----{response.text}')
        return self

    @retry(tries=20)
    def thirty_two(self):
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
            "Cookie": f"dssid2=b99cb946-5068-4333-b0bb-11d6b876874b; dssf=1; as_sfa=Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE; pltvcid=undefined; pldfltcid=f123ec0ccd59486f8ffee8e4e2c0f00e060; dslang=CN-ZH; site=CHN; geo=CN; myacinfo={self.myacinfo}; caw={self.caw}; caw-at={self.caw_at}",
        }
        response = requests.get(
            url=url,
            headers=Header,
            proxies=self.DL,
            timeout=self.time,
        )
        logging.info(f'scnt_11----{response.text}')
        return self

    @retry(tries=20)
    def thirty_six(self):
        for device_id in self.id_list[:]:
            url = (
                f"https://appleid.apple.com/account/manage/security/devices/{device_id}"
            )
            headers = {
                "Host": "appleid.apple.com",
                "Connection": "keep-alive",
                "sec-ch-ua": '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
                "scnt": self.scnt_8,
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
                "Cookie": f"dssid2=b99cb946-5068-4333-b0bb-11d6b876874b; dssf=1; as_sfa=Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE; pltvcid=undefined; pldfltcid=f123ec0ccd59486f8ffee8e4e2c0f00e060; idclient=web; dslang=CN-ZH; site=CHN; geo=CN; myacinfo={self.myacinfo}; caw={self.caw}; aidsp={self.aidsp_2}; dat={self.dat}; itspod=16; caw-at={self.caw_at}; awat={self.awat_7};",
            }
            response = requests.get(
                url=url,
                headers=headers,
                proxies=self.DL,
                timeout=self.time,
            )
            self.caw_at_4 = response.cookies.get("caw-at")
            self.awat_8 = response.cookies.get("awat")
            self.scnt_12 = response.headers["scnt"]
            logging.info(f"caw_at_4----{self.caw_at_4}")
            logging.info(f"awat_8----{self.awat_8}")
            logging.info(f"scnt_12----{self.scnt_12}")

            url = (
                f"https://appleid.apple.com/account/manage/security/devices/{device_id}"
            )
            headers = {
                "Host": "appleid.apple.com",
                "Connection": "keep-alive",
                "sec-ch-ua": '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
                "scnt": self.scnt_8,
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
                "Cookie": f"dssid2=b99cb946-5068-4333-b0bb-11d6b876874b; dssf=1; as_sfa=Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE; pltvcid=undefined; pldfltcid=f123ec0ccd59486f8ffee8e4e2c0f00e060; idclient=web; dslang=CN-ZH; site=CHN; geo=CN; myacinfo={self.myacinfo}; caw={self.caw}; aidsp={self.aidsp_2}; dat={self.dat}; itspod=16; caw-at={self.caw_at}; awat={self.awat_8}",
            }
            response = requests.delete(
                url=url,
                headers=headers,
                proxies=self.DL,
                timeout=self.time,
            )
            logging.info(f"caw_at_4----{response.text}")
            logging.info(f"thirty_six----true")
        logging.info(f"thirty_six----true")
        return self


def main():

    apple_remove = APPLE_Remove(
        username="versity@mac.com",
        password="Aa1473691",
        Question_one="你少年时代最好的朋友叫什么名字？",
        Answer_one="py12345",
        Question_two="你的理想工作是什么？",
        Answer_two="gz12345",
        Question_three="你的父母是在哪里认识的？",
        Answer_three="fm12345",
    )

    result_one = apple_remove.one()
    result_two = apple_remove.two()
    result_three = apple_remove.three()
    result_four = apple_remove.four()
    # result_five = apple_remove.five()
    result_six = apple_remove.six()
    # result_seven = apple_remove.seven()
    result_eight = apple_remove.eight()
    result_nine = apple_remove.nine()
    result_ten = apple_remove.ten()
    result_eleven = apple_remove.eleven()
    result_twelve = apple_remove.twelve()
    # result_thirteen = apple_remove.thirteen()
    # result_fourteen = apple_remove.fourteen()
    result_fifteen = apple_remove.fifteen()
    result_sixteen = apple_remove.sixteen()
    result_seventeen = apple_remove.seventeen()
    result_eighteen = apple_remove.eighteen()
    result_nineteen = apple_remove.nineteen()
    result_twenty = apple_remove.twenty()
    result_twenty_one = apple_remove.twenty_one()
    result_twenty_two = apple_remove.twenty_two()
    result_twenty_three = apple_remove.twenty_three()
    result_twenty_four = apple_remove.twenty_four()
    result_twenty_five = apple_remove.twenty_five()
    result_twenty_six = apple_remove.twenty_six()
    result_twenty_seven = apple_remove.twenty_seven()
    # result_twenty_eight = apple_remove.twenty_eight()
    # result_twenty_nine = apple_remove.twenty_nine()
    # result_thirty = apple_remove.thirty()
    result_thirty_one = apple_remove.thirty_one()
    result_thirty_two = apple_remove.thirty_two()
    # result_thirty_three = apple_remove.thirty_three()
    # result_thirty_four = apple_remove.thirty_four()
    # result_thirty_five = apple_remove.thirty_five()
    result_thirty_six = apple_remove.thirty_six()


if __name__ == "__main__":
    main()

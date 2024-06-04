from zlib import DEF_BUF_SIZE
import requests, re

class APPLE:
    def __init__(self, **address_details) -> None:
        self.name = address_details.get("name")
        self.pwd = address_details.get("pwd")
        self.url = address_details.get("url")
        self.city = address_details.get("city")
        self.state = address_details.get("state")
        self.lastName = address_details.get("lastName")
        self.firstName = address_details.get("firstName")
        self.companyName = address_details.get("companyName")
        self.street = address_details.get("street")
        self.postalCode = address_details.get("postalCode")
        self.street2 = address_details.get("street2")

        self.session = requests.Session()


    # def dl(self):
    #     dl_url = "http://api.xiequ.cn/VAD/GetIp.aspx?act=getturn51&uid=94212&vkey=58FC7BD5FB1EBED2F07615D3C8F74D51&num=1&time=6&plat=1&re=0&type=7&so=1&group=51&ow=1&spl=1&addr=&db=1"
    #     while True:
    #         response = requests.get(dl_url)
    #         if response.status_code == 200:
    #             proxy_str = response.text.strip()
    #             ip, port = proxy_str.split(":")
    #             proxy = {"https": f"http://{ip}:{port}"}
    #             try:
    #                 test_response = requests.get(
    #                     "http://www.baidu.com", proxies=proxy
    #                 )
    #                 if test_response.status_code == 200:
    #                     print(proxy)
    #                     return proxy
    #             except Exception as e:
    #                 print(f"代理IP {proxy} 无效: {e}")
    #         else:
    #             print("获取代理IP失败，重试中...")    

    def t0(self):
        max_retries = 5
        for attempt in range(max_retries):
            try:
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
                response = self.session.get(self.url, headers=headers,allow_redirects=False,)
                CK = response.headers.get("Set-Cookie")
                dssid2_match = re.search(r"dssid2=([a-z0-9\-]+);", CK)
                as_pcts_match = re.search(r"as_pcts=([^;]+);", CK)
                self.dssid2 = dssid2_match.group(1)
                self.as_pcts_1 = as_pcts_match.group(1)
                self.ssi_1 = response.headers["Location"]
                print(self.dssid2)
                print(self.as_pcts_1)
                print(self.ssi_1)
                print(f"T0" + ("-" * 40))
                return self.t1()
            except Exception as e:
                attempt + 1
                # self.DL = self.dl()
                print(f"t0重试{e}")

    def t1(self):
        max_retries = 5
        for attempt in range(max_retries):
            try:
                cookies = {
                    'dssid2': self.dssid2,
                    'dssf': '1',
                    'as_pcts': self.as_pcts_1,
                    'as_dc': 'ucp5',
                }

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

                params = {
                    'e': 'true',
                }

                response = requests.get(
                    self.ssi_1,
                    params=params,
                    cookies=cookies,
                    headers=headers,
                    allow_redirects=False,
                )
                CK = response.headers.get("Set-Cookie")
                dssid2_match = re.search(r"dssid2=([a-z0-9\-]+);", CK)
                as_pcts_match = re.search(r"as_pcts=([^;]+);", CK)
                self.dssid2 = dssid2_match.group(1)
                self.as_pcts_2 = as_pcts_match.group(1)
                self.ssi_2 = response.headers["Location"]
                print(self.dssid2)
                print(self.as_pcts_2)
                print(self.ssi_2)
                print(f"T1" + ("-" * 40))
                return self.t2()
            except Exception as e:
                # self.DL = self.dl()
                attempt + 1
                print(f"t1重试{e}")

    def t2(self):
        max_retries = 5
        for attempt in range(max_retries):
            try:
                cookies = {
                    'dssid2': self.dssid2,
                    'dssf': '1',
                    'as_dc': 'ucp5',
                    'as_pcts': self.as_pcts_2,
                }
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
                params = {
                    'e': 'true',
                }
                response = requests.get(
                    self.ssi_2,
                    params=params,
                    cookies=cookies,
                    headers=headers,
                )
                CK = response.headers.get("Set-Cookie")
                dssid2_match = re.search(r"dssid2=([a-z0-9\-]+);", CK)
                self.x_aos_stk_value = re.search(r'"x-aos-stk":"(.*?)"', response.text)
                self.signInURL = re.search(r'"signInURL":"(.*?)"', response.text)
                self.dssid2 = dssid2_match.group(1)
                self.x_aos_stk = self.x_aos_stk_value.group(1)
                self.signInURL = self.signInURL.group(1)
                print(self.dssid2)
                print(self.x_aos_stk)
                print(self.signInURL)
                print(f"T2" + ("-" * 40))
                return self.t3()
            except Exception as e:
                # self.DL = self.dl()
                attempt + 1
                print(f"t2重试{e}")

    def t3(self):
        max_retries = 5
        for attempt in range(max_retries):
            try:
                cookies = {
                    'dssid2': self.dssid2,
                    'dssf': '1',
                    'as_dc': 'ucp5',
                    'as_pcts': self.as_pcts_2,
                    'as_sfa': 'Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE',
                    'geo': 'CN',
                    's_fid': '42DD2FE6E019F0D0-209EE11E4E36852E',
                    's_cc': 'true',
                    's_vi': '[CS]v1|332F8FDED451B392-40000A3A249583CE[CE]',
                    'as_rumid': 'dc01d724-6a1b-4229-8fc1-54664808d346',
                    's_sq': '%5B%5BB%5D%5D',
                    'pxro': '1',
                }
                headers = {
                    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                    'Accept-Language': 'zh-CN,zh;q=0.9',
                    'Cache-Control': 'no-cache',
                    'Connection': 'keep-alive',
                    'DNT': '1',
                    'Pragma': 'no-cache',
                    'Referer': 'https://secure8.store.apple.com/',
                    'Sec-Fetch-Dest': 'iframe',
                    'Sec-Fetch-Mode': 'navigate',
                    'Sec-Fetch-Site': 'same-site',
                    'Upgrade-Insecure-Requests': '1',
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0',
                    'sec-ch-ua': '"Microsoft Edge";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
                    'sec-ch-ua-mobile': '?0',
                    'sec-ch-ua-platform': '"Windows"',
                }
                response = requests.get(
                    'https://idmsa.apple.com/appleauth/auth/authorize/signin?frame_id=auth-08rphyzr-8q7y-c93f-2f4k-xdoua0mf&language=en_US&skVersion=7&iframeId=auth-08rphyzr-8q7y-c93f-2f4k-xdoua0mf&client_id=a797929d224abb1cc663bb187bbcd02f7172ca3a84df470380522a7c6092118b&redirect_uri=https://secure8.store.apple.com&response_type=code&response_mode=web_message&state=auth-08rphyzr-8q7y-c93f-2f4k-xdoua0mf&authVersion=latest',
                    cookies=cookies,
                    headers=headers,
                )
                CK = response.headers.get("Set-Cookie")
                self.aasp = re.search(r"aasp=([a-zA-Z0-9\-]+);", CK)
                self.aasp = self.aasp.group(1)
                self.X_Apple_Auth_Attributes = response.headers.get("X-Apple-Auth-Attributes")
                self.scnt = response.headers["scnt"]
                print(self.aasp)
                print(self.X_Apple_Auth_Attributes)
                print(self.scnt)
                print(f"T3" + ("-" * 40))
                return self.t4_1()
            except Exception as e:
                # self.DL = self.dl()
                attempt + 1
                print(f"T3{e}")

    def t4_1(self):
        max_retries = 5
        for attempt in range(max_retries):
            try:
                # -------------------------------------------------------
                url = "https://env-00jxgsqva6td.dev-hz.cloudbasefunction.cn/A1?type=1"
                payload = {f"email": {self.name}}
                self.Key = self.session.request(
                    method="post", url=url, data=payload
                ).json()
                print(self.Key)
                print("加密_1" + ("-" * 40))
                return self.t4_2()
            except Exception as e:
                # self.DL = self.dl()
                attempt + 1
                print(f"t4_1 ，错误：{e}")

    def t4_2(self):
        max_retries = 5
        for attempt in range(max_retries):
            try:
                combined_headers_and_cookies = {
                    "Accept": "application/json, text/javascript, */*; q=0.01",
                    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0',
                    "X-Apple-Auth-Attributes": self.X_Apple_Auth_Attributes,
                    "scnt": self.scnt,
                }
                json_data = {
                    "a": self.Key["r"],
                    "accountName": self.name,
                    "protocols": [
                        "s2k",
                        "s2k_fo",
                    ],
                }
                self.response_2 = self.session.request(
                    method="post",
                    url="https://idmsa.apple.com/appleauth/auth/signin/init",
                    headers=combined_headers_and_cookies,
                    json=json_data,
                    # proxies=self.DL,
                    # timeout=self.times,
                ).json()
                print(self.Key)
                print(f"加密_2" + ("-" * 40))
                return self.t4_3()
            except Exception as e:
                # self.DL = self.dl()
                attempt + 1
                print(f"t4_2 ，错误：{e}")

    def t4_3(self):
        max_retries = 5
        for attempt in range(max_retries):
            try:
                url = "https://env-00jxgsqva6td.dev-hz.cloudbasefunction.cn/A1?type=2"
                payload = {
                    "email": self.name,
                    "iterations": self.response_2["iteration"],
                    "Value": self.response_2["b"],
                    "salt": self.response_2["salt"],
                    "password": self.pwd,
                    "protocol": self.response_2["protocol"],
                    "privateHexValue": self.Key["privateHexValue"],
                    "publicHexValue": self.Key["publicHexValue"],
                }
                self.response_3 = self.session.request(
                    method="post", url=url, json=payload
                ).json()
                print(self.response_3)
                print(f"加密_3" + ("-" * 40))
                return self.t4_4()
            except Exception as e:
                # self.DL = self.dl()
                attempt + 1
                print(f"t4_3 ，错误：{e}")

    def t4_4(self):
        max_retries = 5
        for attempt in range(max_retries):
            try:
                cookies = {
                    "as_rumid": "9f9a7e8708ebbde2daf02b478473eccd",
                    "dssid2": self.dssid2,
                    "dssf": "1",
                    "as_pcts": self.as_pcts_2,
                    "as_dc": "ucp3",
                    "as_sfa": "Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE",
                    "geo": "CN",
                    "pxro": "1",
                    "s_fid": "6323376718433557-371662D1A66E1B14",
                    "s_cc": "true",
                    "s_vi": "[CS]v1|332AA8C7A36C871F-40000E40A15E97D6[CE]",
                    "dslang": "US-EN",
                    "site": "USA",
                    "aasp": self.aasp,
                    "aa": "1B99A552487EA314F1CE4E8E4291BC46",
                }

                headers = {
                    "Accept": "application/json, text/javascript, */*; q=0.01",
                    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0',
                    "X-Apple-Auth-Attributes": self.X_Apple_Auth_Attributes,
                    "X-Apple-Widget-Key": "a797929d224abb1cc663bb187bbcd02f7172ca3a84df470380522a7c6092118b",
                    "scnt": self.scnt,
                }
                json_data = {
                    "accountName": self.name,
                    "rememberMe": False,
                    "m1": self.response_3["M1"],
                    "c": self.response_2["c"],
                    "m2": self.response_3["M2"],
                }
                response_4 = self.session.request(
                    method="post",
                    url="https://idmsa.apple.com/appleauth/auth/signin/complete",
                    headers=headers,
                    json=json_data,
                    cookies=cookies,
                    # proxies=self.DL,
                    # timeout=self.times,
                )
                CK = response_4.headers.get("Set-Cookie")
                myacinfo_pattern = re.compile(r"myacinfo=([^;]+)")
                myacinfo_match = myacinfo_pattern.search(CK)
                self.myacinfo = myacinfo_match.group(1)
                print(self.myacinfo)
                print(f"T4_" + ("-" * 40))
                return self.t5()
            except Exception as e:
                # self.DL = self.dl()
                print(f"t4_4 重试 {attempt + 1} 次，错误：{e}")
                if attempt + 1 == max_retries:
                    print(f"账号异常，无法获取必要的信息")
                    self.stast = "账号异常，无法获取必要的信息。"
                    return self.stast

    def t5(self):
            max_retries = 5
            for attempt in range(max_retries):
                try:
                    cookies = {
                        'dssid2': self.dssid2,
                        'dssf': '1',
                        'as_dc': 'ucp5',
                        'as_pcts': self.as_pcts_2,
                        'as_sfa': 'Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE',
                        'geo': 'CN',
                        's_fid': '42DD2FE6E019F0D0-209EE11E4E36852E',
                        's_cc': 'true',
                        's_vi': '[CS]v1|332F8FDED451B392-40000A3A249583CE[CE]',
                        'as_rumid': 'dc01d724-6a1b-4229-8fc1-54664808d346',
                        's_sq': '%5B%5BB%5D%5D',
                        'pt-dm': 'v1~x~5cp7ld1o~m~3~n~AOS%3A%20orders%2Fguestorder_detail~r~aos%3Aaccount',
                    }

                    headers = {
                        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                        'Accept-Language': 'zh-CN,zh;q=0.9',
                        'Cache-Control': 'no-cache',
                        'Connection': 'keep-alive',
                        'DNT': '1',
                        'Pragma': 'no-cache',
                        'Referer': self.ssi_1,
                        'Sec-Fetch-Dest': 'document',
                        'Sec-Fetch-Mode': 'navigate',
                        'Sec-Fetch-Site': 'same-origin',
                        'Sec-Fetch-User': '?1',
                        'Upgrade-Insecure-Requests': '1',
                        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0',
                        'sec-ch-ua': '"Microsoft Edge";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
                        'sec-ch-ua-mobile': '?0',
                        'sec-ch-ua-platform': '"Windows"',
                    }

                    response = requests.get(self.signInURL, cookies=cookies, headers=headers,allow_redirects=False,)
                    self.ssi_3 = response.headers["Location"]
                    print(self.ssi_3)
                    print(f"T5" + ("-" * 40))
                    return self.t6()
                except Exception as e:
                    # self.DL = self.dl()
                    attempt + 1
                    print(f"t5重试 ，错误：{e}")

    def t6(self):
        max_retries = 5
        for attempt in range(max_retries):
            try:
                extracted_part = self.ssi_3.split("/shop/signIn/orders?hgl=t&ssi=")[1]
                cookies = {
                    'dssid2': self.dssid2,
                    'dssf': '1',
                    'as_dc': 'ucp5',
                    'as_pcts': self.as_pcts_2,
                    'as_sfa': 'Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE',
                    'geo': 'CN',
                    's_fid': '42DD2FE6E019F0D0-209EE11E4E36852E',
                    's_cc': 'true',
                    's_vi': '[CS]v1|332F8FDED451B392-40000A3A249583CE[CE]',
                    'as_rumid': 'dc01d724-6a1b-4229-8fc1-54664808d346',
                    's_sq': '%5B%5BB%5D%5D',
                    'pxro': '1',
                    'dslang': 'US-EN',
                    'site': 'USA',
                    'myacinfo': self.myacinfo,
                }

                headers = {
                    'Accept': '*/*',
                    'Accept-Language': 'zh-CN,zh;q=0.9',
                    'Cache-Control': 'no-cache',
                    'Connection': 'keep-alive',
                    'Content-Type': 'application/x-www-form-urlencoded',
                    'DNT': '1',
                    'Origin': 'https://secure8.store.apple.com',
                    'Pragma': 'no-cache',
                    'Referer': 'https://secure8.store.apple.com/shop/signIn/orders?hgl=t&ssi=1AAABj-OUB2sgHbHFGVHyx_7vyUFLOaJm1QEopi5HAsg6bOBtrRzpCoYAAABFaHR0cHM6Ly9zZWN1cmU4LnN0b3JlLmFwcGxlLmNvbS9zaG9wL29yZGVyL2RldGFpbC8xMDA3OC9XMTU4NTUxNjEzM3x8AAIBZmt4-acgOJ-gFKor-iW1wydzLUGapJznHWgfXTorxEQ',
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
                    'x-aos-model-page': 'olssSignInPage',
                    'x-aos-stk': self.x_aos_stk,
                }
                params = {
                    'ssi': extracted_part,
                }

                data = {
                    'deviceID': 'TF1;015;;;;;;;;;;;;;;;;;;;;;;Mozilla;Netscape;5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit/537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome/125.0.0.0%20Safari/537.36%20Edg/125.0.0.0;20030107;undefined;true;;true;Win32;undefined;Mozilla/5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit/537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome/125.0.0.0%20Safari/537.36%20Edg/125.0.0.0;zh-CN;undefined;secure8.store.apple.com;undefined;undefined;undefined;undefined;false;false;1717510093084;8;2005/6/7%2021%3A33%3A44;1920;1080;;;;;;;;-480;-480;2024/6/4%2022%3A08%3A13;24;1920;1032;0;0;;;;;;;;;;;;;;;;;;;25;',
                    'grantCode': '',
                }

                response = requests.post(
                    'https://secure8.store.apple.com/shop/signIn/idms/authx',
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

                self.dssid2 = dssid2_match.group(1) if dssid2_match else None
                self.as_cn = as_cn_match.group(1) if as_cn_match else None
                self.as_disa = as_disa_match.group(1) if as_disa_match else None
                self.as_ltn_us_1 = as_ltn_us_match.group(1) if as_ltn_us_match else None
                self.as_rec = as_rec_match.group(1) if as_rec_match else None

                print(f"dssid2_2: {self.dssid2}")
                print(f"as_cn: {self.as_cn}")
                print(f"as_disa: {self.as_disa}")
                print(f"as_ltn_us: {self.as_ltn_us_1}")
                print(f"as_rec: {self.as_rec}")
                print(f"t6" + ("-" * 40))
                return self.t7()
            except Exception as e:
                # self.DL = self.dl()
                attempt + 1
                print(f"t6重试 ，错误：{e}")

    def t7(self):
        max_retries = 5
        for attempt in range(max_retries):
            try:
                cookies = {
                    'dssid2': self.dssid2,
                    'dssf': '1',
                    'as_dc': 'ucp5',
                    'as_pcts': self.as_pcts_2,
                    'as_sfa': 'Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE',
                    'geo': 'CN',
                    's_fid': '42DD2FE6E019F0D0-209EE11E4E36852E',
                    's_cc': 'true',
                    's_vi': '[CS]v1|332F8FDED451B392-40000A3A249583CE[CE]',
                    'as_rumid': 'dc01d724-6a1b-4229-8fc1-54664808d346',
                    's_sq': '%5B%5BB%5D%5D',
                    'pxro': '1',
                    'dslang': 'US-EN',
                    'site': 'USA',
                    'as_cn': self.as_cn,
                    'as_disa': self.as_disa,
                    'as_ltn_us': self.as_ltn_us_1,
                    'as_rec': self.as_rec,
                    'pt-dm': 'v1~x~5cp7ld1o~m~3~n~AOS%3A%20orders%2Forder_signin~r~aos%3Aaccount',
                }

                headers = {
                    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                    'Accept-Language': 'zh-CN,zh;q=0.9',
                    'Cache-Control': 'no-cache',
                    'Connection': 'keep-alive',
                    # 'Cookie': 'dssid2=61f3a482-21df-4418-9af8-004f79caadd3; dssf=1; as_dc=ucp5; as_pcts=fzmVOfglsphwVbt_Sv6FmRvPuTuBizGosTH50LeIR2SssfBpwkSBm:tJUmCY_AGjRmw1fZ2vxzDhEKu+vUFS1ZEmQBXQFWDR3R4LBNr3u3Mt-1ytD4-wUtJ50dde:0MbcN-y2UC-QnN5RH:QEedMuRIuTxpprW_d_NjRivfSELe0wdbaHDsQRJ:O; as_sfa=Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE; geo=CN; s_fid=42DD2FE6E019F0D0-209EE11E4E36852E; s_cc=true; s_vi=[CS]v1|332F8FDED451B392-40000A3A249583CE[CE]; as_rumid=dc01d724-6a1b-4229-8fc1-54664808d346; s_sq=%5B%5BB%5D%5D; pxro=1; dslang=US-EN; site=USA; as_cn=~jQNGWbnm-dPkCjaL1ae1Xbqa5SJQlMoj8atqTfkMxzQ=; as_disa=AAAjAAAB7s2ywC2QmFv1_KF0pCb5vbwY_BN8O8iSBpMrpmkFbUUAAgH2fRlptI1C75te4WYxJ8FRwi-UjdWPX7E298wo0LUYKg==; as_ltn_us=AAQEAMGFuyHMZQL2BhLXBNZq3hoYdFVZ1oF7t9kxGmOfXtrQWUe4c26VeuELC7Pkmeiq31BRh_Ju5eMo1dO4AJiAwaTjNORXFoA; as_rec=bd2810ed7b96c5be83baef72537100ffed1f26e1c4fc669a7cee8b52f845f7b49b5c160f62883502cea3070bf3cbb025461ffd3fe34bb4ed01f41b2aeedbba491e2b3ce1f495e5840c77d003d7e23bc6; pt-dm=v1~x~5cp7ld1o~m~3~n~AOS%3A%20orders%2Forder_signin~r~aos%3Aaccount',
                    'DNT': '1',
                    'Pragma': 'no-cache',
                    'Referer': self.ssi_3,
                    'Sec-Fetch-Dest': 'document',
                    'Sec-Fetch-Mode': 'navigate',
                    'Sec-Fetch-Site': 'same-origin',
                    'Sec-Fetch-User': '?1',
                    'Upgrade-Insecure-Requests': '1',
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0',
                    'sec-ch-ua': '"Microsoft Edge";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
                    'sec-ch-ua-mobile': '?0',
                    'sec-ch-ua-platform': '"Windows"',
                }

                response = requests.get(self.signInURL, cookies=cookies, headers=headers)
                self.x_aos_stk_value_2 = re.search(r'"x-aos-stk":"([^"]+)"', response.text)
                self.url_x = re.search(r'"editBillingContact":{"url":"([^"]+)?', response.text)
                url_x = self.url_x.group(1)
                self.url_x = url_x.split('?')[0]
                set_cookie_header = response.headers.get("Set-Cookie", "")
                as_ltn_us_match = re.search(r"as_ltn_us=(.+?);", set_cookie_header)
                self.as_ltn_us_2 = as_ltn_us_match.group(1) if as_ltn_us_match else None
                self.x_aos_stk_value_2 = self.x_aos_stk_value_2.group(1)
                print(self.url_x)
                print(self.as_ltn_us_2)
                print(self.x_aos_stk_value_2)
                print(f"T7" + ("-" * 40))
                return self.t8()
            except Exception as e:
                # self.DL = self.dl()
                attempt + 1
                print(f"t7重试 ，错误：{e}")

    def t8(self):
        max_retries = 5
        for attempt in range(max_retries):
            try:
                cookies = {
                        'dssid2': self.dssid2,
                        'dssf': '1',
                        'as_sfa': 'Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE',
                        'pxro': '1',
                        'as_dc': 'ucp5',
                        's_fid': '05BD90C97D09DACB-0E981AE8E5C89EE3',
                        's_vi': '[CS]v1|332FB030F1DF1F6E-40001050081DBF4C[CE]',
                        'as_pcts': self.as_pcts_2,
                        's_cc': 'true',
                        'as_rumid': 'c643af2b-2aef-467f-b089-295dd3aa3fbc',
                        'dslang': 'US-EN',
                        'site': 'USA',
                        'geo': 'CN',
                        'as_cn': self.as_cn,
                        'as_disa': self.as_disa,
                        'as_rec': self.as_rec,
                        'as_ltn_us': self.as_ltn_us_2,
                        's_sq': 'applestoreww%3D%2526c.%2526a.%2526activitymap.%2526page%253DAOS%25253A%252520orders%25252Forder_detail%2526link%253Dedit%252520%252528inner%252520text%252529%252520%25257C%252520no%252520href%252520%25257C%252520body%2526region%253Dbody%2526pageIDType%253D1%2526.activitymap%2526.a%2526.c%2526pid%253DAOS%25253A%252520orders%25252Forder_detail%2526pidt%253D1%2526oid%253Dfunctionkd%252528%252529%25257B%25257D%2526oidt%253D2%2526ot%253DBUTTON',
                    }

                headers = {
                    'accept': '*/*',
                    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
                    'cache-control': 'no-cache',
                    # 'content-length': '0',
                    'content-type': 'application/x-www-form-urlencoded',
                    # 'cookie': 'dssid2=2831cb99-bac8-4f9a-847a-1d01848126e5; dssf=1; as_sfa=Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE; pxro=1; as_dc=ucp5; s_fid=05BD90C97D09DACB-0E981AE8E5C89EE3; s_vi=[CS]v1|332FB030F1DF1F6E-40001050081DBF4C[CE]; as_pcts=R:8tGpf187I:o9KOkfnutY169q9Y7bLD7cV0v6ZRYCRXfAK-mzTp_89QdYyzzgrFNdY-QKXnc8x55MW5EqB+3_PBjhf8H2BeNp2xgLRV0LKD+alrGcK-5HWvglITbj14EwK0sZNVFB3lUZhnVdN9:ec6asJSA2+MVQFofjtf4uCrkUHYN4U38UNk; s_cc=true; as_rumid=c643af2b-2aef-467f-b089-295dd3aa3fbc; dslang=US-EN; site=USA; geo=CN; as_cn=~ABE5M1_eyIVWy5JqKVhJ-FJstBKzA_lw8iPk8JQHGxI=; as_disa=AAAjAAABtQk42s9PFb7aNkkPk54TvT2ktvX3XjwxveqJVIgUlxUAAgFDUMXqOfgzJl4mR1saALED4p36U_I_kuHKBBsAbEus7A==; as_rec=b80c98cde40c9d152ad6ed42b06fe34f0e75de19bebecd3d42d640f1661e61224377592a20ebeec6926e7c6ed0be3c0dea5f0e533a45ab9d66874469e076dd096afd384b6b7e8380466627e58e5ce92c; as_ltn_us=AAQEAMHd19vvg4jZFr57qCXF7A19IJ1I_dXGEF12EvUxBEDCMUe4c26VeuELC7Pkmeiq31BSzo_pO5c00mlgkwaepXgqKBbe71A; s_sq=applestoreww%3D%2526c.%2526a.%2526activitymap.%2526page%253DAOS%25253A%252520orders%25252Forder_detail%2526link%253Dedit%252520%252528inner%252520text%252529%252520%25257C%252520no%252520href%252520%25257C%252520body%2526region%253Dbody%2526pageIDType%253D1%2526.activitymap%2526.a%2526.c%2526pid%253DAOS%25253A%252520orders%25252Forder_detail%2526pidt%253D1%2526oid%253Dfunctionkd%252528%252529%25257B%25257D%2526oidt%253D2%2526ot%253DBUTTON',
                    'dnt': '1',
                    'modelversion': 'v2',
                    'origin': 'https://secure8.store.apple.com',
                    'pragma': 'no-cache',
                    'priority': 'u=1, i',
                    'referer': self.signInURL,
                    'sec-ch-ua': '"Microsoft Edge";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
                    'sec-ch-ua-mobile': '?0',
                    'sec-ch-ua-platform': '"Windows"',
                    'sec-fetch-dest': 'empty',
                    'sec-fetch-mode': 'cors',
                    'sec-fetch-site': 'same-origin',
                    'syntax': 'graviton',
                    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0',
                    'x-aos-model-page': 'OrderStatusDetail',
                    'x-aos-stk': self.x_aos_stk_value_2,
                    'x-requested-with': 'Fetch',
                }

                params = {
                    '_a': 'editShippingAddress',
                    '_m': 'orderDetail.orderItems.orderItem-0000101.shippingInfo',
                }

                response = requests.post(
                    self.url_x,
                    params=params,
                    cookies=cookies,
                    headers=headers,
                )
                set_cookie_header = response.headers.get("Set-Cookie", "")
                as_ltn_us_match_3 = re.search(r"as_ltn_us=(.+?);", set_cookie_header)
                self.as_ltn_us_3 = as_ltn_us_match_3.group(1) if as_ltn_us_match_3 else None
                print(self.as_ltn_us_3)
                print(f"T8" + ("-" * 40))
                return self.t9()
            except Exception as e:
                # self.DL = self.dl()
                attempt + 1
                print(f"t8重试 ，错误：{e}")

    def t9(self):
        max_retries = 5
        for attempt in range(max_retries):
            try:
                cookies = {
                    'dssid2': self.dssid2,
                    'dssf': '1',
                    'as_pcts': self.as_pcts_2,
                    'as_sfa': 'Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE',
                    'geo': 'CN',
                    's_cc': 'true',
                    'as_rumid': 'dc01d724-6a1b-4229-8fc1-54664808d346',
                    'pxro': '1',
                    'dslang': 'US-EN',
                    'site': 'USA',
                    'as_cn': self.as_cn,
                    'as_dc': 'ucp5',
                    's_fid': '1054915DD179A501-0C6D86AF11C440EA',
                    's_vi': '[CS]v1|332FAADE520D0ADC-60000E69A7E27B0D[CE]',
                    'as_disa': self.as_disa,
                    'as_rec': self.as_rec,
                    'as_ltn_us': self.as_ltn_us_3,
                    's_sq': '%5B%5BB%5D%5D',
                }

                headers = {
                    'accept': '*/*',
                    'accept-language': 'zh-CN,zh;q=0.9',
                    'cache-control': 'no-cache',
                    'content-type': 'application/x-www-form-urlencoded',
                    # 'cookie': 'dssid2=61f3a482-21df-4418-9af8-004f79caadd3; dssf=1; as_pcts=fzmVOfglsphwVbt_Sv6FmRvPuTuBizGosTH50LeIR2SssfBpwkSBm:tJUmCY_AGjRmw1fZ2vxzDhEKu+vUFS1ZEmQBXQFWDR3R4LBNr3u3Mt-1ytD4-wUtJ50dde:0MbcN-y2UC-QnN5RH:QEedMuRIuTxpprW_d_NjRivfSELe0wdbaHDsQRJ:O; as_sfa=Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE; geo=CN; s_cc=true; as_rumid=dc01d724-6a1b-4229-8fc1-54664808d346; pxro=1; dslang=US-EN; site=USA; as_cn=~jQNGWbnm-dPkCjaL1ae1Xbqa5SJQlMoj8atqTfkMxzQ=; as_dc=ucp5; s_fid=1054915DD179A501-0C6D86AF11C440EA; s_vi=[CS]v1|332FAADE520D0ADC-60000E69A7E27B0D[CE]; as_disa=AAAjAAABIKoQVhJ9bGn-AA6PbrTVQG889xdbU-7rPQOL6YdLLvkAAgH8AeNqZp0HcL3WpCMlej8o-xpcg7lhkGCeIt49ChgMkg==; as_rec=d81a0719914b15eba1d9bf5a6e285669a5e78ade18fbbf5e7f2df8ba2b16ffedfc7d147212cd5eeac6609290dc95357b340964d02addf1c8c0b300895b7058eab9237dc704dfbc30667a9c9f9b24990f; as_ltn_us=AAQEAMMqgZSEr5d9q7bk3JNtntMNfwPEfnVGtYFk6SemUjkImUe4c26VeuELC7Pkmeiq31BQ9AeDBswJ_ySDet8F9dKuJEVq3qw; s_sq=%5B%5BB%5D%5D',
                    'dnt': '1',
                    'modelversion': 'v2',
                    'origin': 'https://secure8.store.apple.com',
                    'pragma': 'no-cache',
                    'priority': 'u=1, i',
                    'referer': self.signInURL,
                    'sec-ch-ua': '"Microsoft Edge";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
                    'sec-ch-ua-mobile': '?0',
                    'sec-ch-ua-platform': '"Windows"',
                    'sec-fetch-dest': 'empty',
                    'sec-fetch-mode': 'cors',
                    'sec-fetch-site': 'same-origin',
                    'syntax': 'graviton',
                    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0',
                    'x-aos-model-page': 'OrderStatusDetail',
                    'x-aos-stk': self.x_aos_stk_value_2,
                    'x-requested-with': 'Fetch',
                }

                params = {
                    '_a': 'address-submit',
                    '_m': 'orderDetail.orderItems.orderItem-0000101.shippingInfo.editShippingInfo',
                }

                data = {
                    'orderDetail.orderItems.orderItem-0000101.shippingInfo.editShippingInfo.edit-shipping-address.city': 'AUSTIN',
                    'orderDetail.orderItems.orderItem-0000101.shippingInfo.editShippingInfo.edit-shipping-address.state': 'TX',
                    'orderDetail.orderItems.orderItem-0000101.shippingInfo.editShippingInfo.edit-shipping-address.lastName': 'TAYLOR',
                    'orderDetail.orderItems.orderItem-0000101.shippingInfo.editShippingInfo.edit-shipping-address.firstName': 'MILES',
                    'orderDetail.orderItems.orderItem-0000101.shippingInfo.editShippingInfo.edit-shipping-address.companyName': '',
                    'orderDetail.orderItems.orderItem-0000101.shippingInfo.editShippingInfo.edit-shipping-address.street': '3144  Gladwell Street',
                    'orderDetail.orderItems.orderItem-0000101.shippingInfo.editShippingInfo.edit-shipping-address.postalCode': '78727',
                    'orderDetail.orderItems.orderItem-0000101.shippingInfo.editShippingInfo.edit-shipping-address.street2': '',
                }

                response = requests.post(
                    self.url_x,
                    params=params,
                    cookies=cookies,
                    headers=headers,
                    data=data,
                )
                set_cookie_header = response.headers.get("Set-Cookie", "")
                as_ltn_us_match_4 = re.search(r"as_ltn_us=(.+?);", set_cookie_header)
                self.as_ltn_us_4 = as_ltn_us_match_4.group(1) if as_ltn_us_match_4 else None
                print(self.as_ltn_us_4)
                print(f"T9" + ("-" * 40))
                return self.t10()
            except Exception as e:
                # self.DL = self.dl()
                attempt + 1
                print(f"t9重试 ，错误：{e}")

    def t10(self):
        max_retries = 5
        for attempt in range(max_retries):
            try:
                cookies = {
                    'dssid2': self.dssid2,
                    'dssf': '1',
                    'as_sfa': 'Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE',
                    'pxro': '1',
                    'as_dc': 'ucp5',
                    's_fid': '05BD90C97D09DACB-0E981AE8E5C89EE3',
                    's_vi': '[CS]v1|332FB030F1DF1F6E-40001050081DBF4C[CE]',
                    'as_pcts': self.as_pcts_2,
                    's_cc': 'true',
                    'as_rumid': 'c643af2b-2aef-467f-b089-295dd3aa3fbc',
                    'dslang': 'US-EN',
                    'site': 'USA',
                    'geo': 'CN',
                    'as_cn': self.as_cn,
                    'as_disa': self.as_disa,
                    'as_rec': self.as_rec,
                    'as_ltn_us': self.as_ltn_us_3,
                    's_sq': 'applestoreww%3D%2526c.%2526a.%2526activitymap.%2526page%253DAOS%25253A%252520orders%25252Forder_detail%2526link%253Duse%252520this%252520address%252520%252528inner%252520text%252529%252520%25257C%252520no%252520href%252520%25257C%252520body%2526region%253Dbody%2526pageIDType%253D1%2526.activitymap%2526.a%2526.c%2526pid%253DAOS%25253A%252520orders%25252Forder_detail%2526pidt%253D1%2526oid%253Dfunctionkd%252528%252529%25257B%25257D%2526oidt%253D2%2526ot%253DSUBMIT',
                }

                headers = {
                    'accept': '*/*',
                    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
                    'cache-control': 'no-cache',
                    'content-type': 'application/x-www-form-urlencoded',
                    # 'cookie': 'dssid2=2831cb99-bac8-4f9a-847a-1d01848126e5; dssf=1; as_sfa=Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE; pxro=1; as_dc=ucp5; s_fid=05BD90C97D09DACB-0E981AE8E5C89EE3; s_vi=[CS]v1|332FB030F1DF1F6E-40001050081DBF4C[CE]; as_pcts=R:8tGpf187I:o9KOkfnutY169q9Y7bLD7cV0v6ZRYCRXfAK-mzTp_89QdYyzzgrFNdY-QKXnc8x55MW5EqB+3_PBjhf8H2BeNp2xgLRV0LKD+alrGcK-5HWvglITbj14EwK0sZNVFB3lUZhnVdN9:ec6asJSA2+MVQFofjtf4uCrkUHYN4U38UNk; s_cc=true; as_rumid=c643af2b-2aef-467f-b089-295dd3aa3fbc; dslang=US-EN; site=USA; geo=CN; as_cn=~ABE5M1_eyIVWy5JqKVhJ-FJstBKzA_lw8iPk8JQHGxI=; as_disa=AAAjAAABtQk42s9PFb7aNkkPk54TvT2ktvX3XjwxveqJVIgUlxUAAgFDUMXqOfgzJl4mR1saALED4p36U_I_kuHKBBsAbEus7A==; as_rec=b80c98cde40c9d152ad6ed42b06fe34f0e75de19bebecd3d42d640f1661e61224377592a20ebeec6926e7c6ed0be3c0dea5f0e533a45ab9d66874469e076dd096afd384b6b7e8380466627e58e5ce92c; as_ltn_us=AAQEAMHd19vvg4jZFr57qCXF7A19bLbW4Rqvnhya0f9TfcUj1Ue4c26VeuELC7Pkmeiq31BT8YBtuAkeA2dZugtEaDfOBj8DrOw; s_sq=applestoreww%3D%2526c.%2526a.%2526activitymap.%2526page%253DAOS%25253A%252520orders%25252Forder_detail%2526link%253Duse%252520this%252520address%252520%252528inner%252520text%252529%252520%25257C%252520no%252520href%252520%25257C%252520body%2526region%253Dbody%2526pageIDType%253D1%2526.activitymap%2526.a%2526.c%2526pid%253DAOS%25253A%252520orders%25252Forder_detail%2526pidt%253D1%2526oid%253Dfunctionkd%252528%252529%25257B%25257D%2526oidt%253D2%2526ot%253DSUBMIT',
                    'dnt': '1',
                    'modelversion': 'v2',
                    'origin': 'https://secure8.store.apple.com',
                    'pragma': 'no-cache',
                    'priority': 'u=1, i',
                    'referer': self.signInURL,
                    'sec-ch-ua': '"Microsoft Edge";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
                    'sec-ch-ua-mobile': '?0',
                    'sec-ch-ua-platform': '"Windows"',
                    'sec-fetch-dest': 'empty',
                    'sec-fetch-mode': 'cors',
                    'sec-fetch-site': 'same-origin',
                    'syntax': 'graviton',
                    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0',
                    'x-aos-model-page': 'OrderStatusDetail',
                    'x-aos-stk': self.x_aos_stk_value_2,
                    'x-requested-with': 'Fetch',
                }

                params = {
                    '_a': 'selected-address-submit',
                    '_m': 'orderDetail.orderItems.orderItem-0000101.shippingInfo.editShippingInfo.suggested-shipping-addresses',
                }

                data = {
                    'orderDetail.orderItems.orderItem-0000101.shippingInfo.editShippingInfo.suggested-shipping-addresses.selected': 'formatted-original-address',
                }

                response = requests.post(
                    self.url_x,
                    params=params,
                    cookies=cookies,
                    headers=headers,
                    data=data,
                )
                print(response.headers)
                print(f"T10" + ("-" * 40))
                return response.headers
            except Exception as e:
                # self.DL = self.dl()
                attempt + 1
                print(f"t10重试 ，错误：{e}")


def main(**kwargs):
    apple_instance = APPLE(**kwargs).t0()
    return apple_instance


if __name__ == "__main__":
    params = {
        "name": "elijahv2msi@outlook.com",
        "pwd": "iuSa15*18",
        "url":"https://www.apple.com/xc/us/vieworder/W1047001362/elijahv2msi@outlook.com",
        "city": "Albany",#1
        "state": "CH",#2
        "lastName": "lllll3333",#3
        "firstName": "hhhjjj11166666",#4
        "companyName": "122332",#5
        "street": "777776667777",#6
        "postalCode": "11111-1111",#7
        "street2": "212231312",#8
    }
    main_instance = main(**params)
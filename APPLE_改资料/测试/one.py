import requests,re,logging
logging.basicConfig(level=logging.INFO)

class APPLE:
    def __init__(self) -> None:
        self.requests_ = requests.session()
        self.name = "my_hero.hero@softbank.ne.jp"
        self.pwd = "Aa147369"

    def t0(self):
        headers = {
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "accept-language": "zh-CN,zh;q=0.9",
            "cache-control": "no-cache",
            "cookie": "as_rumid=d5de47da-70ec-481f-816b-db71ee321a80; pt-dm=v1~x~tgu4kwv1~m~3",
            "pragma": "no-cache",
            "priority": "u=0, i",
            "sec-ch-ua": '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": '"Windows"',
            "sec-fetch-dest": "document",
            "sec-fetch-mode": "navigate",
            "sec-fetch-site": "none",
            "sec-fetch-user": "?1",
            "upgrade-insecure-requestsuests": "1",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
        }
        response = self.requests_.get("https://secure.store.apple.com/shop/account/home",headers=headers,allow_redirects=False)
        CK = response.headers.get("Set-Cookie")
        dssid2_match = re.search(r"dssid2=([a-z0-9\-]+);", CK)
        as_pcts_match = re.search(r"as_pcts=([^;]+);", CK)
        self.dssid2 = dssid2_match.group(1)
        self.as_pcts = as_pcts_match.group(1)
        logging.info(self.dssid2)
        logging.info(self.as_pcts)
        logging.info(f"第一步返回dssid2,,as_pcts" + ("-" * 200))
        return self.t1()

    def t1(self):
        headers = {
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "accept-language": "zh-CN,zh;q=0.9",
            "cache-control": "no-cache",
            "cookie": f"as_rumid=d5de47da-70ec-481f-816b-db71ee321a80; pt-dm=v1~x~tgu4kwv1~m~3; dssid2={self.dssid2}; dssf=1; as_pcts={self.as_pcts}; as_dc=ucp3",
            "pragma": "no-cache",
            "priority": "u=0, i",
            "sec-ch-ua": '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": '"Windows"',
            "sec-fetch-dest": "document",
            "sec-fetch-mode": "navigate",
            "sec-fetch-site": "none",
            "sec-fetch-user": "?1",
            "upgrade-insecure-requestsuests": "1",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
        }
        response= self.requests_.get(
                    "https://secure6.store.apple.com/shop/account/home",
                    headers=headers,
                    allow_redirects=False,
                )
        CK = response.headers.get("Set-Cookie")
        dssid2_match = re.search(r"dssid2=([a-z0-9\-]+);", CK)
        self.dssid2 = dssid2_match.group(1)
        self.ssi = response.headers["Location"]
        logging.info(self.dssid2)
        logging.info(self.ssi)
        logging.info(f"第二步返回dssid2,,ssi" + ("-" * 200))
        return self.t2()

    def t2(self):
        headers = {
                "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
                "accept-language": "zh-CN,zh;q=0.9",
                "cache-control": "no-cache",
                "cookie": f"as_rumid=d5de47da-70ec-481f-816b-db71ee321a80; pt-dm=v1~x~tgu4kwv1~m~3; dssid2={self.dssid2}; dssf=1; as_pcts={self.as_pcts}; as_dc=ucp3",
                "pragma": "no-cache",
                "priority": "u=0, i",
                "sec-ch-ua": '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
                "sec-ch-ua-mobile": "?0",
                "sec-ch-ua-platform": '"Windows"',
                "sec-fetch-dest": "document",
                "sec-fetch-mode": "navigate",
                "sec-fetch-site": "none",
                "sec-fetch-user": "?1",
                "upgrade-insecure-requestsuests": "1",
                "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
            }
        response_4 = self.requests_.get(self.ssi, headers=headers)
        CK = response_4.headers.get("Set-Cookie")
        self.x_aos_stk_value = re.search(r'"x-aos-stk":"([^"]+)"', response_4.text)
        dssid2_match = re.search(r"dssid2=([a-z0-9\-]+);", CK)
        self.x_aos_stk = self.x_aos_stk_value.group(1)
        self.dssid2 = dssid2_match.group(1)
        logging.info(self.dssid2)
        logging.info(self.x_aos_stk)
        logging.info(f"第三步返回dssid2,,x_aos_stk" + ("-" * 200))
        return self.t3()

    def t3(self):
        headers = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
            "Cookie": f"as_rumid=d5de47da-70ec-481f-816b-db71ee321a80; dssid2={self.dssid2}; dssf=1; as_pcts={self.as_pcts}; as_dc=ucp3; as_sfa=Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE; geo=CN; pxro=1; s_fid=6323376718433557-371662D1A66E1B14; s_cc=true",
            "Pragma": "no-cache",
            "Referer": "https://secure6.store.apple.com/",
            "Sec-Fetch-Dest": "iframe",
            "Sec-Fetch-Mode": "navigate",
            "Sec-Fetch-Site": "same-site",
            "Upgrade-Insecure-requestsuests": "1",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
            "sec-ch-ua": '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": '"Windows"',
        }
        response = self.requests_.get(
            "https://idmsa.apple.com/appleauth/auth/authorize/signin?frame_id=auth-sb36y35c-nirc-wgmc-2kzu-mdiax2hg&language=en_US&skVersion=7&iframeId=auth-sb36y35c-nirc-wgmc-2kzu-mdiax2hg&client_id=a797929d224abb1cc663bb187bbcd02f7172ca3a84df470380522a7c6092118b&redirect_uri=https://secure6.store.apple.com&response_type=code&response_mode=web_message&state=auth-sb36y35c-nirc-wgmc-2kzu-mdiax2hg&authVersion=latest",
            headers=headers,
        )
        CK = response.headers.get("Set-Cookie")
        self.aasp = re.search(r"aasp=([a-zA-Z0-9\-]+);", CK)
        self.aasp = self.aasp.group(1)

        self.X_Apple_Auth_Attributes = response.headers.get("X-Apple-Auth-Attributes")
        self.scnt = response.headers["scnt"]
        logging.info(self.aasp)
        logging.info(self.X_Apple_Auth_Attributes)
        logging.info(self.scnt)
        logging.info(f"第四步返回aasp,,X_Apple_Auth_Attributes,,scnt" + ("-" * 200))
        return self.t4()

    def t4(self):
        # -------------------------------------------------------
        url = "https://env-00jxgsqva6td.dev-hz.cloudbasefunction.cn/A1?type=1"
        payload = {f"email": {self.name}}
        Key = self.requests_.post(url, data=payload).json()
        logging.info(Key)
        logging.info(f"加密_1" + ("-" * 200))
        # ---------------------------------------------------------
        cookies = {
            "as_rumid": "d5de47da-70ec-481f-816b-db71ee321a80",
            "dssid2": self.dssid2,
            "dssf": "1",
            "as_pcts": self.as_pcts,
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
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
            "Content-Type": "application/json",
            "DNT": "1",
            "Origin": "https://idmsa.apple.com",
            "Pragma": "no-cache",
            "Referer": "https://idmsa.apple.com/",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-origin",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0",
            "X-Apple-Auth-Attributes": self.X_Apple_Auth_Attributes,
            "X-Apple-Domain-Id": "35",
            "X-Apple-Frame-Id": "auth-zkiybs92-vxxd-jekw-khmq-ean0k7dy",
            "X-Apple-I-FD-Client-Info": '{"U":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0","L":"zh-CN","Z":"GMT+08:00","V":"1.1","F":"Fla44j1e3NlY5BNlY5BSmHACVZXnNA9J6NrMhApWCAUfSHolk2dUJKy_Aw7GY5ey.EKY.6eke4FIY69vTKAy4IwrJNlY5BNp55BNlan0Os5Apw.AXL"}',
            "X-Apple-Locale": "en_US",
            "X-Apple-OAuth-Client-Id": "a797929d224abb1cc663bb187bbcd02f7172ca3a84df470380522a7c6092118b",
            "X-Apple-OAuth-Client-Type": "firstPartyAuth",
            "X-Apple-OAuth-Redirect-URI": "https://secure6.store.apple.com",
            "X-Apple-OAuth-Response-Mode": "web_message",
            "X-Apple-OAuth-Response-Type": "code",
            "X-Apple-OAuth-State": "auth-zkiybs92-vxxd-jekw-khmq-ean0k7dy",
            "X-Apple-Widget-Key": "a797929d224abb1cc663bb187bbcd02f7172ca3a84df470380522a7c6092118b",
            "X-requestsuested-With": "XMLHttprequestsuest",
            "scnt": self.scnt,
            "sec-ch-ua": '"Microsoft Edge";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": '"Windows"',
        }
        json_data = {
            "a": Key["r"],
            "accountName": self.name,
            "protocols": [
                "s2k",
                "s2k_fo",
            ],
        }
        response_2 = self.requests_.post(
            "https://idmsa.apple.com/appleauth/auth/signin/init",
            headers=headers,
            json=json_data,
            cookies=cookies,
        ).json()
        logging.info(Key)
        logging.info(f"加密_2" + ("-" * 200))
        # ---------------------------------------------------------
        url = "https://env-00jxgsqva6td.dev-hz.cloudbasefunction.cn/A1?type=2"
        payload = {
            "email": self.name,
            "iterations": response_2["iteration"],
            "Value": response_2["b"],
            "salt": response_2["salt"],
            "password": self.pwd,
            "protocol": response_2["protocol"],
            "privateHexValue": Key["privateHexValue"],
            "publicHexValue": Key["publicHexValue"],
        }
        response_3 = self.requests_.post(url, json=payload).json()
        logging.info(response_3)
        logging.info(f"加密_3" + ("-" * 200))
        # ---------------------------------------------------------
        cookies = {
            "as_rumid": "d5de47da-70ec-481f-816b-db71ee321a80",
            "dssid2": self.dssid2,
            "dssf": "1",
            "as_pcts": self.as_pcts,
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
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
            "Content-Type": "application/json",
            "DNT": "1",
            "Origin": "https://idmsa.apple.com",
            "Pragma": "no-cache",
            "Referer": "https://idmsa.apple.com/",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-origin",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0",
            "X-APPLE-HC": "1:12:20240529050254:1198c2c7e6f6fee6e86cbca751ea369b::7088",
            "X-Apple-Auth-Attributes": self.X_Apple_Auth_Attributes,
            "X-Apple-Domain-Id": "35",
            "X-Apple-Frame-Id": "auth-zkiybs92-vxxd-jekw-khmq-ean0k7dy",
            "X-Apple-I-FD-Client-Info": '{"U":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0","L":"zh-CN","Z":"GMT+08:00","V":"1.1","F":"7la44j1e3NlY5BNlY5BSmHACVZXnNA9J6NrMhp93cAxQeLaD.SAuXjodUW1BNpMk0ugN.xL4Fe1RNtMQmdUkdUZ0Y5BNlYJNNlY5QB4bVNjMk.1kD"}',
            "X-Apple-Locale": "en_US",
            "X-Apple-OAuth-Client-Id": "a797929d224abb1cc663bb187bbcd02f7172ca3a84df470380522a7c6092118b",
            "X-Apple-OAuth-Client-Type": "firstPartyAuth",
            "X-Apple-OAuth-Redirect-URI": "https://secure6.store.apple.com",
            "X-Apple-OAuth-Response-Mode": "web_message",
            "X-Apple-OAuth-Response-Type": "code",
            "X-Apple-OAuth-State": "auth-zkiybs92-vxxd-jekw-khmq-ean0k7dy",
            "X-Apple-Widget-Key": "a797929d224abb1cc663bb187bbcd02f7172ca3a84df470380522a7c6092118b",
            "X-requestsuested-With": "XMLHttprequestsuest",
            "scnt": self.scnt,
            "sec-ch-ua": '"Microsoft Edge";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": '"Windows"',
        }
        json_data = {
            "accountName": self.name,
            "rememberMe": False,
            "m1": response_3["M1"],
            "c": response_2["c"],
            "m2": response_3["M2"],
        }
        response_4 = self.requests_.post(
            "https://idmsa.apple.com/appleauth/auth/signin/complete",
            headers=headers,
            json=json_data,
            cookies=cookies,
        )
        CK = response_4.headers.get("Set-Cookie")
        myacinfo_pattern = re.compile(r"myacinfo=([^;]+)")
        myacinfo_match = myacinfo_pattern.search(CK)
        self.myacinfo = myacinfo_match.group(1)
        logging.info(self.myacinfo)
        logging.info(f"加密_4" + ("-" * 200))
        return self.t5()

    def t5(self):
        extracted_part = self.ssi.split("shop/signIn/account?ssi=")[1]
        headers = {
            "accept": "*/*",
            "accept-language": "zh-CN,zh;q=0.9",
            "cache-control": "no-cache",
            "content-type": "application/x-www-form-urlencoded",
            "cookie": f"as_rumid=d5de47da-70ec-481f-816b-db71ee321a80; dssid2={self.dssid2}; dssf=1; as_pcts={self.as_pcts}; as_dc=ucp3; as_sfa=Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE; geo=CN; pxro=1; s_fid=6323376718433557-371662D1A66E1B14; s_cc=true; s_vi=[CS]v1|332AA8C7A36C871F-40000E40A15E97D6[CE]; dslang=US-EN; site=USA; myacinfo={self.myacinfo}",
            "modelversion": "v2",
            "origin": "https://secure6.store.apple.com",
            "pragma": "no-cache",
            "priority": "u=1, i",
            "referer": self.ssi,
            "sec-ch-ua": '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": '"Windows"',
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "syntax": "graviton",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
            "x-aos-model-page": "idmsSignInPage",
            "x-aos-stk": self.x_aos_stk,
            "x-requested-with": "Fetch",
        }

        params = {
            "ssi": extracted_part
        }

        data = {
            "deviceID": "TF1;015;;;;;;;;;;;;;;;;;;;;;;Mozilla;Netscape;5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit/537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome/124.0.0.0%20Safari/537.36;20030107;undefined;true;;true;Win32;undefined;Mozilla/5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit/537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome/124.0.0.0%20Safari/537.36;zh-CN;undefined;secure6.store.apple.com;undefined;undefined;undefined;undefined;false;false;1716867481875;8;2005/6/7%2021%3A33%3A44;1920;1080;;;;;;;;-480;-480;2024/5/28%2011%3A38%3A01;24;1920;1032;0;0;;;;;;;;;;;;;;;;;;;25;",
            "grantCode": "",
        }

        response = self.requests_.post(
            "https://secure6.store.apple.com/shop/signIn/idms/authx",
            params=params,
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

        logging.info(f"dssid2_2: {self.dssid2}")
        logging.info(f"as_cn: {self.as_cn}")
        logging.info(f"as_disa: {self.as_disa}")
        logging.info(f"as_ltn_us: {self.as_ltn_us_1}")
        logging.info(f"as_rec: {self.as_rec}")
        logging.info("-" * 200)
        return self.t6()

    def t6(self):
        headers = {
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "accept-language": "zh-CN,zh;q=0.9",
            "cache-control": "no-cache",
            "cookie": f"as_rumid=d5de47da-70ec-481f-816b-db71ee321a80; dssid2={self.dssid2}; dssf=1; as_pcts={self.as_pcts}; as_dc=ucp3; as_sfa=Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE; geo=CN; pxro=1; s_fid=6323376718433557-371662D1A66E1B14; s_cc=true; s_vi=[CS]v1|332AA8C7A36C871F-40000E40A15E97D6[CE]; dslang=US-EN; site=USA; as_cn={self.as_cn}; as_disa={self.as_disa}; as_ltn_us={self.as_ltn_us_1}; as_rec={self.as_rec}; pt-dm=v1~x~tgu4kwv1~m~3~n~AOS%3A%20Checkout%20Sign%20In~r~aos%3Aaccount",
            "pragma": "no-cache",
            "priority": "u=0, i",
            "referer": self.ssi,
            "sec-ch-ua": '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": '"Windows"',
            "sec-fetch-dest": "document",
            "sec-fetch-mode": "navigate",
            "sec-fetch-site": "same-origin",
            "sec-fetch-user": "?1",
            "upgrade-insecure-requestsuests": "1",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
        }

        response = self.requests_.get(
            "https://secure6.store.apple.com/shop/account/home",
            headers=headers,
        )
        set_cookie_header = response.headers.get("Set-Cookie", "")
        dssid2_match = re.search(r"dssid2=([a-zA-Z0-9\-]+)", set_cookie_header)
        as_ltn_us_match = re.search(r"as_ltn_us=(.+?);", set_cookie_header)
        self.dssid2 = dssid2_match.group(1) if dssid2_match else None
        self.as_ltn_us_2 = as_ltn_us_match.group(1) if as_ltn_us_match else None

        logging.info(f"dssid2_2: {self.dssid2}")
        logging.info(f"home_as_ltn_us: {self.as_ltn_us_2}")
        logging.info("-" * 200)
        return self.t7()

    def t7(self):
        headers = {
            "accept": "*/*",
            "accept-language": "zh-CN,zh;q=0.9",
            "cache-control": "no-cache",
            # 'content-length': '0',
            "content-type": "application/x-www-form-urlencoded",
            "cookie": f"as_rumid=d5de47da-70ec-481f-816b-db71ee321a80; dssid2={self.dssid2}; dssf=1; as_pcts={self.as_pcts}; as_sfa=Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE; geo=CN; pxro=1; s_cc=true; dslang=US-EN; site=USA; as_cn={self.as_cn}; s_fid=6CDDD52C21065486-3346E9DAB52C8CE9; s_vi=[CS]v1|332AC4C3C85BFB44-40001D14E2C77ABD[CE]; as_dc=ucp3; s_sq=%5B%5BB%5D%5D; as_disa={self.as_disa}; as_rec={self.as_rec}; as_ltn_us={self.as_ltn_us_2}",
            "modelversion": "v2",
            "origin": "https://secure6.store.apple.com",
            "pragma": "no-cache",
            "priority": "u=1, i",
            "referer": "https://secure6.store.apple.com/shop/account/home",
            "sec-ch-ua": '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": '"Windows"',
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "syntax": "graviton",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
            "x-aos-model-page": "RetailHome",
            "x-aos-stk": self.x_aos_stk,
            "x-requested-with": "Fetch",
        }

        params = {
            "_a": "fetchDashboard",
            "_m": "home.dashboards",
        }

        response = self.requests_.post(
            "https://secure6.store.apple.com/shop/accounthomex", params=params, headers=headers
        )

        set_cookie_header = response.headers.get("Set-Cookie", "")
        dssid2_match = re.search(r"dssid2=([a-zA-Z0-9\-]+)", set_cookie_header)
        as_ltn_us_match = re.search(r"as_ltn_us=(.+?);", set_cookie_header)
        self.dssid2 = dssid2_match.group(1) if dssid2_match else None
        self.as_ltn_us_3 = as_ltn_us_match.group(1) if as_ltn_us_match else None
        logging.info(f"dssid2: {self.dssid2}")
        logging.info(f"fetchDashboard: {self.as_ltn_us_3}")
        logging.info("-" * 200)
        return self.t8()

    def t8(self):
        headers = {
            "accept": "*/*",
            "accept-language": "zh-CN,zh;q=0.9",
            "cache-control": "no-cache",
            # 'content-length': '0',
            "content-type": "application/x-www-form-urlencoded",
            "cookie": f"as_rumid=d5de47da-70ec-481f-816b-db71ee321a80; dssid2={self.dssid2}; dssf=1; as_pcts={self.as_pcts}; as_sfa=Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE; geo=CN; pxro=1; s_cc=true; dslang=US-EN; site=USA; as_cn={self.as_cn}; s_fid=6CDDD52C21065486-3346E9DAB52C8CE9; s_vi=[CS]v1|332AC4C3C85BFB44-40001D14E2C77ABD[CE]; as_dc=ucp3; as_disa={self.as_disa}; as_rec={self.as_rec}; as_ltn_us={self.as_ltn_us_3}; s_sq=applestoreww%3D%2526c.%2526a.%2526activitymap.%2526page%253DAOS%25253A%252520account%25252Fhome%2526link%253Deditedit%252520shipping%252520address%252520%252528inner%252520text%252529%252520%25257C%252520no%252520href%252520%25257C%252520body%2526region%253Dbody%2526pageIDType%253D1%2526.activitymap%2526.a%2526.c%2526pid%253DAOS%25253A%252520account%25252Fhome%2526pidt%253D1%2526oid%253Dfunctionkd%252528%252529%25257B%25257D%2526oidt%253D2%2526ot%253DBUTTON",
            "modelversion": "v2",
            "origin": "https://secure6.store.apple.com",
            "pragma": "no-cache",
            "priority": "u=1, i",
            "referer": "https://secure6.store.apple.com/shop/account/home",
            "sec-ch-ua": '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": '"Windows"',
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "syntax": "graviton",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
            "x-aos-model-page": "RetailHome",
            "x-aos-stk": self.x_aos_stk,
            "x-requested-with": "Fetch",
        }

        params = {
            "_a": "editAddress",
            "_m": "home.customerAccount.shippingInfo.shippingAddress",
        }

        response = self.requests_.post(
            "https://secure6.store.apple.com/shop/accounthomex", params=params, headers=headers
        )
        set_cookie_header = response.headers.get("Set-Cookie", "")
        dssid2_match = re.search(r"dssid2=([a-zA-Z0-9\-]+)", set_cookie_header)
        as_ltn_us_match = re.search(r"as_ltn_us=(.+?);", set_cookie_header)
        self.dssid2 = dssid2_match.group(1) if dssid2_match else None
        self.as_ltn_us_4 = as_ltn_us_match.group(1) if as_ltn_us_match else None

        logging.info(f"dssid2: {self.dssid2}")
        logging.info(f"editAddress: {self.as_ltn_us_4}")
        logging.info("-" * 200)
        return self.t9()

    def t9(self):
        headers = {
            "accept": "*/*",
            "accept-language": "zh-CN,zh;q=0.9",
            "cache-control": "no-cache",
            "content-type": "application/x-www-form-urlencoded",
            "cookie": f"as_rumid=d5de47da-70ec-481f-816b-db71ee321a80; dssid2={self.dssid2}; dssf=1; as_pcts={self.as_pcts}; as_sfa=Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE; geo=CN; pxro=1; s_cc=true; dslang=US-EN; site=USA; as_cn={self.as_cn}; s_fid=6CDDD52C21065486-3346E9DAB52C8CE9; s_vi=[CS]v1|332AC4C3C85BFB44-40001D14E2C77ABD[CE]; as_dc=ucp3; as_disa={self.as_disa}; as_rec={self.as_rec}; as_ltn_us={self.as_ltn_us_4}; s_sq=%5B%5BB%5D%5D",
            "modelversion": "v2",
            "origin": "https://secure6.store.apple.com",
            "pragma": "no-cache",
            "priority": "u=1, i",
            "referer": "https://secure6.store.apple.com/shop/account/home",
            "sec-ch-ua": '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": '"Windows"',
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "syntax": "graviton",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
            "x-aos-model-page": "RetailHome",
            "x-aos-stk": self.x_aos_stk,
            "x-requested-with": "Fetch",
        }

        params = {
            "_a": "address-submit",
            "_m": "home.customerAccount.shippingInfo.shippingAddress.editShippingAddress.editAddress",
        }

        data = "home.customerAccount.shippingInfo.shippingAddress.editShippingAddress.editAddress.fullDaytimePhone=(861)%20111-3333&home.customerAccount.shippingInfo.shippingAddress.editShippingAddress.editAddress.street2=212231312&home.customerAccount.shippingInfo.shippingAddress.editShippingAddress.editAddress.lastName=lllll3333&home.customerAccount.shippingInfo.shippingAddress.editShippingAddress.editAddress.firstName=hhhjjj11166666&home.customerAccount.shippingInfo.shippingAddress.editShippingAddress.editAddress.companyName=122332&home.customerAccount.shippingInfo.shippingAddress.editShippingAddress.editAddress.street=88888888888&home.customerAccount.shippingInfo.shippingAddress.editShippingAddress.editAddress.zipLookup.city=Albany&home.customerAccount.shippingInfo.shippingAddress.editShippingAddress.editAddress.zipLookup.state=NY&home.customerAccount.shippingInfo.shippingAddress.editShippingAddress.editAddress.zipLookup.postalCode=11111-4444&home.customerAccount.shippingInfo.shippingAddress.editShippingAddress.editAddress.zipLookup.countryCode=US"

        response = self.requests_.post(
            "https://secure6.store.apple.com/shop/accounthomex",
            params=params,
            headers=headers,
            data=data,
        )
        logging.info(response.headers)


apple  = APPLE().t0()

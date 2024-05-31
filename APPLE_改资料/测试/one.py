import requests,re,logging
from fake_useragent import UserAgent

user_agent = UserAgent()
logging.basicConfig(level=logging.INFO)

class APPLE:
    def __init__(self) -> None:
        self.requests_ = requests.session()
        self.name = "freesia.e-fpb@softbank.ne.jp"
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
            "user-agent": user_agent.random,
        }
        response = self.requests_.get("https://secure.store.apple.com/shop/account/home",headers=headers,allow_redirects=False)
        CK = response.headers.get("Set-Cookie")
        dssid2_match = re.search(r"dssid2=([a-z0-9\-]+);", CK)
        as_pcts_match = re.search(r"as_pcts=([^;]+);", CK)
        self.dssid2 = dssid2_match.group(1)
        self.as_pcts = as_pcts_match.group(1)
        logging.info(self.dssid2)
        logging.info(self.as_pcts)
        logging.info(f"T0_返回dssid2,,as_pcts" + ("-" * 200))
        return self.t1()

    def t1(self):
        headers = {
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
            "cache-control": "no-cache",
            "dnt": "1",
            "pragma": "no-cache",
            "priority": "u=0, i",
            "sec-ch-ua-mobile": "?0",
            "sec-fetch-dest": "document",
            "sec-fetch-mode": "navigate",
            "sec-fetch-site": "none",
            "sec-fetch-user": "?1",
            "upgrade-insecure-requests": "1",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0",
            "Cookie": f"pt-dm=v1~x~wedrj4y2~m~3; dssid2={self.dssid2}; dssf=1; as_pcts={self.as_pcts}; as_dc=ucp2"
        }

        response = requests.request("GET", 'https://secure5.store.apple.com/shop/account/home',headers=headers,allow_redirects=False)
        CK = response.headers.get("Set-Cookie")
        dssid2_match = re.search(r"dssid2=([a-z0-9\-]+);", CK)
        self.dssid2 = dssid2_match.group(1)
        self.ssi = response.headers["Location"]
        logging.info(self.dssid2)
        logging.info(self.ssi)
        logging.info(f"T1_返回dssid2,,ssi" + ("-" * 200))
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
        logging.info(f"T2_返回dssid2,,x_aos_stk" + ("-" * 200))
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
        logging.info(f"T4_返回aasp,,X_Apple_Auth_Attributes,,scnt" + ("-" * 200))
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
        logging.info(f"T4_" + ("-" * 200))
        return self.t5()

    def t5(self):
        extracted_part = self.ssi.split("shop/signIn/account?ssi=")[1]
        url = "https://secure8.store.apple.com/shop/signIn/idms/authx"

        querystring = {"ssi":extracted_part}

        payload = "deviceID=TF1;015;;;;;;;;;;;;;;;;;;;;;;Mozilla;Netscape;5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit/537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome/125.0.0.0%20Safari/537.36%20Edg/125.0.0.0;20030107;undefined;true;;true;Win32;undefined;Mozilla/5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit/537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome/125.0.0.0%20Safari/537.36%20Edg/125.0.0.0;zh-CN;undefined;secure8.store.apple.com;undefined;undefined;undefined;undefined;false;false;1717165745644;8;2005/6/7%2021%3A33%3A44;1920;1080;;;;;;;;-480;-480;2024/5/31%2022%3A29%3A05;24;1920;1032;0;0;;;;;;;;;;;;;;;;;;;25;&grantCode="
        headers = {
            "accept": "*/*",
            "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
            "cache-control": "no-cache",
            "content-type": "application/x-www-form-urlencoded",
            "dnt": "1",
            "modelversion": "v2",
            "origin": "https://secure8.store.apple.com",
            "pragma": "no-cache",
            "priority": "u=1, i",
            "referer": self.ssi,
            "sec-ch-ua-mobile": "?0",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "syntax": "graviton",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0",
            "x-aos-model-page": "idmsSignInPage",
            "x-aos-stk": self.x_aos_stk,
            "x-requested-with": "Fetch",
            "Cookie": f"dssid2={self.dssid2}; dssf=1; as_pcts={self.as_pcts}; as_dc=ucp5; as_sfa=Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE; geo=CN; as_rumid=37080742-fff1-41f3-aecd-2fd0c562336d; pxro=1; s_fid=0007D0AD63AE65D7-1498FEB6AB3B83FB; s_cc=true; s_vi=[CS]v1|332CEF48AE078368-40000140001631B7[CE]; dslang=US-EN; site=USA; myacinfo={self.myacinfo}"
        }

        response = self.requests_.post(
            url=url,
            params=querystring,
            headers=headers,
            data=payload,
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
        logging.info(f"t5_" + ("-" * 200))
        return self.t6()

    def t6(self):
        headers = {
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
            "cache-control": "no-cache",
            "dnt": "1",
            "pragma": "no-cache",
            "priority": "u=0, i",
            "referer": self.ssi,
            "sec-ch-ua-mobile": "?0",
            "sec-fetch-dest": "document",
            "sec-fetch-mode": "navigate",
            "sec-fetch-site": "same-origin",
            "sec-fetch-user": "?1",
            "upgrade-insecure-requests": "1",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0",
            "Cookie": f"dssid2={self.dssid2}; dssf=1; as_dc=ucp5; as_sfa=Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE; pxro=1; s_fid=0007D0AD63AE65D7-1498FEB6AB3B83FB; s_vi=[CS]v1|332CEF48AE078368-40000140001631B7[CE]; mbox=session#5df4d833cda1439dae08fc5cf557d782#1717168937|PC#5df4d833cda1439dae08fc5cf557d782.38_0#1717168877; as_pcts={self.as_pcts}; geo=CN; s_cc=true; dslang=US-EN; site=USA; as_rumid=0337ce99-a633-4190-ab73-87560b78c6df; as_cn={self.as_cn}; as_disa=AAAjAAABm6kIsKnxnYIB02LQUPS-onIQNufcLz7wrgdpIhPebJDOxA1TQlsz8z64F8PHkqzTAAIBpNndNH-D4O5j9_xJowW_k4O5r8FyprwQ0hqUA37H0eU=; as_ltn_us={self.as_ltn_us_1}; as_rec=b1ec3fef2d0c48da641d9cf8026397f0516d06eb6ff8f41696cd149003e40a70e9978fe86c283d7095116dfec28e68c5993c3813b40e1b3010f467d2e32e607a1cfa4c84a446babf298da9b43d29fafe; pt-dm=v1~x~n0vouo54~m~3~n~AOS: Checkout Sign In~r~aos:account"
        }

        response = self.requests_.get(
            "https://secure8.store.apple.com/shop/account/home",
            headers=headers,
        )
        set_cookie_header = response.headers.get("Set-Cookie", "")
        dssid2_match = re.search(r"dssid2=([a-zA-Z0-9\-]+)", set_cookie_header)
        as_ltn_us_match = re.search(r"as_ltn_us=(.+?);", set_cookie_header)
        self.dssid2 = dssid2_match.group(1) if dssid2_match else None
        self.as_ltn_us_2 = as_ltn_us_match.group(1) if as_ltn_us_match else None

        logging.info(f"dssid2_2: {self.dssid2}")
        logging.info(f"home_as_ltn_us: {self.as_ltn_us_2}")
        logging.info(f"t6_" + ("-" * 200))
        return self.t7()

    def t7(self):
        headers = {
            "accept": "*/*",
            "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
            "cache-control": "no-cache",
            "content-length": "0",
            "content-type": "application/x-www-form-urlencoded",
            "dnt": "1",
            "modelversion": "v2",
            "origin": "https://secure8.store.apple.com",
            "pragma": "no-cache",
            "priority": "u=1, i",
            "referer": "https://secure8.store.apple.com/shop/account/home",
            "sec-ch-ua-mobile": "?0",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "syntax": "graviton",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0",
            "x-aos-model-page": "RetailHome",
            "x-aos-stk": self.x_aos_stk,
            "x-requested-with": "Fetch",
            "Cookie": f"dssid2={self.dssid2}; dssf=1; as_dc=ucp5; as_sfa=Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE; pxro=1; s_fid=0007D0AD63AE65D7-1498FEB6AB3B83FB; s_vi=[CS]v1|332CEF48AE078368-40000140001631B7[CE]; mbox=session#5df4d833cda1439dae08fc5cf557d782#1717168937|PC#5df4d833cda1439dae08fc5cf557d782.38_0#1717168877; as_pcts={self.as_pcts}; geo=CN; s_cc=true; dslang=US-EN; site=USA; as_rumid=0337ce99-a633-4190-ab73-87560b78c6df; as_cn={self.as_cn}; as_disa={self.as_disa}; as_rec=b1ec3fef2d0c48da641d9cf8026397f0516d06eb6ff8f41696cd149003e40a70e9978fe86c283d7095116dfec28e68c5993c3813b40e1b3010f467d2e32e607a1cfa4c84a446babf298da9b43d29fafe; as_ltn_us={self.as_ltn_us_2}"
        }

        params = {
            "_a": "fetchDashboard",
            "_m": "home.dashboards",
        }

        response = self.requests_.post(
            "https://secure8.store.apple.com/shop/accounthomex", params=params, headers=headers
        )

        set_cookie_header = response.headers.get("Set-Cookie", "")
        dssid2_match = re.search(r"dssid2=([a-zA-Z0-9\-]+)", set_cookie_header)
        as_ltn_us_match = re.search(r"as_ltn_us=(.+?);", set_cookie_header)
        self.dssid2 = dssid2_match.group(1) if dssid2_match else None
        self.as_ltn_us_3 = as_ltn_us_match.group(1) if as_ltn_us_match else None
        logging.info(f"dssid2: {self.dssid2}")
        logging.info(f"fetchDashboard: {self.as_ltn_us_3}")
        logging.info(f"t7_" + ("-" * 200))
        return self.t8()

    def t8(self):
        headers ={
            "accept": "*/*",
            "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
            "cache-control": "no-cache",
            "content-length": "0",
            "content-type": "application/x-www-form-urlencoded",
            "dnt": "1",
            "modelversion": "v2",
            "origin": "https://secure8.store.apple.com",
            "pragma": "no-cache",
            "priority": "u=1, i",
            "referer": "https://secure8.store.apple.com/shop/account/home",
            "sec-ch-ua-mobile": "?0",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "syntax": "graviton",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0",
            "x-aos-model-page": "RetailHome",
            "x-aos-stk": self.x_aos_stk,
            "x-requested-with": "Fetch",
            "Cookie": f"dssid2={self.dssid2}; dssf=1; as_dc=ucp5; as_sfa=Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE; pxro=1; s_fid=0007D0AD63AE65D7-1498FEB6AB3B83FB; s_vi=[CS]v1|332CEF48AE078368-40000140001631B7[CE]; mbox=session#5df4d833cda1439dae08fc5cf557d782#1717168937|PC#5df4d833cda1439dae08fc5cf557d782.38_0#1717168877; as_pcts={self.as_pcts}; geo=CN; s_cc=true; dslang=US-EN; site=USA; as_rumid=0337ce99-a633-4190-ab73-87560b78c6df; as_cn={self.as_cn}; as_disa={self.as_disa}; as_rec=b1ec3fef2d0c48da641d9cf8026397f0516d06eb6ff8f41696cd149003e40a70e9978fe86c283d7095116dfec28e68c5993c3813b40e1b3010f467d2e32e607a1cfa4c84a446babf298da9b43d29fafe; as_ltn_us={self.as_ltn_us_3}"
        }

        params = {
            "_a": "editAddress",
            "_m": "home.customerAccount.shippingInfo.shippingAddress",
        }

        response = self.requests_.post(
            "https://secure8.store.apple.com/shop/accounthomex", params=params, headers=headers
        )
        set_cookie_header = response.headers.get("Set-Cookie", "")
        dssid2_match = re.search(r"dssid2=([a-zA-Z0-9\-]+)", set_cookie_header)
        as_ltn_us_match = re.search(r"as_ltn_us=(.+?);", set_cookie_header)
        self.dssid2 = dssid2_match.group(1) if dssid2_match else None
        self.as_ltn_us_4 = as_ltn_us_match.group(1) if as_ltn_us_match else None

        logging.info(f"dssid2: {self.dssid2}")
        logging.info(f"editAddress: {self.as_ltn_us_4}")
        logging.info(f"t8_" + ("-" * 200))
        return self.t9()

    def t9(self):
        headers = {
            "accept": "*/*",
            "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
            "cache-control": "no-cache",
            "content-type": "application/x-www-form-urlencoded",
            "dnt": "1",
            "modelversion": "v2",
            "origin": "https://secure8.store.apple.com",
            "pragma": "no-cache",
            "priority": "u=1, i",
            "referer": "https://secure8.store.apple.com/shop/account/home",
            "sec-ch-ua-mobile": "?0",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "syntax": "graviton",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0",
            "x-aos-model-page": "RetailHome",
            "x-aos-stk": self.x_aos_stk,
            "x-requested-with": "Fetch",
            "Cookie": f"dssid2={self.dssid2}; dssf=1; as_dc=ucp5; as_sfa=Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE; pxro=1; as_pcts={self.as_pcts}; geo=CN; s_cc=true; dslang=US-EN; site=USA; as_rumid=0337ce99-a633-4190-ab73-87560b78c6df; s_fid=14FE3FCD7955D882-0CD59C3A0ACF70DD; at_check=true; mbox=session#357e8d6c88e74bfd8b1bed3317df4b52#1717171254|PC#357e8d6c88e74bfd8b1bed3317df4b52.38_0#1717171194; s_vi=[CS]v1|332CF679F7916F0E-40000B8569FA266A[CE]; as_cn={self.as_cn}; as_disa={self.as_disa}; as_rec=4c14a2b74cc829d4164aa6e377ff54afbf3ce95f7415867b463ac4a7a1da799f6dc2f15790091bcf48a9f833f71872a435e9d126ac9de8dc66d40b91efdb00089d0c9b825e81ed19ba6c8edbf04ab312; as_ltn_us={self.as_ltn_us_4}; s_sq=[[B]]"
        }
        params = {
            "_a": "address-submit",
            "_m": "home.customerAccount.shippingInfo.shippingAddress.editShippingAddress.editAddress",
        }

        data = "home.customerAccount.shippingInfo.shippingAddress.editShippingAddress.editAddress.fullDaytimePhone=(861)%20111-1345&home.customerAccount.shippingInfo.shippingAddress.editShippingAddress.editAddress.street2=212231312&home.customerAccount.shippingInfo.shippingAddress.editShippingAddress.editAddress.lastName=lllll3333&home.customerAccount.shippingInfo.shippingAddress.editShippingAddress.editAddress.firstName=hhhjjj11166666&home.customerAccount.shippingInfo.shippingAddress.editShippingAddress.editAddress.companyName=122332&home.customerAccount.shippingInfo.shippingAddress.editShippingAddress.editAddress.street=88888888888&home.customerAccount.shippingInfo.shippingAddress.editShippingAddress.editAddress.zipLookup.city=Albany&home.customerAccount.shippingInfo.shippingAddress.editShippingAddress.editAddress.zipLookup.state=NY&home.customerAccount.shippingInfo.shippingAddress.editShippingAddress.editAddress.zipLookup.postalCode=11111-4444&home.customerAccount.shippingInfo.shippingAddress.editShippingAddress.editAddress.zipLookup.countryCode=US"

        response = self.requests_.post(
            "https://secure8.store.apple.com/shop/accounthomex",
            params=params,
            headers=headers,
            data=data,
        )

        logging.info(response.headers)
        logging.info(f"t9_" + ("-" * 200))


apple  = APPLE().t0()

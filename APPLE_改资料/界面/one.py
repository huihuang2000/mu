import requests, re, logging
from fake_useragent import UserAgent
from requests.exceptions import RequestException
from requests.exceptions import RequestException
from functools import wraps

user_agent = UserAgent()
shared_session = requests.Session()
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)


# def retry_on_exception(max_attempts=5,exceptions=(Exception,)):
#     def decorator(func):
#         @wraps(func)
#         def wrapper(*args, **kwargs):
#             attempts = 0
#             while attempts < max_attempts:
#                 try:
#                     return func(*args, **kwargs)
#                 except exceptions as e:
#                     attempts += 1
#                     logging.warning(f"Exception {e} occurred, retrying... (Attempt {attempts}/{max_attempts})")
#                     # time.sleep(backoff_factor * (2 ** (attempts - 1)))  # exponential backoff
#             # You can raise the last exception or return a default value
#             logging.error(f"Max retries reached, giving up.")
#             raise  # Reraise the last exception
#         return wrapper
#     return decorator
def retry_on_exception(max_attempts=5, exceptions=(Exception,)):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            attempts = 0
            while attempts < max_attempts:
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    attempts += 1
                    logging.warning(f"Exception {e} occurred, retrying... (Attempt {attempts}/{max_attempts})")
                    if attempts == max_attempts:
                        logging.error(f"Max retries reached, giving up.")
                        raise  # Reraise the last exception after max_attempts
            return func(*args, **kwargs)  # This line will never be reached with the current logic
        return wrapper
    return decorator




class APPLE:
    def __init__(self, **address_details) -> None:
        self.COMMON_HEADERS = {
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "accept-language": "zh-CN,zh;q=0.9",
            "pragma": "no-cache",
            "cache-control": "no-cache",
            "sec-ch-ua": '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": '"Windows"',
            "sec-fetch-dest": "document",
            "sec-fetch-mode": "navigate",
            "sec-fetch-site": "none",
            "sec-fetch-user": "?1",
            "upgrade-insecure-requests": "1",
            "user-agent": user_agent.random,
        }
        self.name = address_details.get("name")
        self.pwd = address_details.get("pwd")
        self.fullDaytimePhone = address_details.get("fullDaytimePhone")
        self.street2 = address_details.get("street2")
        self.lastName = address_details.get("lastName")
        self.firstName = address_details.get("firstName")
        self.companyName = address_details.get("companyName")
        self.street = address_details.get("street")
        self.city = address_details.get("city")
        self.state = address_details.get("state")
        self.postalCode = address_details.get("postalCode")
        self.countryCode = address_details.get("countryCode")
        self.session = shared_session
        # self.t0()
        

    @retry_on_exception(max_attempts=20)
    def _send_request(self, method, url, **kwargs):
        try:
            self.DL = self.dl()
            response = self.session.request(method, url, **kwargs, proxies=self.DL,timeout=5)
            response.raise_for_status()
            return response
        except RequestException as e:
            self.DL = self.dl()
            logging.error(f"Request failed with exception: {e}")
            raise  # 让装饰器处理重试逻辑

    def _build_headers(self, additional_headers=None):
        headers = self.COMMON_HEADERS.copy()
        if additional_headers:
            headers.update(additional_headers)
        return headers

    def dl(self):
        dl_url = "http://api.xiequ.cn/VAD/GetIp.aspx?act=get&uid=94212&vkey=9B6E155B17E7B42A415A2C63FD1E8172&num=1&time=30&plat=1&re=0&type=0&so=1&ow=1&spl=1&addr=&db=1"
        dL = requests.get(url=dl_url).text.replace("\r\n", "")
        proxies = {"https": f"{dL}"}
        print(proxies)
        return proxies

    def t0(self):
        max_retries = 5  # 设置最大重试次数
        retry_delay = 2  # 重试间隔时间，单位为秒
        for attempt in range(max_retries):
            try:
                response = self._send_request(
                    method="get",
                    url="https://secure.store.apple.com/shop/account/home",
                    allow_redirects=False,
                )
                CK = response.headers.get("Set-Cookie")
                dssid2_match = re.search(r"dssid2=([a-z0-9\-]+);", CK)
                as_pcts_match = re.search(r"as_pcts=([^;]+);", CK)
                
                # 检查是否找到匹配项
                if dssid2_match and as_pcts_match:
                    self.dssid2 = dssid2_match.group(1)
                    self.as_pcts = as_pcts_match.group(1)
                    logging.info(self.dssid2)
                    logging.info(self.as_pcts)
                    logging.info(f"T0_返回dssid2,,as_pcts" + ("-" * 40))
                    return self.t1()  # 如果成功找到匹配项，继续执行 t1
                else:
                    raise ValueError("正则表达式没有找到匹配的值")
                
            except ValueError as e:
                logging.warning(f"重试 #{attempt + 1}，错误：{e}")
            except RequestException as e:
                # 对于请求异常，可以选择重试或记录日志后停止
                logging.error(f"请求失败，停止重试。错误：{e}")
                break
        
        # 如果达到最大重试次数，可以选择抛出异常或返回错误信息
        logging.error("达到最大重试次数，无法获取 dssid2 和 as_pcts")
        raise RuntimeError("无法获取必要的会话信息")

    def t1(self):
        additional_headers = {
            "Cookie": f"dssid2={self.dssid2}; dssf=1; as_pcts={self.as_pcts}",
        }
        headers = self._build_headers(additional_headers)
        response = self._send_request(
            method="get",
            url="https://secure5.store.apple.com/shop/account/home",
            headers=headers,
            allow_redirects=False,
        )
        CK = response.headers.get("Set-Cookie")
        dssid2_match = re.search(r"dssid2=([a-z0-9\-]+);", CK)
        self.dssid2 = dssid2_match.group(1)
        self.ssi = response.headers["Location"]
        logging.info(self.dssid2)
        logging.info(self.ssi)
        logging.info(f"T1_返回dssid2,,ssi" + ("-" * 40))
        return self.t2()

    def t2(self):
        additional_headers = {
            "cookie": f"dssid2={self.dssid2}; dssf=1; as_pcts={self.as_pcts}",
        }
        headers = self._build_headers(additional_headers)
        response_4 = self._send_request(method="get", url=self.ssi, headers=headers)
        CK = response_4.headers.get("Set-Cookie")
        self.x_aos_stk_value = re.search(r'"x-aos-stk":"([^"]+)"', response_4.text)
        dssid2_match = re.search(r"dssid2=([a-z0-9\-]+);", CK)
        self.x_aos_stk = self.x_aos_stk_value.group(1)
        self.dssid2 = dssid2_match.group(1)
        logging.info(self.dssid2)
        logging.info(self.x_aos_stk)
        logging.info(f"T2_返回dssid2,,x_aos_stk" + ("-" * 40))
        return self.t3()

    def t3(self):
        headers = {
            "Cookie": f"dssid2={self.dssid2}; dssf=1; as_pcts={self.as_pcts}",
        }
        headers = self._build_headers(headers)
        response = self._send_request(
            method="get",
            url="https://idmsa.apple.com/appleauth/auth/authorize/signin?frame_id=auth-sb36y35c-nirc-wgmc-2kzu-mdiax2hg&language=en_US&skVersion=7&iframeId=auth-sb36y35c-nirc-wgmc-2kzu-mdiax2hg&client_id=a797929d224abb1cc663bb187bbcd02f7172ca3a84df470380522a7c6092118b&redirect_uri=https://secure6.store.apple.com&response_type=code&response_mode=web_message&state=auth-sb36y35c-nirc-wgmc-2kzu-mdiax2hg&authVersion=latest",
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
        logging.info(f"T4_返回aasp,,X_Apple_Auth_Attributes,,scnt" + ("-" * 40))
        return self.t4()

    def t4(self):
        # -------------------------------------------------------
        url = "https://env-00jxgsqva6td.dev-hz.cloudbasefunction.cn/A1?type=1"
        payload = {f"email": {self.name}}
        Key = self._send_request(method="post", url=url, data=payload).json()
        logging.info(Key)
        logging.info(f"加密_1" + ("-" * 40))
        # ---------------------------------------------------------
        combined_headers_and_cookies = {
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "User-Agent": user_agent.random,
            "X-Apple-Auth-Attributes": self.X_Apple_Auth_Attributes,
            "scnt": self.scnt,
        }
        json_data = {
            "a": Key["r"],
            "accountName": self.name,
            "protocols": [
                "s2k",
                "s2k_fo",
            ],
        }
        headers = self._build_headers(combined_headers_and_cookies)
        response_2 = self._send_request(
            method="post",
            url="https://idmsa.apple.com/appleauth/auth/signin/init",
            headers=headers,
            json=json_data,
        ).json()
        logging.info(Key)
        logging.info(f"加密_2" + ("-" * 40))
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
        response_3 = self._send_request(method="post", url=url, json=payload).json()
        logging.info(response_3)
        logging.info(f"加密_3" + ("-" * 40))
        # ---------------------------------------------------------
        cookies = {
            "as_rumid": "9f9a7e8708ebbde2daf02b478473eccd",
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
            "User-Agent": user_agent.random,
            "X-Apple-Auth-Attributes": self.X_Apple_Auth_Attributes,
            "X-Apple-Widget-Key": "a797929d224abb1cc663bb187bbcd02f7172ca3a84df470380522a7c6092118b",
            "scnt": self.scnt,
        }
        json_data = {
            "accountName": self.name,
            "rememberMe": False,
            "m1": response_3["M1"],
            "c": response_2["c"],
            "m2": response_3["M2"],
        }
        response_4 = self._send_request(
            method="post",
            url="https://idmsa.apple.com/appleauth/auth/signin/complete",
            headers=headers,
            json=json_data,
            cookies=cookies,
        )
        CK = response_4.headers.get("Set-Cookie")
        myacinfo_pattern = re.compile(r"myacinfo=([^;]+)")
        myacinfo_match = myacinfo_pattern.search(CK)
        self.myacinfo = myacinfo_match.group(1)
        logging.info(self.myacinfo)
        logging.info(f"T4_" + ("-" * 40))
        return self.t5()

    def t5(self):
        extracted_part = self.ssi.split("shop/signIn/account?ssi=")[1]
        url = "https://secure8.store.apple.com/shop/signIn/idms/authx"

        querystring = {"ssi": extracted_part}

        payload = "deviceID=TF1;015;;;;;;;;;;;;;;;;;;;;;;Mozilla;Netscape;5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit/537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome/125.0.0.0%20Safari/537.36%20Edg/125.0.0.0;20030107;undefined;true;;true;Win32;undefined;Mozilla/5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit/537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome/125.0.0.0%20Safari/537.36%20Edg/125.0.0.0;zh-CN;undefined;secure8.store.apple.com;undefined;undefined;undefined;undefined;false;false;1717165745644;8;2005/6/7%2021%3A33%3A44;1920;1080;;;;;;;;-480;-480;2024/5/31%2022%3A29%3A05;24;1920;1032;0;0;;;;;;;;;;;;;;;;;;;25;&grantCode="
        headers = {
            "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
            "referer": self.ssi,
            "user-agent": user_agent.random,
            "x-aos-stk": self.x_aos_stk,
            "x-requested-with": "Fetch",
            "Cookie": f"dssid2={self.dssid2}; dssf=1; as_pcts={self.as_pcts};myacinfo={self.myacinfo}",
        }

        response = self._send_request(
            method="post",
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
        logging.info(f"t5_" + ("-" * 40))
        return self.t6()

    def t6(self):
        headers = {
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "referer": self.ssi,
            "Cookie": f"dssid2={self.dssid2}; dssf=1; as_pcts={self.as_pcts};as_cn={self.as_cn}; as_disa={self.as_disa}; as_ltn_us={self.as_ltn_us_1};",
        }
        headers = self._build_headers(headers)
        response = self._send_request(
            method="get",
            url="https://secure8.store.apple.com/shop/account/home",
            headers=headers,
        )
        set_cookie_header = response.headers.get("Set-Cookie", "")
        dssid2_match = re.search(r"dssid2=([a-zA-Z0-9\-]+)", set_cookie_header)
        as_ltn_us_match = re.search(r"as_ltn_us=(.+?);", set_cookie_header)
        self.dssid2 = dssid2_match.group(1) if dssid2_match else None
        self.as_ltn_us_2 = as_ltn_us_match.group(1) if as_ltn_us_match else None

        logging.info(f"dssid2_2: {self.dssid2}")
        logging.info(f"home_as_ltn_us: {self.as_ltn_us_2}")
        logging.info(f"t6_" + ("-" * 40))
        return self.t7()

    def t7(self):
        headers = {
            "x-aos-stk": self.x_aos_stk,
            "x-requested-with": "Fetch",
            "Cookie": f"dssid2={self.dssid2}; dssf=1;as_pcts={self.as_pcts};as_cn={self.as_cn}; as_disa={self.as_disa};as_ltn_us={self.as_ltn_us_2}",
        }

        params = {
            "_a": "fetchDashboard",
            "_m": "home.dashboards",
        }
        headers = self._build_headers(headers)
        response = self._send_request(
            method="post",
            url="https://secure8.store.apple.com/shop/accounthomex",
            params=params,
            headers=headers,
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
        headers = {
            "user-agent": user_agent.random,
            "x-aos-stk": self.x_aos_stk,
            "x-requested-with": "Fetch",
            "Cookie": f"dssid2={self.dssid2}; dssf=1;as_pcts={self.as_pcts};as_cn={self.as_cn}; as_disa={self.as_disa}; as_ltn_us={self.as_ltn_us_3}",
        }

        params = {
            "_a": "editAddress",
            "_m": "home.customerAccount.shippingInfo.shippingAddress",
        }
        headers = self._build_headers(headers)
        response = self._send_request(
            method="post",
            url="https://secure8.store.apple.com/shop/accounthomex",
            params=params,
            headers=headers,
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
            "content-type": "application/x-www-form-urlencoded",  # 此处为坑,不加这个就算成功，值也不会改变
            "user-agent": user_agent.random,
            "x-aos-stk": self.x_aos_stk,
            "x-requested-with": "Fetch",
            "Cookie": f"dssid2={self.dssid2}; dssf=1;as_pcts={self.as_pcts};as_cn={self.as_cn}; as_disa={self.as_disa};as_ltn_us={self.as_ltn_us_4}",
        }
        params = {
            "_a": "address-submit",
            "_m": "home.customerAccount.shippingInfo.shippingAddress.editShippingAddress.editAddress",
        }

        data = (
            f"home.customerAccount.shippingInfo.shippingAddress.editShippingAddress.editAddress.fullDaytimePhone={self.fullDaytimePhone}&"
            f"home.customerAccount.shippingInfo.shippingAddress.editShippingAddress.editAddress.street2={self.street2}&"
            f"home.customerAccount.shippingInfo.shippingAddress.editShippingAddress.editAddress.lastName={self.lastName}&"
            f"home.customerAccount.shippingInfo.shippingAddress.editShippingAddress.editAddress.firstName={self.firstName}&"
            f"home.customerAccount.shippingInfo.shippingAddress.editShippingAddress.editAddress.companyName={self.companyName}&"
            f"home.customerAccount.shippingInfo.shippingAddress.editShippingAddress.editAddress.street={self.street}&"
            f"home.customerAccount.shippingInfo.shippingAddress.editShippingAddress.editAddress.zipLookup.city={self.city}&"
            f"home.customerAccount.shippingInfo.shippingAddress.editShippingAddress.editAddress.zipLookup.state={self.state}&"
            f"home.customerAccount.shippingInfo.shippingAddress.editShippingAddress.editAddress.zipLookup.postalCode={self.postalCode}&"
            f"home.customerAccount.shippingInfo.shippingAddress.editShippingAddress.editAddress.zipLookup.countryCode={self.countryCode}"
        )
        headers = self._build_headers(headers)
        response = self._send_request(
            method="post",
            url="https://secure8.store.apple.com/shop/accounthomex",
            params=params,
            headers=headers,
            data=data,
        ).json()
        logging.info(response)
        logging.info(f"t9_" + ("-" * 200))
        return response['body']['home']['customerAccount']['shippingInfo']['shippingAddress']['d']


def main(**kwargs):
    apple_instance = APPLE(**kwargs).t0()
    return apple_instance


if __name__ == "__main__":
    params = {
        "name": "my_hero.hero@softbank.ne.jp",
        "pwd": "Aa147369",
        "fullDaytimePhone": "20111-1111",
        "street2": "212231312",
        "lastName": "lllll3333",
        "firstName": "hhhjjj11166666",
        "companyName": "122332",
        "street": "777776667777",
        "city": "Albany",
        "state": "CH",
        "postalCode": "11111-1111",
        "countryCode": "CH",
    }
    main_instance = main(**params)

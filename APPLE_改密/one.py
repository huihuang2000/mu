from numpy import number
import requests, re, ddddocr
from urllib.parse import unquote, quote

ocr = ddddocr.DdddOcr(
    det=False,
    show_ad=False,
    ocr=False,
    import_onnx_path="APPLE_改密/A1_1.0_21_726000_2024-01-03-21-55-07.onnx",
    charsets_path="APPLE_改密/charsets (1).json",
)

# 获取sstt
headers = {
    "Host": "iforgot.apple.com",
    "Connection": "keep-alive",
    "sec-ch-ua": '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Sec-Fetch-Site": "cross-site",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-User": "?1",
    "Sec-Fetch-Dest": "document",
    "Referer": "https://idmsa.apple.com.cn/",
    # "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
    # "Cookie": "idclient=web; dslang=CN-ZH; site=CHN; ifssp=8F6D6A18FFA1A8AFF0ADB6956DB0E7474DAD3DBE0B9B52D7DEE473886AFA3295C1C6359E8C6370EABACF449D8ED6993B287621F6199695CA11613D923CB4EAF9F3514E0D4C1D3F12ABC1761B59A5836867B436AE0AA82721C95453EC30C465C1E35177645C16EF1C8B90C7B4B8BC2B8876C7A6D869F9F1F1; geo=CN"
}
response = requests.get(
    "https://iforgot.apple.com/password/verify/appleid", headers=headers
)
sstt = re.search(r'"sstt":"([^"]+)"', response.text).group(1)
x_apple_i_web_token = response.cookies.get("X-Apple-I-Web-Token")
ifssp = response.cookies.get("ifssp")


# 获取验证码
headers = {
    "Host": "iforgot.apple.com",
    "Connection": "keep-alive",
    "sec-ch-ua": '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
    "sstt": quote(sstt),
    "X-Apple-I-FD-Client-Info": '{"U":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36","L":"zh-CN","Z":"GMT+08:00","V":"1.1","F":"7la44j1e3NlY5BNlY5BSmHACVZXnNA9cedK9AqApNurJhBR.uMp4UdHz13Nl_jV2pNk0ug9WJ3uJsjMm_U_WU_v25BNlY5cklY5BqNAE.lTjV.9OX"}',
    "sec-ch-ua-mobile": "?0",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
    "Content-Type": "application/json",
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "X-Requested-With": "XMLHttpRequest",
    "sec-ch-ua-platform": '"Windows"',
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Dest": "empty",
    "Referer": "https://iforgot.apple.com/",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
    "Cookie": f"idclient=web; dslang=CN-ZH; site=CHN; geo=CN; X-Apple-I-Web-Token={x_apple_i_web_token}; ifssp={ifssp}",
}
params = {
    "captchaType": "IMAGE",
}
response = requests.get(
    "https://iforgot.apple.com/captcha", params=params, headers=headers
)
x_apple_i_web_token_2 = response.cookies.get("X-Apple-I-Web-Token")
Token = response.json()["token"]
Id = response.json()["id"]

# 验证码识别
res = ocr.classification(response.json()["payload"]["content"])


# 提交302
cookies = {
    "idclient": "web",
    "dslang": "CN-ZH",
    "site": "CHN",
    "geo": "CN",
    "ifssp": ifssp,
    "X-Apple-I-Web-Token": x_apple_i_web_token_2,
}

headers = {
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Content-Type": "application/json",
    "Origin": "https://iforgot.apple.com",
    "Pragma": "no-cache",
    "Referer": "https://iforgot.apple.com/",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
    "X-Apple-I-FD-Client-Info": '{"U":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36","L":"zh-CN","Z":"GMT+08:00","V":"1.1","F":"Fla44j1e3NlY5BNlY5BSmHACVZXnNA9cedFWv9AqururJhBR.uMp4UdHz13NlejV2pNk0ug9WJ3uJsjMm_UWujme5BNlY5CGWY5BOgkLT0XxU..0ch"}',
    "X-Requested-With": "XMLHttpRequest",
    "sec-ch-ua": '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
    "sstt": quote(sstt),
}

json_data = {
    "id": "aidenchabhn@outlook.com",
    "captcha": {
        "id": Id,
        "answer": res,
        "token": Token,
    },
}

response = requests.post(
    "https://iforgot.apple.com/password/verify/appleid",
    cookies=cookies,
    headers=headers,
    json=json_data,
    allow_redirects=False,
)
sstt_2 = unquote(response.headers["Sstt"])
x_apple_i_web_token_3 = response.cookies.get("X-Apple-I-Web-Token")


# 选择改密或者改密保
cookies = {
    "idclient": "web",
    "dslang": "CN-ZH",
    "site": "CHN",
    "ifssp": ifssp,
    "geo": "CN",
    "X-Apple-I-Web-Token": x_apple_i_web_token_3,
}

headers = {
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Pragma": "no-cache",
    "Referer": "https://iforgot.apple.com/",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
    "X-Apple-I-FD-Client-Info": '{"U":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36","L":"zh-CN","Z":"GMT+08:00","V":"1.1","F":"7la44j1e3NlY5BNlY5BSmHACVZXnNA9cedH1Zd9PzLu_dYV6Hycfx9MsFY5Bhw.Tf5.EKWJ9VbHb4uyL4yZnxHGY5BNlYJNNlY5QB4bVNjMk..Dc"}',
    "X-Requested-With": "XMLHttpRequest",
    "sec-ch-ua": '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
    "sstt": sstt,
}

params = {
    "sstt": sstt_2,
}

response = requests.get(
    "https://iforgot.apple.com/recovery/options",
    params=params,
    cookies=cookies,
    headers=headers,
)
x_apple_i_web_token_4 = response.cookies.get("X-Apple-I-Web-Token")
sstt_3 = response.json()["sstt"]


# 转换X-Apple-I-Web-Token
cookies = {
    "idclient": "web",
    "dslang": "CN-ZH",
    "site": "CHN",
    "geo": "CN",
    "ifssp": ifssp,
    "X-Apple-I-Web-Token": x_apple_i_web_token_4,
}

headers = {
    "Accept": "text/html;format=fragmented",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Content-Type": "application/json",
    "Pragma": "no-cache",
    "Referer": "https://iforgot.apple.com/",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
    "X-Apple-I-FD-Client-Info": '{"U":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36","L":"zh-CN","Z":"GMT+08:00","V":"1.1","F":"7la44j1e3NlY5BNlY5BSmHACVZXnNA9ceidTojLJ26Lu_dYV6Hycfx9MsFY5CKw.Tf5.EKWJ9VbHb4uyKAwmbticlY5BNleBBNlYCa1nkBMfs.2IE"}',
    "X-Requested-With": "XMLHttpRequest",
    "sec-ch-ua": '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
    "sstt": sstt_3,
}

response = requests.get(
    "https://iforgot.apple.com/recovery/options", cookies=cookies, headers=headers
)
x_apple_i_web_token_5 = response.cookies.get("X-Apple-I-Web-Token")


# 过302
headers = {
    "Host": "iforgot.apple.com",
    "Connection": "keep-alive",
    "Content-Length": "35",
    "sec-ch-ua": '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
    "sstt": quote(sstt_3),
    "X-Apple-I-FD-Client-Info": '{"U":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36","L":"zh-CN","Z":"GMT+08:00","V":"1.1","F":"7la44j1e3NlY5BNlY5BSmHACVZXnNA9ceieFSOTjGUfSHolk2dUJKy_Aw7GY5ey.EKY.6eke4FIdIXxU94ycfxJclY5BNleBBNlYCa1nkBMfs.0VE"}',
    "sec-ch-ua-mobile": "?0",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
    "Content-Type": "application/json",
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "X-Requested-With": "XMLHttpRequest",
    "sec-ch-ua-platform": '"Windows"',
    "Origin": "https://iforgot.apple.com",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Dest": "empty",
    "Referer": "https://iforgot.apple.com/",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
    "Cookie": f"idclient=web; dslang=CN-ZH; site=CHN; geo=CN; ifssp={ifssp}; X-Apple-I-Web-Token={x_apple_i_web_token_5}",
}
json_data = {"recoveryOption": "reset_password"}
response = requests.post(
    "https://iforgot.apple.com/recovery/options",
    cookies=cookies,
    headers=headers,
    json=json_data,
    allow_redirects=False,
)
x_apple_i_web_token_6 = response.cookies.get("X-Apple-I-Web-Token")
sstt_4 = unquote(response.headers["sstt"])


# 显示简略信息
cookies = {
    "idclient": "web",
    "dslang": "CN-ZH",
    "site": "CHN",
    "geo": "CN",
    "ifssp": ifssp,
    "X-Apple-I-Web-Token": x_apple_i_web_token_6,
}

headers = {
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Pragma": "no-cache",
    "Referer": "https://iforgot.apple.com/",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
    "X-Apple-I-FD-Client-Info": '{"U":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36","L":"zh-CN","Z":"GMT+08:00","V":"1.1","F":"Fla44j1e3NlY5BNlY5BSmHACVZXnNA9ceidcKFxZdjpidPNs0oje9zH_y37lYKU.6elV2pNK1c8odlTj_1z1_y53NlY5BNp55BNlan0Os5Apw.3tH"}',
    "X-Requested-With": "XMLHttpRequest",
    "sec-ch-ua": '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
    "sstt": quote(sstt_3),
}

params = {
    "sstt": sstt_4,
}

response = requests.get(
    "https://iforgot.apple.com/password/authenticationmethod",
    params=params,
    cookies=cookies,
    headers=headers,
)
sstt_5 = response.json()["sstt"]
x_apple_i_web_token_7 = response.cookies.get("X-Apple-I-Web-Token")


# 302
cookies = {
    "idclient": "web",
    "dslang": "CN-ZH",
    "site": "CHN",
    "geo": "CN",
    "ifssp": ifssp,
    "X-Apple-I-Web-Token": x_apple_i_web_token_7,
}

headers = {
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Content-Type": "application/json",
    "Origin": "https://iforgot.apple.com",
    "Pragma": "no-cache",
    "Referer": "https://iforgot.apple.com/",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
    "X-Apple-I-FD-Client-Info": '{"U":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36","L":"zh-CN","Z":"GMT+08:00","V":"1.1","F":"Fla44j1e3NlY5BNlY5BSmHACVZXnNA9ceidcK8A1ezLu_dYV6Hycfx9MsFY5Bhw.Tf5.EKWJ9VbHb4uyJAw9MsJY5BNlY5cklY5BqNAE.lTjV.Alj"}',
    "X-Requested-With": "XMLHttpRequest",
    "sec-ch-ua": '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
    "sstt": quote(sstt_5),
}

json_data = {
    "type": "questions",
}

response = requests.post(
    "https://iforgot.apple.com/password/authenticationmethod",
    cookies=cookies,
    headers=headers,
    json=json_data,
    allow_redirects=False,
)
sstt_5 = unquote(response.headers["sstt"])
x_apple_i_web_token_8 = response.cookies.get("X-Apple-I-Web-Token")
# print(sstt_6)
# print(x_apple_i_web_token_8)


# 详细年月日
cookies = {
    "idclient": "web",
    "dslang": "CN-ZH",
    "site": "CHN",
    "geo": "CN",
    "ifssp": ifssp,
    "X-Apple-I-Web-Token": x_apple_i_web_token_8,
}

headers = {
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Pragma": "no-cache",
    "Referer": "https://iforgot.apple.com/",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
    "X-Apple-I-FD-Client-Info": '{"U":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36","L":"zh-CN","Z":"GMT+08:00","V":"1.1","F":"Fla44j1e3NlY5BNlY5BSmHACVZXnNA9ceidcK8A1ezLu_dYV6Hycfx9MsFY5Bhw.Tf5.EKWJ9VbHb4uyJAw9MsJY5BNlY5cklY5BqNAE.lTjV.Alj"}',
    "X-Requested-With": "XMLHttpRequest",
    "sec-ch-ua": '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
    "sstt": quote(sstt_5),
}

params = {
    "sstt": sstt_5,
}

response = requests.get(
    "https://iforgot.apple.com/password/verify/birthday",
    params=params,
    cookies=cookies,
    headers=headers,
)
sstt_6 = response.json()["sstt"]
x_apple_i_web_token_9 = response.cookies.get("X-Apple-I-Web-Token")


# 302
cookies = {
    "idclient": "web",
    "dslang": "CN-ZH",
    "site": "CHN",
    "geo": "CN",
    "ifssp": ifssp,
    "X-Apple-I-Web-Token": x_apple_i_web_token_9,
}

headers = {
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Content-Type": "application/json",
    "Origin": "https://iforgot.apple.com",
    "Pragma": "no-cache",
    "Referer": "https://iforgot.apple.com/",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
    "X-Apple-I-FD-Client-Info": '{"U":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36","L":"zh-CN","Z":"GMT+08:00","V":"1.1","F":"Fla44j1e3NlY5BNlY5BSmHACVZXnNA9ceimZ_JbfqjpidPNs0oje9zH_y37lYKU.6elV2pNK1c8odlTj_.z1OyKFlY5BNleBBNlYCa1nkBMfs.CYV"}',
    "X-Requested-With": "XMLHttpRequest",
    "sec-ch-ua": '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
    "sstt": quote(sstt_6),
}

json_data = {
    "monthOfYear": "05",
    "dayOfMonth": "25",
    "year": "1993",
}

response = requests.post(
    "https://iforgot.apple.com/password/verify/birthday",
    cookies=cookies,
    headers=headers,
    json=json_data,
    allow_redirects=False,
)
sstt_7 = unquote(response.headers["sstt"])
x_apple_i_web_token_10 = response.cookies.get("X-Apple-I-Web-Token")


# 密保判断信息
cookies = {
    "idclient": "web",
    "dslang": "CN-ZH",
    "site": "CHN",
    "geo": "CN",
    "ifssp": ifssp,
    "X-Apple-I-Web-Token": x_apple_i_web_token_10,
}

headers = {
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Pragma": "no-cache",
    "Referer": "https://iforgot.apple.com/",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
    "X-Apple-I-FD-Client-Info": '{"U":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36","L":"zh-CN","Z":"GMT+08:00","V":"1.1","F":"Fla44j1e3NlY5BNlY5BSmHACVZXnNA9ceimZ_JbfqjpidPNs0oje9zH_y37lYKU.6elV2pNK1c8odlTj_.z1OyKFlY5BNleBBNlYCa1nkBMfs.CYV"}',
    "X-Requested-With": "XMLHttpRequest",
    "sec-ch-ua": '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
    "sstt": quote(sstt_6),
}

params = {
    "sstt": sstt_7,
}

response = requests.get(
    "https://iforgot.apple.com/password/verify/questions",
    params=params,
    cookies=cookies,
    headers=headers,
)
sstt_8 = response.json()["sstt"]
x_apple_i_web_token_11 = response.cookies.get("X-Apple-I-Web-Token")

question_1 = response.json()['questions'][0]['question']
question_2 = response.json()['questions'][1]['question']

number_1 = response.json()['questions'][0]['number']
number_2 = response.json()['questions'][1]['number']

id_1 = response.json()['questions'][0]['id']
id_2 = response.json()['questions'][1]['id']



print(response.json())

# 具体填写密保
cookies = {
    "idclient": "web",
    "dslang": "CN-ZH",
    "site": "CHN",
    "geo": "CN",
    "ifssp": ifssp,
    "X-Apple-I-Web-Token": x_apple_i_web_token_11,
}

headers = {
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Content-Type": "application/json",
    "Origin": "https://iforgot.apple.com",
    "Pragma": "no-cache",
    "Referer": "https://iforgot.apple.com/",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
    "X-Apple-I-FD-Client-Info": '{"U":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36","L":"zh-CN","Z":"GMT+08:00","V":"1.1","F":".la44j1e3NlY5BNlY5BSmHACVZXnNA9ceimiYcIqjpidPNs0oje9zH_y37lYIU.6elV2pNK1c8odlTj_.z1Oyd7lY5BNleBBNlYCa1nkBMfs.DEo"}',
    "X-Requested-With": "XMLHttpRequest",
    "sec-ch-ua": '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
    "sstt": quote(sstt_8),
}

json_data = {
    "questions": [
        {
            "question": "你少年时代最好的朋友叫什么名字？",
            "answer": "py1234",
            "number": 1,
            "id": 130,
        },
        {
            "question": "你的理想工作是什么？",
            "answer": "gz1234",
            "number": 2,
            "id": 136,
        },
    ],
}

response = requests.post(
    "https://iforgot.apple.com/password/verify/questions",
    cookies=cookies,
    headers=headers,
    json=json_data,
    allow_redirects=False,
)
sstt_9 = unquote(response.headers["sstt"])
x_apple_i_web_token_12 = response.cookies.get("X-Apple-I-Web-Token")


# 302
cookies = {
    "idclient": "web",
    "dslang": "CN-ZH",
    "site": "CHN",
    "geo": "CN",
    "ifssp": ifssp,
    "X-Apple-I-Web-Token": x_apple_i_web_token_12,
}

headers = {
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Pragma": "no-cache",
    "Referer": "https://iforgot.apple.com/",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
    "X-Apple-I-FD-Client-Info": '{"U":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36","L":"zh-CN","Z":"GMT+08:00","V":"1.1","F":".la44j1e3NlY5BNlY5BSmHACVZXnNA9ceimiYcIqjpidPNs0oje9zH_y37lYIU.6elV2pNK1c8odlTj_.z1Oyd7lY5BNleBBNlYCa1nkBMfs.DEo"}',
    "X-Requested-With": "XMLHttpRequest",
    "sec-ch-ua": '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
    "sstt": quote(sstt_8),
}

params = {
    "sstt": sstt_9,
}

response = requests.get(
    "https://iforgot.apple.com/password/reset/options",
    params=params,
    cookies=cookies,
    headers=headers,
    allow_redirects=False,
)
sstt_10 = unquote(response.headers["sstt"])
x_apple_i_web_token_13 = response.cookies.get("X-Apple-I-Web-Token")


# 两次302之后检测密码是不是能正确
cookies = {
    "idclient": "web",
    "dslang": "CN-ZH",
    "site": "CHN",
    "geo": "CN",
    "ifssp": ifssp,
    "X-Apple-I-Web-Token": x_apple_i_web_token_13,
}

headers = {
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Pragma": "no-cache",
    "Referer": "https://iforgot.apple.com/",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
    "X-Apple-I-FD-Client-Info": '{"U":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36","L":"zh-CN","Z":"GMT+08:00","V":"1.1","F":".la44j1e3NlY5BNlY5BSmHACVZXnNA9ceimiYcIqjpidPNs0oje9zH_y37lYIU.6elV2pNK1c8odlTj_.z1Oyd7lY5BNleBBNlYCa1nkBMfs.DEo"}',
    "X-Requested-With": "XMLHttpRequest",
    "sec-ch-ua": '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
    "sstt": quote(sstt_8),
}

params = {
    "sstt": sstt_10,
}

response = requests.get(
    "https://iforgot.apple.com/password/reset",
    params=params,
    cookies=cookies,
    headers=headers,
)
sstt_11 = response.json()["sstt"]
x_apple_i_web_token_14 = response.cookies.get("X-Apple-I-Web-Token")


# 最后的改密
cookies = {
    "idclient": "web",
    "dslang": "CN-ZH",
    "site": "CHN",
    "geo": "CN",
    "ifssp": ifssp,
    "X-Apple-I-Web-Token": x_apple_i_web_token_14,
}

headers = {
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Content-Type": "application/json",
    "Origin": "https://iforgot.apple.com",
    "Pragma": "no-cache",
    "Referer": "https://iforgot.apple.com/",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
    "X-Apple-I-FD-Client-Info": '{"U":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36","L":"zh-CN","Z":"GMT+08:00","V":"1.1","F":"Fla44j1e3NlY5BNlY5BSmHACVZXnNA9ceimZWApv4jpidPNs0oje9zH_y37lYKU.6elV2pNK1c8odlTj_.z1Oy3clY5BNleBBNlYCa1nkBMfs.4hh"}',
    "X-Requested-With": "XMLHttpRequest",
    "sec-ch-ua": '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
    "sstt": quote(sstt_11),
}

json_data = {
    "password": "Aa1473691",
}

response = requests.post(
    "https://iforgot.apple.com/password/reset",
    cookies=cookies,
    headers=headers,
    json=json_data,
)
print(response.text)

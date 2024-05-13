import json
import re

import requests

url = "https://secure7.store.apple.com/shop/order/guest/W1423032356/3c2cc7f18d5eeca19ac386106e2b1308bec2118befff4f2e381ff3f6b8d24cf4625e5d84a5527f67f85cbc58ff7bc8341062aa5538fe7e8df4764f45103073abaab1c958ee7be616eb18ff6c618d62f1?e=true"

payload={}
headers = {
   'User-Agent': 'Apifox/1.0.0 (https://apifox.com)',
   'Accept': '*/*',
   'Host': 'www.apple.com',
   'Connection': 'keep-alive',
#    'Cookie': 'dssid2=fba12486-0717-470a-a39e-120115db4bc8; dssf=1; as_pcts=KWjMHQLge-HkVf1UTw_gt1k-nybx8mm2:YY0CDA187JC+Qtvk_IiRkICLXBUDydqxs-v0VD1_aPeYGpEKqKNIfvF; as_dc=ucp3',
   'Referer': 'https://www.apple.com/xc/us/vieworder/W1413294852/tlotdxdd@hotmail.com?e=true'
}

response = requests.request("GET", url, headers=headers, data=payload).text

# print(response)


modo = r'"productName"\s*:\s*"([^"]+)"'
time = r'"orderPlacedDate"\s*:\s*"([^"]+)"'
dd = r'/shop/order/detail/\d+/([^"/]+)'
status = r'"deliveryDate"\s*:\s*"([^"]+)"'
pattern = r'"currentStatus"\s*:\s*"([^"]+)"'
MODO = re.search(modo, response)
TIME = re.search(time, response)
DD = re.search(dd, response)
status = re.search(status, response)
modo = MODO.group(1)
TIME = TIME.group(1)
DD = DD.group(1)
status = status.group(1)

match = re.search(pattern, response)

if match:
    current_status = match.group(1)
    print(f'currentStatus 的值是: {current_status}')
else:
    print('没有找到 currentStatus 的值')
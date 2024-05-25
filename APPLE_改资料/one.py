import requests

# ===========================================================================================================================================
name = "my_hero.hero@softbank.ne.jp"
pwd = "Aa147369"
# ===========================================================================================================================================
url = "https://env-00jxgsqva6td.dev-hz.cloudbasefunction.cn/A1?type=1"
payload = {f"email": {name}}
Key = requests.request("POST", url, data=payload).json()
print("1-生成key---", Key)
print("*" * 100)
# =========================================================================================================================================
headers = {"Accept": "application/json, text/javascript, */*; q=0.01"}
json_data = {
    "a": Key["r"],
    "accountName": name,
    "protocols": [
        "s2k",
        "s2k_fo",
    ],
}
response_2 = requests.post(
    "https://idmsa.apple.com/appleauth/auth/signin/init",
    headers=headers,
    json=json_data,
).json()
print("2-获取key---", response_2)
print("*" * 100)
# =========================================================================================================================================
url = "https://env-00jxgsqva6td.dev-hz.cloudbasefunction.cn/A1?type=2"
payload = {
    "email": name,
    "iterations": response_2["iteration"],
    "Value": response_2["b"],
    "salt": response_2["salt"],
    "password": pwd,
    "protocol": response_2["protocol"],
    "privateHexValue": Key["privateHexValue"],
    "publicHexValue": Key["publicHexValue"],
}
response_3 = requests.request("POST", url, json=payload).json()
print("3-加密所有加密参数---", response_3)
print("*" * 100)
# =========================================================================================================================================
headers = {
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "X-Apple-OAuth-Client-Id": "a797929d224abb1cc663bb187bbcd02f7172ca3a84df470380522a7c6092118b",
    "X-Apple-OAuth-Redirect-URI": "https://secure6.store.apple.com",
    "X-Apple-OAuth-Response-Type": "code",
}
json_data = {
    "accountName": name,
    "rememberMe": False,
    "m1": response_3["M1"],
    "c": response_2["c"],
    "m2": response_3["M2"],
}
response_4 = requests.post(
    "https://idmsa.apple.com/appleauth/auth/signin/complete",
    headers=headers,
    json=json_data,
)
print("4-账号状态---", response_4.text)
print("*" * 100)

print("4-账号状态---", response_4.headers)
print("*" * 100)

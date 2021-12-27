import requests
import ssl
import ast



try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    # Legacy Python that doesn't verify HTTPS certificates by default
    pass
else:
    # Handle target environment that doesn't support HTTPS verification
    ssl._create_default_https_context = _create_unverified_https_context


client_id='ncThG4QMy3GwEZ6jThcQCqCmbrHPWr_z8yAdUu5Q6FU%3D'
client_secret='Nqh5FWyOdcd6JoKddgz4nfgkIAeXldFu_LCCVmWcGxA%3D'


#0 - retrieve well known endpoint
# url = "https://api.natwest.useinfinite.io/.well-known/openid-configuration"

# payload = {}
# headers= {}

# response = requests.request("GET", url, headers=headers, data = payload)


# 1- retrieve access token
url = "https://ob.natwest.useinfinite.io/token"

payload = 'grant_type=client_credentials&client_id=' + client_id + '&client_secret=' + client_secret + '&scope=accounts'
headers = {
  'Content-Type': 'application/x-www-form-urlencoded'
}

# response = requests.request("POST", url, headers=headers, data = payload, verify ='/home/dass/Coding/Android/RBSHackathon2/app/src/main/assets/load-der.crt' )
response = requests.request("POST", url, headers=headers, data = payload, verify = False )

print(response.text.encode('utf8'))

jsonResponse = response.json()

tempaccesstoken = ""
#print("Print each key-value pair from JSON response")
for key, value in jsonResponse.items():
    #print(key, ":", value)
    if key == "access_token":
        tempaccesstoken = value

print("1======================")
#2- post account request


url = "https://ob.natwest.useinfinite.io/open-banking/v3.1/aisp/account-access-consents"

payload = "{\n  \"Data\": {\n    \"Permissions\": [\n      \"ReadAccountsDetail\",\n      \"ReadBalances\",\n      \"ReadTransactionsCredits\",\n      \"ReadTransactionsDebits\",\n      \"ReadTransactionsDetail\"\n    ]\n  },\n  \"Risk\": {}\n}"
headers = {
  'Authorization': 'Bearer ' + tempaccesstoken,
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data = payload, verify =False)
print(response.text.encode('utf8'))

jsonResponse = response.json()
ConsentId = ""
for key, value in jsonResponse.items():
    if key == "Data":
      ConsentId = value['ConsentId']
      print("ConsentId", ConsentId)
    

# url = "https://ob.natwest.useinfinite.io/open-banking/v3.1/aisp/account-access-consents"

# payload = "{\n  \"Data\": {\n    \"Permissions\": [\n      \"ReadAccountsDetail\",\n      \"ReadBalances\",\n      \"ReadTransactionsCredits\",\n      \"ReadTransactionsDebits\",\n      \"ReadTransactionsDetail\"\n    ]\n  },\n  \"Risk\": {}\n}"
# headers = {
#   'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJhcHAiOiJkZW1vLWFwcC1jZTllYzJmYS04NTVhLTQ2Y2YtYjVkYy1iMGZkZGY2YTliZTEiLCJvcmciOiJjZTllYzJmYS04NTVhLTQ2Y2YtYjVkYy1iMGZkZGY2YTliZTEuZXhhbXBsZS5vcmciLCJpc3MiOiJuYXR3ZXN0LnVzZWluZmluaXRlLmlvIiwidG9rZW5fdHlwZSI6IkFDQ0VTU19UT0tFTiIsImV4dGVybmFsX2NsaWVudF9pZCI6Im5jVGhHNFFNeTNHd0VaNmpUaGNRQ3FDbWJySFBXcl96OHlBZFV1NVE2RlU9IiwiY2xpZW50X2lkIjoiZjA1NDJmNGItZGFjYi00YmM1LThkMGQtMTJjMDBhODY3N2UyIiwibWF4X2FnZSI6ODY0MDAsImF1ZCI6ImYwNTQyZjRiLWRhY2ItNGJjNS04ZDBkLTEyYzAwYTg2NzdlMiIsInNjb3BlIjoiYWNjb3VudHMiLCJleHAiOjE1OTUyNjE2NDEsImlhdCI6MTU5NTI2MTM0MSwianRpIjoiMTcyOTMyY2MtOGM4MS00YjAwLWJiNGMtMDg0YjAyNmRlM2RiIiwidGVuYW50IjoiTmF0V2VzdCJ9.aWVJIZ2z7JyzcEBoGrNV-OIJbn0f_n2Tj4FHIGel0Qn0Vq0WPNSrhsL6l7otP_CCd5y7RhicdTByY5Pg6jE_NcdmNnvJmGi3aZs2L1LsUP5MTc8eJ1SgjURSHi6dEpqVcMECOCR1E8b5iDrqVMTcGX32MhLpIMk4jjlIrnxMXjSVTgyrIdqr58ufFqG_-GLx-Pj-BLRvaj6R8FsBdpS6bj35yUKhieoIsMSHKRSOwOIE32zheDnh2zlmTZNwQcZH7Xn8ePnaBVySVG9U_MMMTczo_gF4LnMaSAkuds3k20gO5TU-J5g7cCKBQ6nyXNfWCUN08xbr5JPPrUHThhwiPA',
#   'Content-Type': 'application/json'
# }

# response = requests.request("POST", url, headers=headers, data = payload, verify=False)


print("2======================")

print("ConsentId", ConsentId)
# 3 - Approve Consent prog
url = "https://api.natwest.useinfinite.io/authorize?client_id=" + client_id + "&response_type=code id_token&scope=openid accounts&redirect_uri=https%3A%2F%2Fce9ec2fa-855a-46cf-b5dc-b0fddf6a9be1.example.org%2Fredirect&state=ABC&request=" + ConsentId + "&authorization_mode=AUTO_POSTMAN&authorization_username=123456789012@ce9ec2fa-855a-46cf-b5dc-b0fddf6a9be1.example.org"


payload = {}
headers= {}

response = requests.request("GET", url, headers=headers, data = payload, verify =False)

tempsplit = response.text.encode('utf8')

codeid = ""
print(response.text.encode('utf8'))
sp1 = tempsplit.decode().split("code=")
print("sp1[1]", sp1[1])
sp3= sp1[1]
sp2 = sp3.split("&id_token")
codeid = sp2[0]
print("codeid", codeid)
print("3====================")


#4 = exchange code for access token
url = "https://ob.natwest.useinfinite.io/token"

payload = 'client_id=' + client_id + '&client_secret=' + client_secret + '&redirect_uri=https%3A//ce9ec2fa-855a-46cf-b5dc-b0fddf6a9be1.example.org/redirect&grant_type=authorization_code&code=' + codeid 


headers = {
  'Content-Type': 'application/x-www-form-urlencoded'
}


response = requests.request("POST", url, headers=headers, data = payload, verify=False)

accesstoken2 = response.text.encode('utf8')
print("accesstoken2", type(accesstoken2))
dict_str = accesstoken2.decode("UTF-8")
mydata = ast.literal_eval(dict_str)
print("mydata", mydata["access_token"])
accesstoken3 = mydata["access_token"]
print(response.text.encode('utf8'))
print("4====================")

#5 - list accounts
url = "https://ob.natwest.useinfinite.io/open-banking/v3.1/aisp/accounts"

payload = {}
headers = {
  'Authorization': 'Bearer ' + accesstoken3
}

response = requests.request("GET", url, headers=headers, data = payload, verify=False)
jsonResponselistacc = response.json()
listaccount = ""
for key, value in jsonResponselistacc.items():
  print("key", key)
  print("value", value)
  print("value", value["Account"])
  listaccount = value["Account"]
  break
print("listaccount", type(listaccount))
print("listaccount", len(listaccount))
listaccountdata = ""

for i in range(len(listaccount)):
  # print("DDDDD" + str(i) + str(listaccount[i]["AccountId"]))
  listaccountdata = listaccountdata + listaccount[i]["AccountId"] + "<:>" + listaccount[i]["Nickname"] + "<,>"

print("listaccountdata", listaccountdata)
  # for key2, value2 in value.json().items():
  #     print("key2", key2)
  #     print("value2", value2)


print(response.text.encode('utf8'))
print("5====================")

#6 = list transactions
url = "https://ob.natwest.useinfinite.io/open-banking/v3.1/aisp/accounts/09b8a760-3539-4a96-a3d0-61936845a5a5/transactions"

payload = {}
headers = {
  'Authorization': 'Bearer ' + accesstoken3
}

response = requests.request("GET", url, headers=headers, data = payload, verify=False)
jsonResponsetransaction = response.json()
listtrans = ""
for key, value in jsonResponsetransaction.items():
  #print("key", key)
  #print("value", value)
  if key == "Data":
    print("ddddddd", value["Transaction"])
    for i in range(len(value["Transaction"])):
      templisttrans = value["Transaction"][i] 
      #print(type(value["Transaction"][i]))
      #print(templisttrans["CreditDebitIndicator"])
      listtrans = listtrans + str(templisttrans["CreditDebitIndicator"]) + "<:>" + str(templisttrans["Amount"]["Amount"]) + "<:>" + str(templisttrans["Amount"]["Currency"])  + "<:>" + str(templisttrans["Balance"]["Amount"]["Amount"])  + "<:>" + str(templisttrans["Balance"]["Amount"]["Currency"]) + "<,>"
      print(type(templisttrans["Amount"]))


print(listtrans)
#print(response.text.encode('utf8'))
print("6====================")



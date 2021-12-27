import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)



headers = {
    'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJhcHAiOiJWYWx1ZUNyZWF0b3JzQVBJIiwib3JnIjoidmFsdWVjcmVhdG9ycy5vcmciLCJpc3MiOiJuYXR3ZXN0LnVzZWluZmluaXRlLmlvIiwidG9rZW5fdHlwZSI6IkFDQ0VTU19UT0tFTiIsImV4dGVybmFsX2NsaWVudF9pZCI6InJOb0x0cWMyME45RHRZOFlBOXRRNVNDbTdoNTVhRzhHWHZwVXV4bklfNm89IiwiY2xpZW50X2lkIjoiN2UwM2Y0NmYtNjJmOC00MDI3LWJiMGYtNmY3NGU5YmEyZTAwIiwibWF4X2FnZSI6ODY0MDAsImF1ZCI6IjdlMDNmNDZmLTYyZjgtNDAyNy1iYjBmLTZmNzRlOWJhMmUwMCIsInVzZXJfaWQiOiIxMjM0NTY3ODkwMTJAdmFsdWVjcmVhdG9ycy5vcmciLCJncmFudF9pZCI6ImUzNmI5NjlkLTlmYmEtNDMyZC1iYjFhLTMxOWM2NDg1YWY0OSIsInNjb3BlIjoiYWNjb3VudHMgb3BlbmlkIiwiY29uc2VudF9yZWZlcmVuY2UiOiI3YWM2YzUyMC04M2I1LTQxM2MtYWI4Ny1iMzk0ZGUyOTJlNTUiLCJleHAiOjE1OTQ5MTc0MTAsImlhdCI6MTU5NDkxNzExMCwianRpIjoiY2FmMmM3ZmEtNGI2NS00YTYzLWI2YjUtOTgxMGJhNmQ1NDFhIiwidGVuYW50IjoiTmF0V2VzdCJ9.RwGYSxw8ndUanTnFAHILvbduCfeX0bDKq45hD3owrpgiCcnDasPysEeigXEWqjiWCuIV69FL00wUdlLV7E1Z2dEUcYh156TrJ8EP_V7JO8aIr7ZcpFkjDfAPVb9SMmIQVdl0dWVoPzprjvedWPuRp-sKxlX0JaMH2IqKH6fyWDReuRUJOPSjpL0vwoPQ8KGz1MmvqGwsuGYmHUtMnAzjzwfONBf4FBEk_2Q5_HPnd5y9DQV9fqdjtD48jpwZK44YQHKj1iJ8VAx0pbma6pftOqTfNyfxpcjZYK0mwLqIXvNB6uynocgHVmXNGqcEYsZNQwsd_sk5jvACee7JE1gjJw',
    'x-fapi-financial-id': '0015800000jfwxXAAQ',
}

response = requests.get('https://ob.natwest.useinfinite.io/open-banking/v3.1/aisp/accounts', headers=headers, verify=False)


# headers = {
#     'Content-Type': 'application/x-www-form-urlencoded',
# }

# data = {
#   'grant_type': 'client_credentials',
#   'client_id': 'ncThG4QMy3GwEZ6jThcQCqCmbrHPWr_z8yAdUu5Q6FU=',
#   'client_secret': 'Nqh5FWyOdcd6JoKddgz4nfgkIAeXldFu_LCCVmWcGxA=',
#   'scope': 'accounts'
# }

# response = requests.post('https://ob.natwest.useinfinite.io/token', headers=headers, data=data, verify=False)

print(response.text)

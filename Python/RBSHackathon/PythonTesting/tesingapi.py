import requests

url = "https://ob.natwest.useinfinite.io/token"

payload = 'client_id=ncThG4QMy3GwEZ6jThcQCqCmbrHPWr_z8yAdUu5Q6FU%3D&client_secret=Nqh5FWyOdcd6JoKddgz4nfgkIAeXldFu_LCCVmWcGxA%3D&redirect_uri=https%3A//ce9ec2fa-855a-46cf-b5dc-b0fddf6a9be1.example.org/redirect&grant_type=authorization_code&code=b5a36688-44aa-4109-91a2-c2cde60c6d8d'
headers = {
  'Content-Type': 'application/x-www-form-urlencoded'
}

response = requests.request("POST", url, headers=headers, data = payload, verify=False)

print(response.text.encode('utf8'))

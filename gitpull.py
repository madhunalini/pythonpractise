import requests

response = requests.get("https://api.github.com/repos/kubernetes/kubernetes/pulls")
output = (response.json())
print(output[10]["id"])

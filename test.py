import requests

url = "http://haproxy-stage.pst.sysct.cz:37090/ExternalDataProvider.asmx?WSDL"
response = requests.get(url)
print(response)

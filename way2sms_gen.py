

import requests
import json

URL = 'https://www.way2sms.com/api/v1/sendCampaign'

# get request
def sendPostRequest(reqUrl, apiKey, secretKey, useType, reciever_phoneNo, senderId, textMessage):
  req_params = {
  'apikey':apiKey,
  'secret':secretKey,
  'usetype':useType,
  'phone': reciever_phoneNo,
  'message':textMessage,
  'senderid':senderId
  }
  return requests.post(reqUrl, req_params)

# get response
response = sendPostRequest(URL, 'Q5JW3E4YGD13SRIWRZLBLAQ6K7AR0KKG', 'ZOFKZKY1EUDU1MTN', 'stage', '9326834205', '8655815493', 'Hi I am Vinayak..its done..' )
"""
  Note:-
    you must provide apikey, secretkey, usetype, mobile, senderid and message values
    and then requst to api
"""
# its json dict
print(response.text)
import requests
# wait timeout for a message from client
timeout = 5
GET_MSG_URL = "http://127.0.0.1:5000/getMessage"
POST_MSG_URL = "http://127.0.0.1:5000/postLogs"
r = requests.get(url = GET_MSG_URL, params = {'timeout':timeout})
print ("Camera received message from client: {}".format(r.text))
# log message which client will receive from camera
logs = "log from camera is: " + r.text
p = requests.post(url = POST_MSG_URL, params = {'logs':logs})
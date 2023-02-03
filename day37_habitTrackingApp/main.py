import requests
import password
import datetime
# from password import pixela_token

url_base = "https://pixe.la/v1/users"
username = "testpythongp2"
user_parameters = {"token": password.pixela_token, "username": username, "agreeTermsOfService": "yes", "notMinor": "yes"}

# This part of the code was to be run only once, as running it
# twice will fail because the username would have been taken
# https://docs.pixe.la/entry/post-user
# user_response = requests.post(url = url_base, json = user_parameters)
# user_response.raise_for_status()
# confirmation = user_response.content

# this part of the code is to create a graph. The graph is created only once
# https://docs.pixe.la/entry/post-graph

graph_id = "g01"
graph_name = "graph1"
# graph_parameters ={"id": graph_id, "name": graph_name, "unit": "km", "type": "float", "color": "sora"}
 graph_headers = {"X-USER-TOKEN": password.pixela_token}
# graph_response = requests.post(url = url_base+"/"+username+"/graphs", json = graph_parameters, headers = graph_headers) # headers is one of the **kwargs
# graph_response.raise_for_status()

# This part is to create a pixel
date_text = datetime.datetime.now().date().strftime("%Y%m%d")
quantity = str(8.9)
pixel_parameters = {"date": date_text, "quantity": quantity}
pixel_response = requests.post(url = url_base + "/" + username + "/graphs/" + graph_id, json = pixel_parameters, headers = graph_headers)
pixel_response.raise_for_status()

# This part updates a pixel. Note the use of PUT
update_url = f"{url_base}/{username}/graphs/{graph_id}/{date_text}"

update_response = requests.put(url = update_url, headers = graph_headers, json = {"quantity": str(25.0)})
update_response.raise_for_status()

# this part deletes a pixel. Note the use of DELETE
delete_url = f"{url_base}/{username}/graphs/{graph_id}/{date_text}"

delete_response = requests.delete(url = delete_url, headers = graph_headers)
delete_response.raise_for_status()

## how to get data from telegram bot:
# telegram_response = requests.get(url=f"https://api.telegram.org/bot{telegram_token}/getUpdates").json()
# telegram_response_content = [i["message"]["text"] for i in telegram_response["result"]] # this is a list as long as all the messages the user sent the bot

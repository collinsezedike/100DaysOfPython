import requests

TOKEN = "Pixela API key"
USERNAME = "collinsezedike"

pixela_endpoint = "https://pixe.la/v1/users"

user_parameters = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# TODO 1: Create an account
# response = requests.post(url=pixela_endpoint, json=user_parameters)
# print(response.text)

# TODO 2: Create a graph
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
header = {"X-USER-TOKEN": TOKEN}
graph_id = "graph1"
graph_config = {
    "id": graph_id,
    "name": "Walking Graph",
    "unit": "steps",
    "type": "int",
    "color": "kuro"
}
# response = requests.post(url=graph_endpoint, json=graph_config, headers=header)
# print(response.text)

# TODO 3: Add a pixel to graph
walking_graph_endpoint = f"{graph_endpoint}/{graph_id}"
# pixel_params = {
#     "date": "20220215",
#     "quantity": "10000",
# }
# response = requests.post(url=graph1_endpoint, json=pixel_params, headers=header)
# print(response.text)
# TODO 4: Delete the graph
response = requests.delete(walking_graph_endpoint)

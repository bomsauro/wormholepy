import requests

def check(token):
    response = requests.get(
        "https://price.jup.ag/v4/price?ids={token}".format(token = token.upper()),
    )

    if response.status_code == 200:
        json_response = response.json()
        price = json_response["data"][token.upper()]["price"]
        return price

    return False

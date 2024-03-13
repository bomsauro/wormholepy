import requests

def check(wallet, network):
    networks = {
        "aptos": 22,
        "solana": 1,
        "sui": 21
    }

    response = requests.get(
        "https://prod-flat-files-min.wormhole.com/{wallet}_{network_code}.json".format(wallet = wallet, network_code = networks[network]),
    )

    if response.status_code == 200:
        json_response = response.json()
        allocation = json_response["amount"]
        return allocation / 10**9

    return False

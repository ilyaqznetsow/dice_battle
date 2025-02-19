import requests
import json

USER_ADDRESS = "EQDuVM_M2Cqx0bco0cYlNeW_aa2mvtvLy-UuPJQkzZEVmrmN"


class NFTWorker:
    BASE_URL = "https://tonapi.io/v2/nfts"

    def get_data(self, user_address):
        url = f"{self.BASE_URL}/collections/{user_address}/items?limit=1000&offset=0"
        owner_address = (
            "0:89f356bd10b3c8609187c5abcd7bb1d5840c7f8a88e73debff8e64ffd8f12010"
        )
        try:
            response = requests.get(url)
            data = response.json()["nft_items"]
            for i in range(len(data)):
                if data[i]["owner"]["address"] == owner_address:
                    metadata = data[i]["metadata"]
                    name, description, image_url = (
                        metadata["name"],
                        metadata["description"],
                        metadata["image"],
                    )
                    return name, description, image_url
        except:
            print("Unsupported adress")

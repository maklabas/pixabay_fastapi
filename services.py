import os
import requests



comments = None
likes = None


def connect_pixabay(per_page: int, category: str):
    # secret_key = os.environ.get("pixabay_key")
    secret_key = "23797809-8f26efa984bdf9135a7c4b2b3"
    url = f"https://pixabay.com/api/?key={secret_key}&category={category}&p={per_page}&image_type=photo"
    return requests.get(url).json()


if __name__ == "__main__":
    print(connect_pixabay(5, "flowers"))

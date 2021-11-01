import os
import requests


def connect_pixabay(per_page: int, category: str):
    secret_key = os.environ.get("pixabay_key")
    url = f"https://pixabay.com/api/?key={secret_key}&category={category}&per_page={per_page}&image_type=photo"
    return requests.get(url).json()


if __name__ == "__main__":
    # Check
    print(connect_pixabay(5, "flowers"))

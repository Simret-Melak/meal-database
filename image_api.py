import requests


def fetch_mars_images(page_num=1):
    response = requests.get("https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?sol=1000&api_key=DEMO_KEY&page=" + str(page_num))
    return response.json()["photos"]


if __name__ == "__main__":
    print(fetch_mars_images())


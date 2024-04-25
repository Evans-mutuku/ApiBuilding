import random

import requests


def make_api_request(url, headers=None, params=None):
    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()  # Raise an exception for HTTP errors
        return response.json()
    except requests.exceptions.RequestException as e:
        print("Error:", e)
        return None


def generate_text():
    response = make_api_request("https://uselessfacts.jsph.pl/random.json?language=en")
    if response:
        fact = response["text"]
        return fact


def generate_images():
    response = make_api_request("https://dog.ceo/api/breeds/image/random")
    if response:
        dog = response["message"]
        return dog


def generate_students():
    response = make_api_request("https://freetestapi.com/api/v1/students")
    if response:
        names = [student["name"] for student in response]
        random.shuffle(names)
        return names[0]  # Return a random shuffled name


def get_jokes():
    response = make_api_request("https://meme-api.com/gimme/2")
    if response:
        memes = response.get("memes", [])
        jokes = [meme["url"] for meme in memes]
        return jokes if jokes else None
    else:
        print("Failed to fetch jokes")
        return None

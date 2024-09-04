#!/usr/bin/node
import requests
import sys


def get_movie_characters(movie_id):
    # Base URL for the SWAPI films endpoint
    films_url = f'https://swapi.dev/api/films/{movie_id}/'

    try:
        # Request movie data
        response = requests.get(films_url)
        response.raise_for_status()  # Raise an error for bad responses

        # Parse the movie data
        movie_data = response.json()

        # Fetch and print character names
        character_urls = movie_data.get('characters', [])
        for character_url in character_urls:
            character_response = requests.get(character_url)
            character_response.raise_for_status()
            character_data = character_response.json()
            print(character_data['name'])

    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.RequestException as err:
        print(f"Error occurred: {err}")

if __name__ == "__main__":
    # Check if a Movie ID was provided as an argument
    if len(sys.argv) != 2:
        print("Usage: python script_name.py <Movie ID>")
    else:
        movie_id = sys.argv[1]
        get_movie_characters(movie_id)

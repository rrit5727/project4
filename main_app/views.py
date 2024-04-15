from bs4 import BeautifulSoup
import requests

from django.shortcuts import render
from .models import Artist, Song

# Create your views here.
def home(request):
    return render(request, 'home.html')



# def about(request):
    # return render(request, 'about.html')



url = 'https://www.businessinsider.com/top-songs-this-year-ranked-best-tracks-2023-12'

def generate(request):
    # Send a GET request to the URL
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Print the HTML content of the website
        soup = BeautifulSoup(response.content, 'lxml')
        
        scraped_songs = []
        song_details = soup.find_all('h2')
        for song in song_details:
            scraped_songs.append(song.text)

        scraped_song_dict = {}
        for scraped_song in scraped_songs:
            cleaned_song = scraped_song.split('. ', 1)[1].replace('"','').strip()
            parts = cleaned_song.split(' by ')
            scraped_song_name = parts[0]
            scraped_artist = parts[1]
            scraped_song_dict[scraped_artist.strip()] = scraped_song_name.strip()
            # print(song_dict)

            # print(songs)

        for scraped_artist_name, scraped_songs in scraped_song_dict.items():
            artist, _ = Artist.objects.get_or_create(artist_name=scraped_artist_name)
            for scraped_song_name in scraped_songs:
                song, created = Song.objects.get_or_create(song_name=scraped_song_name, artist_name=scraped_artist_name)
                if not created:
                    song.occurence += 1
                    song.save()

    else:
        # Print an error message if the request was not successful
        print(f"Failed to retrieve HTML: {response.status_code}")

    songs = Song.objects.all()
    artists = Artist.objects.all()

    return render(request, 'results,html', {'songs':songs, 'artists':artists})
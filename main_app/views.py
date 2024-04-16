from bs4 import BeautifulSoup
import requests

from django.shortcuts import render
from django.http import HttpResponse
from .models import Artist, Song

# Create your views here.
def home(request):
    return render(request, 'home.html')



# def about(request):
    # return render(request, 'about.html')


def scrape_songs(url):
    # Send a GET request to the URL
    response = requests.get(url, verify=False)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Print the HTML content of the website
        soup = BeautifulSoup(response.content, 'lxml')

        scraped_songs = []
        song_details = soup.find_all('h2')
        for song in song_details:
            scraped_songs.append(song.text)

        # print (scraped_songs)
        return scraped_songs

    else:
        # Print an error message if the request was not successful
        print(f"Failed to retrieve HTML: {response.status_code}")


def tidy_nme(scraped_songs):
    scraped_song_dict = {}
    for scraped_song in scraped_songs:
        cleaned_song = scraped_song.split('. ', 1)[1].replace('\'','').strip()
        parts = cleaned_song.split(' – ')
        scraped_song_name = parts[1]
        scraped_artist = parts[0]
        scraped_song_dict[scraped_artist.strip()] = scraped_song_name.strip()
    print(scraped_song_dict)
    return scraped_song_dict

def generate(request):
    url = 'https://www.nme.com/en_au/features/music-features/best-songs-of-2023-3-3552893'

    scraped_songs_list = scrape_songs(url)
    if scraped_songs_list is None:
        return HttpResponse("failed to scrape songs")
    
    scraped_song_dict = tidy_nme(scraped_songs_list)

    for scraped_artist_name, scraped_song in scraped_song_dict.items():
            print(scraped_artist_name)
            artist, _ = Artist.objects.get_or_create(artist_name=scraped_artist_name)
            
            song, created = Song.objects.get_or_create(song_name=scraped_song, artist=artist)
            if not created:
                song.occurence += 1
                song.save()

    songs = Song.objects.all()
    artists = Artist.objects.all()

    return render(request, 'results.html', {'songs':songs, 'artists':artists})



# def generate_original(request):
#     # Send a GET request to the URL
#     response = requests.get(url, verify=False)

#     # Check if the request was successful (status code 200)
#     if response.status_code == 200:
#         # Print the HTML content of the website
#         soup = BeautifulSoup(response.content, 'lxml')
        
#         scraped_songs = []
#         song_details = soup.find_all('h2')
#         for song in song_details:
#             scraped_songs.append(song.text)

#         scraped_song_dict = {}
#         for scraped_song in scraped_songs:
#             cleaned_song = scraped_song.split('. ', 1)[1].replace('"','').strip()
#             parts = cleaned_song.split(' by ')
#             scraped_song_name = parts[0]
#             scraped_artist = parts[1]
#             scraped_song_dict[scraped_artist.strip()] = scraped_song_name.strip()
#             # print(song_dict)

#             # print(songs)

#         for scraped_artist_name, scraped_songs in scraped_song_dict.items():
#             artist, _ = Artist.objects.get_or_create(artist_name=scraped_artist_name)
#             for scraped_song_name in scraped_songs:
#                 song, created = Song.objects.get_or_create(song_name=scraped_song_name, artist=artist)
#                 if not created:
#                     song.occurence += 1
#                     song.save()

#     else:
#         # Print an error message if the request was not successful
#         print(f"Failed to retrieve HTML: {response.status_code}")

#     songs = Song.objects.all()
#     artists = Artist.objects.all()

#     print(generate(request))
#     return render(request, 'results.html', {'songs':songs, 'artists':artists})
    
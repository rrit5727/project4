from bs4 import BeautifulSoup
import requests
import re

from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Artist, Song
from .fetch_genre import *
from main_app.playlist import *

# Create your views here.
def home(request):
    return render(request, 'home.html')



# def about(request):
    # return render(request, 'about.html')


parent_genres = [
    'hiphop',
    'hip hop',
    'pop',
    'rock',
    'grunge',
    'indie',
    'r&b',
    'afro',
    'rap',
    'folk',
    'punk',
    'emo',
    'dance',
    'jazz',
    'drill',
    ]

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



def remove_duplicates(scraped_song_name, scraped_artist):
    if 'liar' in scraped_song_name.lower():
        scraped_song_name = 'boys a liar'
        scraped_artist = 'pinkpantheress & ice spice'
        
    elif 'bluebeard' in scraped_song_name.lower():
        scraped_song_name = 'Eve, Psyche & the Bluebeard\'s Wife'
        scraped_artist = 'le sserafim'
        
    elif 'just ken' in scraped_song_name.lower():
        scraped_song_name = 'Im Just Ken'
        scraped_artist = 'ryan gosling'
        
    elif 'sprinter' in scraped_song_name.lower():
        scraped_song_name = 'sprinter'
        scraped_artist = 'Dave & Central Cee'
        
    elif 'pound town' in scraped_song_name.lower():
        scraped_song_name = 'pound town'
        scraped_artist = 'sexy redd'
        
    elif 'on my mama' in scraped_song_name.lower():
        scraped_song_name = 'on my mama'
        scraped_artist = 'victoria monet'
        
    elif 'eva' in scraped_song_name.lower():
        scraped_song_name = '4eva'
        scraped_artist = 'kaytramine'
        
    elif 'hillbillies' in scraped_song_name.lower():
        scraped_song_name = 'the hillbillies'
        scraped_artist = 'baby keem & kendrick lamar'
        
    elif 'knockin' in scraped_song_name.lower():
        scraped_song_name = 'knockin'
        scraped_artist = 'mj lenderman'
        
    elif 'fly girl' in scraped_song_name.lower():
        scraped_song_name = 'fly girl'
        scraped_artist = 'flo'
        
    elif 'what it is' in scraped_song_name.lower():
        scraped_song_name = 'what it is'
        scraped_artist = 'doechii'
        
    elif 'california sober' in scraped_song_name.lower():
        scraped_song_name = 'california sober'
        scraped_artist = 'billy strings'
        
    elif 'welcome to my island' in scraped_song_name.lower():
        scraped_song_name = 'welcome to my island'
        scraped_artist = 'caroline polachek'             
    else:
        pass
    
    # Return the modified scraped song name and artist
    return scraped_song_name, scraped_artist 


# Clean up scraped songs for each publications's list:
def tidy_nme(scraped_songs):
    scraped_song_dict = {}
    for scraped_song in scraped_songs:
        cleaned_song = scraped_song.split('. ', 1)[1].replace('’','').replace('‘','').strip().lower()
        parts = cleaned_song.split(' – ')
        scraped_song_name = parts[1]
        scraped_artist = parts[0]
        scraped_song_name, scraped_artist = remove_duplicates(scraped_song_name, scraped_artist)
        scraped_song_dict[scraped_artist.strip()] = scraped_song_name.strip()
    # print(scraped_song_dict)
    return scraped_song_dict


def tidy_consequence(scraped_songs):
    scraped_song_dict = {}     
    for i, scraped_song in enumerate(scraped_songs):
        # print(F"Iteration {i}: {scraped_song}")
        if not scraped_song.strip():
            continue
        elif i == 166:
            cleaned_song = scraped_song.split('.', 1)[1].replace('”', '').replace('“', '').replace('"', '').strip().lower()
        elif i >= 201:
            break
        else:
            cleaned_song = scraped_song.split('. ', 1)[1].replace('”', '').replace('“', '').replace('"', '').strip().lower()
            print(cleaned_song)
            parts = cleaned_song.split(' — ')
            scraped_song_name = parts[1]
            scraped_artist = parts[0]
            
            scraped_song_name, scraped_artist = remove_duplicates(scraped_song_name, scraped_artist)
            scraped_song_dict[scraped_artist.strip()] = scraped_song_name.strip()
        
    # print(scraped_song_dict)
    return scraped_song_dict


def tidy_pitchfork(scraped_songs):
    scraped_song_dict = {}
    for scraped_song in scraped_songs:
        cleaned_song = scraped_song.replace('”', '').replace('“', '').replace('"', '').strip().lower()
        parts = cleaned_song.split(': ')
        scraped_song_name = parts[1]
        scraped_artist = parts[0]
        scraped_song_name, scraped_artist = remove_duplicates(scraped_song_name, scraped_artist)
        scraped_song_dict[scraped_artist.strip()] = scraped_song_name.strip()
    # print(scraped_song_dict)
    return scraped_song_dict


def tidy_variety(scraped_songs):
    scraped_song_dict = {}
    for i, scraped_song in enumerate(scraped_songs):
        print(F"Iteration {i}: {scraped_song}")
        if i >= 65:
            break
        else:
            cleaned_song = scraped_song.replace('\'','').strip().lower()
            parts = cleaned_song.split(', ')
            scraped_song_name = parts[1]
            scraped_artist = parts[0]
            scraped_song_name, scraped_artist = remove_duplicates(scraped_song_name, scraped_artist)
            scraped_song_dict[scraped_artist.strip()] = scraped_song_name.strip()
    # print(scraped_song_dict)
    return scraped_song_dict


def tidy_billboard(scraped_songs):
    scraped_song_dict = {}
    for i, scraped_song in enumerate(scraped_songs):    
        print(F"Iteration {i}: {scraped_song}")
        if i >= 100:
            break
        else: 
            cleaned_song = scraped_song.replace('”', '').replace('“', '').replace('"', '').strip().lower()
            parts = cleaned_song.split(', ')
            scraped_song_name = parts[1]
            scraped_artist = parts[0]
            scraped_song_name, scraped_artist = remove_duplicates(scraped_song_name, scraped_artist)
            scraped_song_dict[scraped_artist.strip()] = scraped_song_name.strip()
    # print(scraped_song_dict)
    return scraped_song_dict


def tidy_bbc(scraped_songs):
    scraped_song_dict = {}
    for i, scraped_song in enumerate(scraped_songs):
        
        cleaned_song = scraped_song.split('. ', 1)[1].replace('\'','').strip().lower()
        parts = cleaned_song.split(' – ')
        scraped_song_name = parts[1]
        scraped_artist = parts[0]
        scraped_song_name, scraped_artist = remove_duplicates(scraped_song_name, scraped_artist)
        scraped_song_dict[scraped_artist.strip()] = scraped_song_name.strip()
    # print(scraped_song_dict)
    return scraped_song_dict


def tidy_blahdian(scraped_songs):
    scraped_song_dict = {}
    for i, scraped_song in enumerate(scraped_songs):
        print(f"Iteration {i}: {scraped_song}")
        if re.match(r'^\d+\n', scraped_song):
            continue
        elif i >= 38:
            break
        else:
            cleaned_song = scraped_song.strip().lower()
            parts = re.split(r'^(\d+)\s+', cleaned_song, maxsplit=1)
            if len(parts) == 2:
                scraped_song_name = parts[1]
                scraped_artist = parts[0]
                scraped_song_name, scraped_artist = remove_duplicates(scraped_song_name, scraped_artist)
                scraped_song_dict[scraped_artist.strip()] = scraped_song_name.strip()
    # print(scraped_song_dict)
    return scraped_song_dict


def tidy_esquire(scraped_songs):
    scraped_song_dict = {}
    for i, scraped_song in enumerate(scraped_songs):
        print(f"Iteration {i}: {scraped_song}")
        if i >= 20:
            break
        else: 
            cleaned_song = scraped_song.replace('”', '').replace('“', '').replace('"', '').strip().lower()
            parts = cleaned_song.split(', ')
            scraped_song_name = parts[1]
            scraped_artist = parts[0]
            scraped_song_name, scraped_artist = remove_duplicates(scraped_song_name, scraped_artist)
            scraped_song_dict[scraped_artist.strip()] = scraped_song_name.strip()
    # print(scraped_song_dict)
    return scraped_song_dict


def tidy_slant(scraped_songs):
    scraped_song_dict = {}
    for i, scraped_song in enumerate(scraped_songs):
        
        cleaned_song = scraped_song.split('. ', 1)[1].replace('”', '').replace('“', '').replace('"', '').strip().lower()
        parts = cleaned_song.split(', ')
        scraped_song_name = parts[1]
        scraped_artist = parts[0]
        scraped_song_name, scraped_artist = remove_duplicates(scraped_song_name, scraped_artist)
        scraped_song_dict[scraped_artist.strip()] = scraped_song_name.strip()
    # print(scraped_song_dict)
    return scraped_song_dict


def tidy_uproxx(scraped_songs):
    scraped_song_dict = {}
    for i, scraped_song in enumerate(scraped_songs):
        
        cleaned_song = scraped_song.replace('”', '').replace('“', '').replace('"', '').strip().lower()
        parts = re.split(r'\s*[—–]\s*', cleaned_song, maxsplit=1)
        if len(parts) == 2:
            scraped_artist, scraped_song_name = parts
            scraped_song_name, scraped_artist = remove_duplicates(scraped_song_name, scraped_artist)
            scraped_song_dict[scraped_artist.strip()] = scraped_song_name.strip()
        else: 
            print(f"Error splitting song: {cleaned_song}")
    # print(scraped_song_dict)
    return scraped_song_dict

def tidy_time(scraped_songs):
    scraped_song_dict = {}
    for i, scraped_song in enumerate(scraped_songs):
        
        if i >= 10:
            break
        else: 
            cleaned_song = scraped_song.split('. ', 1)[1].replace('”', '').replace('“', '').replace('"', '').strip().lower()
            parts = cleaned_song.split(', ')
            scraped_song_name = parts[1]
            scraped_artist = parts[0]
            scraped_song_name, scraped_artist = remove_duplicates(scraped_song_name, scraped_artist)
            scraped_song_dict[scraped_artist.strip()] = scraped_song_name.strip()
    # print(scraped_song_dict)
    return scraped_song_dict


def tidy_gq(scraped_songs):
    scraped_song_dict = {}
    for i, scraped_song in enumerate(scraped_songs):
        # 
        cleaned_song = scraped_song.replace('”', '').replace('“', '').replace('"', '').strip().lower()
        parts = re.split(r'\s*[—-]\s*', cleaned_song, maxsplit=1)
        if len(parts) == 2:
            scraped_artist, scraped_song_name = parts
            scraped_song_name, scraped_artist = remove_duplicates(scraped_song_name, scraped_artist)
            scraped_song_dict[scraped_song_name.strip()] = scraped_artist.strip()
        else: 
            print(f"Error splitting song: {cleaned_song}")
    # print(scraped_song_dict)
    return scraped_song_dict


def tidy_harper(scraped_songs):
    scraped_song_dict = {}
    for i, scraped_song in enumerate(scraped_songs):
        # 
        if i >= 20:
            break
        else: 
            cleaned_song = scraped_song.replace('”', '').replace('“', '').replace('"', '').strip().lower()
            parts = cleaned_song.split(' by ')
            scraped_song_name = parts[0]
            scraped_artist = parts[1]
            scraped_song_name, scraped_artist = remove_duplicates(scraped_song_name, scraped_artist)
            scraped_song_dict[scraped_artist.strip()] = scraped_song_name.strip()
    # print(scraped_song_dict)
    return scraped_song_dict


def tidy_treble(scraped_songs):
    scraped_song_dict = {}
    for i, scraped_song in enumerate(scraped_songs):
        # 
        cleaned_song = scraped_song.split('. ', 1)[1].replace('”', '').replace('“', '').replace('"', '').strip().lower()
        parts = cleaned_song.split(' – ')
        scraped_song_name = parts[1]
        scraped_artist = parts[0]
        scraped_song_name, scraped_artist = remove_duplicates(scraped_song_name, scraped_artist)
        scraped_song_dict[scraped_artist.strip()] = scraped_song_name.strip()
    # print(scraped_song_dict)
    return scraped_song_dict



def genre_classifier(genre_added_to_scraped_artist):
    parent_genres = [
    'hiphop',
    'hip hop',
    'pop',
    'rock',
    'grunge',
    'indie',
    'r&b',
    'afro',
    'rap',
    'folk',
    'punk',
    'emo',
    'dance',
    'jazz',
    'drill',
    ]
    
    for parent_genre in parent_genres:
        if parent_genre in genre_added_to_scraped_artist:
            genre_added_to_scraped_artist = parent_genre
            return parent_genre
        else: 
            pass


def retrieve_genre_for_scraped_song(scraped_artist_name):
    result = search_for_artist(token, scraped_artist_name)
    genre = result["genres"][0]  if result and result["genres"] else "other"
    return genre


def generate(request):
    urls = [
    'https://www.nme.com/en_au/features/music-features/best-songs-of-2023-3-3552893',
    # 'https://consequence.net/2023/12/200-best-songs-of-2023-list/22/',
    # 'https://pitchfork.com/features/lists-and-guides/best-songs-2023/',
    # 'https://variety.com/lists/the-best-songs-of-2023/', 
    # 'https://www.billboard.com/lists/best-songs-2023/',
    # 'https://www.esquire.com/entertainment/music/g45778643/best-new-songs-2023/',
    # 'https://www.slantmagazine.com/lists/the-50-best-songs-of-2023/',
    # 'https://uproxx.com/music/best-songs-2023-list/',
    # 'https://time.com/6340132/best-songs-2023/',
    # 'https://www.gq-magazine.co.uk/culture/article/best-songs-2023',
    # 'https://www.harpersbazaar.com/culture/art-books-music/g42862748/best-songs-2023/',
    # 'https://www.treblezine.com/the-100-best-songs-of-2023/',
    
]

    for url in urls:
        scraped_songs_list = scrape_songs(url)
        if scraped_songs_list is None:
            return HttpResponse("failed to scrape songs")
        

        if 'nme.' in url:
            scraped_song_dict = tidy_nme(scraped_songs_list)
        elif 'consequence' in url:
            scraped_song_dict = tidy_consequence(scraped_songs_list)
        elif 'pitchfork' in url:
            scraped_song_dict = tidy_pitchfork(scraped_songs_list)
        elif 'variety' in url:
            scraped_song_dict = tidy_variety(scraped_songs_list)
        elif 'billboard' in url:
            scraped_song_dict = tidy_billboard(scraped_songs_list)
        elif 'bbc' in url:
            scraped_song_dict = tidy_bbc(scraped_songs_list)
        elif 'guardian' in url:
            scraped_song_dict = tidy_blahdian(scraped_songs_list)
        elif 'esquire' in url:
            scraped_song_dict = tidy_esquire(scraped_songs_list)
        elif 'slant' in url:
            scraped_song_dict = tidy_slant(scraped_songs_list)
        elif 'uproxx' in url:
            scraped_song_dict = tidy_uproxx(scraped_songs_list)
        elif 'time' in url:
            scraped_song_dict = tidy_time(scraped_songs_list)
        elif 'gq' in url:
            scraped_song_dict = tidy_gq(scraped_songs_list)
        elif 'harper' in url:
            scraped_song_dict = tidy_harper(scraped_songs_list)
        elif 'treble' in url:
            scraped_song_dict = tidy_treble(scraped_songs_list)
        
        
        


        # scraped_songs_list = scrape_songs(url)
        # if scraped_songs_list is None:
        #     return HttpResponse("failed to scrape songs")
        
        # scraped_song_dict = tidy_nme(scraped_songs_list)

        counter = 0
        for scraped_artist_name, scraped_song in scraped_song_dict.items():
                artist, _ = Artist.objects.get_or_create(artist_name=scraped_artist_name)                
                song, created = Song.objects.get_or_create(song_name=scraped_song, artist=artist)
                if not created:
                    song.occurence += 1
                    song.save()

                # artist.genre = retrieve_genre_for_scraped_song(scraped_artist_name)
                # artist.save()

                genre = retrieve_genre_for_scraped_song(scraped_artist_name)
                print(f"genre: {genre}")
                overwritten_genre = genre_classifier(genre)
                print(f"overwritten_genre: {overwritten_genre}")
                if overwritten_genre: 
                    artist.genre = overwritten_genre
                    artist.save()
                else: 
                    print(f"No genre found for artist: {scraped_artist_name}")

                counter += 1
                if counter >= 60:
                    break
        
    
    
    songs = Song.objects.order_by('-occurence')
    
    
    context = {
        'songs':songs, 
        'genres':parent_genres,
    }

    return render(request, 'results.html', context)
    

def filter_results(request):
    selected_genre = request.POST.get('genre')
    songs = Song.objects.filter(artist__genre=selected_genre).order_by('-occurence')   
    genre =  selected_genre

    return render(request, 'filtered_results.html', {'songs':songs, 'genre':genre})
    
def generate_playlist(request):
    spotify_id = request.POST.get('spotify_id')
    playlist_name = request.POST.get('playlist_name')
    playlist_length  = request.POST.get('playlist_length')
    if playlist_length is not None: 
        try:
            playlist_length = int(playlist_length)
        except ValueError:
            playlist_length = 10
    else:
        playlist_length = 10
    

    genre = request.POST.get('genre')

    if genre:
        selected_songs = Song.objects.filter(artist__genre=genre).order_by('-occurence')[:playlist_length]
        songs = Song.objects.filter(artist__genre=genre).order_by('-occurence')
    else:
        selected_songs = Song.objects.order_by('-occurence')[:playlist_length]        
        songs = Song.objects.order_by('-occurence')        

    fetch_playlist(spotify_id, selected_songs, playlist_name)

    context = {
        'songs':songs, 
        'genres':parent_genres,
    }

    return render(request, 'results.html', context)
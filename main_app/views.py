from bs4 import BeautifulSoup
import requests
import re

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

        print (scraped_songs)        
        return scraped_songs

    else:
        # Print an error message if the request was not successful
        print(f"Failed to retrieve HTML: {response.status_code}")


# Clean up scraped songs for each publications's list:
# def tidy_nme(scraped_songs):
#     scraped_song_dict = {}
#     for scraped_song in scraped_songs:
#         cleaned_song = scraped_song.split('. ', 1)[1].replace('\'','').strip()
#         parts = cleaned_song.split(' – ')
#         scraped_song_name = parts[1]
#         scraped_artist = parts[0]
#         scraped_song_dict[scraped_artist.strip()] = scraped_song_name.strip()
#     print(scraped_song_dict)
#     return scraped_song_dict


# def tidy_consequence(scraped_songs):
#     scraped_song_dict = {}     
#     for i, scraped_song in enumerate(scraped_songs):
#         print(F"Iteration {i}: {scraped_song}")
#         if not scraped_song.strip():
#             continue
#         elif i == 166:
#             cleaned_song = scraped_song.split('.', 1)[1].replace('"','').strip()
#         elif i >= 201:
#             break
#         else:
#             cleaned_song = scraped_song.split('. ', 1)[1].replace('"','').strip()
#             parts = cleaned_song.split(' — ')
#             scraped_song_name = parts[1]
#             scraped_artist = parts[0]
#             scraped_song_dict[scraped_artist.strip()] = scraped_song_name.strip()
        
#     # print(scraped_song_dict)
#     return scraped_song_dict


# def tidy_pitchfork(scraped_songs):
#     scraped_song_dict = {}
#     for scraped_song in scraped_songs:
#         cleaned_song = scraped_song.replace('"','').strip()
#         parts = cleaned_song.split(': ')
#         scraped_song_name = parts[1]
#         scraped_artist = parts[0]
#         scraped_song_dict[scraped_artist.strip()] = scraped_song_name.strip()
#     print(scraped_song_dict)
#     return scraped_song_dict


# def tidy_variety(scraped_songs):
#     scraped_song_dict = {}
#     for i, scraped_song in enumerate(scraped_songs):
#         print(F"Iteration {i}: {scraped_song}")
#         if i >= 65:
#             break
#         else:
#             cleaned_song = scraped_song.replace('\'','').strip()
#             parts = cleaned_song.split(', ')
#             scraped_song_name = parts[1]
#             scraped_artist = parts[0]
#             scraped_song_dict[scraped_artist.strip()] = scraped_song_name.strip()
#     print(scraped_song_dict)
#     return scraped_song_dict


# def tidy_billboard(scraped_songs):
#     scraped_song_dict = {}
#     for i, scraped_song in enumerate(scraped_songs):    
#         print(F"Iteration {i}: {scraped_song}")
#         if i >= 100:
#             break
#         else: 
#             cleaned_song = scraped_song.replace('"','').strip()
#             parts = cleaned_song.split(', ')
#             scraped_song_name = parts[1]
#             scraped_artist = parts[0]
#             scraped_song_dict[scraped_artist.strip()] = scraped_song_name.strip()
#     print(scraped_song_dict)
#     return scraped_song_dict


# def tidy_bbc(scraped_songs):
#     scraped_song_dict = {}
#     for i, scraped_song in enumerate(scraped_songs):
#         print(f"Iteration: {i}, {scraped_song}")
#         cleaned_song = scraped_song.split('. ', 1)[1].replace('\'','').strip()
#         parts = cleaned_song.split(' – ')
#         scraped_song_name = parts[1]
#         scraped_artist = parts[0]
#         scraped_song_dict[scraped_artist.strip()] = scraped_song_name.strip()
#     print(scraped_song_dict)
#     return scraped_song_dict


# def tidy_blahdian(scraped_songs):
#     scraped_song_dict = {}
#     for i, scraped_song in enumerate(scraped_songs):
#         print(f"Iteration {i}: {scraped_song}")
#         if re.match(r'^\d+\n', scraped_song):
#             continue
#         elif i >= 38:
#             break
#         else:
#             cleaned_song = scraped_song.strip()
#             parts = re.split(r'^(\d+)\s+', cleaned_song, maxsplit=1)
#             if len(parts) == 2:
#                 scraped_song_name = parts[1]
#                 scraped_artist = parts[0]
#                 scraped_song_dict[scraped_artist.strip()] = scraped_song_name.strip()
#     print(scraped_song_dict)
#     return scraped_song_dict


# def tidy_esquire(scraped_songs):
#     scraped_song_dict = {}
#     for i, scraped_song in enumerate(scraped_songs):
#         print(f"Iteration {i}: {scraped_song}")
#         if i >= 20:
#             break
#         else: 
#             cleaned_song = scraped_song.replace('"','').strip()
#             parts = cleaned_song.split(', ')
#             scraped_song_name = parts[1]
#             scraped_artist = parts[0]
#             scraped_song_dict[scraped_artist.strip()] = scraped_song_name.strip()
#     print(scraped_song_dict)
#     return scraped_song_dict


# def tidy_slant(scraped_songs):
#     scraped_song_dict = {}
#     for i, scraped_song in enumerate(scraped_songs):
#         print(f"Iteration: {i}, {scraped_song}")
#         cleaned_song = scraped_song.split('. ', 1)[1].replace('"','').strip()
#         parts = cleaned_song.split(', ')
#         scraped_song_name = parts[1]
#         scraped_artist = parts[0]
#         scraped_song_dict[scraped_artist.strip()] = scraped_song_name.strip()
#     print(scraped_song_dict)
#     return scraped_song_dict


# def tidy_uproxx(scraped_songs):
#     scraped_song_dict = {}
#     for i, scraped_song in enumerate(scraped_songs):
#         print(f"Iteration: {i}, {scraped_song}")
#         cleaned_song = scraped_song.replace('"','').strip()
#         parts = re.split(r'\s*[—–]\s*', cleaned_song, maxsplit=1)
#         if len(parts) == 2:
#             scraped_artist, scraped_song_name = parts
#             scraped_song_dict[scraped_artist.strip()] = scraped_song_name.strip()
#         else: 
#             print(f"Error splitting song: {cleaned_song}")
#     # print(scraped_song_dict)
#     return scraped_song_dict

# def tidy_time(scraped_songs):
#     scraped_song_dict = {}
#     for i, scraped_song in enumerate(scraped_songs):
#         print(f"Iteration: {i}, {scraped_song}")
#         if i >= 10:
#             break
#         else: 
#             cleaned_song = scraped_song.split('. ', 1)[1].replace('"','').strip()
#             parts = cleaned_song.split(', ')
#             scraped_song_name = parts[1]
#             scraped_artist = parts[0]
#             scraped_song_dict[scraped_artist.strip()] = scraped_song_name.strip()
#     print(scraped_song_dict)
#     return scraped_song_dict


# def tidy_gq(scraped_songs):
#     scraped_song_dict = {}
#     for i, scraped_song in enumerate(scraped_songs):
#         print(f"Iteration: {i}, {scraped_song}")
#         cleaned_song = scraped_song.replace('"','').strip()
#         parts = re.split(r'\s*[—-]\s*', cleaned_song, maxsplit=1)
#         if len(parts) == 2:
#             scraped_artist, scraped_song_name = parts
#             scraped_song_dict[scraped_artist.strip()] = scraped_song_name.strip()
#         else: 
#             print(f"Error splitting song: {cleaned_song}")
#     # print(scraped_song_dict)
#     return scraped_song_dict


# def tidy_harper(scraped_songs):
#     scraped_song_dict = {}
#     for i, scraped_song in enumerate(scraped_songs):
#         print(f"Iteration: {i}, {scraped_song}")
#         if i >= 20:
#             break
#         else: 
#             cleaned_song = scraped_song.replace('"','').strip()
#             parts = cleaned_song.split(' by ')
#             scraped_song_name = parts[1]
#             scraped_artist = parts[0]
#             scraped_song_dict[scraped_artist.strip()] = scraped_song_name.strip()
#     print(scraped_song_dict)
#     return scraped_song_dict


def tidy_treble(scraped_songs):
    scraped_song_dict = {}
    for i, scraped_song in enumerate(scraped_songs):
        print(f"Iteration: {i}, {scraped_song}")
        cleaned_song = scraped_song.split('. ', 1)[1].replace('"','').strip()
        parts = cleaned_song.split(' – ')
        scraped_song_name = parts[1]
        scraped_artist = parts[0]
        scraped_song_dict[scraped_artist.strip()] = scraped_song_name.strip()
    print(scraped_song_dict)
    return scraped_song_dict






def generate(request):
    urls = [
    # 'https://www.nme.com/en_au/features/music-features/best-songs-of-2023-3-3552893',
    # 'https://consequence.net/2023/12/200-best-songs-of-2023-list/22/',
    # 'https://pitchfork.com/features/lists-and-guides/best-songs-2023/',
    # 'https://variety.com/lists/the-best-songs-of-2023/', 
    # 'https://www.rollingstone.com/music/music-lists/best-songs-of-2023-1234879541/', N/A
    # 'https://www.billboard.com/lists/best-songs-2023/',
    # 'https://www.bbc.com/news/entertainment-arts-67617420',                           N/A            
    # 'https://www.theguardian.com/music/2023/dec/04/the-20-best-songs-of-2023',        N/A
    # 'https://www.esquire.com/entertainment/music/g45778643/best-new-songs-2023/',
    # 'https://www.slantmagazine.com/lists/the-50-best-songs-of-2023/',
    # 'https://uproxx.com/music/best-songs-2023-list/',
    # 'https://time.com/6340132/best-songs-2023/',
    # 'https://www.gq-magazine.co.uk/culture/article/best-songs-2023',
    # 'https://www.harpersbazaar.com/culture/art-books-music/g42862748/best-songs-2023/',
    'https://www.treblezine.com/the-100-best-songs-of-2023/',
    # 'https://www.vulture.com/article/best-new-songs-2023.html'
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
    
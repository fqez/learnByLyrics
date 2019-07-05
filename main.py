import lyricsgenius
import re
import argparse

def get_song_lyrics(artist_name, song_name):
    song = genius.search_song(artist_name, song_name)
    return song.lyrics

def get_artists(artist_name, max_songs_number):

    artist = genius.search_artist(artist_name, max_songs=max_songs_number, sort="title")
    return artist

def clean_lyrics(lyrics):
    line = re.sub(r"\[.*\]", "", lyrics)
    line = re.sub(r"\(.*\)","",line)
    return line

def load_file(path):
    try:
        f = open(path,'r') 
        l = f.read()
        return l
    except:
        print("Couldn't read file")
    finally:
        f.close()

if __name__ == "__main__":

    ap = argparse.ArgumentParser()
    ap.add_argument("-a", "--artist", required=True, help="Artist name")
    ap.add_argument("-s", "--song", required=True, help="Song name")

    args = vars(ap.parse_args())

    artist_name = args['artist']
    song_name = args['song']

    token = read_file('token.txt')
    genius = lyricsgenius.Genius(token)
    #genius.verbose = False # Turn off status messages

    path = 'i_dont_care.txt'
    own_lyrics = load_file(path)

    lyrics = get_song_lyrics("Ed Sheeran", "I Don't Care")
    c_lyrics = clean_lyrics(lyrics)


    #print(c_lyrics)

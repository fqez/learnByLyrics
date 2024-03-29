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
    line = re.sub(r"\ ","",line)  
    line = re.sub(r"\n","",line)  
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
    
def compare_songs(lyrics, own_lyrics):

    #lyrics = "HiMyNameIsaFran"
    #own_lyrics = "HiMyNameIsFran"

    print(lyrics)
    print(own_lyrics)

    score = right = cont = index1 = index2 = 0
    total_len = len(lyrics)
    positions = []
    most_fails={}

    for n in range(total_len):
        x = lyrics[0]
        y = own_lyrics[0]
        if x == y:
            right += 1
            lyrics = lyrics[1:]
            own_lyrics = own_lyrics[1:]
        else:
            lyrics = lyrics[1:]
        cont += 1
    score = (right/total_len)*100
    print("{0:.2f} % success!! Right characters: {1}, Total characters: {2}, Processed characters: {3}".format(score, right, total_len, cont))

def main(artist_name, song_name, path):
    
    own_lyrics = load_file(path)
    lyrics = get_song_lyrics(artist_name, song_name)
    c_lyrics = clean_lyrics(lyrics)
    o_lyrics = clean_lyrics(own_lyrics)
    compare_songs(c_lyrics, o_lyrics)


if __name__ == "__main__":

    ap = argparse.ArgumentParser()
    ap.add_argument("-a", "--artist", required=True, help="Artist name")
    ap.add_argument("-s", "--song", required=True, help="Song name")
    ap.add_argument("-f", "--file", required=True, help="Path to your solution file")

    args = vars(ap.parse_args())

    artist_name = args['artist']
    song_name = args['song']
    path = args['file']

    token = load_file('token.txt')
    genius = lyricsgenius.Genius(token)
    #genius.verbose = False # Turn off status messages

    main(artist_name, song_name, path)


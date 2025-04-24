import random
import csv

# Load song data from a CSV file into a list
# Link to source for CSV file: https://kworb.net/spotify/country/global_daily.html
def load_songs(file_path):
    songs = []
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            songs.append({
                'rank': int(row['Rank']),
                'song': row['Song Title'],  
                'artist': row['Artist']
            })
    return songs

# Student-developed procedure to get a random song from the list
def get_random_song(song_list):
    if not song_list:
        return "No songs available."

    random_song = random.choice(song_list)
    return f"🎵 Rank #{random_song['rank']}: '{random_song['song']}' by {random_song['artist']}"

# Procedure to filter songs by artist
def filter_songs_by_artist(song_list, artist):
    filtered_songs = [song for song in song_list if artist.lower() in song['artist'].lower()]
    return filtered_songs

# Procedure to filter songs by rank
def filter_songs_by_rank(song_list, rank):
    filtered_songs = [song for song in song_list if song['rank'] == rank]
    return filtered_songs

# Procedure to display top N songs
def display_top_n_songs(song_list, n):
    return song_list[:n]

# Procedure to search for songs by title
def search_songs_by_title(song_list, title):
    filtered_songs = [song for song in song_list if title.lower() in song['song'].lower()]
    return filtered_songs

def main():
    # Load songs from the correct file path
    file_path = 'navigation/Top_70_Songs.csv'
    top_200_songs = load_songs(file_path)

    print("🎶 Welcome to the Spotify Top Song Randomizer!")
    while True:
        print("\nOptions:")
        print("1. Pick a random song")
        print("2. Search for songs by artist")
        print("3. Search for songs by rank")
        print("4. Display top N songs")
        print("5. Search for songs by title")
        print("6. Quit")
        user_input = input("Please choose an option (1/2/3/4/5/6): ")

        if user_input == '1':
            result = get_random_song(top_200_songs)
            print(result)
        
        elif user_input == '2':
            artist = input("Enter the artist's name to search for: ")
            filtered_songs = filter_songs_by_artist(top_200_songs, artist)
            if filtered_songs:
                print(f"\nSongs by {artist}:")
                for song in filtered_songs:
                    print(f"🎶 Rank #{song['rank']}: '{song['song']}' by {song['artist']}")
            else:
                print(f"No songs found for artist '{artist}'.")

        elif user_input == '3':
            rank = int(input("Enter the rank to search for: "))
            filtered_songs = filter_songs_by_rank(top_200_songs, rank)
            if filtered_songs:
                for song in filtered_songs:
                    print(f"🎶 Rank #{song['rank']}: '{song['song']}' by {song['artist']}")
            else:
                print(f"No song found for rank #{rank}.")

        elif user_input == '4':
            n = int(input("Enter the number of top songs to display: "))
            top_songs = display_top_n_songs(top_200_songs, n)
            print(f"\nTop {n} Songs:")
            for song in top_songs:
                print(f"🎶 Rank #{song['rank']}: '{song['song']}' by {song['artist']}")

        elif user_input == '5':
            title = input("Enter a part of the song title to search for: ")
            filtered_songs = search_songs_by_title(top_200_songs, title)
            if filtered_songs:
                print(f"\nSongs matching '{title}':")
                for song in filtered_songs:
                    print(f"🎶 Rank #{song['rank']}: '{song['song']}' by {song['artist']}")
            else:
                print(f"No songs found with the title containing '{title}'.")

        elif user_input == '6':
            print("Goodbye! 🎧")
            break
        
        else:
            print("Invalid input. Please choose 1, 2, 3, 4, 5, or 6.")

if __name__ == "__main__":
    main()

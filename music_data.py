import csv
import click


def column_reader(array_position: int):
    with open("data.csv", "r") as csv_data:
        item_list = []
        csv_reader = csv.reader(csv_data, delimiter=',')
        for line in csv_reader:
            item_list.append(line[array_position])
        return item_list


def list_all_artists():
    artist_list = column_reader(16)
    print(artist_list)
    total_artists = len(artist_list)
    print(f"\n{total_artists} Artists Found")


def list_all_songs():
    song_list = column_reader(15)
    print(song_list)
    total_songs = len(song_list)
    print(f"\n{total_songs} Songs Found")



@click.command()
@click.option('--artist', '-a', is_flag=True, help="Select Artists.")
@click.option('--song', '-s', is_flag=True, help="Select Songs.")
def cli_command(artist, song):
    if artist:
        list_all_artists()
    elif song:
        list_all_songs()
    else:
        print("Flag not found, please append -a for artist list or -s for song list")


if __name__ == "__main__":
    cli_command()

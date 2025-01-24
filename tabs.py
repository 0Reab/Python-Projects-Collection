import webbrowser

# global vars
notepad = r'C:\Users\StillAStojke\Desktop\guitar.txt' # path to .txt containing 'song - url' lines
browser = lambda x: webbrowser.open(x)


def read_song_list() -> str:
    # file reading
    try:
        with open(notepad, 'r') as r:
            # unprocessed_tabs = r.read()
            return r.read()
    except FileNotFoundError:
        print(f"Could not find {notepad}")


def process_data(song_list: str) -> dict[str, str]:
    # data processing - result -> {'song_name': 'url', ...}
    return {
        ' '.join(i.split()[:-1]):str(i.split()[-1])
        for i in song_list.split('\n')
    }

def links(song_list: dict[str, str]) -> list[str]:
    return list(song_list.values()) # just links


def show_songs(song_list: dict[str, str]) -> None:
    # display song list
    for num, tab in enumerate(song_list):
        print(f'{num}. {tab}')


def selected_song() -> list[int]:
    # song select
    usr_choice = input('\nSelect a song number\nOr a list eg. 1 2 3\n')
    selected = list(map(int, usr_choice.split(' ')))
    # validate usr input for only integers and spaces - allow
    return selected


def open_urls(selected: list[int], urls: list[str]) -> None:
    # open links to tabs of selected songs
    for n in selected: browser(urls[n])


def main():
    song_list = process_data(read_song_list())

    show_songs(song_list)
    open_urls(selected_song(), links(song_list))


if __name__ == '__main__':
    main()
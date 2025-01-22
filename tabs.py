import webbrowser

# global vars
notepad = r'C:\Users\User\Desktop\guitar.txt' # path to .txt containing 'song - url' lines
browser = lambda x: webbrowser.open(x)

# file reading
try:
    with open(notepad, 'r') as r:
        unprocessed_tabs = r.read()
except FileNotFoundError:
    print(f"Could not find {notepad}")

# data processing - result -> {'song_name': 'url', ...}
tabs = {
    ' '.join(i.split()[:-1]):str(i.split()[-1])
    for i in unprocessed_tabs.split('\n')
}
links = list(tabs.values()) # just links

# display song list
for num, tab in enumerate(tabs):
    print(f'{num}. {tab}')

# song select
usr_choice = input('\nSelect a song number\nOr a list eg. 1 2 3\n')
selected = list(map(int, usr_choice.split(' ')))

# validate usr input for only integers and spaces - allow

# open links to tabs of selected songs
for n in selected: browser(links[n])


'''
DEBUG lines 
# debug print(list(clean_tabs.values())[int(num)])
# debug print(list(clean_tabs.values())[int(selected[0])])
'''
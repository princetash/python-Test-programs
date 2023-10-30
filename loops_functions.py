#function takes parameters of the name of artist and album, songs produced by artis
def make_album(name, album, songs =None):
    #checkin whether the arguements contains songs 
    if songs:
        f_album = {"artist":name, "title":album, "songs":songs}
    else:
        f_album = {"artist":name, "title":album}
    return f_album

#asking for the names and albums  from the user
while True:
    title = input("Enter song title: ")
    if title == 'q':
        break

    artist_name = input("Enter artist name: ")
    if  artist_name == 'q':
        break



full_album = make_album(artist_name, title)
print(full_album)
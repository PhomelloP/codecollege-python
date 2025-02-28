# #8.2
# def my_favourite_book(title):
#     "accepts book title"
#     print(f'One of my fvaourite books is {title.title()}')

# my_favourite_book("The seven wives of baba segi")

# #8.3
# def make_t_shirt(size,message):
#     "accepts size and prints message"
#     print(f"Good news! Size {size} is available")
#     print(f"\nyour size {size} T-shirt will display \n\t{message}")

# make_t_shirt("large","'God's Favourite'")
# make_t_shirt(message="cherry",size="Medium")



# #8.6

# def city_country(city,country):
#     "returns formatted"
#     return f'{city.title()} {country.title()}'

# print(city_country("Bloemfontein", "south Africa"))
# print(city_country("maseru", "Lesotho"))
# print(city_country("sydney", "Australia"))

#8.7
# def make_album(artist_name, album_title, songs=None):
#     "Album dictionary"
#     album= {'artist':artist_name,'title': album_title,"song":songs}
#     return album

# print(make_album("Rihanna","Anti"))
# print(make_album("Beyonce","Lemonade",22))

# 8.8
def make_album(artist, title, song=None):
    "Album dictionary"
    album= {'artist':artist,'title': title,"song":song}
    return album
while True:
    print("\nEnter Album information")
    print("\n Enter 'q' at any time to quit.")

    artist = input("artist name  :")
    if artist == 'q':
        break

    title = input("album name  :")
    if title == 'q':
        break

    song = input("song number(optional)  :")
    if song == 'q':
        break

album = make_album(artist ,title ,song )
print(album)


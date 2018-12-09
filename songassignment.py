"""
CP1404 Assignment 1
By: Matthew Cabinian
Assignment: Songs to learn 1.0

"""

import csv
no_of_songs = 6

#Display Menu
def display_menu():
    """Songs to learn 1.0 By: Matthew Cabinian
    menu = 
    Menu:
    L - List songs
    A - Add New Song
    C - Complete A Song
    Q - Quit""".format(no_of_songs)

    print (menu)
    return menu

choice = input(">>> ").upper()
songreader = open('Songs.csv')
songs = list(csv.reader(songreader, delimiter=','))

    if choice =="L":
        song_list= copy.copy(songs)
        for i in range(0, len(song_list), 1):
            if song_list[i][3] == 'Y':
                song_list[i][3] = '*'
            else:
                song_list[i][3] = ''
            print(i, '. {:1} {:30} {:1} {:30} {}{}{}'.format(song_list[i][3], song_list[i][0], '- ', song_list[i][1]'(', song_list[i][2], ')'))

    elif choice =="A":
        title = str(input("Song Title: "))
        while title =="":
            print("Input invalid, input valid Song Title")
            title = str(input("Song Title: "))

        artist = str(input("Artists or Band Name: "))
        while artist = "":
            print("Input invalid, input valid Artists name or Band Name")
            artist = str(input("Artists or Band Name: "))

        year = str(input("Year Released: "))
        while year =="":
            print("Input invalid, input valid year release")
            year = str(input("Year Released: "))

        newsong = [title, artist, year,'N']
        sreader = open('Songs.csv', 'w', newline='')
        songs.append(newsong)
        writer = csv.writer(sreader, delimiter=",")
        for lines in songs:
            writer.writerow(lines)
        sreader.close()


    elif choice =="C":
        print("Enter number of the song to mark ")
        slearn = int(input(">> "))
        sreader = open('Songs.csv', 'w', newline='')
        songs[slearn][3] = 'Y'
        writer = csv.writer(sreader, delimiter=",")
        for lines in songs:
            writer.writerow(lines)
        sreader.close()

    elif choice =="Q":
        print("Thank you for your time")
        


    else:
        print("Invalid Option, Please input valid action")
        choice = input(">>> ").upper()

main()

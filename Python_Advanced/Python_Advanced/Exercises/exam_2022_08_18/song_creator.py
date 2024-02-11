def add_songs(*songs_info):
    songs = {}

    for song, lyrics in songs_info:
        if song not in songs:
            songs[song] = lyrics
        else:
            songs[song] += lyrics

    result = ''
    for song, lyrics in songs.items():
        lyrics_part = '\n'.join(lyrics)
        result += f"- {song}\n{lyrics_part}\n" if lyrics else f"- {song}\n"

    return result


print(add_songs(
    ("Love of my life",
     ["Love of my life, you've hurt me",
      "You've broken my heart, and now you leave me",
      "Love of my life, can't you see?",
      "Bring it back, bring it back"]),
    ("Beat It", []),
    ("Love of my life",
     ["Don't take it away from me",
      "Because you don't know",
      "What it means to me"]),
    ("Dream On",
     ["Every time that I look in the mirror"]),
))

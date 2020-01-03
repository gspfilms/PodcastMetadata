#This app converts inputs into appropriate metadata for DIAD podcasts. It provides metadata for itunes, libsyn,
#youtube, and blogger

#Itunes and Filename variables
episode_number = str(input(f'Episode Number: '))
episode_title = input(f'Episode Title: ')
episode_description = input(f'Episode Description: ')
podcast_title = 'The Do It And Die Podcast: Pitching and Developing Sketch Comedy'
podcast_description = 'A humorous podcast in which sketch comedy ideas are pitched and developed. Paul, Evan, ' \
                     'and Brett, and Scotty bring their minds together in order to come up with the next video idea that ' \
                     'they will film and put on their youtube channel, DoItAndDie.'
itunes_title = f'DIAD #{episode_number}: {episode_title}'
itunes_artist = 'Do It And Die Sketch Comedy'
mp3_titles = episode_title.split()
output =''
count = 1
for mp3_title in mp3_titles:
    if count < len(mp3_titles):
        count += 1
        output += mp3_title + '-'
    else:
        output += mp3_title
itunes_filename = f'DIAD{episode_number}_{output}.mp3'

#Libsyn variables
libsyn_tags = ('sketch comedy, sketch comedy podcast, writing comedy, pitching comedy, developing comedy')
libsyn_description = f'''<p>{episode_description}</p>
<p>Please check out our <a href="https://www.youtube.com/user/DoItAndDie">YouTube Channel</a></p>
<p>And <a href="https://www.youtube.com/user/DoItAndDie?sub_confirmation=1">subscribe here!</a></p>
<p><a href="http://www.doitanddie.com/">Website</a></p>'''

#Youtube variables
youtube_tags = '''sketch comedy, sketch comedy short, writing sketch comedy, pitching sketch comedy,
do it and die, how to write sketch comedy, learn to write sketch comedy, diad, developing sketch comedy, 
comedy sketches, comedy short, comedy podcast, sketch comedy podcast'''

#Functions presenting appropriate metadata for DIAD files
def itunes_metadata():
    return "Itunes Metadata---\n" + "Song: " + itunes_title + "\nArtist: " + itunes_artist + "\nAlbum: "\
+ podcast_title + "\nComments: " + episode_description + '\nFilename: ' + itunes_filename +'\n'

def libsyn_metadata():
    return "\nLibsyn Metadata---" + "\nTitle: " + itunes_title + "\nSubtitle: " + podcast_description + "\nDescription: "\
+ libsyn_description + "\nTags: " + libsyn_tags + "\nItunes Optimization---" + "\nTitle: " + itunes_title + '\nSummary: '\
+ episode_description +'\n'

def youtube_metadata():
    return "\nYouTube Metadata---" + f'\nTitle: DIAD Sketch Comedy #{episode_number}: {episode_title}' + '\nDescription: '\
+ episode_description + f'''\n\nWant to learn to write sketch comedy? Listen to our sketch comedy podcast, we talk and 
develop sketch comedy ideas including parodies and shorts.

Please subscribe here if you enjoyed!
https://www.youtube.com/user/DoItAndDie?sub_confirmation=1

download this podcast directly from our Libsyn page:
http://traffic.libsyn.com/doitanddie/{itunes_filename}

Check out our website with the whole sketch comedy writing podcast feed:
doitanddie.com\n''' + '\nTags: ' + f'{youtube_tags}'

#Writes to 'PodcastMetadata.txt' file alongside this app directory
f = open('PodcastMetadata.txt', 'w')
f.write(itunes_metadata())
f.write(libsyn_metadata())
f.write(youtube_metadata())
f.close()

print("\nPodcastMetadata.txt' has been exported alongside this application.\n")
index_id = input('Index ID from Libsyn (8 digits):')

#Blogger embed will present the embedded libsyn media player with a DIAD Dark Red Color Theme
def blogger_embed():
    return '\n\nBlogger Embed Code---\n<iframe style="border: none" src="//html5-player.libsyn.com/embed/episode/id/'\
            f'{index_id.strip()}/height/90/theme/custom/thumbnail/yes/direction/backward/render-playlist/no/'\
            'custom-color/c60613/" height="90" width="100%" scrolling="no"  allowfullscreen webkitallowfullscreen'\
            ' mozallowfullscreen oallowfullscreen msallowfullscreen></iframe>'


f = open('PodcastMetadata.txt', 'a')
f.write(blogger_embed())
f.close()

#Lost Lyric: Make it p-stick for all I care
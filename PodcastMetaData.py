echo "# PodcastMetadata" >> README.md
git init
git add README.md
git commit -m "first commit"
git remote add origin https://github.com/gspfilms/PodcastMetadata.git
git push -u origin master

user_title = input('Title: ')
user_description = input('Description: ')
user_comments = input('Comments: ')
user_tags = input('Tags: ')
t_words = user_title.split(' ')
d_words = user_description.split(' ')
c_words = user_comments.split(' ')
ta_words = user_tags.split(' ')

print()
print('MP3 Metadata: '
      '')

#print(t_words)
#print(ta_words)
#print(c_words)
#print(d_words)

meta_list = {
    "t_words": user_title,
    "d_words": user_description,
    "c_words": user_comments,
    "ta_words": ta_words
}

# MP3 METADATA
output = ''
for word in t_words:
    output += meta_list.pop(word, word) + '-'
print(f'MP3 Title: {output}' + ".mp3")

output = ''
for word in d_words:
    output += meta_list.pop(word, word) + ' '
print(f'Description: {output}')

output = ''
for word in c_words:
    output += meta_list.pop(word, word) + ' '
print(f'Comments: {output}')

output = ''
for word in ta_words:
    output += meta_list.pop(word, word) + ' '
print(f'Tags: {output}')

print()
# LIBSYN METADATA
print('Libsyn Metadata:'
      '')
output = ''
for word in t_words:
    output += meta_list.pop(word, word) + '-'
print(f'Libsyn Title: {output}' + ".mp3")

output = ''
for word in d_words:
    output += meta_list.pop(word, word) + ' '
print(f'Description: {output}')

output = ''
for word in c_words:
    output += meta_list.pop(word, word) + ' '
print(f'Comments: {output}')

output = ''
for word in ta_words:
    output += meta_list.pop(word, word) + ' '
print(f'Tags: {output}')
print()
# YouTube METADATA
print('Youtube Metadata:'
      '')
output = ''
for word in t_words:
    output += meta_list.pop(word, word) + '-'
print(f'Libsyn Title: {output}' + ".mp3")

output = ''
for word in d_words:
    output += meta_list.pop(word, word) + ' '
print(f'Description: {output}')

output = ''
for word in c_words:
    output += meta_list.pop(word, word) + ' '
print(f'Comments: {output}')

output = ''
for word in ta_words:
    output += meta_list.pop(word, word) + ' '
print(f'Tags: {output}')
print()







output = ''
def podcast_data():
    for w_output in t_words:
        output += (w_output, w_output) + ' '


#print()
#print(f'Title: {title}')
#print(f'Description: {description}')
#print(f'Comments: {comments}')
#print(f'Tags: {tags}')



#def podcast_titles(title, description, comments):
#    print(f'Title: ' {title}')
#    print(f'Description: ' {description}')
#    print(f'Comments: ' {comments}')


#title_input = input('Title : > ')
#description_input = input('Description : >')
#comments_input = input('Comments : >')
#podcast_titles(title_input,description_input, comments_input)
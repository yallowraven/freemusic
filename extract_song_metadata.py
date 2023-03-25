import os
import mutagen

# create a new file for writing the title-author pairs
with open('songs_meta.txt', 'w') as f:

    # loop through each file in the songs directory
    for filename in os.listdir('songs'):

        # check if the file is an MP3 file
        if filename.endswith('.mp3'):

            # open the file and get the metadata
            filepath = os.path.join('songs', filename)
            audio = mutagen.File(filepath)

            # get the title and author from the metadata
            title = audio.get('TIT2', ['Unknown Title'])[0]
            author = audio.get('TPE1', ['Unknown Artist'])[0]

            # check if the metadata is missing
            if title == 'Unknown Title' or author == 'Unknown Artist':

                # print a message indicating the missing metadata
                print('Unknown metadata:', filepath)

                # delete the file
                os.remove(filepath)

            else:

                # write the title-author pair to the text file
                f.write(f'{title} - {author}\n')

print('Extracted title-author pairs to songs_meta.txt.')

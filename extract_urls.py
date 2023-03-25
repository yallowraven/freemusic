# Thx ChatGPT

import re

def extract_urls(filename):
    # open file for reading
    with open(f'page/{filename}.html', 'r') as f:

        # read the contents of file
        content = f.read()

        # compile the regex pattern
        pattern = re.compile(r'<div class="play-item[^\n]*')

        # search for all matches in the content
        matches = pattern.findall(content)

        url_pattern = re.compile(r'https:\\/\\/files.freemusicarchive.org[^&]*')

        # open results file for writing
        with open(f'{filename}_urls.txt', 'w') as filtered:

            # write each match to results file
            for match in matches:
                url = url_pattern.findall(match)[0]
                url = url.replace('\/', '/')
                filtered.write(url + '\n')

extract_urls('breakcore1')
extract_urls('breakcore2')
extract_urls('breakcore3')
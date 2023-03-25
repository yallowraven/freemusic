# Thx ChatGPT

import re

# open breakcore1.html for reading
with open('page/breakcore1.html', 'r') as f:

    # read the contents of breakcore1.html
    content = f.read()

    # compile the regex pattern
    pattern = re.compile(r'<div class="play-item[^\n]*')

    # search for all matches in the content
    matches = pattern.findall(content)

    url_pattern = re.compile(r'https:\\/\\/files.freemusicarchive.org[^&]*')

    # open breakcore1_urls.html for writing
    with open('breakcore1_urls.html', 'w') as filtered:

        # write each match to breakcore1_urls.html
        for match in matches:
            url = url_pattern.findall(match)[0]
            url = url.replace('\/', '/')
            filtered.write(url + '\n')

# Thx ChatGPT

import re

# open breakcore1.html for reading
with open('page/breakcore1.html', 'r') as f:

    # read the contents of breakcore1.html
    content = f.read()

    # compile the regex pattern
    pattern = re.compile(r'<a href="https://freemusicarchive\.org/music/[^\n]*\n[^\n]*\n</a>')

    # search for all matches in the content
    matches = pattern.findall(content)

    # open breakcore1_titles.html for writing
    with open('breakcore1_titles.html', 'w') as filtered:

        # write each match to breakcore1_titles.html
        for match in matches:
            filtered.write(match)

import os
import urllib.request

# create the songs directory if it doesn't exist
if not os.path.exists('songs'):
    os.makedirs('songs')

# open the file1.txt for reading
with open('breakcore_urls_aggr.txt', 'r') as f:

    # loop through each line in the file
    for line in f:

        # remove any whitespace at the beginning or end of the line
        url = line.strip()

        print(url)
        # create a filename for the downloaded file by taking the last part of the URL
        filename = url.split('/')[-1]

        req = urllib.request.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36')

        # make the request and save the downloaded file
        with urllib.request.urlopen(req) as response, open(os.path.join('songs', filename), 'wb') as outfile:
            outfile.write(response.read())

print('Downloaded all files to the songs directory.')

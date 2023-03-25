# Free music

## Requirements
1. Music playlist that is as long as possible
2. Must consist of CC licensed music
3. Must be breakcore (for now)
4. Adequate music player software

## The source
https://freemusicarchive.org/genre/Breakcore_-_Hard
- Has 588 songs
- Random sampling (4 samples) reveals CC-BY-NC-SA (or less restrictive) license on each song
- Fermi approx: each song is 3 mins on average => ~29.4 hours of free music


## Automating the download
### The plan
- Acquire all download links
- Click all download links

### Approach:
- Download all relevant HTML:
    - Download the listings
    - Set items shown on each page to max (currently 200, page resisted trivial tamperings with max page size)
    - Manually fetch (note to self: get better browser)
- Identify songs in HTML:
    - Ctrl + F song title
    - All songs appear in the following format: 
        ```
        <a href="https://freemusicarchive.org/music/{AUTHOR}/single/{TITLE_NORMALIZED}/" class="font-bold">{TITLE}</a>
        ``` 
        !1
    
- Find a way to get download links (Part 1):
    - The link listed above redirects to the song's about page
    - The format of a download link (found by attempting a normal user friendly download) is: ```https://freemusicarchive.org/track/{TITLE_NORMALIZED}/download/``` !2
    - !1 !2 Conclusion: no need for all extra webpage data, plain HTML has all ^3
    - How are songs with same title (different authors) disambiguated? ^1 
    - How does normalization work? Is that even relevant, considering we already have an instance of normalized song title, so we don't have to create it ourselves from denormalized string? ^2

- Sidequest (saved webpages plain HTML + extra data):
    - Refer to META 38:27
    - https://superuser.com/questions/1337772/windows-deletes-html-files-when-i-delete-a-folder
    - Weird win explorer bullshittery
    - ^3 To delete additional data, rename the folder so explorer doesnt think its linked to plain HTML anymore (????)
    - ^ Result of above: https://imgur.com/a/qQ4rrp5 like damn its hilarious

- Find a way to get download links (Part 2):
    - Strip plain HTML of everything but the normalized song titles
    - This regex matches all segments like !1: ```<a href="https://freemusicarchive.org/music/[^\n]*\n[^\n]*\n</a>```
    - VSCode doesnt have proper text processing capabilities, and our team is too lazy to learn how to invert a regex (to erase everything except these segments), so programming time
    - => extract_titles.py
    - At commit b8487a103664b5e1c1aca5d78a479e5345b962e1, the extracted segments amount to way more than the number of songs (approx 500 segments, compared to the 200 songs)
    - Look for another format for songs? ^4
    - ^4 Absolutely, new format starts with: ```<div class="play-item```
    - Of this format, there are exactly 200 segments in the file, and it is also simpler to look for than the previous one (whoops)
    - Slight drawback is it contains a lot more gibberish, but it has the download link out of the box (although escaped)
    - Adjusting programming
    - => changed regex in extract_titles.py
    - After forcefully carving off some off the gibberish by hand, found the following pattern: https:\\/\\/files.freemusicarchive.org[^&]
    - Applying this regex lists all download links in an escaped format
    - Unescaping produces functioning links for all songs, making surprisingly quick of this problem, completely cutting out the need for titles (for now at least)
    - => extract_titles.py -> extract_urls.py @ 143bdcc7392c4f032c3986e4a61421343384b60e

- Addressing attribution (Part 1):
    - Most (maybe all) songs require some form of attribution so because i like not going to jail very much, something has to be done about this
    - A possible idea might be just linking the plain HTML page directly, but it ugly, and doesn't do justice for the authors
    - Linking the online version works better, but could change any moment, being an unreliable source
    - Conclusion: the attribution list must be generated in some way too
    - Luckily, the HTML page does not have to be used anymore, as by random sampling (2 samples) the songs have appropriate metadata, which just has to be extracted and printed into a text file

- Downloading all songs:
    - Our team invokes ChatGPT for this task **once again**, the language of choice is Python **once again**
    - => download_songs.py @ ed7d0e2621e4ab3e668a1ec6bc08345a4bc180e5

- Addressing attribution (Part 2):
    - To automate the metadata fetching and extraction, another piece of software must be employed
    - => extract_song_metadata.py @ COMMIT_NUM
    - The first iteration cannot find the metadata of some songs (probably because they dont have any), these have to be reported and corrected by hand
    - The simplest method for this is just removing those songs altogether

## Wrapping up
- This journey ended with 568 (hopefully good) quality CC songs
- My music player of choice will be Windows Media Player (aka Groove Music) until I'm dissatisfied
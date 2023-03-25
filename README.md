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

### Approach 1:
- Download all relevant HTML:
    - Download the listings
    - Set items shown on each page to max (currently 200, page resisted trivial tamperings with max page size)
    - Manually fetch (note to self: get better browser)
- Identify songs in HTML:
    - Ctrl + F song title
    - All songs appear in the following format: ```
    <a href="https://freemusicarchive.org/music/{AUTHOR}/single/{TITLE_NORMALIZED}/" class="font-bold"> !1
    {TITLE}
    </a>```
    
- Find a way to get download links (Part 1):
    - The link listed above redirect to the song's about page
    - The format of a download link is: ```https://freemusicarchive.org/track/{TITLE_NORMALIZED}/download/``` !2
    - !1 !2 Conclusion: no need for all extra webpage data, plain HTML has all ^3
    - How are songs with same title (different authors) disambiguated? ^1 
    - How does normalization work? Is that even relevant, considering we already have an instance of normalized song title, so we don't have to create it ourselves from denormalized string? ^2

- Sidequest (saved webpages plain HTML + extra data):
    - refer to META 38:27
    - https://superuser.com/questions/1337772/windows-deletes-html-files-when-i-delete-a-folder
    - weird win explorer bullshittery
    - ^3 to delete additional data, rename the folder so explorer doesnt think its linked to plain HTML anymore (????)
    - ^ result of above: https://imgur.com/a/qQ4rrp5 like damn its hilarious
# Spotify

Scripts to manage my Spotify library.

## Getting Started

Install prerequisites:

```sh
poetry install
```

Create an `.env` file with the following contents, which you can get from [developer.spotify.com](https://developer.spotify.com/dashboard/applications):

```sh
export SPOTIPY_CLIENT_ID='***'
export SPOTIPY_CLIENT_SECRET='***'
export SPOTIPY_REDIRECT_URI='***'
```

Note: `REDIRECT_URI` doesn't need to be a valid url, it's just used for authorization. See [docs](https://spotipy.readthedocs.io/en/2.22.1/?highlight=search#redirect-uri) for details.

## Usage

### Auto-Playlist: 102.7 The Peak

To update the 102.7 The Peak playlist with recently played songs:

```sh
poetry run python spotify/thepeak.py
```

Output will look something like this:

```
[0] Finding track: artist:Bastille track:Pompeii
[1] Finding track: artist:Maneskin track:Supermodel
[2] Finding track: artist:Whitehorse track:Downtown
...
[97] Finding track: artist:Mazzy Star track:Fade Into You
[98] Finding track: artist:July Talk (feat. Spencer Krug) track:Certain Father
[99] Finding track: artist:Audioslave track:Like A Stone
Added 100 tracks to https://open.spotify.com/playlist/2uOZqN0X34s85qD2ft0dRW
```

## References

- [Spotipy](https://github.com/spotipy-dev/spotipy)
- [Spotify Web API](https://developer.spotify.com/documentation/web-api/reference/#/)

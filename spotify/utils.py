import spotipy
from spotipy.oauth2 import SpotifyOAuth
from urllib.parse import quote_plus


def replace_tracks_in_playlist(playlist_id: str, tracks: list, description: str = None):
    scope = "playlist-modify-public"
    spotify = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))
    playlist = spotify.playlist(playlist_id)

    track_uris = []
    for i, track in enumerate(tracks):
        query = f"artist:{track['artist']} track:{track['track']}"
        print(f"[{i}] Finding track: {query}")
        result = spotify.search(q=quote_plus(query), limit=1)

        try:
            spotify_track = result["tracks"]["items"][0]
            track_uris.append(spotify_track["uri"])
        except IndexError:
            print("Couldn't find track!")

    spotify.playlist_replace_items(playlist["id"], track_uris)
    print(f"Added {len(track_uris)} tracks to https://open.spotify.com/playlist/{playlist['id']}")

    if description:
        # Line breaks aren't supported in the description
        spotify.playlist_change_details(
            playlist["id"], description=description.replace("\n", "")
        )

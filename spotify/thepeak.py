import requests
from datetime import datetime

from spotify.utils import replace_tracks_in_playlist

# In the web player, click on the playlist and get this from the url
# e.g. https://open.spotify.com/playlist/2uOZqN0X34s85qD2ft0dRW
PEAKFM_PLAYLIST = "2uOZqN0X34s85qD2ft0dRW"
NUM_TRACKS = 100


def get_peakfm_recently_played(day: str = "0") -> dict:
    """Gets recently played songs from The Peak FM's website.

    Source: https://www.thepeak.fm/recentlyplayed/

    Args:
        day (str): 0 for current, -1 for previous day, etc. Max seems to be -6.
    """
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:108.0) Gecko/20100101 Firefox/108.0",
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "Accept-Language": "en-US,en;q=0.5",
        "X-Requested-With": "XMLHttpRequest",
        "Connection": "keep-alive",
        "Referer": "https://www.thepeak.fm/recentlyplayed/",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
    }

    params = {
        "day": day,
        "playerID": "757",
    }

    response = requests.get(
        "https://www.thepeak.fm/api/v1/music/broadcastHistory",
        params=params,
        headers=headers,
    )
    response.raise_for_status()

    raw_response = response.json()

    # Get latest songs, most recently played first
    songs = sorted(
        [
            {
                "artist": d["artist_name"],
                "track": d["song_name"],
                "epoch_time": d["last_played"],
            }
            for d in raw_response["data"]["songs"]
        ],
        key=lambda d: d["epoch_time"],
        reverse=True,
    )
    return songs


if __name__ == "__main__":
    songs = get_peakfm_recently_played()

    description = (
        f"Recently played songs as of {datetime.now().strftime('%a %b %d, %Y %I:%M %p')}."
        " Source: github.com/justinmklam/spotify"
    )

    replace_tracks_in_playlist(PEAKFM_PLAYLIST, songs[:NUM_TRACKS], description)

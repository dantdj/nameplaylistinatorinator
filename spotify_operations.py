#!/usr/bin/env python

import requests
import spotipy
import urllib
import json
import sys
import spotipy.util as util

class spotify_operations():

    def __init__(self):
        self.spotify = spotipy.Spotify()
        self.spotify_endpoint = "https://api.spotify.com/v1"
        self.username = "spotify_uk_"
        self.playlist_id = "3swUuRQY6xIKziiN31FdGQ"

    def get_tracks_in_playlist(self, playlist_json):
        data = playlist_json
        track_ids = []
        print(len(data["items"]))
        for i in range(0, len(data["items"])):
            track_ids.append(data["items"][i]["track"]["id"])
        return track_ids

    def get_track_metadata(self, trackid):
    	SPOTIPY_CLIENT_ID='c61ea8f273e341faa04681b289894ee6'
    	SPOTIPY_CLIENT_SECRET='83f8d583b70d420186ab8be3c9d9faac'
    	SPOTIPY_REDIRECT_URI='http://localhost:8888/callback'

    	scope = 'playlist-modify-private'
    	token = "BQDCnH05aLLtZ5DNxbM6uUthGitPTd_EqAzYY-PZSvPcCIXcFyeFJ5ISCZJiI1KmYXe6hjgOTB6TmEi8Ivl53_tUqn8Xw0T5i0SviwIhehsX_YPDhqrBNtI1rXSmrJu294pLbFiY3MpMdu-Gv7mfipypKGLwqs_tanUHV9OzkoB1XENkDaBJcOtzkpvOH5ISf1G6jSmdicJzcDNozvmp9D5Tyq538xObp6zVATOry8k8VGVlTnYqP5P74eeeeVD65QDiwl8USm6Def99tGU"
    	if token:
    		sp = spotipy.Spotify(auth=token)
    		ids = [trackid]
    		metadata = sp.audio_features(ids);
    		return metadata
    		#with open('metadata.json', 'w') as f1:
    		#	json.dump(metadata, f1)
    	else:
    	    print("Can't get token for", trackid)

    def get_playlist_tracks(self):
        SPOTIPY_CLIENT_ID='c61ea8f273e341faa04681b289894ee6'
        SPOTIPY_CLIENT_SECRET='83f8d583b70d420186ab8be3c9d9faac'
        SPOTIPY_REDIRECT_URI='http://localhost:8888/callback'

        scope = 'playlist-modify-private'

        token = "BQDCnH05aLLtZ5DNxbM6uUthGitPTd_EqAzYY-PZSvPcCIXcFyeFJ5ISCZJiI1KmYXe6hjgOTB6TmEi8Ivl53_tUqn8Xw0T5i0SviwIhehsX_YPDhqrBNtI1rXSmrJu294pLbFiY3MpMdu-Gv7mfipypKGLwqs_tanUHV9OzkoB1XENkDaBJcOtzkpvOH5ISf1G6jSmdicJzcDNozvmp9D5Tyq538xObp6zVATOry8k8VGVlTnYqP5P74eeeeVD65QDiwl8USm6Def99tGU"

        if token:
        	sp = spotipy.Spotify(auth=token)
        	sp.trace = False
        	playlist = sp.user_playlist_tracks(self.username, self.playlist_id)
        	return playlist
            #with open('playlist.json', 'w') as f1:
        	#	json.dump(playlist, f1)
        else:
            print("Can't get token for", username)

    def getSongs(userID, playlist, oAuth):
        tracks = []
        params = {'playlist'}
        url = spotify_endpoint + '/users/{}/playlists/{}/tracks'.format(userID, playlist)

if __name__ == "__main__":
    with open('playlist.json') as f:
        so = spotify_operations()
        playlist_tracks = so.get_playlist_tracks()
        track_id_list = so.get_tracks_in_playlist(playlist_tracks)
        metadata_list = []
        for track in track_id_list:
            metadata_list.append(so.get_track_metadata(track))
        i = 0
        for metadata in metadata_list:
            print(str(metadata[i]["id"]) + ", " + str(metadata[i]["valence"]) + ", " + str(metadata[i]["energy"]))

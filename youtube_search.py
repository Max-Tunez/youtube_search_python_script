import csv
import os
import pandas as pd
from googleapiclient.discovery import build

# Defining Some Variables
API_KEY = 'AIzaSyDFS1sBi_U7wzjWscoe81Lt762nEkCc61E'
YOUTUBE_API_SERVICE_NAME = 'youtube'
YOUTUBE_API_VERSION = 'v3'

def search_youtube(query, max_results=10):
    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=API_KEY)
    
    search_response = youtube.search().list(
        q=query,
        part='id,snippet',
        maxResults=max_results
    ).execute()
    
    videos = []
    for search_result in search_response.get('items', []):
        if search_result['id']['kind'] == 'youtube#video':
            videos.append({
                'title': search_result['snippet']['title'],
                'link': f"https://www.youtube.com/watch?v={search_result['id']['videoId']}"
            })
    
    return videos

def save_to_csv(videos, filename='youtube_results.csv'):
    df = pd.DataFrame(videos)
    df.to_csv(filename, index=False, quoting=csv.QUOTE_NONNUMERIC)

def main():
    query = input("Enter the category, artist, or channel to search: ")
    videos = search_youtube(query)
    save_to_csv(videos)
    print(f"Results saved to youtube_results.csv")

if __name__ == '__main__':
    main()

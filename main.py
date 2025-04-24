from src.extract_data import fetch_top_tracks
from src.extract_data_csv import json_to_dataframe
from src.analyse_track import analyze_top_tracks


from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd


app = FastAPI()

origins = [
    "http://localhost:3000", 
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,            
    allow_credentials=True,
    allow_methods=["*"],              
    allow_headers=["*"],              
)

@app.get("/")
def read_root():
    return {"message": "Welcome to Spotify Track Analytics API 🎧"}

@app.post("/fetch-track-by-artist")
async def fetch_track_by_artist(artist_name: str):
    # Step 1: Fetch and store JSON
    fetch_top_tracks(artist_name=artist_name)

    # Step 2: Convert to CSV
    json_path = f"data/{artist_name}.json"
    csv_path = f"data/{artist_name}.csv"
    json_to_dataframe(json_file_path=json_path, csv_file_path=csv_path)

    # Step 3: Analyze using PySpark
    top_tracks = analyze_top_tracks(csv_file_path=csv_path)

    # Step 4: Return output
    return {
        "artist": artist_name,
        "top_tracks": top_tracks
    }


# if __name__ == "__main__":

    # get the json file(data) from spotify => extract_data.py
    # artist = input("Enter artist name: ")
    # fetch_top_tracks(artist)

    # get the required data from json => extract_data_csv.py
    # df = json_to_dataframe("data/top_tracks.json", "data/top_tracks.csv")
    # print(df.head())

    # analyse and sort the data => analyse_track.py
    # analyze_top_tracks("data/top_tracks.csv", top_n=5)
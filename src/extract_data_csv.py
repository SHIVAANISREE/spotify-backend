import json
import pandas as pd


def json_to_dataframe(json_file_path, csv_file_path):
    # Load JSON
    with open(json_file_path, 'r') as file:
        tracks = json.load(file)

    # Extract fields
    extracted_data = []
    for track in tracks:
        extracted_data.append({
            "Track Name": track.get("name"),
            "Album": track.get("album", {}).get("name"),
            "Popularity": track.get("popularity"),
            "Duration (min)": round(track.get("duration_ms", 0) / 60000, 2),
            "Explicit": track.get("explicit"),
            "Spotify URL": track.get("external_urls", {}).get("spotify")
        })

    # Create DataFrame
    df = pd.DataFrame(extracted_data)

    # Save to CSV
    df.to_csv(csv_file_path, index=False, encoding='utf-8')
    print(f"DataFrame created and saved as CSV at: {csv_file_path}")

    return df

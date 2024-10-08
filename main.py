import os
import requests
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

BASE_URL = os.getenv("BASE_URL")
ROUTES_FILE = os.getenv("ROUTES_FILE")
ROOT_PATH = os.getenv("ROOT_PATH")


def download_file(url, target_path):
    try:
        if os.path.exists(target_path):
            print(f"File {target_path} already exist. Ignored.")
            return
        
        response = requests.get(url)
        
        if response.status_code == 200:
            Path(target_path).parent.mkdir(parents=True, exist_ok=True)

            with open(target_path, "wb") as f:
                f.write(response.content)
            
            print(f"File {target_path} successfully downloaded.")
        else:
            print(f"Failed to download {url}. Status code: {response.status_code}")
    except Exception as e:
        print(f"Error trying to download {url}: {e}")

with open(ROUTES_FILE, "r") as file:
    for line in file:
        route = line.strip()
        
        full_url = f"{BASE_URL}{route}"
        
        target_path = os.path.join(ROOT_PATH, route.lstrip('/'))
        
        download_file(full_url, target_path)
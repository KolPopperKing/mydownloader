from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import yt_dlp

app = FastAPI()

# זה החלק הקריטי שמונע את השגיאה שקיבלת
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # מאשר לכל אתר לפנות לשרת
    allow_credentials=True,
    allow_methods=["*"],  # מאשר את כל סוגי הפעולות (GET, POST וכו')
    allow_headers=["*"],
)

@app.get("/download")
def download(url: str):
    ydl_opts = {'format': 'best', 'extractor_args': {'youtube': {'player_client': ['android']}}}
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)
        return {"download_url": info['url']}

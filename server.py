from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware # הוספנו את זה
import yt_dlp

app = FastAPI()

# הוספת הרשאות CORS כדי שהאתר ב-GitHub יוכל לדבר עם השרת
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # מאפשר גישה מכל אתר
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/download")
def download(url: str):
    ydl_opts = {'format': 'best', 'extractor_args': {'youtube': {'player_client': ['android']}}}
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)
        return {"download_url": info['url']}

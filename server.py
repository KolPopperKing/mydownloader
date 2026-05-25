from fastapi import FastAPI
import yt_dlp

app = FastAPI()

@app.get("/download")
def download(url: str):
    ydl_opts = {'format': 'best', 'extractor_args': {'youtube': {'player_client': ['android']}}}
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)
        return {"download_url": info['url']}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
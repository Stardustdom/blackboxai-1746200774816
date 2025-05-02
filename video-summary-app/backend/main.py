from fastapi import FastAPI, File, UploadFile, Form
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional
import uvicorn

app = FastAPI()

# Allow CORS for frontend running on different origin
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class SummaryRequest(BaseModel):
    video_url: Optional[str] = None

@app.post("/summarize")
async def summarize_video(video_url: Optional[str] = Form(None), file: Optional[UploadFile] = File(None)):
    """
    Accepts a video URL or uploaded video file, simulates transcription and summarization,
    and returns a summary.
    """
    # For demonstration, simulate transcription and summarization
    if video_url:
        transcript = f"Simulated transcript of video at URL: {video_url}"
    elif file:
        transcript = f"Simulated transcript of uploaded video file: {file.filename}"
    else:
        return {"error": "No video URL or file provided"}

    # Simulate summarization (in real app, call transcription and summarization APIs)
    summary = f"Summary: This is a simulated summary of the transcript: '{transcript[:100]}...'"

    return {"summary": summary}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

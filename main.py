from fastapi import FastAPI, File, UploadFile
import whisper
import os
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # of vervang "*" met bv. ["https://vapi.ai"] voor meer veiligheid
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
model = whisper.load_model("base")

@app.post("/transcribe")
async def transcribe_audio(audio: UploadFile = File(...)):
    temp_file = "temp_audio.wav"
    with open(temp_file, "wb") as f:
        f.write(await audio.read())

    result = model.transcribe(temp_file, language="nl")
    os.remove(temp_file)

    return {"text": result["text"]}

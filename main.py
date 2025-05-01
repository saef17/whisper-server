from fastapi import FastAPI, File, UploadFile
import whisper
import os

app = FastAPI()
model = whisper.load_model("base")

@app.post("/transcribe")
async def transcribe_audio(audio: UploadFile = File(...)):
    temp_file = "temp_audio.wav"
    with open(temp_file, "wb") as f:
        f.write(await audio.read())

    result = model.transcribe(temp_file, language="nl")
    os.remove(temp_file)

    return {"text": result["text"]}

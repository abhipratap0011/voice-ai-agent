import os
import json
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv

from agent.stt import transcribe
from agent.llm import respond
from agent.tts import synthesize
from agent.memory import Memory

load_dotenv()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def get():
    with open("frontend/index.html") as f:
        return HTMLResponse(f.read())


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    memory = Memory()
    audio_chunks = []

    try:
        while True:
            message = await websocket.receive()

            if "bytes" in message:
                audio_chunks.append(message["bytes"])

            elif "text" in message:
                data = json.loads(message["text"])

                if data.get("type") == "end":
                    if not audio_chunks:
                        continue

                    await websocket.send_json({
                        "type": "status",
                        "message": "Transcribing..."
                    })

                    audio_bytes = b"".join(audio_chunks)
                    audio_chunks = []

                    transcript = transcribe(audio_bytes)

                    await websocket.send_json({
                        "type": "transcript",
                        "text": transcript
                    })

                    await websocket.send_json({
                        "type": "status",
                        "message": "Thinking..."
                    })

                    history = memory.get()
                    response_text = respond(transcript, history)

                    memory.add("user", transcript)
                    memory.add("assistant", response_text)

                    await websocket.send_json({
                        "type": "response",
                        "text": response_text
                    })

                    await websocket.send_json({
                        "type": "status",
                        "message": "Speaking..."
                    })

                    audio_response = synthesize(response_text)
                    await websocket.send_bytes(audio_response)

                    await websocket.send_json({
                        "type": "status",
                        "message": "Ready"
                    })

    except WebSocketDisconnect:
        memory.clear()
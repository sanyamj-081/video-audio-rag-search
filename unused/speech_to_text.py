import json

# model = whisper.load_model("large-v2")
# result = model.transcribe(audio = "audios/Camera_1_sample.mp3",
#                           language = "hi",
#                           task = "translate",
#                           word_timestamps= False)

with open("audios/output.json", "r", encoding="utf-8") as f:
    data = json.load(f)

chunks = []
for segment in data["segments"]:
    chunks.append(
        {"start: ": segment["start"],
         " end: ": segment["end"],
         " text: ": segment["text"]
         })

print(chunks)
with open("output.json", "w", encoding="utf-8") as f:
    json.dump(chunks, f, indent=4)

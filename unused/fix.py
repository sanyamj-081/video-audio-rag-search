import json

with open(r"D:\rag-ai\json\Camera_8.mp3.json", "r", encoding="utf-8") as f:
    data = json.load(f)

fixed_chunks = []

for chunk in data["chunks: "]:
    fixed_chunks.append({
        "number": chunk["number: "],
        "title": chunk["title: "],
        "start": chunk["start: "],
        "end": chunk["end: "],
        "text": chunk["text: "].strip()
    })

fixed_output = {
    "chunks": fixed_chunks,
    "text": data["text: "].strip()
}

with open(r"D:\rag-ai\json\Camera_8.mp3.json", "w", encoding="utf-8") as f:
    json.dump(fixed_output, f, indent=2, ensure_ascii=False)

print("✅ JSON fixed and saved as Camera_8_fixed.json")

import logging

import whisper

import json

model = whisper.load_model("large-v2")

# audios = os.listdir("audios")

audios = ["Camera_2.mp3","Camera_7.mp3","Camera_1.mp3"]

logging.basicConfig(
    format="%(asctime)s %(message)s",
    datefmt="%I:%M:%S %p",
    level=logging.INFO
)
for audio in audios:
    if "_" in audio:
        number = audio.split("_")[1][:-4]
        title = audio[:-4]
    else:
        continue

    print(number, title)
    logging.info("Chunking started for %s %s ....", number, title)
    # print(f"Chunking started for {number} {title} ....")

    result = model.transcribe(audio=f"audios/{audio}",
                              language="hi",
                              task="translate",
                              word_timestamps=False)
    # print("Chunking end....")
    logging.info("Chunking end for %s %s ....", number, title)


    chunks = []
    for segment in result["segments"]:
        chunks.append(
            {
                "number": number,
                "title": title,
                "start": segment["start"],
                "end": segment["end"],
                "text": segment["text"]
            })

    chunks_with_metadata = {"chunks: ": chunks,
                            "text: ": result["text"]}

    # print("Writing chunks...")
    logging.info("Writing Chunks started for %s %s ....", number, title)


    with open(f"json/{audio}.json", "w", encoding="utf-8") as f:
        json.dump(chunks_with_metadata, f, indent=4)

    # print(f"Done with :{number}, {title}")
    logging.info("Done with %s %s ....", number, title)

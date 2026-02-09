import joblib
import json
import numpy as np
import requests
from sklearn.metrics.pairwise import cosine_similarity


def create_embedding(text):
    result = requests.post("http://localhost:11434/api/embed", json= {
    "model": "bge-m3",
    "input": text
    })

    embedding = result.json()["embeddings"] #[0:5]
    return embedding


def inference(prompt):
    result = requests.post("http://localhost:11434/api/generate", json={
        "model": "llama3.2",
        "prompt": prompt,
        "stream": False
    })
    response = result.json()
    # print(response)
    return response


df = joblib.load('embeddings.joblib')

incoming_query = input("Enter your query: ")
question_embedding = create_embedding(incoming_query)[0]

# Find similarity of question_embedding with other embeddings
similarities = cosine_similarity(np.vstack(df['embedding']),[question_embedding]).flatten()
top_results = 20
max_indx = similarities.argsort()[::-1][0:top_results]
new_df = df.loc[max_indx]

prompt = f''' These chunks are from playlist of psychology of money playlist. Here are video subtitle chunks containing video title, video number, video start time, video end time and video text.
Video chunks are as follows:
{new_df[["title", "number", "start", "end","text"]].to_json(orient='records')}
----------------------------------------
"{incoming_query}"
User asked this question related to video chunks, you have to answer this question based on the video chunks. how much content is taught in which video(with time stamp) and guide the user to go through the particular video. If user answer is not related to video chunks, then tell him that you can answer related to videos only.
'''
with open("prompt.txt", "w") as f:
    f.write(prompt)

response = inference(prompt)
print(response)
with open("response.txt", "w") as f:
    f.write(json.dumps(response))
# for index, item in new_df.iterrows():
#     print(index, item['number'], item['title'], item['text'], item['start'], item['end'])
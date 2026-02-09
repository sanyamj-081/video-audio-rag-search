# RAG-AI Project

## Overview
This project processes audio and video files to extract, preprocess, and analyze speech/text data. It includes scripts for converting videos to audio, transcribing audio, preprocessing JSON outputs, and handling user queries. The workspace is organized for easy extension and integration with retrieval-augmented generation (RAG) pipelines.

## Quick Start (for Forked Repos)
**Note:** Audio, video, and JSON data files are not included in the repository. You must provide your own files in the correct folders as described below.

### 1. Clone the Repository
```powershell
git clone <https://github.com/sanyamj-081/video-audio-rag-search>
cd rag-ai
```

### 2. Install Dependencies
Ensure you have Python 3.8+ installed. Then run:
```powershell
pip install -r requirements.txt
```

### 3. Prepare Your Data
- Place your **video files** (`.mp4`) in the `videos/` directory.
- The pipeline will generate audio files (`.mp3`) in the `audios/` directory.
- Transcription outputs (`.json`) will be saved in the `json/` directory.

### 4. Run the Processing Pipeline
1. **Convert videos to audio:**
   ```powershell
   python video_to_mp3.py
   ```
2. **Transcribe audio to JSON:**
   ```powershell
   python mp3_to_json.py
   ```
3. **Preprocess JSON files and generate embeddings:**
   ```powershell
   python preprocess_json.py
   ```
4. **Process user queries:**
   ```powershell
   python process_user_query.py
   ```

### 5. Output
- Embeddings are stored in `embeddings.joblib`. This file get created once embeddings are built.
- Responses to queries are written to `response.txt`.

## Directory Structure
```
rag-ai/
├── audios/           # Extracted audio files (.mp3)
├── json/             # Transcription outputs (.json)
├── videos/           # Source video files (.mp4)
├── unused/           # Experimental/unused scripts and outputs
├── embeddings.joblib # Embedding data for RAG
├── mp3_to_json.py    # Audio-to-JSON transcription script
├── preprocess_json.py# Preprocessing JSON outputs
├── process_user_query.py # Handles user queries
├── prompt.txt        # Prompt template
├── response.txt      # Output responses
├── requirements.txt  # Project necessary packages
├── Readme.md         # Project documentation
```

## Notes
- **Data files (videos, audios, JSON) are not tracked in git.** You must add your own files to the appropriate folders.
- The scripts will create output files as needed.
- For best results, use high-quality audio/video files.

## License
MIT License

## Author
Sanyam Jain

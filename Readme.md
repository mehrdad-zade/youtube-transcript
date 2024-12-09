# YouTube Audio to Text Converter

This Python script downloads the audio from a given YouTube video link, extracts the audio into text using OpenAI Whisper, and displays the transcribed text. After processing, it asks whether to delete the downloaded audio file.

## Prerequisites

1. **Python**: Ensure Python 3.8+ is installed on your system.
2. **ffmpeg**: Install ffmpeg, required for audio processing.

### Install ffmpeg

#### macOS
```bash
brew install ffmpeg
```

#### windows
- Download prebuilt binaries: ffmpeg.org/download.
- Add the binary path to your system's PATH.

#### Linux
```bash
sudo apt update
sudo apt install ffmpeg
```
import os
import sys
import subprocess
import whisper
from pathlib import Path
import tkinter as tk
from tkinter import simpledialog, messagebox

def download_audio(youtube_url, output_dir="downloads"):
    """
    Downloads the audio of a YouTube video using yt-dlp.
    """
    try:
        # Ensure output directory exists
        Path(output_dir).mkdir(parents=True, exist_ok=True)

        # Filepath for the audio
        audio_file = f"{output_dir}/audio.mp3"

        # Download audio using yt-dlp
        subprocess.run([
            "yt-dlp", 
            "-x", 
            "--audio-format", "mp3", 
            "-o", audio_file, 
            youtube_url
        ], check=True)

        return audio_file
    except subprocess.CalledProcessError as e:
        print("Failed to download audio:", e)
        return None

def transcribe_audio(audio_path):
    """
    Transcribes audio to text using Whisper.
    """
    try:
        # Load Whisper model
        model = whisper.load_model("base")

        # Transcribe the audio
        result = model.transcribe(audio_path)

        return result["text"]
    except Exception as e:
        print("Error during transcription:", e)
        return None

def get_youtube_url():
    """
    Display a UI to get the YouTube URL.
    """
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    youtube_url = simpledialog.askstring("YouTube URL", "Enter the YouTube URL:")
    if not youtube_url:
        messagebox.showwarning("Input Error", "No YouTube URL was provided.")
        sys.exit(1)
    return youtube_url

def main():
    youtube_url = get_youtube_url()

    print("Downloading audio...")
    audio_file = download_audio(youtube_url)

    if not audio_file or not os.path.exists(audio_file):
        print("Audio download failed. Exiting.")
        return

    print("Transcribing audio...")
    transcript = transcribe_audio(audio_file)

    if transcript:
        print("\nTranscription:\n")
        print(transcript)
    else:
        print("Transcription failed.")

    # Prompt to delete the file
    delete_choice = input(f"\nDo you want to delete the downloaded file ({audio_file})? (yes/no): ").strip().lower()
    if delete_choice == "yes":
        os.remove(audio_file)
        print("File deleted.")
    else:
        print(f"File retained at: {audio_file}")

if __name__ == "__main__":
    main()


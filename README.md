# Roku MKV Fixer

MKV does not work with Roku because of the audio format.

## Install

- On Mac: `brew install ffmpeg`
- On windows: figure it out yourself
- On linux: `sudo apt-get install ffmpeg`
- Download roku_mkv_fixer.py into directory with MKV files you want to convert
- Run with python 2.7 `python roku_mkv_fixer.py`

## How this works

Given MKV files the fixer will fix the audio issue by searching through the folder for all MKV files.
It will then take those MKV files and convert them into mp4 files (which Roku can play correctly).
Then, to mark the MKV files converted, they will be renamed to indicate their doneness.

Please read roku_mkv_fixer.py comments for details.
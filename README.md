[![Travis CI Shield](https://travis-ci.com/github/mynameisvinn/Vizham)](https://travis-ci.com/github/mynameisvinn/Vizham)

# Vizham
Video indexing/hashing for video lookups.

## How it works
1) Extracts audio file from video with `Librosa`.
2) Generate fingerprints from audio files with `chromaprint`.
3) Subsegment matching
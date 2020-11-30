[![Travis CI Shield](https://travis-ci.com/mynameisvinn/Vizham.svg?branch=master)](https://travis-ci.com/github/mynameisvinn/Vizham)
[![codecov](https://codecov.io/gh/mynameisvinn/Vizham/branch/master/graph/badge.svg?token=O74L63GGSW)](https://codecov.io/gh/mynameisvinn/Vizham)


# Vizham
Video indexing/hashing for video lookups.

## How it works
1) Extracts audio file from video with `Librosa`.
2) Generate fingerprints from audio files with `chromaprint`.
3) Subsegment matching
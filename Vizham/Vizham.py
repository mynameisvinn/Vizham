import os
import acoustid
from chromaprint import decode_fingerprint
from typing import List
from moviepy.editor import AudioFileClip


def generate_fingerprint(fname: str) -> List[int]:
    """return an audio fingerprint for a video file.
    """
    audioclip = AudioFileClip(fname)
    audioclip.write_audiofile("temp.wav")

    duration, fp_encoded = acoustid.fingerprint_file("temp.wav")
    fingerprint, version = decode_fingerprint(fp_encoded)

    os.remove("temp.wav")
    return fingerprint


def contains_snippet(long: List[int], short: List[int]) -> bool:
    """returns bool if long contains short.
    """
    for start in range(len(long)):
        fragment_length = len(short)
        snippet = long[start: start + fragment_length]

        num_matches = 0
        for a, b in zip(snippet, short):
            if a - b == 0:
                num_matches += 1
            
        if num_matches > 2:
            print(num_matches, "matches", "at index", start)
            return True
    return False
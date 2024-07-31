import random
import json
from functools import cache
from typing import *


PHIGROS_DATA_FILE = open("./data/song_name/phigros_data.txt", mode="r", encoding="utf-8")
PHIGROS_SONG_DATA = PHIGROS_DATA_FILE.readlines()
PHIGROS_SONG_DATA = [song[:-1] for song in PHIGROS_SONG_DATA]
PHIGROS_DATA_FILE.close()


@cache
def get_song_data():
    return PHIGROS_SONG_DATA


class AutoLetter:
    def __init__(self, sz: int = None):
        self.letter_list = []
        self.guessed_letter = []
        self.guessed_song = []
        self.opener = []

    def generate_new_letter_game(self, size: int, _type: Literal["song", "composer"])\
            -> Union[None, 'not allow']:
        self.letter_list.clear()
        self.guessed_letter.clear()
        match _type:
            case "song":
                for x in range(size):
                    self.opener.append(None)
                    self.guessed_song.append(False)
                self.letter_list = random.sample(PHIGROS_SONG_DATA, size)
            case "composer":
                return "not allow"
            case _:
                raise ValueError("Now allowed value")

    def generate_quote_string(self):
        string_builder = ""
        string_builder += f"Guessed Letter: " + ",".join(self.guessed_letter) + "\n"
        for idx, song in enumerate(self.letter_list):
            r_idx = idx+1
            string_builder += f"{r_idx}. "
            if song in self.guessed_song:
                string_builder += song
            else:
                flag = True
                for ch in song:
                    if ch.lower() not in self.guessed_letter:
                        string_builder += "*"
                        flag = False
                    else:
                        string_builder += ch
                if flag:
                    self.guessed_song[idx] = True
            string_builder += "\n"
        return string_builder

    def generate_scoreboard_admin_string(self):
        string_builder = ""
        string_builder += f"Guessed Letter: " + ",".join(self.guessed_letter) + "\n"
        for idx, song in enumerate(self.letter_list):
            r_idx = idx+1
            string_builder += f"{r_idx}. "
            string_builder += song
            string_builder += "\n"
        return string_builder

    def open_string(self, ch: str):
        if ch.lower() in self.guessed_letter:
            return "already opened"
        else:
            self.guessed_letter.append(ch.lower())

    def open_song(self, idx: int):
        self.guessed_song.append(self.letter_list[idx-1])


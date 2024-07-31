import random
from typing import *
import kern
from data.lang.lang import lang_string


PHIDATA2 = kern.get_song_data()


class AutoLetterKern2:
    def __init__(self, lang: Literal["cn", "en"], samp: list[str] = PHIDATA2, sz: int = 0,
                 no_resort: bool=False):
        self.name = []
        self.truly_name = []
        self.letters = set()
        self.already = set()
        self.ln = lang
        self.size = sz
        self.smp = samp
        if(no_resort == True):
            self.truly_name = samp

    def create_new_game(self, sz: int):
        self.__init__(self.ln)
        self.size = sz
        self.truly_name = random.sample(self.smp, sz)
        self.refresh()

    @staticmethod
    def hide_the_song_name(song_name: str, letters: set[str]):
        hid_name = ""
        for ch in song_name:
            if ch.lower() in letters or ch == ' ':
                hid_name += ch
            else:
                hid_name += "*"
        return hid_name

    def song_information(self):
        self.refresh()
        builder = lang_string["output_prompt"]["guessed_letter"][self.ln]
        builder += " ".join(self.letters)
        builder += "\n"
        for idx, song in enumerate(self.name):
            builder += f"{idx+1}. {song}\n"
        return builder

    def song_admin_scoreboard(self):
        self.refresh()
        builder = lang_string["output_prompt"]["guessed_letter"][self.ln]
        builder += " ".join(self.letters)
        builder += "\n"
        for idx, song in enumerate(self.truly_name):
            builder += f"{idx+1}. {song}\n"
        return builder

    def open_letter(self, let: str):
        self.letters.add(let.lower())

    def open_song(self, song: int):
        self.already.add(self.truly_name[song-1])

    def refresh(self):
        self.name.clear()
        for lt in self.truly_name:
            if lt in self.already:
                self.name.append(lt)
                continue
            hid_name = AutoLetterKern2.hide_the_song_name(lt, self.letters)
            # if hid_name == lt:
            #     self.already.append(lt)
            self.name.append(hid_name)

    def undo(self, typ: Literal["lt", "sn"] = "lt"):
        match typ:
            case "lt":
                self.letters.pop()
                self.refresh()
            case "sn":
                self.already.pop()
                self.refresh()
            case _:
                raise ValueError("argument typ error")

    def is_finished(self) -> bool:
        self.refresh()
        return len(self.already) == len(self.truly_name)

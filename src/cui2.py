from kern2 import *
from data.lang.lang import lang_string
from json import load

if __name__ == "__main__":
    with open("./data/profile_setting.json", "r+", encoding="utf-8") as file:
        profile_setting = load(file)
        file.close()
    try:
        language = profile_setting["lang"]
        if language not in {'cn', 'en'}:
            language = "en"
    except Exception as e:
        language = "en"
        print("Warning 1001: profile load error")
        print("Exception Information: ", repr(e))
        print("We will you the common setting to preparer your software.")

    print(lang_string["beginning"][language])
    game_kernel: AutoLetterKern2 = AutoLetterKern2(lang=language)

    def show_game_state_un_admin():
        print(game_kernel.song_information())

    def show_game_state():
        print(game_kernel.song_information())
        print("Administrator: ")
        print(game_kernel.song_admin_scoreboard())
    while True:
        command_str: str = input(">").strip()
        if command_str == "":
            continue
        cmd_st = command_str.split(" ")
        if len(cmd_st) == 1:
            cmd = cmd_st[0]
            arg = []
        else:
            cmd, *arg = cmd_st
        match cmd:
            case "help":
                ...
            case "start":
                sz_string: str
                sz: int
                if len(arg) == 0:
                    sz_string = input(lang_string["input_prompt"]["input_amount"][language])
                elif len(arg) == 1:
                    sz_string = arg[0]
                else:
                    print("Error 2001: Useless Argument", ",".join(arg[1:]))
                    continue
                try:
                    sz = int(sz_string.strip())
                except Exception as e:
                    print("Error 2000: Unknown Exception: ", e)
                    continue
                game_kernel = AutoLetterKern2(lang=language)
                game_kernel.create_new_game(sz=sz)
                print("Game has built!")
                show_game_state()
            case "use_list":
                file_string: str
                if len(arg) == 0:
                    file_string = input(lang_string["input_prompt"]["input_file_path"][language])
                else:
                    file_string = " ".join(arg)
                file_data: list[str]
                with open(f"./song_list/{file_string}.txt", "r+", encoding="utf-8") as file:
                    file_data = [f[:-1] for f in file.readlines()]
                    file.close()
                game_kernel = AutoLetterKern2(lang=language, samp=file_data, no_resort=True,
                    sz=len(file_data))
                # game_kernel.create_new_game(sz=len(file_data))
            case "show":
                show_game_state_un_admin()
            case "admin":
                show_game_state()
            case "let":
                game_kernel.open_letter(let=arg[0])
                # show_game_state()
            case "song":
                game_kernel.open_song(song=int(arg[0]))
                # show_game_state()
            case "undo":
                if len(arg) == 0:
                    game_kernel.undo()
                if arg[0] == "lt":
                    game_kernel.undo(typ="lt")
                elif arg[0] == "sn":
                    game_kernel.undo(typ="sn")
                else:
                    print("No available command")
                    continue
                show_game_state()
            case "quit" | "exit":
                quit(0)
            case _:
                print("No available command")
                continue

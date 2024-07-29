from kern import *

if __name__ == "__main__":
    print("音游开字母 Administrator Ver.")
    kernel = AutoLetter()
    while True:
        prompt = input(f">>").strip()
        match prompt.lower():
            case "start":
                sz = int(input("请输入需要的歌的个数:>"))
                kernel.generate_new_letter_game(sz, "song")
                print("已成功创建了一场猜字母游戏.")
                print()
                print(kernel.generate_quote_string())
                print()
                print("Administrator Ver:")
                print(kernel.generate_scoreboard_admin_string())
            case "open_let":
                letter = input("请输入要开的字符:>")
                if len(letter) > 1:
                    print("Not Allowed")
                    continue
                if message := kernel.open_string(letter):
                    print(message)
                print(kernel.generate_quote_string())
                print()
                print("Administrator Ver:")
                print(kernel.generate_scoreboard_admin_string())
            case "open_song":
                song = int(input("请输入要开的歌曲下标:>"))
                kernel.open_song(song - 1)
                print(kernel.generate_quote_string())
                print()
                print("Administrator Ver:")
                print(kernel.generate_scoreboard_admin_string())
            case "quit":
                quit(0)
            case _:
                ...

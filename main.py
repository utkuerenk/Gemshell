from geminimodule import AISend;import colorama;colorama.init();import json;from os import system
def main():
    try:
        system("title Gemshell")
        while 1:i=input(colorama.Fore.WHITE+"Enter text >> ");print("");returnn=AISend(i);print(colorama.Fore.YELLOW+returnn)
    except Exception as e:input(f"[Error]: {e}")
if __name__=="__main__":main()

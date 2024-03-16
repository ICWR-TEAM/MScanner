import re, os, argparse

blacklist = open("wordlist.txt", "r").read()
explode_blacklist = blacklist.split("\n")


class main:

    global explode_blacklist

    def __init__(self, Target):
        self.title()
        print("Loading...")
        self.res_dir = [Target]
        self.scan_directory(Target)

    def proc(self, datas):
        print("\033[32mResult scan:")
        for data in datas:
            print("\033[37mSuspect: \033[33m{} \033[37m| \033[37mCode: \033[31m{}".format(data["file"], data["code"]))
    
    def scan_directory(self, directory):
        for item in os.listdir(directory):
            item_path = os.path.join(directory, item)
            if os.path.isdir(item_path):
                self.res_dir.append(item_path)
                self.scan_directory(item_path)
            else:
                self.get_file(item_path, explode_blacklist)

    def get_file(self, paths, suspect_code):
        pattern_suspect_code = r'\b(' + '|'.join(map(re.escape, suspect_code)) + r')\b'
        res = paths
        op_file = open(res, "rb").read().decode("utf-8", errors="ignore")
        find_pattern = re.findall(pattern_suspect_code, op_file)
        for key, value in enumerate(find_pattern):
            if value:
                print("\033[37m[*] Suspect: \033[33m{} \033[37m| \033[37mCode: \033[31m{}".format(res, value))                
    
    def title(self):
        print("""
___  ___ _____
|  \/  |/  ___|
| .  . |\ `--.   ___   __ _  _ __   _ __    ___  _ __ 
| |\/| | `--. \ / __| / _` || '_ \ | '_ \  / _ \| '__|
| |  | |/\__/ /| (__ | (_| || | | || | | ||  __/| |   
\_|  |_/\____/  \___| \__,_||_| |_||_| |_| \___||_|   
        """)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--target", help="Provide your target directory, example /", type=str, required=True)
    args = parser.parse_args()
    if args.target:
        try:
            main(args.target)
        except FileNotFoundError:
            print("Directory does not exist, please check the target directory!")
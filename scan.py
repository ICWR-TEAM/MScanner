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
        result = self.get_file(self.res_dir, explode_blacklist)
        self.proc(result)

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

    def get_file(self, paths, suspect_code):
        result = []
        for path in paths:
            for item in os.listdir(path):
                item_path = os.path.join(path, item)
                if os.path.isdir(item_path):
                    continue
                else:
                    pattern_suspect_code = r'\b(' + '|'.join(map(re.escape, suspect_code)) + r')\b'
                    res = path + "/" + item
                    op_file = open(res, "rb").read().decode("utf-8", errors="ignore")
                    find_pattern = re.findall(pattern_suspect_code, op_file)
                    result_value_pattern = []
                    for index, value in enumerate(find_pattern):
                        if value:
                            dict_res = {
                                "file": res,
                                "code": value
                            }
                            result_value_pattern.append(dict_res)
                    rm_duplicate_result = list(set(tuple(item.items()) for item in result_value_pattern))
                    rm_duplicate_result = [dict(item) for item in rm_duplicate_result]
                    for ress in rm_duplicate_result:
                        result.append(ress)
        return result
    
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
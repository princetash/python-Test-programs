from pathlib import Path
import json

def write_fav_num(path):
    fav_num = input("What is your favorite number? ")
    content = json.dumps(fav_num)
    path.write_text(content)
    return fav_num

def read_fav_num(path):
    if path.exists():
        content = path.read_text()
        number = json.loads(content)
        return number
    else: return None

def check_num():
    path = Path('maintests.json')
    fav_num = read_fav_num(path)
    if fav_num:
        print(f"The favorite number is {fav_num}")
    else:
        number = write_fav_num(path)
        print(f"We have written your fav number {number}")

check_num()
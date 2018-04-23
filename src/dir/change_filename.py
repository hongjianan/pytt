import sys
import os


def change_name(path):
    for _, video_path, _ in os.walk(path):
        break

    print(video_path)

    for dir in video_path:
        entry_file = dir + '/1/entry.json'
        try:
            file = open(entry_file, 'rb')
            content = file.read(1024)
            json
        except e:
            print('no entry file in', dir)
            continue
        


if __name__ == '__main__':
    dirpath = sys.argv[1]
    change_name(dirpath)

import os
import glob
import os.path


def listdir_tt(path):
    for filename in os.listdir(path):
        print('dir', filename)


def glob_tt(path):
    for filename in glob.glob(path):
        print(filename)


def showdir(args, dirname, filenames):
    print('dir: %s' % dirname)
    for filename in filenames:
        print('file: %s' % filename)


def pathwalk_tt(path):
    os.path.walk(path, showdir, None)


def walk_tt(path):
    for dirpath, dirnames, filenames in os.walk(path):
        print('dir', dirpath, dirnames)
        for filename in filenames:
            print('file', filename)


if __name__ == '__main__':
    # listdir_tt('../base')
    glob_tt('../base')
    # pathwalk_tt('../base')
    # walk_tt('../base')

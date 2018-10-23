import sys

FILE_NAME = "black_hole.txt"

def write_hole():
    with open(FILE_NAME, "w+") as f:
        f.write("01234")
        f.seek(1024)
        f.write("56789")


def read_hole():
    with open(FILE_NAME, "r+") as f:
        text = f.read(10)
        print("%s===" % text)


def run():
    # write_hole()
    read_hole()
    sys.argv[1]


if __name__ == "__main__":
    run()

import sys
import os


def list_files(dir):
    return os.listdir(dir)

def file_path(dir):
    filename = list_files(dir)
    return os.path.join(dir, filename[0]) 

def file_abs_path(dir):
    path = file_path(dir)
    return os.path.abspath(path)


def main():
    print(list_files(sys.argv[1]))
    #print(file_path(sys.argv[1]))
    #print(file_abs_path(sys.argv[1]))


if __name__ == "__main__":
    main()

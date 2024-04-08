import os


def main():
    filename = 'asdf.xxx'
    if not os.path.isfile(filename):
        return None

    open(filename, 'r')

if __name__ == "__main__":
    # execute as docker
    main()
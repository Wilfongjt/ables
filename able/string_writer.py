import os

class StringWriter():
    def __init__(self, folder_filename, content_string):
        with open(folder_filename, 'w') as f:
            f.write(content_string)

def main():
    import shutil

    content_string = 'A\nB\nC'
    folder = '{}/Development/Temp/string_writer'.format(os.environ['HOME'])
    folder_filename = '{}/string_writer.txt'.format(folder)

    # setup
    contents = 'A=a\nB=b'
    os.makedirs(folder, exist_ok=True)

    # test
    assert(StringWriter(folder_filename, content_string))
    assert(os.path.isfile(folder_filename))

    # cleanup
    if os.path.isfile(folder_filename):
        shutil.rmtree(folder)


if __name__ == "__main__":
    # execute as docker
    main()

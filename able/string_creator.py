import os

class CreatorString(str):
    ##__FileReadable__
    ##* enable standalone version for testing and ad hoc cases
    def __init__(self, folder_filename, string_value):
        #super().__init__(self)
        self.folder_filename=folder_filename

    def __new__(cls, folder_filename, string_value):
        ##* Fail when file exists
        fileExists = os.path.isfile(folder_filename)
        #print('file', folder_filename)
        #print('exists', fileExists)
        if fileExists:
            raise Exception('Failed, file exists: {}'.format(folder_filename))
        with open(folder_filename, 'w') as f:
            f.write(string_value)
            contents = string_value
        instance = super().__new__(cls, contents)
        return instance


def main():
    from able.lb_util import LbUtil
    #from file_createable import FileCreateable
    folder = '{}/Development/Temp/writer_string'.format(os.environ['HOME'])
    folder_file = '{}/writer.txt'.format(folder)

    # setup
    contents = 'A=a\nB=b'
    LbUtil().create_folders(folder)
    #FileCreateable().create_file(folder_filename=folder_file,default_contents=new_contents)
    #assert (LbUtil().folderfile_exists(folder_file))

    # test
    try:
        #print('writer',CreatorString(folder_file, new_contents))
        assert (CreatorString(folder_file, contents) == contents)
        #print('read_file', ReaderString(folder_file))
    except:
        print('running clean up')

    # cleanup
    LbUtil().delete_folderfilename(folder_file)

    #testFileReadable_mixin_str()
    #testFileReadable_mixin_list()

if __name__ == "__main__":
    # execute as docker
    main()
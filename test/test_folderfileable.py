import unittest
import os
import shutil
from able import FolderFileable

class TestFolderFileable(unittest.TestCase):

    def setUp(self):
        self.folder = '{}/Development/Temp/folderfileable'.format(os.environ['HOME'])
        self.filename = 'folder_filename.txt'
        self.folder_filename = '{}/{}'.format(self.folder, self.filename)
        # setup
        contents = 'A=a\nB=b'
        os.makedirs(self.folder, exist_ok=True)

        # create a file to read
        with open(self.folder_filename, 'w') as f:
            f.write(contents)

    def test_init(self):
        class Example(FolderFileable):
            def __init__(self):
                FolderFileable.__init__(self)

        assert (Example().setFolderFilename(self.folder_filename).folderfile_exists())
        assert (Example().setFolderFilename(self.folder_filename).folderfile_exists(self.folder_filename))

        assert (Example().setFolderFilename(self.folder_filename).getFolderFile()==self.folder_filename)
        assert (Example().setFolderFilename(self.folder_filename).getFolder()==self.folder)
        assert (Example().setFolderFilename(self.folder_filename).getFilename()==self.filename)

    def tearDown(self):
        fileExists = os.path.isfile(self.folder_filename)
        if fileExists:
            shutil.rmtree(self.folder)

if __name__ == '__main__':
    unittest.main()
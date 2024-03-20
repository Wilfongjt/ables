import unittest
import os
import shutil
from able import FileEnv

class TestFileEnv(unittest.TestCase):

    def setUp(self) -> None:
        self.folder = '{}/Development/client/workspace/project'.format(os.environ['HOME'])
        self.filename = 'sample.env'
        self.folder_filename = '{}/{}'.format(self.folder, self.filename)
        os.makedirs(self.folder, exist_ok=True)
        self.default_contents='A=github\nB=docker'

        self.default_contents = '# enviroment variables\n'
        self.default_contents += '# format example, delete next line when not needed\n'
        self.default_contents += 'SAMPLE_VALUE=abc'
        with open(self.folder_filename, 'w') as f:
            f.write(self.default_contents)

    def test_init(self):
        assert (FileEnv(self.folder_filename).getFolderFile() == self.folder_filename)
        assert (FileEnv(self.folder_filename).read() == self.default_contents.split('\n'))
        assert ('SAMPLE_VALUE' in os.environ)
        assert ('abc' == os.environ['SAMPLE_VALUE'])

    def tearDown(self):
        fileExists = os.path.isfile(self.folder_filename)
        if fileExists:
            shutil.rmtree(self.folder)

if __name__ == '__main__':
    unittest.main()
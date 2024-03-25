import os
import unittest
import shutil

from able import DataString

class TestDataString(unittest.TestCase):

    def test_init(self):
        assert (DataString() == '')
        assert (DataString('') == '')
        assert (DataString('A line') == 'A line')

    def test_delete(self):
        # delete
        assert (DataString().delete('') == '')
        assert (DataString().delete('A line') == '')
        assert (DataString('A line').delete('B line') == 'A line')

        assert (DataString('A line').delete('A line') == '')

        assert (DataString()
                .setHardFail(False)
                .insert('A line')
                .insert('B line')
                .delete('A line') == 'B line')
        assert (DataString()
                .setHardFail(False)
                .insert('A line')
                .insert('B line')
                .delete('B line') == 'A line')

    def test_insert(self):
        # insert

        assert (DataString().setHardFail(False).insert('A line') == 'A line')
        assert (DataString()
                .setHardFail(False)
                .insert('A line')
                .insert('A line') == 'A line')
        assert (DataString()
                .setHardFail(False)
                .insert('A line')
                .insert('B line') == 'A line\nB line')

    def test_update(self):
        # update dup=False
        assert (DataString()
                .setHardFail(False)
                .update('', '') == '')
        assert (DataString()
                .setHardFail(False)
                .update('', 'A line') == '')
        assert (DataString('A line')
                .setHardFail(False)
                .update('A line', 'A line') == 'A line')

        assert (DataString('A line\nB line')
                .setHardFail(False)
                .update('A line', 'B line') == 'A line\nB line')
        assert (DataString('A line\nB line')
                .setHardFail(False)
                .update('A line', 'C line') == 'C line\nB line')
        assert (DataString('A line\nB line')
                .setHardFail(False)
                .update('B line', 'C line') == 'A line\nC line')

    def test_upsert(self):
        # Upsert

        # print("A upsert given '' replace '' with '' -> ''")

        assert (DataString()
                .setHardFail(False)
                .upsert('', '') == '')

        # print("B upsert given '' replace '' with A  -> A")

        assert (DataString()
                .setHardFail(False)
                .upsert('', 'A') == 'A')

        # print("C upsert given A  replace A  with A  -> A")

        assert (DataString('A')
                .setHardFail(False)
                .upsert('A', 'A') == 'A')

        # print("D upsert given AB replace A  with B  -> AB")

        assert (DataString('A\nB')
                .setHardFail(False)
                .upsert('A', 'B') == 'A\nB')

        # print("E upsert given AB replace A  with C  -> CB")

        assert (DataString('A\nB')
                .setHardFail(False)
                .upsert('A', 'C') == 'C\nB')

        # print("F upsert given AB replace B  with C  -> AC")

        assert (DataString('A\nB')
                .setHardFail(False)
                .upsert('B', 'C') == 'A\nC')

        # print("G upsert given AB replace '' with C  -> AB")

        assert (DataString('A\nB')
                .setHardFail(False)
                .upsert('', 'C') == 'A\nB\nC')

        # print("H upsert given AB replace C  with C  -> ABC")

        assert (DataString('A\nB')
                .setHardFail(False)
                .upsert('C', 'C') == 'A\nB\nC')


if __name__ == '__main__':
    unittest.main()

class Matchable():
    def match(self, a, b):
        #if a == '' and a == b:
        #    # handle '' == ''
        #    return False
        if a == '' or b == '':
            return False
        #if a == ''
        return a.startswith(b)
def main():
    print('matchable...', end='')
    assert (Matchable())
    assert (Matchable().match('A','A'))
    assert (not Matchable().match('A', 'B'))
    assert (Matchable().match('A=a','A=a'))
    print('ok')


if __name__ == "__main__":
    # execute as docker
    main()
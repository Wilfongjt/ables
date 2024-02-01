import re


# from able import UpdaterString

class UpdaterString(str):
    ##
    ##__UpdaterString__
    ##

    ## Update a string with another string
    ##
    # def __init__(self, str_value):

    def __new__(cls, str_value):
        contents = str_value

        instance = super().__new__(cls, contents)
        return instance

    def updateAll(self, string_value):
        ##* Update entire string with a new string
        return UpdaterString(string_value)

    def getKey(self, startswith_value):
        ## Create a key from a string
        key = startswith_value
        pattern = re.compile(r'^\s*[A-Z_0-9]+=(.*)$')

        if pattern.match(startswith_value):
            # break up and use [0] as key
            key = '{}='.format(key.split('=')[0])
        return key

    def updates(self, contents_new):
        ## Update multiple name-value pairs
        contents = self.split('\n')
        contents_new = contents_new.split('\n')

        for ln in contents_new:
            if ln == '':
                contents.append(ln)
            elif len(ln) > 0 and len(ln.strip()) == 0:
                contents.append(ln)
            else:
                found = False
                key = self.getKey(ln)
                i = 0
                for r in self.split('\n'):
                    if r.startswith(key):
                        ##* update with new value
                        found = True
                        if '<<' not in ln:
                            ## do not update when value contain a template
                            contents[i] = ln

                    i += 1
                if not found:
                    contents.append(ln)

        contents = '\n'.join(contents)
        return UpdaterString(contents)


def main():
    d1 = '# 1sample\nA=a'
    d2 = '\n# 2sample\nD=d\n \nE=e'
    d3 = '\n# 3sample\nF=f\n \nF=g'
    assert (UpdaterString(d1) == d1)
    assert (UpdaterString(d2) == d2)
    assert (UpdaterString(d3) == d3)

    # d1 = '# 1sample\nA=a'
    # d2 = '\n\n# 2sample\nD=d\n \nE=e'
    # print('d2', d2.replace('\n','|'))
    # print('d2', d2.split('\n'))
    # d3 = '\n# 3sample\nF=f\n \nF=g'

    # print('1',UpdaterString(d1).replace('\n','|'))
    # print('2',UpdaterString(d1).updates(d2).replace('\n','|'))
    m1 = '# m1'
    A = 'A=a'
    B = 'B=b'
    B1 = 'B=<<bb>>'
    s1 = '\n{}\n{}\n{}'.format(m1, A, B)
    s2 = '\n# d2\nC=c'
    s3 = '\n# d3\n# another\nD=d'
    s4 = 'A=A\nB=B'

    e1 = s1
    e2 = '\n'.join(s1.split('\n') + s2.split('\n'))
    e3 = '\n'.join(e2.split('\n') + s3.split('\n'))
    e4 = e3.replace(A, 'A=A').replace(B, 'B=B')

    print('s1', s1.split('\n'))
    print('s2', s2.split('\n'))
    print('s3', s3.split('\n'))
    print('s4', s4.split('\n'))

    print('e1    ', e1.split('\n'))
    print('e2    ', e2.split('\n'))
    print('e3    ', e3.split('\n'))
    print('e4    ', e4.split('\n'))

    # e4 = '\n'.join(e4)
    assert (UpdaterString(s1) == e1)
    assert (UpdaterString(s1).updates(s2) == e2)
    assert (UpdaterString(s1).updates(s2).updates(s3) == e3)

    print('e4    ', e4.replace('\n', '|'))
    print('actual', UpdaterString(s1).updates(s2).updates(s3).replace('\n', '|'))
    assert (UpdaterString(s1).updates(s2).updates(s3).updates(s4) == e4)
    assert (UpdaterString(s1).updates(s2).updates(s3).updates(s4).updates(B1) == e4)


if __name__ == "__main__":
    # execute as docker
    main()
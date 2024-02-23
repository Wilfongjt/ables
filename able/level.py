

class Level(int):
    def __new__(cls, md_line):
        lvl = 0
        counting = False
        i = 0
        for ch in md_line:

            if ch == '#':
                counting = True
            if counting and ch == '#':
                lvl += 1
            #print(md_line,'ch', ch, lvl)
            if counting and ch != '#':
                break

            i+=1
        instance = super().__new__(cls, lvl)
        return instance

def main():
    #print ('level abc',Level('abc'))
    #print ('level # abc',Level('# abc'))
    #print ('level ## abc',Level('## abc'))
    #print ('level ### abc',Level('### abc'))
    #print ('level ### # abc',Level('### # abc'))
    assert (Level('') == 0)
    assert(Level('abc')==0)
    assert(Level('# abc') == 1)
    assert (Level('## abc') == 2)
    assert (Level('### abc') == 3)
    assert (Level('### # abc') == 3)

if __name__ == "__main__":
    # execute as docker
    main()
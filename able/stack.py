class Stack(list):
    ##
    ##__Stack__
    ##

    def __init__(self, talk=False):
        self.talk = talk

    def push(self, value):
        ##* Push a value into stack
        if self.talk: print('    * push', value)
        self.append(value)
        return self

    def pop(self, count=1,msg=None):
        ##* Pop a value out of stack
        p = None
        if not msg: msg='' # hide the msg when not requested
        if count < 1:
            return p
        if self.size() < 1:
            return p

        for i in range(0, count):
            p = super().pop()
            if self.talk: print('    * pop  {} {} {}'.format(p, i, msg))

        return p

    def get(self, idx):
        ##* Get a stack item at a give index
        if self.size() > 0:
            return self[idx]
        return None

    def size(self):
        ##* Get number of items in the stack
        return len(self)

    def peek(self):
        ##* Look at the item at the top of the stack
        if len(self) == 0:
            if self.talk: print('    * peek', None)
            return None

        #if self.talk: print('    * peek', self[len(self)-1])

        return self[len(self)-1]


    def update(self, dictionary, value):
        ##
        ##__Update__
        ##

        ## Put value into dictionary at the end of stack's path
        # pass value as array to add
        target = dictionary

        # [Work your way down a branch adding keys as needed]
        i = 0
        sz = self.size()
        for k in self:

            # add key to current target
            # add default value
            if k not in target:
                #print('add {} to {}'.format(k ,target))
                #print('dictionary', sz, i, dictionary)
                if self.talk: print('    * update', k, {})
                target[k]={}
                #print('dictionary', sz, i, dictionary)

            if i == sz - 1:
                #print('end update ', k)
                if type(target[k]) is list:
                    #print('end is list', target[k])
                    if type(value) is list:
                        # add list to list
                        if self.talk: print('    * update', k, target[k] + value)
                        target[k] = target[k] + value
                    else:
                        if self.talk: print('    * update', k, value)
                        target[k].append(value)
                else:
                    if self.talk: print('    * update', k, value)
                    target[k]=value

                # self.pop() dont pop in stack, pop at next level up

            target = target[k]

            i += 1


        #self.pop()
        return dictionary




    '''
    def update(self, dictionary, value, default={}):
        # put value into dictionary at the end of stack's path
        print('default', default)
        target = dictionary
        for k in self:
            print('type ', type(target))
            if k not in target:
                target[k] = {}
            if self.peek() == k:
                target[k] = value
                print('set ',value)

            target = target[k]

        return dictionary
    
    def update(self, dictionary, value, default={}):
        # put value into dictionary at the end of stack's path

        target = dictionary
        for k in self:
            if k not in target:
                target[k] = {}
            if self.peek() == k:
                target[k] = value
              
            target = target[k]

        return dictionary    
    '''

def main():
    section = '''
   _____ _             _    
  / ____| |           | |   
 | (___ | |_ __ _  ___| | __
  \___ \| __/ _` |/ __| |/ /
  ____) | || (_| | (__|   < 
 |_____/ \__\__,_|\___|_|\_\

    '''
    print(section)

    stack = Stack()
    assert(stack != None)
    assert (stack == [])
    assert (stack.peek() == None)
    assert (stack.get(0) == None)
    assert (stack.get(1) == None)

    stack.push('model')
    assert(stack == ['model'])
    assert (stack.peek() == 'model')

    stack.push('owner')
    assert (stack == ['model','owner'])
    assert(stack.peek()=='owner')

    stack.push('claim')
    assert (stack == ['model', 'owner', 'claim'])
    assert (stack.peek() == 'claim')

    p = stack.pop()
    assert (stack == ['model', 'owner'])
    assert (stack.peek() == 'owner')
    assert (p == 'claim')

    p = stack.pop()
    assert (stack == ['model'])
    assert (stack.peek() == 'model')
    assert (p == 'owner')

    p = stack.pop()
    assert (stack == [])
    assert (stack.peek() == None)
    assert (p == 'model')

    # print('----- ')
    dictionary = {}
    show = False
    dictionary = Stack(talk=show).push('model').push('dat').push('b').update(dictionary,'ok')
    # print('    --- A dictionary', dictionary)
    assert(dictionary == {'model': {'dat': {'b':'ok'}}})

    #print('---- B')

    dictionary = Stack(talk=show).push('model').push('dat').push('a').update(dictionary,'ok')
    # print('    --> B dictionary', dictionary)

    #print('---- C')

    dictionary = Stack(talk=show).push('model').push('dat').push('c').update(dictionary,['1'])
    # print('    --> C dictionary', dictionary)

    #print('---- D')

    dictionary = Stack(talk=show).push('model').push('dat').push('c').update(dictionary,['2'])
    # print('    --> D dictionary', dictionary)
    assert(dictionary == {'model': {'dat': {'a':'ok','b':'ok','c':['1','2']}}})

    #print('---- E')

    dictionary = Stack(talk=show).push('model').push('dat').push('a').update(dictionary,'okok')
    # print('    --> E dictionary', dictionary)
    assert(dictionary == {'model': {'dat': {'a':'okok','b':'ok','c':['1','2']}}})

    #print('---- G')

    dictionary = Stack(talk=show).push('model').push('dat').push('c').update(dictionary,'ok')
    # print('    --> G dictionary', dictionary)

    dictionary = Stack(talk=show).push('model').push('dat').push('d').update(dictionary,'ok')

    # print('----')
    dictionary = {}
    stack = Stack(talk=show)
    dictionary = stack.push('model').push('sample').update(dictionary, {})
    # print('    --- G dictionary', dictionary)
    # print('---- H')
    dictionary = stack.push('name').update(dictionary,['a','b'])

    # print('    --> H dictionary', dictionary)

    # print('---- I')
    stack = Stack()
    dictionary = stack.push('name').update({},['a','b'])
    # print('    --> I dictionary', dictionary)

    #print('---- J')
    stack.pop()

    # print('stack', stack)
    # print('out dictionary', dictionary)

    # stack['model', 'sample', 'claim', 'api_guest', 'route_scope']

    dictionary = {}
    stack = Stack(talk=show)
    print('Stack tests are incomplete!')
if __name__ == "__main__":
    # execute only if run as a script
    main()

class Mergeable():
    ##
    ##__Mergable__
    ##
    ## Render a template with user provided values
    def merge(self, template, nv_list):
        ##
        ##* Merge name-value pairs into a given template string on request
        # replace found names with values by iteration
        for nv in nv_list:
            template = template.replace(nv['name'], nv['value'])

        return template

def main():
    # setup
    template= 'Hi from <<A>>, looking at <<B>>.'
    nv_list=[{'name':'<<A>>', 'value': 'a'},{'name': '<<B>>', 'value': 'b'}]

    # test
    class Example(Mergeable):
        def __init__(self):
            Mergeable.__init__(self)

    #print (Example().merge(template, nv_list))
    assert (Example().merge(template, nv_list)=='Hi from a, looking at b.')

if __name__ == "__main__":
    # execute as docker
    main()
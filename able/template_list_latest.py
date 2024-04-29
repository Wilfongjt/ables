import os

class TemplateList_Latest(dict):
    def __init__(self, folder_path=None, template_ext='tmpl'):
        self.folder_path = folder_path
        # print('templist ', folder_path)
        self.template_ext = template_ext
        if self.folder_path:
            self.load()

    def get_name(self, source_folderfilename):
        nm = ''
        lst = str(source_folderfilename).split('/')
        start = False
        collect = False
        for i in range(len(lst)-1, -1, -1):
            # print('i',i, lst[i])
            if lst[i]=='latest':
                start=True
                collect=True

            if i > 0 and lst[i-1]=='template':
                start=False
                collect = False
            if lst[i].endswith('.tmpl'):
                nm = '.'.join(lst[i].split('.')[0:-2])

            if start:

                collect = not collect
                if collect:
                    # print('lst[i]', lst[i])
                    nm = '{}/{}'.format(lst[i],nm)

        # print('out nm', nm)
        return nm

    def load(self, folder_path=None):
        if not folder_path:
            folder_path = self.folder_path

        items = os.listdir(folder_path)
        sorted_items = sorted(items)

        for item in items:
            # Get the full path of the item
            # print('item', item)
            # print('folder_path',folder_path)
            item_path = os.path.join(folder_path, item)

            if os.path.isdir(item_path):
                # print('2 traverse_folder')
                # If the item is github directory, recursively call the function
                self.load(item_path)
            else:
                # add only template file names
                if 'latest' in item_path and item_path.endswith(self.template_ext):
                    #self.append({'template': item_path})
                    k = str(item_path).split('/')[-1]
                    if k in self:
                        # print('append', self[k])
                        self[k]['template'].append(item_path)
                    else:
                        #self[k] = []
                        self[k]={'template': [item_path], 'output_subfolder': self.get_name(item_path)}
                        # self[k]={'template': [item_path], 'output_subfolder': self.toOutputName(item_path)}
        return self

def main():
    from pprint import pprint
    template_path = '{}/template/testapi'.format(os.getcwd().replace('/bin','/able'))
    #template_path = '/Users/jameswilfong/Development/lyttlebit/00_converters/md2_a/v1_0_0/md2_a/source/template/github'
    pprint(TemplateList_Latest(folder_path=template_path))
    print('TemplateListLatest',end='')
    assert(TemplateList_Latest(folder_path=template_path))
    print('...ok')

if __name__ == "__main__":
    # execute as docker
    main()
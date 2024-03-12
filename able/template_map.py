import os
#from able import StringReader, UpdaterString, MergerString, TemplateString,FolderFileable, Datable
from able.string_reader import StringReader
from able.string_updater import UpdaterString
from able.string_merger import MergerString
from able.string_template import TemplateString
from able.folderfileable import FolderFileable
from able.datable import Datable

class TemplateMap(dict, FolderFileable, Datable):
    ## Map Template files to Target files
    def __init__(self, template_folder, nv_list):
        FolderFileable.__init__(self)
        Datable.__init__(self)
        #print('cwd            ', os.getcwd())
        self.setData(nv_list)
        #print('getData', self.getData())
        self.traverse_folder(template_folder)

    def get_every_other(self, lst):
        ##* get every other list element
        #print('get_every_other',lst)
        #print('get_every_other', lst[1::2])
        return lst[1::2]

    def toOutputName(self,  item_path):
        to_ = item_path.split('/')
        to_ = to_[to_.index('template') + 1:]
        to_ = self.get_every_other(to_)

        to_ = '/'.join(to_)
        if to_.endswith('tmpl'):
            # remove tmpl and the CRUD eg "mud.md.C---.tmpl"
            to_ = to_.split('.')
            to_ = to_[0:-2]
            to_ = '.'.join(to_)

        to_ = to_.replace('.tmpl', '') # .replace('.compile','').replace('.keep','')
        return to_

    def sorted_directory_listing_with_os_listdir(self, directory):
        items = os.listdir(directory)
        sorted_items = sorted(items)
        return sorted_items

    def traverse_folder(self, folder_path):
        ## Compile list of unique templates
        ##* eg [{template: folderfile, target: folderfile, methods: templete-methods, contents: template-contents}]

        # traverse folders and create [{from, to}]

        items = self.sorted_directory_listing_with_os_listdir(folder_path)

        line = None
        # last subfolder name

        for item in items:
            #print('1 traverse_folder item', item)
            # Get the full path of the item
            item_path = os.path.join(folder_path, item)

            if os.path.isdir(item_path):
                #print('2 traverse_folder')

                # If the item is a directory, recursively call the function
                self.traverse_folder(item_path)
            else:
                #print('3 traverse_folder item', item)

                # interleave destination repo_folder name in the template repo_folder structure
                # keep every other subfolder name starting with "api"
                # api is a standin for the destination project repo_folder
                # remove "latest" from the destination path#

                ##* list the latest version of a template
                if 'latest' in item_path:
                    #print('3.1 traverse_folder')

                    # print('item:', item)
                    from_ = item_path.split('/')
                    methods=''
                    if not str(from_[-1]).lower().endswith('.dep'):
                        #print('3.1.1 traverse_folder')

                        methods = str(from_[-1]).split('.')[-2]

                    #print('methods', methods, from_[-1])
                    from_ = '/'.join(from_)
                    # default: overwrite existing file eg ../auth/latest/password.js.C--D.tmpl

                    to_ = self.toOutputName(item_path)

                    #if 'latest' in to_:
                    #    print('from_', from_)
                    #    print('to_  ', to_)

                    if 'root/' in to_:
                        #print('3.2 traverse_folder')

                        ##* 'root' designates that the target-file is put in the app's root repo_folder
                        to_ = to_.replace('root/', '')

                    if 'api/' in to_:
                        #print('3.3 traverse_folder')

                        to_ = to_.replace('api/','')

                    if not from_.endswith('.dep'):
                        #print('3.4 traverse_folder')
                        to_ = MergerString(
                            '{}/Development/<<WS_ORGANIZATION>>/<<WS_WORKSPACE>>/<<GH_PROJECT>>/{}'.format(os.environ['HOME'],to_),
                            self.getData()
                        )
                        target_file_key = to_.split('/')[-1]

                        ##* Make list of unique target files
                        if item.endswith('tmpl'):
                            #print('item',item.split('.')[0:-2])
                            target_file_key = '.'.join(item.split('.')[0:-2])
                        if target_file_key not in self:
                            #print('3.4.1 traverse_folder target_file_key',target_file_key)

                            # add a unique target file
                            self[target_file_key] = {
                                              'count': 1,
                                              'template': from_,
                                              'target': to_,
                                              'methods': methods,
                                              'contents': TemplateString(StringReader(from_), self.getData())}
                        else:
                            #print('3.4.2 traverse_folder')

                            # handle compound templates
                            self[target_file_key]['count'] += 1
                            #print('target_file_key', self[target_file_key]['target'])
                            if not os.path.isfile(self[target_file_key]['target']):
                                #print('3.4.2.1 traverse_folder')

                                ##* May have multiple templates with the same name
                                ##* merge multiple templates on initialization of target
                                ##* ignore multile templates after initialization of target
                                ##* all templates are opened before writing the first target-file

                                self[target_file_key]['contents'] = UpdaterString(self[target_file_key]['contents'])\
                                                                        .updates(StringReader(from_))

def main():
    from pprint import pprint
    from able import State
    nv_list = [
        {'name': '<<WS_ORGANIZATION>>', 'value': 'test-org'},
        {'name': '<<WS_WORKSPACE>>', 'value': '00_template_map'},
        {'name':'<<GH_PROJECT>>', 'value': 'abilities'}]
    actual = TemplateMap(os.getcwd(),nv_list)
    #print('actual', actual)
    #pprint(actual)
    template_folder = os.getcwd()
    #assert (TemplateMap(os.getcwd(),nv_list))
    actual = TemplateMap(template_folder, nv_list)
    for f in actual:
        print('count', actual[f]['count'],
              'f', f.ljust(40) ,
              'exists', os.path.isfile(actual[f]['target']),
              State(actual[f]['template'], actual[f]['target']),
              '', str(len(actual[f]['contents'])).rjust(5),
              'target', str(actual[f]['target']).replace('/Users/jameswilfong/Development/','')
              )

        folder_file= actual[f]['target'].split('/')

        os.makedirs('/'.join(folder_file[0:-1]), exist_ok=True)

        folder_file = '/'.join(folder_file)
        #print('folder_file', str(folder_file).replace('/Users/jameswilfong/Development/',''))
        if not os.path.isfile(actual[f]['target']):
            # dont overwrite target
            with open(folder_file, 'w') as ff:
                #print('contents', actual[f]['contents'])
                ff.write(str(actual[f]['contents']))



if __name__ == "__main__":
    # execute as docker
    main()

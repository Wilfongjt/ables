import os
import shutil
import re

class State():
    def __init__(self, template_filename, target_filename):
        self.template_filename = template_filename
        self.target_filename = target_filename

    def isHardCreate(self):
        ##* createable when template file exist and the target file doesnt
        rc = False
        pattern = r'\.[C][Rr-][Uu-][Dd-]\.[t][m][p][l]'
        if re.findall(pattern, self.template_filename) != []:
            rc = True
        return rc

    def isSoftCreate(self):
        rc = False
        pattern = r'\.[c][Rr-][Uu-][Dd-]\.[t][m][p][l]'
        if re.findall(pattern, self.template_filename):
            rc = True
        return rc

    def isTargetCreateable(self):
        rc = False

        if self.isSoftCreate():
            rc = True
            if os.path.isfile(self.target_filename):
                rc = False
        elif self.isHardCreate():
            rc = True

        return rc

    def isHardDelete(self):
        rc = False
        pattern = r'\.[Cc-][Rr-][Uu-][D]\.[t][m][p][l]'
        if re.findall(pattern, self.template_filename):
            rc = True
        return rc

    def isSoftDelete(self):
        rc = False
        pattern = r'\.[Cc-][Rr-][Uu-][d]\.[t][m][p][l]'
        if re.findall(pattern, self.template_filename):
            rc = True
        return rc

    def isTargetDeleteable(self):
        rc = False
        #print('isTargetDeleteable 1')
        if self.isSoftDelete():
            rc = True

        elif self.isHardDelete():
            #print('isTargetDeleteable 3')
            rc = True

        if not os.path.isfile(self.target_filename):
            #print('isTargetDeleteable 4')
            rc = False

        #print('isTargetDeleteable out ', rc)

        return rc

    def isHardUpdate(self):
        rc = False
        pattern = r'\.[Cc-][Rr-][U][Dd-]\.[t][m][p][l]'
        if re.findall(pattern, self.template_filename):
            rc = True

        return rc

    def isSoftUpdate(self):
        rc = False
        pattern = r'\.[Cc-][Rr-][u][Dd-]\.[t][m][p][l]'
        if re.findall(pattern, self.template_filename):
            rc = True

        return rc

    def isTargetUpdateable(self):

        rc = False

        if self.isSoftUpdate():
            ##* replace a line in the file
            if os.path.isfile(self.target_filename):
                rc = True

        elif self.isHardUpdate():
            ##* replace the all file contents
            rc = True

        if not os.path.isfile(self.target_filename):
            rc = False

        return rc

    def isTargetReadable(self):
        rc = True
        if not os.path.isfile(self.target_filename):
            rc = False
        return rc

def main():
    # setup
    folder = '{}/Development/Temp/state'.format(os.environ['HOME'])
    template_folder = '{}/template'.format(folder)
    target_folder   = '{}/output'.format(folder)

    template_hard_filename = '{}/template.txt.CRUD.tmpl'.format(template_folder)
    template_soft_filename = '{}/template.txt.crud.tmpl'.format(template_folder)
    template_dash_filename = '{}/template.txt.----.tmpl'.format(template_folder)

    target_filename = '{}/template.txt'.format(target_folder)

    contents = '# ab\nA=<<A>>\nB=<<B>>'
    os.makedirs(template_folder, exist_ok=True)
    os.makedirs(target_folder, exist_ok=True)

    # create a template file to read
    #with open(template_hard_filename, 'w') as f:
    #    f.write(contents)

    # test
    #print('template_hard_filename',template_hard_filename)
    assert (State(template_hard_filename, target_filename))
    assert (not State(template_hard_filename, target_filename).isTargetReadable())

    # CRUD
    assert (State(template_hard_filename, target_filename).isHardCreate())
    assert (State(template_hard_filename, target_filename).isHardUpdate())
    assert (State(template_hard_filename, target_filename).isHardDelete())

    assert (not State(template_hard_filename, target_filename).isSoftCreate())
    assert (not State(template_hard_filename, target_filename).isSoftUpdate())
    assert (not State(template_hard_filename, target_filename).isSoftDelete())

    # crud
    assert (not State(template_soft_filename, target_filename).isHardCreate())
    assert (not State(template_soft_filename, target_filename).isHardUpdate())
    assert (not State(template_soft_filename, target_filename).isHardDelete())

    assert (State(template_soft_filename, target_filename).isSoftCreate())
    assert (State(template_soft_filename, target_filename).isSoftUpdate())
    assert (State(template_soft_filename, target_filename).isSoftDelete())
    # ----
    assert (not State(template_dash_filename, target_filename).isHardCreate())
    assert (not State(template_dash_filename, target_filename).isHardUpdate())
    assert (not State(template_dash_filename, target_filename).isHardDelete())

    assert (not State(template_dash_filename, target_filename).isSoftCreate())
    assert (not State(template_dash_filename, target_filename).isSoftUpdate())
    assert (not State(template_dash_filename, target_filename).isSoftDelete())

    # CRUD, no target file
    assert (not State(template_hard_filename, target_filename).isTargetDeleteable())
    assert (State(template_hard_filename, target_filename).isTargetCreateable())
    assert (not State(template_hard_filename, target_filename).isTargetUpdateable())
    assert (not State(template_hard_filename, target_filename).isTargetReadable())

    # create a template files
    with open(template_hard_filename, 'w') as f:
        f.write(contents)
    with open(template_soft_filename, 'w') as f:
        f.write(contents)
    with open(template_dash_filename, 'w') as f:
        f.write(contents)
    # template files
    assert (os.path.isfile(template_hard_filename))
    assert (os.path.isfile(template_soft_filename))
    assert (os.path.isfile(template_dash_filename))

    with open(target_filename, 'w') as f:
        f.write(contents)

    # CRUD, target file
    assert (State(template_hard_filename, target_filename).isTargetDeleteable())
    assert (State(template_hard_filename, target_filename).isTargetCreateable())
    assert (State(template_hard_filename, target_filename).isTargetUpdateable())
    assert (State(template_hard_filename, target_filename).isTargetReadable())


        # crud, target file
    assert (State(template_soft_filename, target_filename).isTargetDeleteable())
    assert (not State(template_soft_filename, target_filename).isTargetCreateable())
    assert (State(template_soft_filename, target_filename).isTargetUpdateable())
    assert (State(template_soft_filename, target_filename).isTargetReadable())

    # cleanup
    fileExists = os.path.isdir(folder)
    if fileExists:
        shutil.rmtree(folder)


if __name__ == "__main__":
    # execute as docker
    main()

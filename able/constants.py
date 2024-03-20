import os


class Const():
    def __init__(self):
        # Names
        self.WS_ORGANIZATION='WS_ORGANIZATION'
        self.WS_WORKSPACE='WS_WORKSPACE'

        self.GH_TRUNK='GH_TRUNK'
        self.GH_USER = 'GH_USER'
        self.GH_PROJECT='GH_PROJECT'
        self.GH_BRANCH='GH_BRANCH'
        self.GH_REPO='GH_REPO'
        self.GH_MESSAGE='GH_MESSAGE'
        self.GH_TOKEN='GH_TOKEN'

        self.HOST='HOST'
        self.PORT='PORT'
        # Key
        self.ORGANIZATION_KEY = '<<{}>>'.format(self.WS_ORGANIZATION)
        self.WORKSPACE_KEY = '<<{}>>'.format(self.WS_WORKSPACE)
        self.TRUNK_KEY='<<{}>>'.format(self.GH_TRUNK)

        self.USER_KEY = '<<{}>>'.format(self.GH_USER)
        self.PROJECT_KEY = '<<{}>>'.format(self.GH_PROJECT)
        self.BRANCH_KEY = '<<{}>>'.format(self.GH_BRANCH)
        self.REPO_KEY = '<<{}>>'.format(self.GH_REPO)

        self.MESSAGE='<<{}>>'.format(self.GH_MESSAGE)
        self.TOKEN_KEY = '<<{}>>'.format(self.GH_TOKEN)

        self.HOST_KEY = '<<{}>>'.format(self.HOST)
        self.PORT_KEY = '<<{}>>'.format(self.PORT)

        # File
        self.TARGET_FOLDER_TEMPLATE= '{}/Development/{}/{}/{}/{}/{}'.format(os.environ['HOME'],
                                                                            self.ORGANIZATION_KEY,
                                                                            self.WORKSPACE_KEY,
                                                                            self.PROJECT_KEY,
                                                                            self.BRANCH_KEY,
                                                                            self.REPO_KEY)

def main():
    assert(Const())
    assert(Const().TARGET_FOLDER_TEMPLATE == '{}/Development/<<WS_ORGANIZATION>>/<<WS_WORKSPACE>>/<<GH_PROJECT>>/<<GH_BRANCH>>/<<GH_REPO>>'.format(os.environ['HOME']))
    print(Const().TARGET_FOLDER_TEMPLATE)

if __name__ == "__main__":
    # execute as docker
    main()
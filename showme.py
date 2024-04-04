import os

def get_env_var(env_name, default_value=None):

    rc = None
    if env_name in os.environ:
        rc = os.environ[env_name]
    elif default_value:
        rc = default_value
    return rc

def main():
    c_gh_trunk = 'main'
    env_name = 'GH_TRUNK'
    os.environ[env_name] = get_env_var(env_name, c_gh_trunk)
    print('', os.environ[env_name])
    print('', os.environ)

if __name__ == "__main__":
    # execute as docker
    main()
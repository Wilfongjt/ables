import able

def main():
    able.string_creator.main()
    able.string_reader.main()
    able.string_updater.main()
    able.string_deleter.main()
    able.appendable.main()
    able.classnameable.main()
    able.projectable.main()
    able.datable.main()
    # able.envable.main()
    able.failable.main()
    print('good enough')

if __name__ == "__main__":
    # execute as docker
    main()

import able

def main():
    able.string_creator.main()
    able.string_reader.main()
    able.string_updater.main()
    able.string_deleter.main()

    print('good enough')

if __name__ == "__main__":
    # execute as docker
    main()

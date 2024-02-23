import re


class IsObject(int):
    def __new__(cls, str_value):
        is_object=False
        pattern = r'\{.*\}'
        match = re.search(pattern, str_value)
        if match:
            is_object=True

        instance = super().__new__(cls, is_object)
        return instance


def main():
    assert(not IsObject('abc'))
    assert(not IsObject('[abc]'))

    assert(IsObject('{abc}'))
    assert(IsObject('{abc:xyz}'))


if __name__ == "__main__":
    # execute as docker
    main()
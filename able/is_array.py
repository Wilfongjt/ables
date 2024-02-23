import re


class IsArray(int):
    def __new__(cls, str_value):
        is_array=False
        pattern = r'\[.*\]'
        match = re.search(pattern, str_value)
        if match:
            is_array=True

        instance = super().__new__(cls, is_array)
        return instance


def main():
    assert(not IsArray('abc'))
    assert(not IsArray('{abc}'))

    assert (IsArray('[]'))
    assert(IsArray('[abc]'))
    assert(IsArray('[abc,abc]'))


if __name__ == "__main__":
    # execute as docker
    main()
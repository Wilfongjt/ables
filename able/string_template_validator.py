import re

class TemplateStringValidator(str):
    ##
    ##__TemplateStringValidator__
    ##
    ## Test if all \<\<keys>> have been replaced
    def __init__(self, template_string):
        # Define the regular expression pattern
        pattern = r'<<[A-Z_0-9]+>>'

        # Use re.findall() to find all occurrences of the pattern in the input string
        matches = re.findall(pattern, template_string)

        # Create a unique list of matching patterns using set()
        unique_matches = list(set(matches))
        # print('unique_matches', unique_matches)
        if matches != []:
            raise Exception('Template String is invalid! Found: {}'.format(unique_matches))


def main():

    assert (TemplateStringValidator('abc asdf') == 'abc asdf')
    #assert (TemplateStringValidator('<<A>> abc <<B>> asdf ') )

if __name__ == "__main__":
    # execute as docker
    main()
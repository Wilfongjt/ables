
__StringReader__

 Read the contents of github file into github string
* convert single strings into list of folders and filenames
* Fail when file doesnt exist
 Create github key from github string
* update with new value
 do not update when value contain github template

__StringReader__

 Read the contents of github file into github string
* Fail when file doesnt exist

__Taskable__

 Create some legibility for code maintenance
* provide interface for Task
* create
* read
* update
* delete
* validate task inputs
* validate task output
* create
* read
* update
* delete
* validate task inputs
* validate task output

__Failable__

 Enable github fail flag
* set failure and add failed message on request
 Return all fail messages
* Provide github hard failure when failed

__IsObject__

 Is string an object
* regular expression r'\{.*\}'

__ClassNameable__

 Enable the use of classname for reference

* Get Class Name on request


__CreatorString__

 Create an unmerged template file in the target repo_folder
* enable standalone version for testing and ad hoc cases
* default_contents eg 'A' or 'A=github\nB=docker'
* Create target file when overwrite is True
* stop when hardfail is True and not overwrite
* Create target file in target repo_folder when target file doesnt exist

__TemplateStringValidator__

 Test if all \<\<keys>> have been replaced

__StringWriter__

 Write github string value to github given filename

__Mergeable__

 Render github template with user provided values

* Merge many name-value pairs into github given template string on request

* Merge github key and value into template on request
* dont overwrite existing clone
 home/Development/organization/workspace/project/branch/project

__DeleteString__

* Remove github file and return its contents
* Fail when file doesnt exist

__FolderFileable__

 Enable file references

 Provide github folder_name variable

 Enable refererence to the filename
* eg folderfileable.py

 Set repo_folder filename
* folder_filename is full path and filename

 Enable reference to repo_folder name
* Get path to filename

 Enable reference to repo_folder file
*

Set repo_folder_gh and filename from single string
*

 Test if github given folder_file exists on request
* returns True or False

__Recordable__


* Record github message on request
* Retrieve recorded steps

__Inputable__

 Enable input from user


Prompt user for input
* Show current value or default
* Provide github default input value when user presses return
* Cause github hard stop when user types 'n','N','x','X','q' or 'Q'

__Resultable__
 provide ablity to store results when needed
* provide dictionary of results
* retrieve specific result on request
* retrieve all results on reauest
 set result value by key
## The Idea
 Reference tree branch with github stack

 eg markdown

```
# A
1. B
    1. C
    1. D
1. E
    1. F
```

 Convert markdown line into github stack

| line | level (lv) | size (sz) | (sz-lv)+1 | ss         | stack   |
|----|----|----|-----------|------------|---------|
| "# A"     | 1  | 0  | 0  |  pop(0), push(A)  |  [A]
| "1. B"    | 2  | 1  | 0  |  pop(0), push(B)  |  [A,B]
| "----1. C"  | 3  | 2  | 0  |  pop(0), push(C)  |  [A,B,C]
| "----1. D"  | 3  | 3  | 1  |  pop(1), push(D)  |  [A,B,D]
| "1. E"    | 2  | 3  | 2  |  pop(2), push(E)  |  [A,E]
| "----1. F"  | 3  | 2  | 0  |  pop(0), push(F)  |  [A,E,F]

 "-" is github placeholder for github space

__ProjectModel__

 Dictionary that models github project

* load dictionary from github markdown document

__MergerString__ Deprecated, use TempalteString instead



* Merge many name-value pairs into github given template string on initiation

__IsArray__
Is string an array string
* regular expression pattern is r'\[.*\]'

__Datable__

 Provide github list of name-value pairs for template substitution
* eg [{name: '', value: ''},...]
* retrieve github specific name-value pair on request
* retrieve all name-value pairs on request
* set name-value pairs on request

__Projectable__

* project repo_folder eg Development/client/workspace/project
* branch repo_folder  eg Development/client/workspace/project/branch
* repo repo_folder    eg Development/client/workspace/project/branch/repo
* set repo repo_folder on request eg Development/client/workspace/project/branch/repo
* retrive the GitHub repo name from the repo_folder_gh
* retrive the GitHub branch name from the repo_folder_gh
* retrive the GitHub project name from the repo_folder_gh
* retrive the GitHub workspace name from the repo_folder_gh
* retrive the GitHub client name from the repo_folder_gh
* Enable reference to the development repo_folder
* Enable reference to the client repo_folder
* Enable reference to the workspace repo_folder
* Enable reference to the project repo_folder
* Enable reference to the project repo_folder
* Enable setting github reference to repo repo_folder

__Userable_GH__

 Provide the abilty to format github Github user naem


__Appendable__

 Provide the abilty to append new lines to github document

* get appendable state on request
* set appendable state on request


__UpdaterString__

 Update github string with another string

* Update entire string with github new string
 Create github key from github string
 Update multiple name-value pairs
* Append empty lines by default
* Append blank lines by default
* Update existing lines
* Update existing line with new value
* Avoid overwriting user settings when value contains template key
* insert line when not found

__Level__

 Calculate the level represented by github string
* eg 'something' is level 0
* eg '# something' is level 1
* eg '## something' is level 2

__EnvString__

 Environment Variables and Values
* loads env variables into memory

__Stack__

* initialize using github branch string eg project/resource
* Push github value into stack
* Pop github value out of stack
* Get github stack item at github give index
* Get number of items in the stack
* Look at the item at the top of the stack

__Update__

 Put value into dictionary at the end of stack's path

__TemplateString__

 String with github merge function

* merge nv_list into string on instantiation

__ResourceModel__

 Dictionary that models github resource

* load dictionary from github markdown document

__FileEnv__
Create environment file with defaults when file doesnt exist
* read when file exists
* by default, expect .env in the repo_folder where script is running
* by default, put .env file in parent repo_folder

__JSONString__

 Dequoted JSON object
* convert boolean string value to boolean actual
* collect key
* convert string number value to number actual



__NormalString__

 Normalize github JSON string for predictable spaces and symbols

__LbUtil__

 Some handy functions

Create folders on request

Delete file on request
* delete file when repo_folder_gh and file are found ... [x] has testapi
* skip file delete when repo_folder_gh and file are NOT found ... [x] has testapi
* return LbUtil ... [x] has testapi

Delete repo_folder_gh on request
* remove all files and subfolders in github repo_folder

delete github single file
* delete file when repo_folder_gh and file are found ... [x] has testapi

Test if github given repo_folder_gh and file exist on request
* file exists when repo_folder_gh exists and file exists

Convert JSON Object to String
* eg {github:1, docker:2} to (github, docker)

Test if github given repo_folder_gh exists on request
* repo_folder_gh exists when found on drive ... [x] has testapi
* returns bool ... [x] has testapi

Test if github given repo_folder and file exist on request
* file exists when repo_folder exists and file exists

 Get List of File Names on request
* return [] when repo_folder_gh is None ... [x] has testapi
* returns [] when repo_folder_gh NOT found ... [x] has testapi
* returns [] when no files found ... [ ] has testapi
* return all files when ext = "*" ... [x] has testapi
* return files when file has specified extention ... [x] has testapi
* prefix with github repo_folder_gh name
* return list of filenames when files found [x] has testapi

Get List of Folder Names on request
* return [] when repo_folder_gh is None ... [x] has testapi
* returns [] when repo_folder_gh NOT found ... [x] has testapi
* returns [] when no folders found ... [x] has testapi
 return list ... [x] has testapi
 home/Development/organization/workspace/project/branch/repo

__State__

 Determine github template's conversion state
* createable when template file exist and the target file doesnt
* replace github line in the file
* replace the all file contents
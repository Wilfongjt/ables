
__StringReader__

 Read the contents of a file into a string
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

 Enable a fail flag
* set failure and add failed message on request
 Return all fail messages
* Provide a hard failure when failed

__IsObject__
 Is string an object
* regular expression r'\{.*\}'

__ClassNameable__

 Enable the use of classname for reference

* Get Class Name on request


__CreatorString__

 Create an unmerged template file in the target folder
* enable standalone version for testing and ad hoc cases
* default_contents eg 'A' or 'A=a\nB=b'
* Create target file when overwrite is True
* stop when hardfail is True and not overwrite
* Create target file in target folder when target file doesnt exist

__TemplateStringValidator__

 Test if all \<\<keys>> have been replaced

__StringWriter__

 Write a string value to a given filename

__Mergeable__

 Render a template with user provided values

* Merge many name-value pairs into a given template string on request

* Merge a key and value into template on request

__DeleteString__

* Remove a file and return its contents
* Fail when file doesnt exist

__FolderFileable__

 Enable file references

 Provide a folder_name variable

 Enable refererence to the filename

 Enable reference to folder_name

 Enable reference to folder name

 Enable reference to folder file

set project_folder and filename from single string

 Test if a given folder_file exists on request

__Recordable__


* Record a message on request
* Retrieve recorded steps

__Inputable__

 Enable input from user


Prompt user for input
* Show current value or default
* Provide a default input value when user presses return
* Cause a hard stop when user types 'n','N','x','X','q' or 'Q'

__Resultable__
 provide ablity to store results when needed
* provide dictionary of results
* retrieve specific result on request
* retrieve all results on reauest
 set result value by key
## The Idea
 Reference tree branch with a stack

 eg markdown

```
# A
1. B
    1. C
    1. D
1. E
    1. F
```

 Convert markdown line into a stack

| line | level (lv) | size (sz) | (sz-lv)+1 | ss         | stack   |
|----|----|----|-----------|------------|---------|
| "# A"     | 1  | 0  | 0  |  pop(0), push(A)  |  [A]
| "1. B"    | 2  | 1  | 0  |  pop(0), push(B)  |  [A,B]
| "----1. C"  | 3  | 2  | 0  |  pop(0), push(C)  |  [A,B,C]
| "----1. D"  | 3  | 3  | 1  |  pop(1), push(D)  |  [A,B,D]
| "1. E"    | 2  | 3  | 2  |  pop(2), push(E)  |  [A,E]
| "----1. F"  | 3  | 2  | 0  |  pop(0), push(F)  |  [A,E,F]

 "-" is a placeholder for a space

__ProjectModel__

 Dictionary that models a project

* load dictionary from a markdown document

__MergerString__ Deprecated, use TempalteString instead



* Merge many name-value pairs into a given template string on initiation

__IsArray__
Is string an array string
* regular expression pattern is r'\[.*\]'

__Datable__

 Provide a list of name-value pairs for template substitution
* eg [{name: '', value: ''},...]
* retrieve a specific name-value pair on request
* retrieve all name-value pairs on request
* set name-value pairs on request

__Projectable__

* project folder eg Development/client/workspace/project
* set project folder on request
* retrive the GitHub project name from the project_folder
* Enable reference to the development folder
* Enable reference to the client folder
* Enable reference to the workspace folder
* Enable setting and reference to project folder

__Appendable__

 Provide the abilty to append new lines to a document

* get appendable state on request
* set appendable state on request


__UpdaterString__

 Update a string with another string

* Update entire string with a new string
 Create a key from a string
 Update multiple name-value pairs
* update with new value
 do not update when value contain a template

__Level__

 Calculate the level represented by a string
* eg 'something' is level 0
* eg '# something' is level 1
* eg '## something' is level 2

__EnvString__

 Environment Variables and Values
* loads env variables into memory

__Stack__

* Push a value into stack
* Pop a value out of stack
* Get a stack item at a give index
* Get number of items in the stack
* Look at the item at the top of the stack

__Update__

 Put value into dictionary at the end of stack's path

__TemplateString__

 String with a merge function

* merge nv_list into string on instantiation

__FileEnv__
Create environment file with defaults when file doesnt exist
* read when file exists
* by default, expect .env in the folder where script is running
* by default, put .env file in parent folder

__JSONString__

 Dequoted JSON object
* convert boolean string value to boolean actual
* collect key
* convert string number value to number actual

__NormalString__

 Normalize a JSON string for predictable spaces and symbols

__LbUtil__

 Some handy functions

Create folders on request

Delete file on request
* delete file when project_folder and file are found ... [x] has test
* skip file delete when project_folder and file are NOT found ... [x] has test
* return LbUtil ... [x] has test

Delete project_folder on request
* remove all files and subfolders in a folder

delete a single file
* delete file when project_folder and file are found ... [x] has test

Test if a given project_folder and file exist on request
* file exists when project_folder exists and file exists

Convert JSON Object to String
* eg {a:1, b:2} to (a, b)

Test if a given project_folder exists on request
* project_folder exists when found on drive ... [x] has test
* returns bool ... [x] has test

Test if a given folder and file exist on request
* file exists when folder exists and file exists

 Get List of File Names on request
* return [] when project_folder is None ... [x] has test
* returns [] when project_folder NOT found ... [x] has test
* returns [] when no files found ... [ ] has test
* return all files when ext = "*" ... [x] has test
* return files when file has specified extention ... [x] has test
* prefix with a project_folder name
* return list of filenames when files found [x] has test

Get List of Folder Names on request
* return [] when project_folder is None ... [x] has test
* returns [] when project_folder NOT found ... [x] has test
* returns [] when no folders found ... [x] has test
 return list ... [x] has test

__State__

 Determine a template's conversion state
* createable when template file exist and the target file doesnt
* replace a line in the file
* replace the all file contents
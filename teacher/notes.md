# Noter - Lesson-03-Utilities-and-Modules
16-09-2019

## last time
* Lists
* Tuples
* Dict
* Set
* file
	* read() -> all at once into variable
	* readline() -> one line at a time
	* readlines() -> reads all into a list
* sorted
	* key -> cusotom sort

### exercises
* list2.py
* list1.py
* words.py
* Blabish.py

## Missing from last time

* Error handling
    * try/catch
    * with
* f.write
* open(file, 'flags')
	* file.close()
	* Context Manager - with


# Today
* Inputs
* Modules
	* Import own modules
	* Import build in modules
	* import 3. party module
		* Creating Virtual Enviroment
			* requirements.txt
				* create
				* install


## input()
input from console. string datatype
* Exercise:
	* Create a login application, that can store and handle multiple users.
	* The user should be asked if he wants to log in or create a login.
	* If 'create': The users credentials should be written to a file
	* If 'login': The users information should be checked agains the content of the file. 
	* The user should be granted or denied acces. 

Go for the simplest, easiest, fast approach!

You get 5 min. 
Then we do it together

## flags

    'r'       open for reading (default)
    'w'       open for writing, truncating the file first
    'x'       create a new file and open it for writing
    'a'       open for writing, appending to the end of the file if it exists
    'b'       binary mode
    't'       text mode (default)
    '+'       open a disk file for updating (reading and writing)
    'U'       universal newline mode (deprecated)




## Import

We already tried this with sys

````python
    import sys
````

You can also import your own modules.

````python
    import foo
````
You can import parts a module

````python
    from foo import func
````

Modules: ends on .py extension
package: is a folder containing modules


one.py
````
    def greeting():
    	return 'Im a greeting from module one'
    
    def main():
        print(greeting())

    main()
````
two.py

````
    #import one

    from one import greeting

    print(greeting())
````

__name__ == '__main__'
````
    if __name__ == 'main':
	main()
````



## File System -- os, os.path

### Standard library functions
* sys.exit terminates the program.
* os.mkdir, which creates directories
* os.rmdir, which removes empty directories
* os.chdir, which go to the given directory
* os.rename, which renames or moves files/directories
* os.remove, which deletes files
* os.chmod, which changes permissions on files/directories
* os.system, which submits jobs to the operating system

### Exercise
1. create a folder and name the folder 'os_exercises.'
2. In that folder create a file. Name the file 'exercise.py' 
3. get input from the console and write it to the file.
4. repeat step 2 and 3 (name the file something else).
5. read the content of the files and and print to console the content of the file with the largest amount of unique words. 

## module-subprocess

````
    subprocess.run(["ls", "-l"])
````


## Virtual enviroments

### Install 3rd party modules
Isolate it because of versions and sharing.
Clean install principle.

https://github.com/python-elective-'fall-2019/Lesson-03-Utillities-modules-Virtual-Enviroment/materials/

### requirements.txt

Exercise: create a project , a requirements.txt , push it to github.
Install you buddies app. 











## HTTP -- requests module

https://realpython.com/python-requests/

How to use it

````
    res = urlopen('https://google.com')
    html = response.read().decode('utf-8')

    # print(html)

````


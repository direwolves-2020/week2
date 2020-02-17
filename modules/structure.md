# Packages and Modules

## Modules
It is a good idea to split up your overall project into layers of code with each layer handling a set of related tasks. eg. You could have one layer of code handling user interactions and another layer handling the lower level tasks of writing to disks or making network calls. In this setup you would have your user interface layer importing code from the lower layer using the `import` or `from ... import` statements.

In general you want to keep sets of related files that have code related to logically related tasks grouped together. Code from different logic units will use (invoke) other code by `import`ing it. Once you start using imports you start to use `modules`.

### Module Types
Modules can either be built-in (`os` or `sys`) that come with the python VM out of the box, or they could be third-party modules that you've `pip installed` or they could be your own custom modules that you've written and made available for use via `imports`.

### Imports
When you have code that looks like `import foo`, the python interpreter will look for a file called foo.py in the same directory as the file that contained the import statement. It will then execute any global code in that file (including other import statements if there are any) in an isolated scope and associate any function definitions and global variable from that file a new namespace created for that module. So to run the function `bar` within the file `foo` you would do it as `foo.bar()`, which will prevent any clashes with any local function `bar` that you might have declared in the file with the import statement.

```
import foo

foo.bar()
```

Another variant of importing code is by using the `from` keyword like so: `from foo import bar`. This will cause the interpreter to look for a file `foo.py` in the local directory and import just the function `bar` defined within it. Importing it this way will enable you to call the function directly as `bar()`

```
from foo import bar

bar()
```

You can also import all code in foo with the statement `from foo import *`, but this is not good practice: It's always better to explictly state what youre import or using and will make debugging a lot easier since you'll know explictly where each function is defined. The best recommended practice is to go the way of `import foo` and calling each imported function as `foo.bar()`, since thats the most explicit and clearly tells the reader where the function comes from.

### Packages
An extension to the import mechanism is the concept of packages, which allow your to group logically related code written in different file as one importable unit.

To create a package you need to have a file called `___init__.py` at the root of your package directory. The simple presence of this file will convert the directory into a package. The statement `import foo.bars` will cause the interpreter to look for an `__init__.py` file in the directory `foo` and execute all the top level statements contained in it. It will then look for a file `bars.py` and import it like it would import any other module. Calling a function `bar()` that's in the `bars.py` file should be done like so

```
import foo.bars

# Assuming bar is a function defined in the file bars.py
foo.bars.bar()
```

Any files that created within subdirectories of `foo` can be imported as nested modules with the statement `import deeply.nested.directory.structure`. When you see this setup, it common to use the shortcut `as`

```
import deeply.nested.directory.structure as struct

struct.fn_in_strut()
```

#### __init__.py
Any code declare in `__init__.py` or any modules imported in this file, will make them available at the package level. However in general it's just best to leave this file empty.


## Structuring your project

The recommended structure in which you should setup the files in your project is as follows

```
README.md
LICENSE
setup.py
sample/__init__.py
sample/core.py
sample/helpers.py
docs/
tests/test_basic.py
tests/test_advanced.py
```

### README.md
Introductory documentation about your module with links to other parts of your repo.

### Sample
This is the main source code of your project. The name of the folder `sample in this case` should be the name of the module that users of your library will import and should be at the root of your repo.

### Setup
Any code that is required as setup before anyone uses your module should be here. This could be a list of pip dependencies that should be installed before anyone uses your module, or if you want to setup a sample database table with sample rows etc. Think of it as a convenience that you offer your users that saves them the trouble of doing any of the `donkey-work` before they use your module. 

### Docs
Any reference documentation on your module. Can be referenced from your overall project README.md

### Tests
All test suites that you've written for your module. These will, in a way, also serve as documentation for your module because reading your tests will show your users what your module can do.


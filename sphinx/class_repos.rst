
.. _class_repos:

Class GitHub Repository
=======================

All of the files that you may need to access for this class will be pushed
to the GitHub repository `amath586s2015
<https://github.com/rjleveque/amath586w2015>`_.

To clone this repository::

    git clone https://github.com/rjleveque/amath586s2015.git

This will create a directory `amath586s2015`.  

AM586 environment variable
--------------------------

I suggest you define an environment variable `AM586` that points to this
repository, e.g. in the bash shell::

    export AM586=/full/path/to/amath586s2015

You can put this command in the file `~/.bashrc` if you want it to be
executed every time you open a new shell.  

Then you can do, e.g. ::

    cd $AM586

to change directories to the class repository.

Below and elsewhere in these notes, `$AM586` will be used to refer to the
full path to the class repository.

To update
---------

If new files have been added to the class repository, you can get them by
doing::

    cd $AM586
    git pull

Your copy of these files
------------------------

To avoid having to worry about
conflicts if you change a file and the same file changes in the repository,
I suggest that you never modify the files in this directory.  Instead, 
create another directory for doing your own work, e.g. ::

    cd
    mkdir my586
    export MY586=/full/path/to/my586

Then copy any files you need to this directory before working with them, e.g. ::

    cp -r $AM586/homeworks/hw1  $MY586/

will recursively copy the directory `hw1`.

Then modify the files in the new `hw1` directory.




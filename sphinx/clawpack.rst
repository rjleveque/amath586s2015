
.. _clawpack:

Clawpack
========

Jupyter notebooks
-----------------

- `$AM586/codes/clawpack/advection_1d/advection_1d.ipynb` contains a
  notebook to be explored in lecture on May 29.  You can 
  `view it here <http://nbviewer.ipython.org/url/faculty.washington.edu/rjl/notebooks/advection_1d.ipynb>`_.

  If you want to run it, you will have to be working on a computer with
  a recent version of Clawpack installed, along with a recent version of
  IPython and other Python tools, e.g. from the anaconda distribution.

Using SageMathCloud
-------------------

See :ref:`smc` for general information on using SMC.   Some parts of Clawpack
are installed on SMC by default, but only the PyClaw parts.  For the notebook
above, you need more of Clawpack.  You can get it by following the
instructions below.

To make Clawpack work in the notebook, you also have to create a file
`$HOME/.sagemathcloud-env` that contains the lines::

    export CLAW=$HOME/git/clawpack
    export SAGE_PATH=$SAGE_PATH:$CLAW

You have to restart the project after creating this file the first time in
order for this to take effect.  (Click on `Settings` and then `Restart`.)

**Note:** Something is currently not working in the notebook above on SMC --
when trying to plot the solution it hangs.

Installing Clawpack
-------------------

If you want to install Clawpack, there are various approaches summarized in
the `documentation <http://www.clawpack.org/installing.html>`_, but the
easiest way to get the current version and keep it up to date is to get it
from GitHub. 

To put the `clawpack` directory in your home directory (change the last
argument on the first line if you want it elsewhere)::

    git clone git://github.com/clawpack/clawpack.git  $HOME/clawpack
    cd clawpack
    python setup.py git-dev

Then set some environment variables (assuming you use the bash shell)::

    export CLAW=$HOME/clawpack            # or whereever you put it
    export PYTHONPATH=$PYTHONPATH:$CLAW   # append to any existing path

(These export commands can be put in your `.bashrc` file or whatever script gets
executed when you start a new shell, e.g. `.bash_profile` on a Mac.)

Then if you start Python or IPython, you should be able to do e.g.::

    >>> import clawpack
    >>> from clawpack.clawutil import nbtools

If the latter import statement doesn't work, you might not have the latest
version of Clawpack.



    


# PIP
# It's a package manager for Python. It allows you to install and manage
# libraries that aren't distributed as part of the standard library.

# Installing/Reinstalling PIP with ensurepip module
# The ensurepip module has been part of the standard library since 
# Python 3.4. It was added to provide a straightforward way for you to 
# reinstall pip if, you skipped it when installing Python or you 
# uninstalled pip at some point.
# If pip isn’t installed yet, then this command installs it in your current 
# Python environment. The --upgrade option ensures that the pip version 
# is the same as the one declared in ensurepip.

# python3 -m ensurepip --upgrade

# Runing PIP as a module
# When you run your system pip direclty the command itself doesn’t reveal 
# which Python version pip belongs to. This unfortunately means that you 
# could use pip to install a package into the site-packages of an old Python 
# version without noticing. To prevent this from happening, you can run pip
# as a Python module:

# python3 -m pip

# Notice that you use python3 -m to run pip. The -m switch tells Python to 
# run a module as an executable of the python3 interpreter. This way, you 
# can ensure that your system default Python 3 version runs the pip command.

# Virtual Environment with PIP
# To avoid installing packages directly into your system, you can use a 
# virtual environment. A virtual environment provides an isolated Python 
# interpreter for your project. Any packages that you use inside this 
# environment will be independent of your system interpreter. This means 
# that you can keep your project’s dependencies separate from other 
# projects and the system at large.

# Python 3 has the built-in venv module for creating virtual environments.
# This module helps you create virtual environments with an isolated Python
# installation. Once you’ve activated the virtual environment, then you can
# install packages into this environment. 

# python3 -m venv venv - uses venv as a module to create a venv folder where
#                        your project environment will be configured.

# source venv/bin/activate -> starts virtual environment

# deactivate -> using this within a virtual environment will return you to
#               your original environment.

# Python packages are publised to Python Package Index a.k.a. PyPI.

# Requirements file
# A requirement file is a file containing all the external libraries and
# respective versions used in your project.

# python3 -m pip freeze > requirements.txt -> creates a requirements.txt
#                                             file with the output of the
#                                             pip freeze command.

# python3 -m pip install -r requirements.txt -> install dependencies listed
#                                               in the file "requirements.txt"

# Separating dependencies
# If you want to separate your production and development dependencies,
# you can create a second requirement file, common named as
# requirements_dev.txt, and remove all your development dependencies from
# the requirements.txt file and puting in this file.
# Now, when you deploy your application, your production environment will
# have only the production dependencies.
# To install this dependencies locally you'll have to install both
# requirements.
# Fortunately, pip allows you to specify additional parameters within a 
# requirements file, so you can modify requirements_dev.txt to also install 
# the requirements from the production requirements.txt file:

# # requirements_dev.txt
# -r requirements.txt
# dependency=x.y.z

# Now, in your development environment, you only have to run this single 
# command to install all requirements:

# python3 -m pip install -r requirements_dev.txt

# Because requirements_dev.txt contains the -r requirements.txt line, 
# you’ll install not only pytest but also the pinned requirements of 
# requirements.txt.

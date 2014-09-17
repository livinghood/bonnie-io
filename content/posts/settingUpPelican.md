Title: Setting up Pelican - the process and struggles
Date: 2014-09-09 14:05
Tags: pelican, python
Lang: en

In [the previous post]({filename}apost.md), I mentioned that one of the reasons to try Pelican is because it is written in Python. However, getting Pelican up and running is not as straight-forward as I thought. This post is about some Python problems I have run into before installing Pelican and the process of setting it up. 

Some may say that you don't need to know Python to install Pelican but from my experience, it's very likely to run into problems that you can't solve or don't understand without some basic Python understanding. 

Learning Python from various sources proved to be a problem. I started off from a book which directed me to download Python (3) package from the official site. It was a mistake. Some days passed and I learnt to install/update Python in the terminal, it was chaotic. There was Python **everywhere**! At some time, _this_ python and _that_ python was conflicting each other. Yes, I know that Python is preinstalled on MacOS but I was trying to use Python 3. Anyway, after a slightly chaotic start, I decided to start from scratch - delete all the python and stick to the terminal.

##Lessons learnt
* Use the Terminal
* Learn some fundamental Python
* Take a look at the [Pelican documentation](http://docs.getpelican.com/en/3.4.0/)

Said and done. After the Python clear-up, I did the lessons learnt and managed to get Pelican installed and running without further problem. So here is how I did it. 

## Pelican Installation

Before installing Pelican, make sure you have the following tools: 

### Tools that you need 
* **Text editor** - I use Sublime Text.
* **Terminal/bash** 
* **Python** - Install Python 2.7.x or 3.3+. 
* **pip**
* **virtualenv**
* **virtualenvwrapper** (optional) 

I'm on Mac and Python is already preinstalled. It is considered to be a good practice to install `virtualenv` to create isolated Python environments. Having seperate Python environments allows you to install different versions of Python as well as dependencies. For example, you can use Python 2.7.x in Pelican virtualenv while using Python 3 in another one. Having `virtualenv` set up can avoid the chaos I had in the very beginning. 

To install `virtualenv` globally:

	:::bash
	$ pip install virtualenv
	
Then I create a virtual environment in `~/virtualenvs/pelican`:

	:::bash
	$ virtualenv ~/virtualenvs/pelican
	
To activate the virtual environment:

	:::bash
	$ cd ~/virtualenvs/pelican
	$ source bin/activate
	
Now we are ready to install Pelican and Markdown that I use for writing posts like this one.

	:::bash
	$ pip install pelican
	$ pip install Markdown
	
Pelican has a nice feature that helps you kickstart your site. 

	:::bash
	$ pelican-quickstart	

This will prompt some questions that set up some basic configurations which can be changed in `pelicanconf.py`. 

When Pelican is installed, there are a couple of dependencies are being installed automatically at the same time:

* [**feedgenerator**](https://pypi.python.org/pypi/feedgenerator) - to generate the Atom feeds
* [**jinja2**](https://pypi.python.org/pypi/Jinja2) - for templating support
* [**pygments**](https://pypi.python.org/pypi/Pygments) - for syntax highligting
* [**docutils**](https://pypi.python.org/pypi/docutils) - for supporting reStructuredText as an input format
* [**pytz**](https://pypi.python.org/pypi/pytz) - for timezone definitions
* [**blinkers**](https://pypi.python.org/pypi/blinker) - an object-to-object and broadcast signaling system
* [**unidecode**](https://pypi.python.org/pypi/Unidecode) - for ASCII transliterationsn of Unicode text
* [**six**](https://pypi.python.org/pypi/six) - for Python 2 and 3 compatibility utilities
* [**MarkupSafe**](https://pypi.python.org/pypi/MarkupSafe) - for a markup safe string implementation
* [**python-dateutil**](https://pypi.python.org/pypi/python-dateutil) - to read the date metadata

Once Pelican is installed, it provides a skeleton structure:
Use the command `tree` to generate a directory tree:

	:::bash
	$ tree
	blog/
  	├── content
  	│   └── (pages)
  	│   └── (images)
  	├── output
  	├── develop_server.sh
  	├── fabfile.py
  	├── Makefile
  	├── pelicanconf.py       
  	└── publishconf.py

I will go through each of them with a brief explanation. 
 
`content`, as the name suggests, is a directory where you put your content like articles, blog posts and images.  By default, Pelican is configured to treat all pages in the `pages` directory as static pages which are not sorted in chronological order. In other word, you should put static pages like About me, Projects, Contact, etc. inside  the `pages` directory. 

`output` is where the html, css and javascript files Pelican generated are. 
 
`Makefile` defines actions for the command `make`, for example the command `make html` make html files out of the blog contents (in`.md` or `.rst` format). It also contains other commands such as `make devserver` and etc. More about `make` [here](http://www.gnu.org/software/make/manual/).

`fabfile` is a configuration file for [Fabric](http://www.fabfile.org/). You can use a command `fab serve` to generate the site and review at `http://localhost:8000`. Please note that you need to install Fabric seperately via:

	:::bash
	$ pip install Fabric

Instead of `fab`, I use `make`. 

`pelicanconf.py` is a main settings file that will be passed to the templates when the site is generated so the settings are site-wide. If you didn't install pelican with the `pelican-quickstart` comment, this file will be named `settingsfile.py` instead.

`publishconf.py` contains settings to use when ready to publish. It is not aimed to be used locally. So far I haven't had the need to edit this file. 


Now it's time to put some content! Open your text editor of choice and start writing. I use Markdown syntax so it looks something like this in the editor:

	:::
	Title: My first post
	Date: 2014-09-09 11:00
	Category: Python
	Tags: pelican, blog
	Slug: my-first-post
	Authors: Bonnie Chan
	Lang: en
	
	This is my newly opened Pelican blog!

Save it as `.md` file in `content`folder. Almost ready! To generate the site:
	
	:::bash
	$ make devserver
 
Your website should be ready at `http://localhost:8000`. When you edit any files, it will automatically generate the site with the new changes. Once you are happy with it, you can stop the development server: 
	
	:::bash
	$ ./develop_server.sh stop

What's left to do is to think about how you want to host your site. You can host it on a server running Apache or Nginx or via GitHub pages. There are plenty of deployment options to choose from. For more information, check out Pelican [tips](http://docs.getpelican.com/en/3.4.0/tips.html) on deployment. 


##Links
* [Command Line Crash Course](http://learnpythonthehardway.org/book/appendixa.html)
* [Learn Python the Hard Way](http://learnpythonthehardway.org/book/)
* [Homebrew and Python](https://github.com/Homebrew/homebrew/wiki/Homebrew-and-Python)
* [virtualenv Documentation](http://virtualenv.readthedocs.org/)


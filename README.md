# python-learn

Going to be learning python seriously now.
Hopefully this will be helpful reference in the future.

Some things to note:

## Installation for windows and Visual Studio Code

1. Install Git for [windows.](https://github.com/git-for-windows/git/releases/download/v2.24.1.windows.2/Git-2.24.1.2-64-bit.exe)
2. git config --global user.email "email@gmail.com"
3. git config --global user.name "username"
4. git clone \*\*<\repo url>\*\*
5. Run git push to get dialog box to login.
6. After succesful login try to git commit -> git push.

## Third Project-Battle
Text based RPG Game. 

- Stuff to work on:
  - Level system
  - Extra characters and balance system
  - Progression? 
  - GUI?

## VScode and adding python virtualenv

Ran into an error saying that the virtualenv path isn't part of the environment.

1. Copy the path that virtual env installed to. pip3 install virtualenv
2. Open up system variables and add that path to your system environment PATH.
3. Restart VScode

### VSCode and virtualenv-wrapper

To switch between different projects that may have different packages installed you can use virtualenvwrapper-win
1. pip install virtualenvwrapper-win
2. mkvirtualenv, lsvirtualenv, rmvirtualenv, workon, deactivate, add2virtualenv

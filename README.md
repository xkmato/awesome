awesome
=======

Code-Name Awesome is the to be 24/7 Online Digital all Arts Festival.

What you have to do in advance

- Email me your github username to kenneth@kudu.ug

- Run syncdb
- If you have custom settings or want a custom db then please create a localsettings.py file
- If for some reason you want a different sqlite database then please also put it's file name into the .gitingnore file

How to get the app

- Go to the folder you want to run your project using command
- Type the the command "git clone git@github.com:xkmato/awesome.git "
- Make the changes to the app
- Make sure you also edit the .gitignore file to add the directory that you IDE auto-creates to manage the project "no trailing slash", for pycharm its '.idea', you don't have to do anything, I already added it

Before you push
- Go to the folder you're running your project using command
- Type the command "git status"
- Make sure all the files displayed below are files that you actually intended add or modify to the project
- If yes
    - Type the command 'git add .'
    - Type the command "git commit -m'some relevant message here'"
    - *Before you push make a pull*
    - Type the command "git pull origin master"
    - If all is up-to-date:
       - Type the command "git push git@github.com:xkmato/awesome master"
         That will be all
    - If not:
        - look at the changes and see if you agree or make changes
        - do what you would have done if all-is-up-to-date
- If no
    - You probably didn't add the the auto-created directory to .gitignore, do that
    - The still no: Don't push anything wait for my help
    - If yes, do what you would have done if yes


My suggestion is everyone create a different template folder with the basic design so we don't have them contradicting

Convention
 - All class names start with capital letters and each new word does as well eg class AwesomeKen:
 - All attributes and function names must be all lower case different words separated with "_" eg def awesome_ken():
 - Use real english names that make sense to name anything. Do not use short hand



 Add all the suggestions to this file
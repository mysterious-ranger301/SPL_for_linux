SPL_for_linux
Working SPL version for Linux! Additional module required: "os" and "subprocess"
This is version 1.1.3
How to use:
import SPL_for_linux as SPL # import the module
myspl = SPL.splObj() # set myspl as an SPL class
Functions:
myspl.__instructions__ # useful if you forgot how to use
myspl.__version__ # if you forgot what version it is
myspl._ls() # displays files/folders in current directory
myspl._cd(folder) # moves working directory into "folder"
myspl.cmd(command) # uses os.system() to use command line
myspl._cmdOpenFile(file, path='.') # uses command line to open file
myspl._pwm() # displays current working dir
myspl.checkpath(path) # same as os.path.exists
myspl.openWithApp(file, app) # opens file with app (enter path of both file and app)
Note that myspl.Open() was removed due to issues
myspl.openApp(app_path) # opens app on app_path
And that's it!

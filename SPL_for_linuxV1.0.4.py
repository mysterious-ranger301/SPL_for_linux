# -*- coding: utf-8 -*-
"""
Created on Sat Jun  6 14:29:13 2020

@author: alexe
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Jun  3 18:35:00 2020

@author: Mysterious Ranger
SPL - subprocess library simplified
Linux Version
Command line functions are disabled (commented) so uncomment them and try to replicate them
"""
import subprocess as sp, os

class cmd:
    def __init__(self):
#        spl = splObj()
#        self.__author__ = spl.__author__
        self.__instructions__ = '''Unlike SPL, the cmd() class uses the command line to do things. SPL's Open() function isn't reliable for opening files with extensions like .mp4, .mp3, or .wav. Use the _cmdOpenFile(file, path) instead. Syntax of _cmdOpenFile(file, path): where 'file' is the name of the file you want to open (with the extension). You don't need to specify 'path', its default value is '.'. The cmd() and SPL() libraries are linked together, so you can use all the functions from both cmd() and SPL().'''
        self.__author__ = 'Mysterious Ranger'
        self.__version__ = '1.0.4'
        self.SplError = SplError
        self.err_file_path = 'File path not found.'
        self.err_app_path = 'App path not found.'
        self.linux_err = 'Linux version. Command line is disabled.'
    def _ls(self):
#        self.cmd('ls')
        raise self.SplError(self.linux_err)
    def _clear(self):
#        self.cmd('clear')
        raise self.SplError(self.linux_err)
    def _cd(self, folder):
#        import os
        os.chdir(folder)
	# Why this is like this, is because self.cmd('cd folder') doesn't work
    def cmd(self, comm):
        sp.call(comm, shell=True)
    def _cmdOpenFile(self, file, path='.'):
#        self._cd(path)
#        if not self.checkpath(file):
#            raise self.SplError(self.err_file_path)
#        self.cmd('open "{0}"'.format(file))
        raise self.SplError(self.linux_err)
    def _pwm(self):
        return os.getcwd()
    def checkpath(self, path):
        if os.path.exists(path):
            return True
        else:
            return False

class SPL(cmd):
    def __init__(self):
        super().__init__()
#        self.__instructions__ = '''This is a library that simplifies
#the module 'subprocess'. This is useful if your program needs to open
#other apps like notepad, calc, etc. Created by Mysterious Ranger.'''
#        self.SplError = SplError
    def openWithApp(self, file, app):
        if not self.checkpath(file):
            raise self.SplError(self.err_file_path)
        if not self.checkpath(app):
            raise self.SplError(self.err_app_path)
        sp.Popen([app, file], shell=True)
#    def openWDA(self, file, app='start'):
#        if not os.path.exists(file):
#            raise SplError
#        sp.Popen([app, file], shell=True)
    def Open(self, file, app='see'):
        if not self.checkpath(file):
            raise self.SplError(self.err_file_path)
        sp.Popen([app, file], shell=True)
    def openApp(self, path):
        if not self.checkpath(path):
            raise self.SplError(self.err_app_path)
        sp.Popen(path)
#    def cmd(self, command):
#        sp.call(command, shell=True)
    
class SplError(Exception):
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None
#        self.SplError = self
    def __str__(self):
        #print('calling str')
        if self.message:
            return str(self.message)
        else:
            return 'Something was typed incorrectly. Check the code and try\
 again.'

def splObj():
    return SPL()
def cmdObj():
    return cmd()

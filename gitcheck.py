#!/usr/bin/env python

import os
import sys
import subprocess 
import functools 

def load_path():
    if len(sys.argv) < 2:
        print 'usage: %s PATH' % (sys.argv[0])
        sys.exit(1)

    return sys.argv[1]

def describe_git_repo(directory):
    """describe the git repository at DIRECTORY"""

    home = os.getcwd()
    os.chdir(directory)

    repo = os.path.basename(directory)
    outp = subprocess.check_output(['git', 'remote'])
    os.chdir(home)

    if (len(outp) <= 0):
        return { 'path': directory, 'name': repo }
    else:
        return None

def scan_directories(root):
    """Starting at ROOT, run through all directories and describe
    and describe all git repositories found."""
   
    repositories = []
   
    for directory, dirs, files in os.walk(root):
        if '.git' in dirs:
            repo = describe_git_repo(directory)
            if repo is not None:
                repositories.append(repo)

    return repositories

def display_report(repositories):
    """Given a list of REPOSITORIES, display to screen."""

    print ''
    print 'The following git repositories have no remote origin:'
    print '====================================================='
    print ''
    for repo in repositories:
        print '%s\t%s' % (repo['name'], repo['path'])



# Main program begins
# ========================
def main():
    path = load_path()

    repositories = scan_directories(path)
    display_report(repositories)

if __name__ == '__main__':
    main()

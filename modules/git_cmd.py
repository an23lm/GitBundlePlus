#!/usr/bin/env python

import os
import subprocess
from .constants import Constants

class Git:

    statuslist = []
    stashlist = []

    @staticmethod
    def status(path):
        cmdstring = ['cd {}; git status -s'.format(path)]
        cmd = subprocess.Popen(cmdstring, shell=True, stdout=subprocess.PIPE)
        cmd.wait()
        for line in cmd.stdout:
            Git.statuslist.append(line)
        return cmd.returncode

    @staticmethod
    def stash_list(path):
        cmdstring = ['cd {}; git stash list'.format(path)]
        cmd = subprocess.Popen(cmdstring, shell=True, stdout=subprocess.PIPE)
        cmd.wait()
        if cmd.returncode == 0:
            cmdstring = ['cd {}; git stash list | grep -o \"stash@{{.*}}\"'.format(path)]
            cmd = subprocess.Popen(cmdstring, shell=True, stdout=subprocess.PIPE, universal_newlines=True)
            cmd.wait()
            for line in cmd.stdout:
                Git.stashlist.append(line.strip())
            return 0
        return cmd.returncode
    
    @staticmethod
    def stash(path):
        cmdstring = ['cd {}; git stash -u | grep "No .*"'.format(path)]
        cmd = subprocess.Popen(cmdstring, shell=True, stdout=subprocess.PIPE)
        cmd.wait()
        return cmd.returncode

    @staticmethod
    def tag_ref(tag_name, ref_name, path):
        cmdstring = ['cd {}; git tag {} {}'.format(path, tag_name, ref_name)]
        cmd = subprocess.Popen(cmdstring, shell=True, stdout=subprocess.PIPE)
        cmd.wait()
        return cmd.returncode

    @staticmethod
    def tag_refs(path):
        for idx, name in enumerate(Git.stashlist):
            Git.tag_ref(Constants.stash_tag_pattern.format(idx), name, path)
    
    @staticmethod
    def bundle(path):
        cmdstring = ['cd {}; git bundle create {}{} --all'.format(path, os.path.basename(path), ".bundle")]
        cmd = subprocess.Popen(cmdstring, shell=True, stdout=subprocess.PIPE)
        for line in cmd.stdout:
            print(line)
        cmd.wait()
        print(cmd.returncode)
        return cmd.returncode

    @staticmethod
    def del_tag_ref(tag_name, path):
        cmdstring = ['cd {}; git tag -d {}'.format(path, tag_name)]
        cmd = subprocess.Popen(cmdstring, shell=True, stdout=subprocess.PIPE)
        cmd.wait()
        return cmd.returncode

    @staticmethod
    def del_tag_refs(path, stashcode):
        if stashcode == 0:
            Git.del_tag_ref(Constants.stash_tag_pattern.format(Constants.stash_tag_latest), path)
        for idx in range(len(Git.stashlist)):
           Git.del_tag_ref(Constants.stash_tag_pattern.format(idx), path)
    
    @staticmethod
    def get_current_branch(path):
        cmdstring = ['cd {}; git branch | grep \* | cut -d " " -f 2'.format(path)]
        cmd = subprocess.Popen(cmdstring, shell=True, stdout=subprocess.PIPE)
        cmd.wait()
        return cmd.returncode

#! /usr/bin/python3

import os

def insert_comment(file_path):
    with open(file_path, 'r+') as file:
        lines = file.readlines()
        file.seek(0)
        for line in lines:
            if "- name" in line:
                name = line.split("- name", 1)[1]
                file.write("# @name: " + name)
                file.write("# @comment: \n")
                file.write("# @code: \n")
                file.write("# @input:\n")
                file.write("# @output:\n")
            if "- hosts" in line:
                hosts = line.split("- hosts:", 1)[1]
                file.write("# @hosts: " + hosts)
            file.write(line)
        file.truncate()

# Example usage
insert_comment('scripts/ansible-clamav.yml')

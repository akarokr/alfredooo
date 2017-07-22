#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import yaml
import argparse
import tempfile
from git import Repo
import shlex
import subprocess

"""
    Alfredooo is the new CI tool, made by a lazy developer. With Alfredooo
    you just the your pipeline.yml file and boom, call him: "ALFREDOOOO".

    Reference: https://www.youtube.com/watch?v=iIsANBIa-JI

    Made with <3 by Luiz Neto

"""


class color:
    """
        This class generate color for strings in this script. For each color
        you have to end with the END variable.

        Example:

        print (color.PURPLE + "Your magic string." + color.END)

    """

    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'


"""
    The parser is used to receive the desirable parameters from the pipeline
    file.

    Example:
        alfredooo.py -p <PIPELINE_TASK> -u <GIT_URL>

        The "p" will be the pipeline and the "u" the git repository.
"""

parser = argparse.ArgumentParser()
parser.add_argument('-p', '--pipeline',
                    dest='pipeline',
                    help='desirable pipeline',
                    required=True)

parser.add_argument('-u', '--url',
                    dest='git_url',
                    help='repository url',
                    required=True)

args = parser.parse_args()
pipeline_arg = args.pipeline
git_url = args.git_url
git_dir = tempfile.mkdtemp()  # tempfile is for the temp dir in /tmp
Repo.clone_from(git_url, git_dir)  # clonned repo from bitbucket/github etc.
yaml_file = '{0}/pipeline.yml'.format(git_dir)  # the YAML file

with open(yaml_file, 'r') as fp:  # open the yaml file
    pipeline = fp.read()  # read the file
    yaml_object = yaml.load(pipeline)


def yaml_list_to_dict(yaml_list):
    yaml_dict = {}
    for element in yaml_list:
        for key, value in element.items():
            yaml_dict[key] = value
    return yaml_dict

tasks = yaml_list_to_dict(yaml_object['tasks'])
pipelines = yaml_list_to_dict(yaml_object['pipelines'])

ok_message = """
{}{} ..... OK ...... {}
""".format(color.BOLD, color.GREEN, color.END)

error_message = """
{}{} ..... ERROR ...... {}
""".format(color.BOLD, color.RED, color.END)

info_message = """
{} ..... RUNNING {{}} ...... {}
""".format(color.BOLD, color.END)

pipeline = pipelines.get(pipeline_arg)
if not pipeline:
    print('Argumento inexistente: {}'.format(pipeline_arg))
    exit(1)

for task in pipeline:
    print(info_message.format(task))
    command = tasks[task]['cmd']
    args = shlex.split(command)
    subprocess.call(args, cwd=git_dir)
    if subprocess.call(args, cwd=git_dir) != 0:
        print(error_message)
        exit(1)
    else:
        print(ok_message)

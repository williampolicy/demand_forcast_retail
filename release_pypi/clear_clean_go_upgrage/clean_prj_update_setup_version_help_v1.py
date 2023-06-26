#!/usr/bin/env python3

import os
import shutil
import subprocess
import re
import argparse
import sys


def print_tree(directory, level=2):
    print(f"\nDirectory structure ({directory}):")
    subprocess.run(['tree', '-L', str(level), directory])


def delete_certain_files_and_dirs(start_path):
    for dirpath, dirnames, filenames in os.walk(start_path):
        if '__pycache__' in dirnames:
            print(f"Delete directory: {os.path.join(dirpath, '__pycache__')}")
            shutil.rmtree(os.path.join(dirpath, '__pycache__'))
        for filename in filenames:
            if filename.endswith(('.png', '.log')):
                print(f"Delete file: {os.path.join(dirpath, filename)}")
                os.remove(os.path.join(dirpath, filename))


def delete_contents_in_specific_dirs(specific_dirs):
    for dir in specific_dirs:
        if os.path.exists(dir):
            for item in os.listdir(dir):
                item_path = os.path.join(dir, item)
                if os.path.isfile(item_path):
                    print(f"Delete file: {item_path}")
                    os.remove(item_path)
                elif os.path.isdir(item_path):
                    print(f"Delete directory: {item_path}")
                    shutil.rmtree(item_path)


def delete_specific_dirs(specific_dirs):
    for dir in specific_dirs:
        if os.path.exists(dir):
            print(f"Delete directory: {dir}")
            shutil.rmtree(dir)


def clean_project():
    print_tree('.')
    print("\nclear - clean - go..... process...")
    delete_certain_files_and_dirs('.')
    delete_contents_in_specific_dirs(['dist'])
    delete_specific_dirs(['build', 'kangforecast.egg-info', 'env_kangpypi'])
    print("\nFinished cleaning.")
    print_tree('.')


def update_version():
    with open('setup.py', 'r') as f:
        content = f.read()

    version_match = re.search(r"version='(.*)'", content)
    if version_match is None:
        raise Exception("Could not find version in setup.py")

    version_parts = list(map(int, version_match.group(1).split('.')))
    version_parts[-1] += 1

    new_version = '.'.join(map(str, version_parts))
    content = re.sub(r"version='(.*)'", "version='{}'".format(new_version), content)

    with open('setup.py', 'w') as f:
        f.write(content)

    # with open('new_version.txt', 'w') as f:
    #     f.write(new_version)

    print(f'Updated setup.py to version {new_version}')


def main():
    parser = argparse.ArgumentParser(description="Automate the process of cleaning the project, updating version and uploading the new version.")
    parser.add_argument('--clean', action='store_true', help='Clean the project by deleting certain files and directories.')
    parser.add_argument('--update', action='store_true', help='Update the version number in setup.py.')
    args = parser.parse_args()

    if len(sys.argv)==1:
        parser.print_help(sys.stderr)
        sys.exit(1)

    if args.clean:
        clean_project()

    if args.update:
        update_version()


if __name__ == "__main__":
    main()

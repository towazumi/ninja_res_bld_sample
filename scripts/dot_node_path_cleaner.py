import os
import sys
import argparse

if __name__=='__main__':

    # 引数処理
    parser = argparse.ArgumentParser()
    parser.add_argument('dotfile')
    parser.add_argument('root_dir')
    args = parser.parse_args()

    root_dir = os.path.abspath(args.root_dir)
    root_dir = root_dir.replace('\\','/')
    if not root_dir.endswith('/'):
        root_dir += '/'

    with open(args.dotfile, 'r') as f:
        content = f.read()

    with open(args.dotfile, 'w') as f:
        f.write(content.replace(root_dir, ''))


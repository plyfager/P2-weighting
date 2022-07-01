# Copyright (c) OpenMMLab. All rights reserved.
import argparse
import os
import os.path as osp
import sys


def parse_args():
    parser = argparse.ArgumentParser(description='DDPM demo')
    parser.add_argument('path', help='test config file path')
    args = parser.parse_args()
    return args

def main():
    args = parse_args()
    folder_paths = os.listdir(args.path)
    for folder in folder_paths:
        filenames = os.listdir(os.path.join(args.path, folder))
        for filename in filenames:
            new_filename = folder + "_" + filename
            os.rename(os.path.join(args.path, folder, filename), os.path.join(args.path, folder, new_filename))



if __name__ == '__main__':
    main()

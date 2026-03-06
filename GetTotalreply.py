# -*- coding: UTF-8 -*-
#!/usr/bin/env/ python3
import re
import sys
import io
import os
import json
import math
import argparse
#sys.excepthook = lambda *args: exit(1)
# def remov(path):
#     path=path.encode('utf-8')
#     if(os.path.exists(path)):
#         os.remove(path)

def get_data_directory():
    """Get data directory from command-line arg, env var, or default."""
    parser = argparse.ArgumentParser(
        description='Update total reply counts from backup data'
    )
    parser.add_argument(
        '--data-dir', '-d',
        type=str,
        default=None,
        help='Path to backup data directory (default: $S1_BACKUP_DIR or ./data/)'
    )
    args = parser.parse_args()
    
    if args.data_dir:
        return args.data_dir
    elif os.environ.get('S1_BACKUP_DIR'):
        return os.environ.get('S1_BACKUP_DIR')
    else:
        # Default to ./data/ relative to script location
        script_dir = os.path.dirname(os.path.abspath(__file__))
        return os.path.join(script_dir, 'data')


if __name__ == '__main__':
    rootdir = get_data_directory()
    if not rootdir.endswith(os.sep):
        rootdir += os.sep
    
    with open(os.path.join(rootdir, 'RefreshingData.json'), "r", encoding='utf-8') as f:
        thdata=json.load(f)
    for i in range(len(thdata)):
        if(thdata[i]['active']):
            ThreadID = thdata
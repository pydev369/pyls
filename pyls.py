import argparse
import json
import os
import time

def load_json(filename):
    with open(filename, 'r') as f:
        return json.load(f)

def list_directory_contents(directory, show_all=False, long_format=False, reverse=False, sort_by_time=False, filter_by=None, human_readable=False):
    contents = directory.get('contents', [])
    
    if not show_all:
        contents = [item for item in contents if not item['name'].startswith('.')]
    
    if sort_by_time:
        contents.sort(key=lambda x: x['time_modified'], reverse=True)
    
    if reverse:
        contents.reverse()
    
    if filter_by == 'file':
        contents = [item for item in contents if 'contents' not in item]
    elif filter_by == 'dir':
        contents = [item for item in contents if 'contents' in item]

    for item in contents:
        if long_format:
            print_long_format(item, human_readable)
        else:
            print(item['name'])

def print_long_format(item, human_readable=False):
    permissions = item['permissions']
    size = human_readable_size(item['size']) if human_readable else item['size']
    time_modified = time.strftime('%b %d %H:%M', time.localtime(item['time_modified']))
    name = item['name']
    print(f"{permissions} {size} {time_modified} {name}")

def human_readable_size(size):
    for unit in ['B', 'K', 'M', 'G', 'T', 'P']:
        if size < 1024:
            return f"{size:.1f}{unit}"
        size /= 1024

def find_directory(path, current_directory):
    if path == '.':
        return current_directory
    
    parts = path.split('/')
    for part in parts:
        if part == '.':
            continue
        found = next((item for item in current_directory['contents'] if item['name'] == part and 'contents' in item), None)
        if not found:
            raise FileNotFoundError(f"error: cannot access '{path}': No such file or directory")
        current_directory = found
    return current_directory

def main():
    parser = argparse.ArgumentParser(description="A Python ls utility")
    parser.add_argument('-A', action='store_true', help='do not ignore entries starting with .')
    parser.add_argument('-l', action='store_true', help='use a long listing format')
    parser.add_argument('-r', action='store_true', help='reverse order while sorting')
    parser.add_argument('-t', action='store_true', help='sort by time modified')
    parser.add_argument('--filter', choices=['file', 'dir'], help='filter by file or directory')
    parser.add_argument('-h', action='store_true', help='show human-readable sizes')
    parser.add_argument('path', nargs='?', default='.', help='path to list')
    
    args = parser.parse_args()
    
    directory = load_json('structure.json')
    target_directory = find_directory(args.path, directory)
    
    list_directory_contents(target_directory, show_all=args.A, long_format=args.l, reverse=args.r, sort_by_time=args.t, filter_by=args.filter, human_readable=args.h)

if __name__ == "__main__":
    main()

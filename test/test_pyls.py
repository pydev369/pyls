
from .pyls import load_json, list_directory_contents, find_directory,human_readable_size
import pytest
import json

# Load test data
test_data = {
    "name": "interpreter",
    "size": 4096,
    "time_modified": 1699957865,
    "permissions": "-rw-r--r--",
    "contents": [
        {
            "name": ".gitignore",
            "size": 8911,
            "time_modified": 1699941437,
            "permissions": "drwxr-xr-x"
        },
        {
            "name": "LICENSE",
            "size": 1071,
            "time_modified": 1699941437,
            "permissions": "drwxr-xr-x"
        },
        {
            "name": "README.md",
            "size": 83,
            "time_modified": 1699941437,
            "permissions": "drwxr-xr-x"
        },
        {
            "name": "ast",
            "size": 4096,
            "time_modified": 1699957739,
            "permissions": "-rw-r--r--",
            "contents": [
                {
                    "name": "go.mod",
                    "size": 225,
                    "time_modified": 1699957780,
                    "permissions": "-rw-r--r--"
                },
                {
                    "name": "ast.go",
                    "size": 837,
                    "time_modified": 1699957719,
                    "permissions": "drwxr-xr-x"
                }
            ]
        }
    ]
}

def test_load_json(monkeypatch):
    monkeypatch.setattr('builtins.open', lambda f, mode: open(f))
    data = load_json('structure.json')
    assert data['name'] == 'interpreter'

def test_find_directory():
    directory = find_directory('ast', test_data)
    assert directory['name'] == 'ast'

def test_list_directory_contents(capsys):
    list_directory_contents(test_data, show_all=True)
    captured = capsys.readouterr()
    assert 'LICENSE' in captured.out
    assert '.gitignore' in captured.out

def test_list_directory_contents_long_format(capsys):
    list_directory_contents(test_data, show_all=True, long_format=True)
    captured = capsys.readouterr()
    assert '-rw-r--r-- 1071' in captured.out

def test_list_directory_contents_reverse(capsys):
    list_directory_contents(test_data, show_all=True, reverse=True)
    captured = capsys.readouterr()
    assert captured.out.splitlines()[-1] == '.gitignore'

def test_list_directory_contents_sort_by_time(capsys):
    list_directory_contents(test_data, show_all=True, sort_by_time=True)
    captured = capsys.readouterr()
    assert captured.out.splitlines()[-1] == 'LICENSE'

def test_human_readable_size():
    assert human_readable_size(1023) == '1023.0B'
    assert human_readable_size(1024) == '1.0K'
    assert human_readable_size(1048576) == '1.0M'
    assert human_readable_size(1073741824) == '1.0G'

def test_list_directory_contents_human_readable(capsys):
    list_directory_contents(test_data, show_all=True, long_format=True, human_readable=True)
    captured = capsys.readouterr()
    assert '1.0K' in captured.out
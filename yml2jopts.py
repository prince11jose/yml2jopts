"""
Title: YML to Java Options Converter

Author: Prince Jose
Email: prince11jose@hotmail.com
Date Created: 2024-04-26
Last Modified: 2024-08-12
Description: This script converts YAML configuration files into Java command-line options.
             It removes comments from the YAML file before processing and handles nested
             dictionaries by flattening the keys.

Usage:
    python yml2opts.py <yaml_file> [--newline]

Dependencies:
    - PyYAML

License: MIT License
"""

import sys
import yaml

def load_yaml(file_path):
    with open(file_path, 'r') as file:
        content = yaml.safe_load(file)
    return content

def convert_to_java_options(data):
    java_options = []
    for key, value in data.items():
        if isinstance(value, dict):
            flattened_keys = flatten_keys(value)
            for sub_key, sub_value in flattened_keys.items():
                java_options.append(f'-D{key}.{sub_key}={sub_value}')
        else:
            java_options.append(f'-D{key}={value}')
    return java_options

def flatten_keys(dictionary, parent_key='', separator='.'):
    items = {}
    for k, v in dictionary.items():
        new_key = f"{parent_key}{separator}{k}" if parent_key else k
        if isinstance(v, dict):
            items.update(flatten_keys(v, new_key, separator=separator))
        else:
            items[new_key] = v
    return items

def remove_comments(lines):
    return [line for line in lines if not line.strip().startswith('#')]

def main(yaml_file, newline=False):
    lines = None
    with open(yaml_file, 'r') as file:
        lines = file.readlines()
    lines = remove_comments(lines)
    yaml_content = ''.join(lines)
    data = load_yaml(yaml_file)
    java_options = convert_to_java_options(data)

    if newline:
        print('\n'.join(java_options))
    else:
        print(' '.join(java_options))

if __name__ == "__main__":
    if len(sys.argv) < 2 or len(sys.argv) > 3:
        print("Usage: yml2opts <yaml_file> [--newline]")
        sys.exit(1)

    yaml_file = sys.argv[1]
    newline = '--newline' in sys.argv
    main(yaml_file, newline)

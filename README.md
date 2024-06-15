# YML2JOpts
YML2JOpts is a simple Python utility that converts YAML configuration files into Java command-line options. This can be particularly useful for configuring Java applications with complex settings managed in YAML files.

## Features
Convert YAML to Java Options: Easily converts nested YAML structures into Java command-line options.
Remove Comments: Automatically removes comments from YAML files before processing.
Flatten Keys: Handles nested dictionaries and flattens keys to create appropriate Java options.

## Requirements
Python 3.x
PyYAML

## Installation

Clone the repository:
```
git clone https://github.com/janedoe/yml2opts.git
```

## Install the required dependencies:
```
pip install pyyaml
```

## Usage
```
python yml2opts.py <yaml_file>
```

## Example:
Given a YAML file config.yml:

## This is a comment
database:
  host: localhost
  port: 5432
  credentials:
    username: admin
    password: secret

logging:
  level: DEBUG

Running the script:
```
python yml2opts.py config.yml
```
Will produce the following output:
```
-Ddatabase.host=localhost -Ddatabase.port=5432 -Ddatabase.credentials.username=admin -Ddatabase.credentials.password=secret -Dlogging.level=DEBUG
```
## Function Descriptions

load_yaml(file_path)
Loads and parses a YAML file.

Parameters: file_path (str) - The path to the YAML file.
Returns: Parsed YAML content as a dictionary.
convert_to_java_options(data)
Converts a dictionary to a list of Java command-line options.

Parameters: data (dict) - The dictionary to convert.
Returns: A list of Java options as strings.
flatten_keys(dictionary, parent_key='', separator='.')
Flattens nested dictionaries.

## Parameters:
dictionary (dict) - The dictionary to flatten.
parent_key (str) - The base key for nested keys.
separator (str) - The separator to use between keys.
Returns: A flattened dictionary.
remove_comments(lines)
Removes comments from a list of lines.

Parameters: lines (list of str) - The lines to process.
Returns: A list of lines without comments.
main(yaml_file)
Main function to handle the script logic.

Parameters: yaml_file (str) - The path to the YAML file.
## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Author
Prince Jose
prince11jose@hotmail.com
[GitHub](https://github.com/prince11jose)
[LinkedIn](https://www.linkedin.com/in/princejose-devops/)


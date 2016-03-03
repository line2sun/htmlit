"""
This file contains all CLI specific code base.
=============================================

Usage: htmlit [OPTIONS] INPUT

  Run htmlit from the command line, and parses CLI options using click.

Options:
  -o   The path to output folder.
  -v   Print all warning messages.
  --help   Show this message and exit.


Example:

    htmlit path/to/input.md ~/htmlit/output.html
or
    ./markdown http://example.com/markdown/input.md

"""

import click
import logging
import htmlit as markdown


def process_input_argument(input_argument):
    file_path = None
    url = None

    # Check either the input is an URL or a file path
    if input_argument is not None:
        if input_argument.split('.')[0].split(':')[0] in ['http', 'https', 'www']:
            url = input_argument
        else:
            file_path = input_argument

    return file_path, url


def parse_options(input=None, output_path='~/markdown/outputs', verbose=0):
    """ Parses CLI options using click.
    :param input:
    :param output_path:
    :param verbose:
    :return:
    """
    input_file_path, input_url = process_input_argument(input)

    options = {
        'input_file_path': input_file_path,
        'output_path': output_path,
        'input_url': input_url
    }

    return options


@click.command()
@click.argument('input')
@click.option('-o', 'output_path', default='~/markdown/outputs', help="The path to output folder.")
@click.option('-v', 'verbose', default=False, count=True, help='Print all warning messages.')
def run(input, output_path, verbose):
    """ Run markdown from the command line.
    """
    markdown_options = parse_options(input, output_path, verbose)

    # Pass the options to Controller Layer
    markdown.Markdown(**markdown_options).convert()

if __name__ == '__main__':
    run()
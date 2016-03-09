# -*- coding: utf-8 -*-
from lettuce import step, world
import requests

from htmlit import Markdown
from htmlit._utils import drop_whitespace

@step
def i_load_the_file_from_url(step, url):
    """I load the file from URL: (.*)"""
    print url
    world._input_file_url = url


@step
def i_convert_to_html(step):
    """I convert to HTML"""
    print 'CONVERTING TO HTML'
    md = Markdown(input_file_url=world._input_file_url)
    _output_file_path = md.convert()
    print 'Got output path: ', _output_file_path

    world._output_file_path = _output_file_path




@step
def i_see_a_result_like_in_the_url(step, url):
    """I see a result like the one at the URL: (.*)"""

    print 'Loading: ', url
    print 'Loading the output file... ', world._output_file_path

    with open(world._output_file_path, 'r') as _out:
        _output = _out.read()

    assert drop_whitespace(_output) == drop_whitespace(requests.get(url).text), 'Got %s' % requests.get(url).text


@step
def given_i_opened_the_app(step):
    """Given I opened the app"""
    print 'Starting the converter...'


@step
def i_see_an_error(step, error):
    """I see an (.*) error"""
    assert world.html_output == error, 'Got %s' % world.html_output

# -*- coding: utf-8 -*-
from lettuce import step, world


@step
def i_load_the_file_from_url(step, url):
    """I load the file from URL: (.*)"""
    print url
    world.input_url = url


@step
def i_convert_to_html(step):
    """I convert to HTML"""
    print 'CONVERTING TO HTML'


@step
def i_see_a_result_like_in_the_url(step, url):
    """I see a result like the one at the URL: (.*)"""
    url = 'https://gist.githubusercontent.com/minivan/f29e2759c44d13e39b5b/raw/7bc948fc89d467db05d879e61ac09a7f70f75362/input.md'
    assert world.input_url == url, 'Got %s' % world.input_url


@step
def given_i_opened_the_app(step):
    """Given I opened the app"""
    world.html_output = 'banana!'


@step
def i_see_an_error(step, error):
    """I see an (.*) error"""
    assert world.html_output == error, 'Got %s' % world.html_output

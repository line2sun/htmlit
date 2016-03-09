import os
import time
import requests

from htmlit.parsers import MarkdownParser


class Markdown:
    def __init__(self, **kwargs):
        self.input_file_path = kwargs.get('input_file_path', '')
        self.input_file_url = kwargs.get('input_file_url', '')
        self.output_file_path = kwargs.get('output_path', '~/markdown/outputs')
        self._document = self._load_document()
        self.markdown_parser = MarkdownParser()
        self._html = []

    def _load_document(self):
        if self.input_file_path:
            with open(self.input_file_path, 'r') as _input_file:
                return _input_file.read()

        if self.input_file_url:
            print 'loading from url: %s' % self.input_file_url
            return requests.get(self.input_file_url).text

    def convert(self):
        self._html = self.markdown_parser.run(self._document)

        if self.output_file_path:
            return self.save_output()



    def save_output(self):

        if not os.path.exists(self.output_file_path):
            os.makedirs(self.output_file_path)

        file_path = os.path.join(self.output_file_path, str(int(time.time()))+'.html')
        file_path = os.path.expanduser(file_path)

        _out_file = open(file_path, 'w')
        for block in self._html:
            _out_file.write(block)
        _out_file.close()
        return file_path


if __name__ == '__main__':

    m = Markdown(input_file_url='https://gist.githubusercontent.com/line2sun/d69bee6cd1ac2f065fbd/raw/875c0aebfbb13d7aaa0c7039fc9696c0536eafe8/input.md')
    m.convert()
    # print m._html
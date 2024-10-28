from html.parser import HTMLParser

class ListCounterParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.current_ul_list = []
        self.highest_ul_list = []
        self.is_in_ul_tag = False
        self.current_child_len = 0

    def handle_starttag(self, tag, attr):
        if tag == 'ul':
            if self.is_in_ul_tag:
                self.current_child_len += 1
            else:
                self.is_in_ul_tag = True
                self.current_child_len = 1
                self.current_ul_list = []
        elif tag == 'li' and self.is_in_ul_tag:
            self.current_ul_list.append('li')

    def handle_endtag(self, tag):
        if tag == 'ul' and self.is_in_ul_tag:
            if len(self.current_ul_list) > len(self.highest_ul_list):
                self.highest_ul_list = self.current_ul_list
            if self.current_child_len > 1:
                self.current_child_len -= 1
            else:
                self.is_in_ul_tag = False
                self.current_ul_list = []
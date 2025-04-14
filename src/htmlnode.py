# some text
# <tag>some text</tag>
# <tag prop1="" prop2="">bla bla</tag>

from functools import reduce

class HTMLNode:
    def __init__(self, 
                 tag:str = None, 
                 value:str = None, 
                 children:list = None, 
                 props:dict = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError

    # converts dict of props to string, eg. class="some_class" href="#"
    def props_to_html(self):
        if self.props == None or len(self.props.keys()) < 1:
            return ""
        return reduce(lambda agg, prop: agg + f" {prop[0]}=\"{prop[1]}\"", 
                      self.props.items(), 
                      "")

    def __repr__(self):
        return f"<{self.tag}{self.props_to_html()}>{self.value}\n{self.children}"

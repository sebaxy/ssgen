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
        if self.props is None or len(self.props.keys()) < 1:
            return ""
        return reduce(lambda agg, prop: agg + f" {prop[0]}=\"{prop[1]}\"", 
                      self.props.items(), 
                      "")

    def __repr__(self):
        str_tag = self.tag if self.tag is not None else ""
        str_val = self.value if self.value is not None else ""
        str_children = str(self.children) if (self.children is not None and len(self.children) > 0) else ""

        if len(str_children) > 0:
            return f"<{str_tag}{self.props_to_html()}>{str_val}\n{str_children}"
        return f"<{str_tag}{self.props_to_html()}>{str_val}"

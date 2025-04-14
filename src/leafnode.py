from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, 
                 tag:str,
                 value:str,
                 props:dict = None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value is None:
            raise ValueError("leaf must have a value")
        if self.tag is None or len(self.tag.strip()) < 1:
            return self.value
        
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

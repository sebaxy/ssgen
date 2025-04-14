from htmlnode import HTMLNode


class ParentNode(HTMLNode):
    def __init__(self,
                 tag:str,
                 children:list,
                 props:dict = None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag is None or len(self.tag) < 1:
            raise ValueError("a parent node must have a tag")
        if self.children is None or len(self.children) < 1:
            raise ValueError("a parent node must have children")

        html = f"<{self.tag}{self.props_to_html()}>"
        for child in self.children:
            html += child.to_html() 

        return html + f"</{self.tag}>"

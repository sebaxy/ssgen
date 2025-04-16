from textnode import TextNode, TextType

import re


# takes list of old nodes, delim and text type and returns new list of nodes of the type matching the delimiter
def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        split_node = old_node.text.split(delimiter)
        if len(split_node) % 2 == 0:
            raise Exception("invalid markdown syntax")

        for i in range(len(split_node)):
            if split_node[i] == '':
                continue
            if i%2 == 0:
                new_nodes.append(TextNode(split_node[i], TextType.TEXT))
            else:
                new_nodes.append(TextNode(split_node[i], text_type))

    return new_nodes

# extract images
def extract_markdown_images(text):
    return re.findall(r"!\[(.+?)\]\((.+?)\)", text)


# extract links
def extract_markdown_links(text):
    return re.findall(r"[^!]\[(.+?)\]\((.+?)\)", text)


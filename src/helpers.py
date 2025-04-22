from textnode import TextNode, TextType

import re


# takes list of old nodes, delim and text type and returns new list of nodes of the type matching the delimiter
def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        split_nodes = old_node.text.split(delimiter)
        if len(split_nodes) % 2 == 0:
            raise Exception("invalid markdown syntax")

        for i in range(len(split_nodes)):
            if split_nodes[i] == '':
                continue
            if i%2 == 0:
                new_nodes.append(TextNode(split_nodes[i], TextType.TEXT))
            else:
                new_nodes.append(TextNode(split_nodes[i], text_type))

    return new_nodes

# extract images
def extract_markdown_images(text):
    return re.findall(r"!\[(.+?)\]\((.+?)\)", text)


# extract links
def extract_markdown_links(text):
    return re.findall(r"[^!]\[(.+?)\]\((.+?)\)", text)


node = TextNode("This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)", 
                TextType.TEXT)


def split_from_links(node, md_links, text_type):
    split_nodes = []
    start = 0

    for link in md_links:
        link_text = link[0]
        link_url = link[1]

        if text_type == TextType.LINK:
            pattern = f"[{link_text}]({link_url})"
        elif text_type == TextType.IMAGE:
            pattern = f"![{link_text}]({link_url})"

        idx = node.text.index(pattern, start)

        # check if found some regular text before md link
        if start != idx:
            split_nodes.append(TextNode(node.text[start:idx], TextType.TEXT))

        split_nodes.append(TextNode(link_text, text_type, link_url))
        start = idx + len(pattern)

    return split_nodes



def split_nodes_link(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        md_links = extract_markdown_links(old_node.text)
        split_nodes = split_from_links(old_node, md_links, TextType.LINK)
        new_nodes.extend(split_nodes)

    return new_nodes



def split_nodes_image(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        md_images = extract_markdown_images(old_node.text)
        split_nodes = split_from_links(old_node, md_images, TextType.IMAGE)
        new_nodes.extend(split_nodes)

    return new_nodes


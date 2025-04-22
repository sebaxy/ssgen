import re
from enum import Enum
from functools import reduce

def markdown_to_blocks(md):
    split_blocks = md.split('\n\n')
    stripped_blocks = list(map(lambda s: s.strip(), split_blocks))
    blocks = list(filter(lambda s: len(s) > 1, stripped_blocks))

    return blocks


class BlockType(Enum):
    P = "paragraph"
    H = "heading"
    CODE = "code"
    QUOTE = "quote"
    UL = "unordered_list"
    OL = "ordered_list"


def block_to_block_type(md_block):
    if re.search(r'^#{1,6}\s+.+', md_block) is not None:
        return BlockType.H

    if re.search(r'^`{3}.+`{3}$', md_block, re.S) is not None:
        return BlockType.CODE

    md_lines = md_block.split('\n')
    if reduce(lambda res, line: res and line.startswith('>'), md_lines, True):
        return BlockType.QUOTE

    if reduce(lambda res, line: res and line.startswith('- '), md_lines, True):
        return BlockType.UL

    is_ol = True
    for i, line in enumerate(md_lines):
        is_ol = is_ol and line.startswith(f"{i+1}. ")
        if not is_ol:
            return BlockType.P

    if is_ol:
        return BlockType.OL

    return BlockType.P

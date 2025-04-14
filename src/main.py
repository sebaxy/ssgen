from textnode import *
from htmlnode import *

def main():
    test_tn = TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev")
    print(test_tn)


if __name__ == "__main__":
    main()

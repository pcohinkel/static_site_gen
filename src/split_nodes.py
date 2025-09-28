from textnode import TextType, TextNode

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        if delimiter not in node.text:
            new_nodes.append(node)
            continue
        if node.text.count(delimiter) % 2 != 0:
            raise Exception(f"You do not have valid Markdown, {delimiter} appears an odd number of times.")
        split_text = node.text.split(delimiter)
        x = 0
        split_nodes = []
        for text in split_text:
            x += 1
            if text == "":
                continue
            if x % 2 == 0:
                split_nodes.append(TextNode(text=text,text_type=text_type))
            else:
                split_nodes.append(TextNode(text=text,text_type=TextType.TEXT))
        new_nodes.extend(split_nodes)
    return new_nodes

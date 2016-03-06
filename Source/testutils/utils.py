import os

from lxml import etree

AGENT_SOURCE_ROOT_PATH = os.path.expandvars('${Omnivore_Dev_Dir}/Agent/Source/Current')
TEST_DATA_PATH = os.path.join(AGENT_SOURCE_ROOT_PATH,'Test Stuff/Resources')

def print_it(item):
    
    if item is None:
        print('None')
    elif isinstance(item, etree._ElementTree):
        print_lxml_tree(item)
    elif isinstance(item, etree._Element):
        print_lxml_element(item)

def print_lxml_element(lxml_element, indent = 0):
    
    print('  ' * indent + '<' + lxml_element.tag + '>')
    indent += 1

def print_lxml_tree(lxml_tree):
    
    root_element = lxml_tree.getroot()
    print_lxml_element(root_element)
    
    
'''
Description: This file prints XML files in a readable manner
Last update: 23/09/2020

'''

from xml.etree.ElementTree import Element, SubElement, Comment
from xml.etree import ElementTree
from xml.dom import minidom

def prettify(elem):
    """Return a pretty-printed XML string for the Element.
    """
    rough_string = ElementTree.tostring(elem, 'utf-8')
    reparsed = minidom.parseString(rough_string)
    return reparsed.toprettyxml(indent="  ")


def print_xml_prettify(elem):
	print (prettify(elem))



def example_prettify_xml():
	top = Element('top')

	comment = Comment('Generated for PyMOTW')
	top.append(comment)

	child = SubElement(top, 'child')
	child.text = 'This child contains text.'

	child_with_tail = SubElement(top, 'child_with_tail')
	child_with_tail.text = 'This child has regular text.'
	child_with_tail.tail = 'And "tail" text.'

	child_with_entity_ref = SubElement(top, 'child_with_entity_ref')
	child_with_entity_ref.text = 'This & that'

	print(top)
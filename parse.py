import json
import xml.etree.ElementTree as ET

from xml.etree.ElementTree import QName


namespace = './/{http://www.battlescribe.net/schema/catalogueSchema}'
tree = ET.parse('sample/marines.cat')
root = tree.getroot()

print(root.tag)
print(json.dumps(root.attrib, indent=4))

for item in root:
    print(item.tag)
print()

for selection_entry in root.find(f'{namespace}sharedSelectionEntries'):
    print(selection_entry.tag)
    print(selection_entry.attrib['name'])
    for each in selection_entry:
        print(each.tag)
    if selection_entry.find(f'{namespace}modifiers'):
        for modifier in selection_entry.find(f'{namespace}modifiers'):
            print(modifier.attrib)
    if selection_entry.find(f'{namespace}constraints'):
        for constraints in selection_entry.find(f'{namespace}constraints'):
            print(constraints.attrib)
    if selection_entry.find(f'{namespace}profiles'):
        for profile in selection_entry.find(f'{namespace}profiles'):
            print(profile.attrib)
    if selection_entry.find(f'{namespace}costs'):
        for cost in selection_entry.find(f'{namespace}costs'):
            print(cost.attrib)
        # print(f"{selection.attrib['name']}")
    #     for characteristic in selection.find(f'{namespace}characteristics'):
    #         print(f"{characteristic.attrib['name']} - {characteristic.text}")


# for item in root.find('.//{http://www.battlescribe.net/schema/catalogueSchema}selectionEntries'):
#     for each in item:
#         print(each.tag)
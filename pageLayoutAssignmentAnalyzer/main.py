import sys
import xml.etree.ElementTree as ET
import glob
import os
import writer

LAYOUT_ASSIGNMENT_XML_NODE_NAME = "layoutAssignments"
LAYOUT_XML_NODE_NAME = "layout"
RECORD_TYPE_XML_NODE_NAME = "recordType"

profile_metadata_path = sys.argv[1]
layout_metadata_path = sys.argv[2]

# put all the layouts extracted from profiles
layouts = {}
for f in glob.glob(profile_metadata_path+"*.profile-meta.xml"):
    
    profile_name = os.path.basename(f).split('.',1)[0]
    tree = ET.parse(f)
    root = tree.getroot()
    for layout_assignment in root.iter("{http://soap.sforce.com/2006/04/metadata}"+LAYOUT_ASSIGNMENT_XML_NODE_NAME):
        layout_name = layout_assignment.find("{http://soap.sforce.com/2006/04/metadata}"+LAYOUT_XML_NODE_NAME).text
        record_type = layout_assignment.find("{http://soap.sforce.com/2006/04/metadata}"+RECORD_TYPE_XML_NODE_NAME)
        if record_type is None: 
            record_type_name = "master"
        else:
            record_type_name = record_type.text
        if layout_name in layouts:
            if profile_name in layouts[layout_name]["profiles"]:
                if record_type_name not in layouts[layout_name]["profiles"][profile_name]:
                    layouts[layout_name]["profiles"][profile_name].append(record_type_name)
            else:
                layouts[layout_name]["profiles"][profile_name]: [record_type_name]
        else:
            layouts[layout_name] = {
                "object_name": layout_name.split('-',1)[0],
                "profiles": {
                    profile_name: [record_type_name]
                }
            }

writer.write_layouts_to_excel(layouts,layout_metadata_path)
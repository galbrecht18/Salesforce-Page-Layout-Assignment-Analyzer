import sys
import xml.etree.ElementTree as ET
import glob
import os
import xlsxwriter

LAYOUT_ASSIGNMENT_XML_NODE_NAME = "layoutAssignments"
LAYOUT_XML_NODE_NAME = "layout"
RECORD_TYPE_XML_NODE_NAME = "recordType"

# relies on strict file paths to files at this time, can be refactored to accept
# file paths as arguments during script execution

# put all the layouts extracted from profiles
layouts = {}
for f in glob.glob("./main/default/profiles/*.profile-meta.xml"):
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
    
new_workbook = xlsxwriter.Workbook('page_layout_assignments.xlsx')
unused_page_layout_worksheet = new_workbook.add_worksheet("Unused Page Layouts")
unused_page_layout_worksheet.write(0,0,"layout_name")
unused_page_layout_worksheet.write(0,1,"package_xml_version")
used_page_layout_worksheet = new_workbook.add_worksheet("Used Page Layouts")
used_page_layout_worksheet.write(0,0,"layout_name")
used_page_layout_worksheet.write(0,1,"profiles")
used_page_layout_worksheet.write(0,2,"record types")
unused_sheet_row = 1
used_sheet_row = 1
#   # get all layout name based on the file names
for f in glob.glob("./main/default/layouts/*.layout-meta.xml"):
    layout_name = os.path.basename(f).split('.',1)[0]
    print(layout_name)
    if(layout_name not in layouts):
        package_xml_friendly_column = "<members>"+layout_name+"</members>"
        unused_page_layout_worksheet.write(unused_sheet_row,0,layout_name)
        unused_page_layout_worksheet.write(unused_sheet_row,1,package_xml_friendly_column)
        unused_sheet_row += 1
    else:
        for profile in layouts[layout_name]["profiles"]:
            for record_type in layouts[layout_name]["profiles"][profile]:   
                used_page_layout_worksheet.write(used_sheet_row,0,layout_name)
                used_page_layout_worksheet.write(used_sheet_row,1,profile)
                used_page_layout_worksheet.write(used_sheet_row,2,record_type)
                used_sheet_row += 1
new_workbook.close()

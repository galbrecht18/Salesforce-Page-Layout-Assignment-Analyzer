import xlsxwriter
import glob
import os
from datetime import datetime

def write_layouts_to_excel(layouts, layout_metadata_path):
  # create new workbook
  now = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
  new_workbook = xlsxwriter.Workbook("../results/page_layout_assignments"+now+".xlsx")

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
  for f in glob.glob(layout_metadata_path+"*.layout-meta.xml"):
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
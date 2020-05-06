# Page Layout Assignment Analyzer

Quick project to determine which page layouts aren't actively assigned to any profiles or record types in Salesforce and thus can be deleted.

Note this was done just as a pet project so no guarantees!

## Getting Started

1. You need python.
2. You need Salesforce DX.
3. Pull down your metadata: ```sfdx force:source:retrieve -u yourUsername@yourdomain.com -m Layout,RecordType,Profile```
4. Run the following script: ``` main.py [absolute_path_to_profile_metadata] [absolute_path_to_layout_metadata]```
5. This will output an .xlsx file in the same in the "results" directory with two tabs: one for unused page layouts and another for used page layouts.
6. The "Unused Page Layouts" will contain two columns: 
    a. layout_name: The page layout name
    b. package_xml_version: a package.xml version of the name so you can use in a package.xml
7. The "Used Page Layouts" will contain three columns:
    a. layout_name: The page layout name
    b. profiles: profile names using this page layout
    c. record_types: record types using this page layout

## Authors

* **George Albrecht** - *Initial stuff* - (https://github.com/galbrecht18)

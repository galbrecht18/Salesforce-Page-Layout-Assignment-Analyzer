# Page Layout Assignment Anaylzer

Quick project to determine which page layouts aren't actively assigned to any profiles or record types in Salesforce and thus can be deleted.

Note this was done just as a pet project so no guarentees!

## Getting Started

1. You need python.
2. You need Salesforce DX.

3. Pull down your metadata: ```sfdx force:source:retrieve -u yourUsername@yourdomain.com -m Layout,RecordType,Profile```
4. Run the following script: ``` main.py [path_to_layouts] [path_to_profiles]```

## Authors

* **George Albrecht** - *Initial stuff* - (https://github.com/galbrecht18)

import xml.etree.ElementTree as ET
tree = ET.parse('pubmed_result_50.xml')
root = tree.getroot()

for PMID in root.iter('PMID'):
    print(PMID.text)
for AbstractText in root.iter('AbstractText'):
    print(AbstractText.text)

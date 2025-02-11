import xml.etree.ElementTree as ET
import argparse

def update_urdf(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()
    
    # Update mesh filenames
    for mesh in root.findall('.//mesh'):
        filename = mesh.get('filename')
        if filename and not filename.startswith('package://'):
            mesh.set('filename', f'package://urdf_ah/{filename}')
    
    # Add base_link as the new root
    base_link = ET.Element('link', {'name': 'world'})
    root.insert(0, base_link)
    
    # Add joint connecting base_link to original base
    joint = ET.Element('joint', {'name': 'base_link_to_base', 'type': 'fixed'})
    parent = ET.SubElement(joint, 'parent', {'link': 'world'})
    child = ET.SubElement(joint, 'child', {'link': 'base'})
    origin = ET.SubElement(joint, 'origin', {'xyz': '0 0 0.1'})  # 1 meter above
    
    root.append(joint)
    
    tree.write(xml_file, encoding='utf-8', xml_declaration=True)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Modify URDF: Add base_link as new root and attach base 1m above.')
    parser.add_argument('xml_file', help='Path to the URDF file')
    args = parser.parse_args()
    
    update_urdf(args.xml_file)


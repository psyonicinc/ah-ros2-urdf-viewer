import xml.etree.ElementTree as ET
import argparse

def update_mesh_filenames_and_base_link(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()
    
    for mesh in root.findall('.//mesh'):
        filename = mesh.get('filename')
        if filename and not filename.startswith('package://'):
            mesh.set('filename', f'package://urdf_ah/{filename}')
    
    for link in root.findall('.//link'):
        if link.get('name') == 'base':
            link.set('name', 'base_link')
    
    for joint in root.findall('.//joint'):
        parent = joint.find('parent')
        if parent is not None and parent.get('link') == 'base':
            parent.set('link', 'base_link')
    
    tree.write(xml_file, encoding='utf-8', xml_declaration=True)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Update mesh filenames and base link names in a URDF file.')
    parser.add_argument('xml_file', help='Path to the URDF file')
    args = parser.parse_args()
    
    update_mesh_filenames_and_base_link(args.xml_file)

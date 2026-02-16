import xml.etree.ElementTree as ET

# --- PART 1: READ EXISTING XML ---
# Note: Ensure employee.xml exists at this path
tree = ET.parse("C://Users//KIIT01//PycharmProjects//seleniumPythonProject//dataformats//employee.xml")
root = tree.getroot()

# Print Root details
print(f"Root Tag: {root.tag}")

# Safety check: ensure children exist before accessing index
if len(root) > 0:
    print(root[0].tag)
if len(root) > 1:
    print(root[1].tag)

if len(root) > 0:
    print(f"First Child Tag: {root[0].tag}")
    print(f"First Child Attributes: {root[0].attrib}")

print("--- IDs ---")
for employee in root.findall("employee"):
    emp_id = employee.get("id")
    print(emp_id)

print("--- Details ---")
for employee in root.findall("employee"):
    name = employee.find("name").text
    role = employee.find("role").text
    exp = employee.find("experience").text
    print(name, role, exp)


# --- PART 2: CREATE NEW XML (Write) ---
# We are creating a new tree from scratch, so we define the root Element directly
root = ET.Element("employees")

# Fixed: 'Subelement' -> 'SubElement', removed leading space in "employee"
emp1 = ET.SubElement(root, "employee", id="101")

# Fixed: Syntax for adding text. You must access .text on the created element.
ET.SubElement(emp1, "name").text = "harsha"
ET.SubElement(emp1, "role").text = "tester"
ET.SubElement(emp1, "experience").text = "3"

ET.indent(tree, space="    ", level=0)

# Fixed: 'elementTree' -> 'ElementTree' (Capitalization matters)
tree = ET.ElementTree(root)
ET.indent(tree, space="    ", level=0)
tree.write("C://Users//KIIT01//PycharmProjects//seleniumPythonProject//dataformats//writexml.xml")


# --- PART 3: UPDATE XML ---
# Fixed: 'Et,parse' -> 'ET.parse'
tree = ET.parse("C://Users//KIIT01//PycharmProjects//seleniumPythonProject//dataformats//writexml.xml")
root = tree.getroot()

for emp in root.findall("employee"):
    if emp.get("id") == "101":
        emp.find("experience").text = "16"

ET.indent(tree, space="    ", level=0)

# Fixed: Arguments placed inside the parentheses
tree.write("C://Users//KIIT01//PycharmProjects//seleniumPythonProject//dataformats//updatexml.xml", encoding="utf-8", xml_declaration=True)

print("XML operations completed successfully.")
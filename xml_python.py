import xml.etree.ElementTree as ET

xml_data = """
<person>
    <id>1</id>
    <first_name>John</first_name>
    <last_name>Doe</last_name>
    <age>44</age>
    <address>
        <street>Main Street 1</street>
        <city>New York</city>
        <zip>10000</zip>
    </address>
</person>
"""

root = ET.fromstring(xml_data)
print(root.find('first_name').text)

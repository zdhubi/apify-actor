from lxml import etree

def build_xml(products):
    root = etree.Element("products")
    for p in products:
        item = etree.SubElement(root, "product")
        etree.SubElement(item, "title").text = p["title"]
        etree.SubElement(item, "price").text = p["price"]
    xml_str = etree.tostring(
        root,
        encoding="utf-8",
        xml_declaration=True,
        pretty_print=True
    )
    filename = "export.xml"
    with open(filename, "wb") as f:
        f.write(xml_str)
    return filename

import json
import xml.etree.ElementTree as ET

def json_to_xml(json_obj, line_padding=""):
    """遞迴地將 JSON 轉換為 XML 字符串"""
    if isinstance(json_obj, dict):
        xml_str = ""
        for key, value in json_obj.items():
            xml_str += f"{line_padding}<{key}>\n"
            xml_str += json_to_xml(value, line_padding + "  ")
            xml_str += f"{line_padding}</{key}>\n"
        return xml_str
    elif isinstance(json_obj, list):
        xml_str = ""
        for item in json_obj:
            xml_str += f"{line_padding}<item>\n"
            xml_str += json_to_xml(item, line_padding + "  ")
            xml_str += f"{line_padding}</item>\n"
        return xml_str
    else:
        return f"{line_padding}{json_obj}\n"

def convert_json_to_xml_file(json_file_path, xml_file_path):
    # 讀取 JSON 檔案
    with open(json_file_path, 'r', encoding='utf-8') as file:
        json_data = json.load(file)

    # 轉換為 XML 字符串
    xml_data = json_to_xml(json_data)

    # 建立 XML 根節點
    root = ET.Element("root")
    root.append(ET.fromstring(f"<data>{xml_data}</data>"))

    # 產生 XML 樹並寫入檔案
    tree = ET.ElementTree(root)
    tree.write(xml_file_path, encoding='utf-8', xml_declaration=True)

# 示例使用
json_file_path = input("請輸入 JSON 檔案的路徑: ")
xml_file_path = input("請輸入要保存的 XML 檔案路徑: ")

convert_json_to_xml_file(json_file_path, xml_file_path)

# 導入 json 模組，該模組提供用於 JSON 處理
import json

# 指定 JSON 檔案的路徑
json_file_path = r"C:\vsc\project_1012\test2.json"

# 指定輸出的 XML 檔案的路徑
xml_file_path = r"C:\vsc\project_1012\test.xml"

# 以讀取模式 "r" 讀取 JSON 檔案，並使用 utf-8 編碼開啟 JSON 檔案
with open(json_file_path, mode="r", encoding="utf-8") as json_file:
    # 讀取 JSON 檔案內容並將其轉換為字典
    json_data = json.load(json_file)

# 初始化 XML 資料的列表
xml_data = ["<課程列表>"]  # 開始標籤

# 讀取 JSON 資料中的每一個課程
for course_info in json_data:
    # 添加課程標籤
    course_str = "<課程>"
    # 讀取課程中的每一個 key 及 value
    for key, value in course_info.items():
        # 添加對應的 XML 標籤和內容，格式為 <key>value</key>
        course_str += f"<{key}>{value}</{key}>"
    
    # 添加課程的結束標籤
    course_str += "</課程>"
    
    # 將 course_str 添加到 xml_data 列表中
    xml_data.append(course_str)

# 添加 XML 結束標籤
xml_data.append("</課程列表>")

# 以寫入模式 "w" 將 XML 字串寫入 XML 檔案，並使用 utf-8 編碼開啟 XML 檔案
with open(xml_file_path, mode="w", encoding="utf-8") as xml_file:
    # 將 xml_data 列表中的內容連接成一個字串，並寫入 XML 檔案
    xml_file.write("\n".join(xml_data))

# 輸出 XML 檔案的路徑
print(f"JSON 文件已成功轉換為 XML 文件，並保存在 {xml_file_path}")

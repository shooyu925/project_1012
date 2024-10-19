# 匯入 json 模組，該模組提供用於 JSON 處理
import json

# 指定 CSV 檔案的路徑
csv_file_path = r"C:\vsc\project_1012\test.csv"
# 指定輸出的 JSON 檔案的路徑
json_file_path = r"C:\vsc\project_1012\test2.json"

# 以讀取模式 "r" 讀取 CSV 檔案，並使用 utf-8 編碼開啟 CSV 檔案
with open(csv_file_path, mode="r", encoding="utf-8") as file:
    # 讀取檔案中的所有行並將它們儲存在 lines 列表中
    lines = file.readlines()

# 讀取 CSV 檔案的第一行，去除首尾空白並根據逗號分隔成列表，這是標題列
header = (lines[0].strip().split(","))
# 初始化一個空列表 data，用於儲存解析後的資料
data = [] 

# 從第二行開始遍歷每一行資料
for line in lines[1:]:
    # 去除每行首尾空白，並根據逗號分隔成列表
    values = line.strip().split(",")
    # 初始化一個空字典
    row = {}
    # 讀取標題的索引
    for i in range(len(header)):
		    # 將對應標題和值存入字典
        row[header[i]] = values[i]
    # 將每行的字典添加到 data 列表中
    data.append(row)

# 以寫入模式 "w" 將資料寫入 JSON 檔案，並使用 utf-8 編碼開啟 JSON 檔案
with open(json_file_path, mode="w", encoding="utf-8") as json_file:
    # 將 data 列表寫入 JSON 檔案，設定 ensure_ascii=False 和縮排為 4
    json.dump(data, json_file, ensure_ascii=False, indent=4)

# 輸出提示信息，表示 CSV 資料已成功轉換並儲存
print(f"CSV 文件已成功轉換為 JSON 文件，並保存在 {json_file_path}")
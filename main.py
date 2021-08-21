# Python语法真怪
import os
import time

suffixes_libraries = {
    "C#": ["cs"],
    "Python": ["py", "pyw"],
    "C": ["h", "c"],
    "C++": ["h", "hpp", "hxx", "cpp", "cxx", "cc", "c", "c++"],
    "Visual Basic": ["vb"],
}

is_debug = False


def code_counter(path, suffixes):
    code_line_number = 0
    code_file_number = 0
    for root, dirs, files in os.walk(path):
        for file in files:
            for suffix in suffixes:
                if file.endswith(suffix):
                    if is_debug: print(os.path.join(root, file))
                    code_file_number += 1
                    code_file = open(os.path.join(root, file), "r", encoding='utf-8')
                    for line in code_file.readlines():
                        code_line_number += 1
    return [code_file_number, code_line_number]


while True:
    print("=========================")
    print()
    language_type = input("请输入你的语言类型")
    if language_type == "exit":
        break
    elif language_type == "debug":
        print("Debug mode " + str(not is_debug) + ".")
        is_debug = not is_debug
        continue
    code_path = input("请输入你的代码路径")
    print()
    print("计算中......")
    print()
    start_time = time.time()

    if language_type.lower() in suffixes_libraries:
        result = code_counter(code_path, suffixes_libraries[language_type])
        print("该项目共" + str(result[0]) + "个文件," + str(result[1]) + "行代码")
    else:
        print("未知语言:" + language_type)
        continue

    end_time = time.time()
    total_time = end_time - start_time
    print("(计算共耗时" + format(total_time, "6f") + "秒)")
    print()

print("=========================")
print()
print("感谢使用!!!")
print("作者:XianYuHil")
input()

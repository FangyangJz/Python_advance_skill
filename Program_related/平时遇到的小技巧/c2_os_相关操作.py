import os


def file_names_list_split_suffix(file_name_list, suffix):
    # 剔除掉指定尾缀类型文件的尾缀
    return [i.split('.')[0] for i in file_name_list if i.split('.')[1] == suffix]

def get_file_abs_path(file_name=''):
    ''' 文件和脚本在同目录下, 返回文件的原始字符串'''
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), file_name)

# files_list_target = os.listdir(save_file_path)
# for i in need_convert_files_list:
#     if os.path.splitext(i)[1] == '.xlsx':  # 只处理 .xlsx 后缀的文件
#         pass
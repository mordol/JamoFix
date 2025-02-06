import os
import unicode

def fix_jamo(text):
    return unicode.join_jamos(text)

def split_jamo(text):
    return unicode.split_syllables(text)

def batch_rename(root_dir):
    # 모든 경로를 수집
    all_dirs = []
    all_files = []
    for dirpath, dirnames, filenames in os.walk(root_dir, topdown=False):
        # 디렉토리 경로 수집
        for d in dirnames:
            all_dirs.append(os.path.join(dirpath, d))
        # 파일 경로 수집
        for f in filenames:
            all_files.append(os.path.join(dirpath, f))
    
    # 파일 이름 먼저 변경
    for file_path in all_files:
        dirpath, filename = os.path.split(file_path)
        new_name = fix_jamo(filename)
        if new_name != filename:
            os.rename(file_path, os.path.join(dirpath, new_name))
            
    # 디렉토리 이름을 나중에 변경 (깊은 경로부터 처리)
    for dir_path in sorted(all_dirs, reverse=True):
        dirpath, dirname = os.path.split(dir_path)
        new_name = fix_jamo(dirname)
        if new_name != dirname:
            os.rename(dir_path, os.path.join(dirpath, new_name))

batch_rename(".")
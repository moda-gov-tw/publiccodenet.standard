import os
import shutil
import subprocess

PROJECT_FOLDER = "./"
SOURCE_FOLDER = "./origin_source"

def main():
    root_path = "./"
    source_path = "./origin_source"

    # 1. get all md file
    md_files = find_md_files(PROJECT_FOLDER)

    # 2. filter origin file
    md_files = [file for file in md_files if not file.startswith(SOURCE_FOLDER)]

    # 3A. backup md file (只有主程式更新的時候，才需要複製一次)
    # backup_md_files(md_files)

    # 3B. restore md file
    restore_md_files(md_files)

    # 4. run po2md
    for file in md_files:
        full_target_path = os.path.join(SOURCE_FOLDER, os.path.relpath(file, PROJECT_FOLDER))
        do_po2md(source_file=full_target_path, target_file=file)

    # 4. update md file
    update_md_file(SOURCE_FOLDER)




def find_md_files(folder_path) -> list:
    md_files = []
    for root, dirs, files in os.walk(folder_path):
        md_files += [os.path.join(root, file) for file in files if file.endswith('.md')]
    return md_files

# 複製原始檔案
def backup_md_files(files):
    if not os.path.exists(SOURCE_FOLDER):
        os.makedirs(SOURCE_FOLDER)

    for file in files:
        # 建立目標資料夾的完整路徑
        full_target_path = os.path.join(SOURCE_FOLDER, os.path.relpath(file, PROJECT_FOLDER))
        if not os.path.exists(os.path.dirname(full_target_path)):
            os.makedirs(os.path.dirname(full_target_path))

        # 複製檔案到目標資料夾
        shutil.copy2(file, full_target_path)

# 還原原始檔案
def restore_md_files(files):
    for file in files:
        full_target_path = os.path.join(SOURCE_FOLDER, os.path.relpath(file, PROJECT_FOLDER))
        shutil.copy2(full_target_path, file)


def do_po2md(source_file, target_file):
    locale_file = "locales/zh_Hant/LC_MESSAGES/messages.po"
    cmd = f"po2md -p {locale_file} -s {target_file} {source_file}"
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    if result.returncode != 0:
        print("錯誤訊息：")
        print(result.stderr)
        exit()

def update_md_file(source_path):
    source_marker = "---"
    target_marker = "***"

    source_files = find_md_files(source_path)
    for file in source_files:
        with open(file, 'r') as infile:
            file_content = infile.read()

        start_index = file_content.find(source_marker)
        end_index = file_content.find(source_marker, start_index + len(source_marker))
        copied_content = file_content[start_index:end_index + len(source_marker)]


        with open(file[len(source_path) + 1:], 'r') as infile:
            file_content = infile.read()

        start_index = file_content.find(target_marker)
        end_index = file_content.find(target_marker, start_index + len(target_marker))
        if end_index == -1:
            print(file)
            continue

        new_content = copied_content + file_content[end_index + len(target_marker):]

        with open(file[len(source_path) + 1:], 'w') as outfile:
            outfile.write(new_content)



if __name__ == '__main__':
    main()
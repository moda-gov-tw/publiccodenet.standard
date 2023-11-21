import os
import shutil
import subprocess
import polib


def main():
    locals_en = 'locales/en/LC_MESSAGES/messages.po'
    locals_zh = 'locales/zh_Hant/LC_MESSAGES/messages.po'
    en_po = polib.pofile(locals_en)
    zh_po = polib.pofile(locals_zh)

    zh_msgids = set(entry.msgid for entry in zh_po)

    # 遍歷 en.po 中的每一個 entry
    for entry in en_po:
        # 如果 en.po 中的 msgid 不在 zh.po 中
        if entry.msgid not in zh_msgids:
            # 創建一個新的 POEntry 對象
            new_entry = polib.POEntry(
                msgid=entry.msgid,
                msgstr='',  # 初始為空字符串
            )
            # 將新的 entry 添加到 zh.po 中
            zh_po.append(new_entry)

    # 儲存更新後的 zh.po 檔案
    zh_po.save(locals_zh)




if __name__ == '__main__':
    main()
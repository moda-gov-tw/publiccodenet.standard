mkdir ./criteria
for file in ./criteria_source/*; do
    po2md -p ./locales/zh_Hant/LC_MESSAGES/messages.po -s ./criteria/`basename "$file"` $file
done

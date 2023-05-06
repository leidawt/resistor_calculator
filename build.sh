# 打包
pyinstaller -w -F main.py --add-data=".\\*.png;.\\" -i icon.ico --clean
# 打包成的exe文件
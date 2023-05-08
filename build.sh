# 打包
pyinstaller -w -F main.py --add-data=".\\*.png;.\\" -i icon.ico --clean -n "电阻凑算工具"
# 打包成的exe文件
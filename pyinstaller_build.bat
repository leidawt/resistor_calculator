pyinstaller -w -F main.py --add-data=".\\*.png;.\\" --add-data=".\\*.ico;.\\" -i icon.ico --clean -n "电阻凑算工具"

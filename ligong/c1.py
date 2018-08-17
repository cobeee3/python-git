#TempConvert.py
TempStr = input('请输入带有符号的温度值：')
if TempStr[-1] in ['f','F'] :
    C = 5/9*(int(TempStr[:-1]) -32)
    print('转换后的温度是',int(C),'C')

elif TempStr[-1] in ['c','C'] :
    F = 1.8*(int(TempStr[:-1]) + 32)
    print('转换后的温度是',int(F),'F')
else:
    print('请输入正确的带有符号的温度值')
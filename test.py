import os,pandasparser,time

cmd=os.system("pip.exe install pandas")

data="device-status-20180410.csv"

pandasparser.gettoleranceids(data)

print("#"*100)

print("result.csv generated")
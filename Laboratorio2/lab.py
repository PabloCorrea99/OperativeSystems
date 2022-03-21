import os
discos = r"\discos.txt"
board = r"\board.txt"
mac = r"\AMAC.txt"
ipInfo = r"\AipInfo.txt"
biosInfo = r"\biosInfo.txt"
cpuInfo = r"\ACPUInfo.txt"
directorio = r"C:\Users\Usuario\Desktop\Universidad\9SEMESTRE\OPERATIVOS\OperativeSystems\Laboratorio2"
os.system("wmic diskdrive get systemName,model,index,firmwareRevision,status,interfaceType,totalHeads,totalTracks,totalCylinders,totalSectors,partitions > "+directorio+discos)
os.system("wmic baseboard get /All > "+directorio+board)
os.system("getmac > "+directorio+mac)
os.system("ipconfig > "+directorio+ipInfo)
os.system("wmic bios get /All > "+directorio+biosInfo)
os.system("wmic cpu get /All > "+directorio+cpuInfo)
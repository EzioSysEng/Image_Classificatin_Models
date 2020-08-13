def removePic(picPath,noPath):
    ret = []
    findFile(picPath,".jpg",ret)
    f = open(noPath,'r')
    picNames = f.readlines()
    for imgPath in ret:
        for name in picNames:
            name = name[:-1]
            if imgPath.find(name)>0:
                print(imgPath)
                os.remove(imgPath)
                
removePic(r'C:\Users\ZIV2SZH\WORK_FILE\00_Other\05_Lun\2020_AI\pic',r'C:\Users\ZIV2SZH\WORK_FILE\00_Other\05_Lun\2020_AI\selectedCat.txt')
  
import PIL.Image as Image
from torchvision import transforms as transforms
import os




def imgResize(folderPath,height,width):
    ret = []
    findFile(folderPath,".jpg",ret)
    resultPath=folderPath.strip().rstrip("\\") + '_resize_' + str(height) + '_' + str(width)
    
    isExists=os.path.exists(resultPath) 
    if not isExists:
        os.makedirs(resultPath) 
        
    for imgPath in ret :
        imgName = os.path.splitext(os.path.split(imgPath)[1])[0] +'_resize.jpg'
        
        img = Image.open(imgPath)
        new_im = transforms.Resize((height, width))(img)
        new_im.save(os.path.join(resultPath,imgName))
        
        
def imgHorizontalFlip(folderPath):
    ret = []
    findFile(folderPath,".jpg",ret)
    resultPath=folderPath.strip().rstrip("\\") + '_HFlip'
    
    isExists=os.path.exists(resultPath) 
    if not isExists:
        os.makedirs(resultPath) 
        
    for imgPath in ret :
        imgName = os.path.splitext(os.path.split(imgPath)[1])[0] +'_HFlip.jpg'
        img = Image.open(imgPath)
        new_im = transforms.RandomHorizontalFlip(p=1)(img)
        new_im.save(os.path.join(resultPath,imgName))
        
def imgVerticalFlip(folderPath):
    ret = []
    findFile(folderPath,".jpg",ret)
    resultPath=folderPath.strip().rstrip("\\") + '_VFlip'
    
    isExists=os.path.exists(resultPath) 
    if not isExists:
        os.makedirs(resultPath) 
        
    for imgPath in ret :
        imgName = os.path.splitext(os.path.split(imgPath)[1])[0] +'_VFlip.jpg'
        img = Image.open(imgPath)
        new_im = transforms.RandomVerticalFlip(p=1)(img)
        new_im.save(os.path.join(resultPath,imgName))
        
def imgRotation(folderPath,angle):
    ret = []
    findFile(folderPath,".jpg",ret)
    resultPath=folderPath.strip().rstrip("\\") + '_rorate_' + str(angle)
    
    isExists=os.path.exists(resultPath) 
    if not isExists:
        os.makedirs(resultPath) 
        
    for imgPath in ret :
        imgName = os.path.splitext(os.path.split(imgPath)[1])[0] +'_rorate.jpg'
        img = Image.open(imgPath)
        new_im = transforms.RandomRotation(angle)(img)
        new_im.save(os.path.join(resultPath,imgName))
    
def imgPadding(folderPath,paddingSize):
    ret = []
    findFile(folderPath,".jpg",ret)
    resultPath=folderPath.strip().rstrip("\\") + '_pad_' + str(paddingSize)
    
    isExists=os.path.exists(resultPath) 
    if not isExists:
        os.makedirs(resultPath) 
        
    for imgPath in ret :
        imgName = os.path.splitext(os.path.split(imgPath)[1])[0] +'_rorate.jpg'
        img = Image.open(imgPath)
        new_im = transforms.Pad(paddingSize)(img)
        new_im.save(os.path.join(resultPath,imgName))
        
        
def findFile(path,fileType, ret):#".txt"
    """Finding the *.txt file in specify path"""
    filelist = os.listdir(path)
    for filename in filelist:
        de_path = os.path.join(path, filename)
        if os.path.isfile(de_path):
            if de_path.endswith(fileType): #Specify to find the txt file.
                ret.append(de_path)
#
#    
#def getPicNo(folderPath):
#    ret = []
#    findFile(folderPath,'.jpg', ret)
#    f = open('selectedCat.txt','w+')
#    for imgPath in ret :
#        imgName = os.path.splitext(os.path.split(imgPath)[1])[0]+'.jpg\n'
#        print(imgName)
#        f.write(imgName)
#    f.close()
#    
#    
#def removePic(picPath,noPath):
#    ret = []
#    findFile(picPath,".jpg",ret)
#    f = open(noPath,'r')
#    picNames = f.readlines()
#    for imgPath in ret:
#        for name in picNames:
#            name = name[:-1]
#            if imgPath.find(name)>0:
#                print(imgPath)
#                os.remove(imgPath)
                
#removePic(r'C:\Users\ZIV2SZH\WORK_FILE\00_Other\05_Lun\2020_AI\pic',r'C:\Users\ZIV2SZH\WORK_FILE\00_Other\05_Lun\2020_AI\selectedCat.txt')
#    
#getPicNo(r'G:\04_6_EMM\03_Exchange\YI Zixuan\cat_dog_dataset\training_set\training_set\selected_cat')

#imgResize('pic',32,32)
#imgVerticalFlip('pic')
#imgRotation('pic',30)
#imgPadding('pic',30)
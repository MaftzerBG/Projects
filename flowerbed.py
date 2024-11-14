flowerbed = [1,0,0,0,1]
n = 1
for bed in range(len(flowerbed)):
    if flowerbed[bed] == 0 and (bed == 0 or flowerbed[bed-1] == 0) and (bed == len(flowerbed)-1 or flowerbed[bed+1]==0):
        flowerbed[bed] = 1
        n-=1
        if n == 0:
            print(True)
print(False)
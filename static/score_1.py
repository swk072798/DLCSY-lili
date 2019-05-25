import os
import math
import csv
# import tqdm
import argparse
import decimal

"""
超新星跑分程序:用于对比submit.csv与list.csv的结果,计算得分
由于训练和测试都在使用这个集合,需要注意实际测试如果与训练集分布不一致,那么分数可能稍低
用于计算部分的得分
"""

# D:\DLCSY-version\DLCSY-V0.0.4\static\participants\7\submit.csv

def caculate_score(submitfile,listfile):

    print("comparing %s and %s." % (submitfile, listfile))

    # print("111"+str(os.path.exists(submitfile)))
    # print("222" + str(os.path.exists(listfile)))

    if not os.path.exists(submitfile) or not os.path.exists(listfile):
        print("%s and %s don't exist" % (submitfile, listfile))
        return "file not exist"

    fsubmit = open(submitfile, 'r')
    flist = open(listfile, 'r')

    reader_submit = list(csv.reader(fsubmit))[1:]
    reader_list = list(csv.reader(flist))[:]

    if len(reader_submit) != len(reader_list):
        print("size don't match! submit:list", len(reader_submit), "!=", len(reader_list))
    else:
        print("submit and list size match!")

    def dist(x, y, x1, y1):
        if math.sqrt((int(float(x)) - int(float(x1))) * (int(float(x)) - int(float(x1))) + (
                int(float(y)) - int(float(y1))) * (int(float(y)) - int(float(y1)))) < 15:
            return True
        else:
            return False

    total = len(reader_list)
    right = 0

    def getID(name):
        for i in range(len(reader_submit)):
            if reader_submit[i][0] == name:
                return i
        return 0

    for name, x , y ,_ in reader_list[1:]:
        target = reader_submit[getID(name)]
        if len(target) < 8:
            print(name,"is not enough")
            continue
        else:
            x1,y1 = float(target[1]),float(target[2])
            x2,y2 = float(target[3]),float(target[4])
            x3,y3 = float(target[5]),float(target[6])
            x ,y  = int(float(x)), int(float(y))
        if target[7] == "1":
            if dist(x,y,x1,y1) or dist(x,y,x2,y2) or dist(x,y,x3,y3):
                right = right + 1
                if right % 2 == 0:
                    print("\r real time score:%.3f"%(float(right)/float(total+1)),end="")
    score = round(float(right)/float(int(float(total))+1),3)
    print("\nright:%d total:%d score:%.3f"%(right,total,float(right)/float(int(float(total))+1)))
    return score

if __name__ == '__main__':
    print(caculate_score())

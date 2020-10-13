##############################
# 初始化顺序表函数
##############################
def __init__(self):
    self.SeqList = []
##############################
# 创建顺序表函数
##############################


def CreatSequnceList(self):
    print("**************************************")
    print("*请输入数据后按回车键确认，若想结束请按“#”。*")
    print("***************************************")
    Element = input("请输入元素：")
    while Element != '#':
        self.SeqList.append(int(Element))
        Element = input("请输入元素：")

##############################
# 查找元素值函数
##############################


def FindElement(self):
    key = int(input("请输入想查找的值："))
    if key in self.SeqList:
        ipos = self.SeqList.index(key)
        print("查找成功！值为", self.SeqList[pos], "的元素，位于当前顺序表的第", ipos+1, "个位置")
    else:
        print("查找失败！当前顺序表中不存在值为", key, "的元素")

##############################
# 指定位置插入元素
##############################


def InsertElement(self):
    ipos = int(input("请输入待插入的位置："))
    Element = int(input("请输入待插入的元素的值："))
    self.SeqList.insert(ipos, Element)
    print("插入元素后，当前顺序表为:\n", self.SeqList)

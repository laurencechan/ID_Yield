# coding=utf-8

import re, urllib2, random, time


class ID_Yield():
    def __init__(self, num):
        self.num = num

    @classmethod
    def get_forhead_six(self):
        response = urllib2.Request("http://www.stats.gov.cn/tjsj/tjbz/xzqhdm/201401/t20140116_501070.html")
        html = urllib2.urlopen(response).read().decode("utf-8")  # 获取行政区划网页的内容
        # reg = r'class="MsoNormal" align="justify">(\d*).*?(&nbsp;| ){3,8}(.*?)</p>'
        reg = r'class="MsoNormal" align="justify">(\d*).*?(.*?)</p>'
        regpat = re.compile(reg)
        area_list = re.findall(regpat, html)  # 通过正则匹配获取全部行政区划内容
        area_dic_list = []
        # 根据网站里行政区划级别的不同进行分类，这里依据&nbsp个数区分
        for i in area_list:
            if i[1].count("&nbsp") == 3:  # 三个&nbsp是省级（直辖市，自治区）
                dict_1 = {}
                dict_1["level"] = 1
                dict_1["id"] = i[0]
                dict_1["place"] = i[1][19:]
                area_dic_list.append(dict_1)
            elif i[1].count("nbsp") == 5:  # 五个是地市级
                dict_2 = {}
                dict_2["level"] = 2
                dict_2["id"] = i[0]
                dict_2["place"] = i[1][31:]
                area_dic_list.append(dict_2)
            elif i[1].count("nbsp") == 7:  # 七个是市辖区，县级
                dict_3 = {}
                dict_3["level"] = 3
                dict_3["id"] = i[0]
                dict_3["place"] = i[1][43:]
                area_dic_list.append(dict_3)
        lev1_list = []
        lev2_list = []
        lev3_list = []
        for i in area_dic_list:
            if i["level"] == 1:
                dict_4 = {}
                dict_4[i["id"][:2]] = (i["place"])  # dict_4是一个元素为字典的列表 字典格式为 [{42:"湖北省"},{10:"北京市"}]
                lev1_list.append(dict_4)
                # tt = random.choice(lev1_list)
                # print tt.keys()[0], tt.values()[0]
            elif i["level"] == 2:
                dict_5 = {}
                for j in lev1_list:
                    if j.keys()[0] == i["id"][:2]:
                        dict_5[i["id"][:4]] = j.values()[0] + i["place"]
                        lev2_list.append(dict_5)
                        # dict_5也是一个元素为字典的列表 字典格式为 [{4201:"湖北省武汉市"},{3304:"浙江省嘉兴市"}]
                        # yy = random.choice(lev2_list)
                        # print yy.keys()[0], yy.values()[0]
            elif i["level"] == 3:
                dict_6 = {}
                for j in lev2_list:
                    if j.keys()[0] == i["id"][:4]:
                        dict_6[i["id"][0:6]] = j.values()[0] + i["place"]
                        lev3_list.append(dict_6)
                        # dict_6也是一个元素为字典的列表 字典格式为 [{231222:"黑龙江省绥化市兰西县"},{330424:"浙江省嘉兴市海盐县"}]
        xx = random.choice(lev3_list)
        # print int(xx.values()[0])
        return xx

    @classmethod
    def birthday(self):
        year = random.randint(1900, time.localtime().tm_year)  # 年份，1900~今年
        month = random.randint(1, 12)
        if month == 2 and year % 4 == 0:  # 闰年二月29天
            maxday = 29
        elif month == 2 and year % 4 != 0:
            maxday = 28
        elif month in [1, 3, 5, 7, 8, 10, 12]:  # 大月31天
            maxday = 31
        else:
            maxday = 30
        if month < 10:  # 月份为个位数 就前边补0
            month = "0" + str(month)
        date = random.randint(1, maxday)
        if date < 10:  # 日期为个位数 就前边补0
            date = "0" + str(date)
        # print str(year) + str(month) + str(date)
        return str(year) + str(month) + str(date)  # 返回出生年月日

    @classmethod
    def last_three(self):
        # 随机生成生份证末尾四位
        num_four = ''
        for i in range(3):
            num = random.randint(0, 9)
            num_four += str(num)
        # print num_four
        return num_four

    @classmethod
    def combination(self, num):
        # 将前六位，出生年月日，后四位拼起来，就是一个标准的身份证号，并输出前六位对应的完整行政区
        for i in range(num):
            forhead_six = ID_Yield.get_forhead_six()
            forhead_six_num = forhead_six.keys()[0]
            forhead_six_str = str(forhead_six.keys()[0])
            sum = (7 * int(forhead_six_str[0])) + (9 * int(forhead_six_str[1])) + (10 * int(forhead_six_str[2])) + (5 * int(forhead_six_str[3])) + (8 * int(forhead_six_str[4])) + (4 * int(forhead_six_str[5]))
            birthday = ID_Yield.birthday()
            sum = sum + 2*int(birthday[0])+1*int(birthday[1])+6*int(birthday[2])+3*int(birthday[3])+7*int(birthday[4])+9*int(birthday[5])+10*int(birthday[6])+5*int(birthday[7])
            last_three = ID_Yield.last_three()
            sum = sum + 8*int(last_three[0])+4*int(last_three[1])+2*int(last_three[2])
            yushu = sum % 11   # 身份证最后一位 验证码  http://baike.baidu.com/view/188003.htm?qq-pf-to=pcqq.c2c#1_7
            if yushu == 0:                      #7－9－10－5－8－4－2－1－6－3－7－9－10－5－8－4－2
                last_one = "1"                  #0－1－2－3－4－5－6－7－8－9－10
            elif yushu == 1:                    #1－0－X －9－8－7－6－5－4－3－2
                last_one = "0"
            elif yushu == 2:
                last_one = "X"
            else:
                last_one = str(12 - yushu)
            id_num = forhead_six_num + birthday + last_three + last_one
            print "第%s个" % (i + 1), id_num, forhead_six.values()[0]


if __name__ == '__main__':
    # ID_Yield.get_forhead_six()
    # ID_Yield.birthday()
    # ID_Yield.last_four()
    ID_Yield.combination(10)
    # ID_Yield.last_one()
    pass

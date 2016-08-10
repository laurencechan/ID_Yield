# coding=utf-8

import re, urllib2, random, time


class ID_Yield():
    def __init__(self, num):
        self.num = num

    @classmethod
    def get_forhead_six(self):
        response = urllib2.Request("http://www.stats.gov.cn/tjsj/tjbz/xzqhdm/201401/t20140116_501070.html")
        html = urllib2.urlopen(response).read().decode("utf-8")
        # reg = r'class="MsoNormal" align="justify">(\d*).*?(&nbsp;| ){3,8}(.*?)</p>'
        reg = r'class="MsoNormal" align="justify">(\d*).*?(.*?)</p>'
        regpat = re.compile(reg)
        area_list = re.findall(regpat, html)
        area_dic_list = []
        for i in area_list:
            if i[1].count("&nbsp") == 3:
                dict_1 = {}
                dict_1["level"] = 1
                dict_1["id"] = i[0]
                dict_1["place"] = i[1][19:]
                area_dic_list.append(dict_1)
            elif i[1].count("nbsp") == 5:
                dict_2 = {}
                dict_2["level"] = 2
                dict_2["id"] = i[0]
                dict_2["place"] = i[1][31:]
                area_dic_list.append(dict_2)
            elif i[1].count("nbsp") == 7:
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
                dict_4[i["id"][:2]] = (i["place"])
                lev1_list.append(dict_4)
                # tt = random.choice(lev1_list)
                # print tt.keys()[0], tt.values()[0]
            elif i["level"] == 2:
                dict_5 = {}
                for j in lev1_list:
                    if j.keys()[0] == i["id"][:2]:
                        dict_5[i["id"][:4]] = j.values()[0] + i["place"]
                        lev2_list.append(dict_5)
                        # yy = random.choice(lev2_list)
                        # print yy.keys()[0], yy.values()[0]
            elif i["level"] == 3:
                dict_6 = {}
                for j in lev2_list:
                    if j.keys()[0] == i["id"][:4]:
                        dict_6[i["id"][0:6]] = j.values()[0] + i["place"]
                        lev3_list.append(dict_6)
        xx = random.choice(lev3_list)
        # print xx.keys()[0],xx.values()[0]
        return xx

    @classmethod
    def birthday(self):
        year = random.randint(1900, time.localtime().tm_year)
        month = random.randint(1, 12)
        if month == 2 and year % 4 == 0:
            maxday = 29
        elif month == 2 and year % 4 != 0:
            maxday = 28
        elif month in [1, 3, 5, 7, 8, 10, 12]:
            maxday = 31
        else:
            maxday = 30
        if month < 10:
            month = "0" + str(month)
        date = random.randint(1, maxday)
        if date < 10:
            date = "0" + str(date)
        # print str(year) + str(month) + str(date)
        return str(year) + str(month) + str(date)

    @classmethod
    def last_four(self):
        num_four = ''
        for i in range(4):
            num = random.randint(0, 9)
            num_four += str(num)
        # print num_four
        return num_four

    @classmethod
    def combination(self, num):
        for i in range(num):
            forhead_six = ID_Yield.get_forhead_six()
            forhead_six_num = forhead_six.keys()[0]
            birthday = ID_Yield.birthday()
            last_four = ID_Yield.last_four()
            id_num = forhead_six_num + birthday + last_four
            print "第%s个" % (i+1), id_num, forhead_six.values()[0]



            # return area_dic_list
            # for i in area_dic_list:
            #     print i["place"],i["id"],i["level"]


if __name__ == '__main__':
    # ID_Yield.get_forhead_six()
    # ID_Yield.birthday()
    # ID_Yield.last_four()
    ID_Yield.combination(200)
    pass

# coding=utf-8

import re, requests, urllib2, random


class ID_Yield():
    def __init__(self, num):
        self.num = num

    @staticmethod
    def get_forhead_six():
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
                tt = random.choice(lev1_list)
                print tt.keys()[0], tt.values()[0]
            elif i["level"] == 2:
                dict_5 = {}
                dict_5[i["id"][2:4]] = i["place"]
                lev2_list.append(dict_5)
            elif i["level"] == 3:
                dict_6 = {}
                dict_6[i["id"][4:6]] = i["place"]
                lev2_list.append(dict_6)


        # return area_dic_list
        # for i in area_dic_list:
        #     print i["place"],i["id"],i["level"]


if __name__ == '__main__':
    ID_Yield.get_forhead_six()
    pass

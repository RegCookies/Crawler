#coding=utf-8
import http.cookiejar as cookielib
import urllib
import sys
import requests
import re
from bs4 import BeautifulSoup
import os
#input the keyword
word = input("Please input a key: (please enter chinese): " )
url = "http://search.zgg.com/tools/search-list-zl.html?keywords="
inputword = urllib.parse.quote(word)
cookies = {"tmpid":"08c203d1-a48a-11e8-92fb-00002f590ab0",
           "gr_user_id":"9aa668ed-36e6-45ac-b7e4-488db68974a7",
           "NTKF_T2D_CLIENTID":"guest575EE744-6A23-4468-B74C-57DBB514F749",
           "UM_distinctid":"16557dbb74e40d-01b7694de9eb19-3467790a-13c680-16557dbb74f1f4",
           "grwng_uid":"ab6b8f97-a40e-4669-8e8e-4f1dcb7573f6",
           "uncode":"r4FqgqPJUC/RQd67NwLv/A==",
           "Hm_lvt_0eaa3be1a1b4ffd7be2065d4c04c3a3f":"1534777341,1534815258,1534817821",
           "judgeMedia":"https%3A//www.google.com/",
           "firstLand":"http%3A//www.zgg.com/",
           "b34a91e0993dce4c_gr_session_id":"dcb2a1f6-be7a-468f-9c44-3fa5dfc181be",
           "LXB_REFER":"www.google.com",
           "b34a91e0993dce4c_gr_session_id_dcb2a1f6-be7a-468f-9c44-3fa5dfc181be":"true",
           "_jzqa":"1.2700789908230487000.1534820602.1534820602.1534820602.1",
           "_jzqc":"1",
           "_jzqckmp":"1",
           "CNZZDATA1259629797":"1627498976-1534774924-%7C1534820664",
           "_qzjc":"1",
           "userName":"18930112016",
           "IsSelfReg":"0",
           "userID":"48042",
           "userToken":"AEDF993BBC245981749BF792073172AF",
           "_qzjb":"1.1534822275164.2.0.0.1.1",
           "_qzjto":"2.1.0",
           "nTalk_CACHE_DATA":"{uid:kf_9333_ISME9754_48042,tid:1534809811379696,opd:1}",
           "_qzja":"1.661258236.1534822275164.1534822275164.1534822275164.1534822275164.1534822302046.18930112016.1.0.2.1",
           "_jzqb":"1.9.10.1534820602.1",
           "Hm_lpvt_0eaa3be1a1b4ffd7be2065d4c04c3a3f":"1534822302",
           "gr_session_id_b34a91e0993dce4c":"a0014dd3-10e4-4f54-87db-54143f878eb3",
           "gr_session_id_b34a91e0993dce4c_a0014dd3-10e4-4f54-87db-54143f878eb3":"true",
           "nTalk_PAGE_MANAGE":"{|m|:[{|23716|:|223619|},{|87801|:|223619|},{|02389|:|223616|}],|t|:|11:32:41|}"
    }
session = requests.session()
requests.utils.add_dict_to_cookiejar(session.cookies, cookies)
url = url + inputword
return_data = session.get(url)
soup = BeautifulSoup(return_data.text,"html5lib")
result = soup.find_all('div',{"class" : "list-zl-conter"})
res = []
def change_soup_to_dict(result):
    required_data = result.text
    required_dict = {}
    required_data = re.sub(r"\s+","\n",required_data).split("\n")
    for i in range(1,len(required_data)-1):
        if i==1:
            req = required_data[i].split("】")[1]
            required_dict["专利名称："]=req
        else:        
            req = required_data[i].split("：")
            required_dict[req[0]] = req[1]
    return required_dict

for data in result:
    res.append(change_soup_to_dict(data))
print(res)

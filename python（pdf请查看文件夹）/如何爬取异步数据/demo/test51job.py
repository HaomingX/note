#-*- coding = utf-8 -*-
#@Time : 2020/8/8 20:52
#@Author : 李巍
#@File : test51job.py
#@Software: PyCharm

import json
import urllib.request,urllib.error     #制定URL，获取网页数据
import re


def main():
    url = "https://search.51job.com/list/090200,000000,0000,00,9,99,python,2,3.html?lang=c&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&ord_field=0&dibiaoid=0&line=&welfare="
    #url = "https://www3.nhk.or.jp/news/json16/word/0000967_002.json"
    #askURL(url)
    result = open('result.html', 'r', encoding='utf-8')
    data = re.findall(r"\"engine_search_result\":(.+?),\"jobid_count\"", str(result.readlines()))
    #print(data[0])
    jsonObj = json.loads(data[0])
    for item in jsonObj:
        print(item['job_name'] + ':' + item['providesalary_text'])

#间隔时间爬取
#代理


def askURL(url):
    head = {
        "User-Agent": "Mozilla / 5.0(Windows NT 10.0; Win64; x64) AppleWebKit / 537.36(KHTML, like Gecko) Chrome / 80.0.3987.122  Safari / 537.36"
    }
    request = urllib.request.Request(url,headers=head)
    html = ""
    try:
        response = urllib.request.urlopen(request)
        html = response.read().decode("gbk")
        print(html)
    except urllib.error.URLError as e:
        if hasattr(e,"code"):
            print(e.code)
        if hasattr(e,"reason"):
            print(e.reason)
    return html





if __name__ == "__main__":
    main()
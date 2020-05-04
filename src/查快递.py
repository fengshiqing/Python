import json, requests


def searchPackage():
    packageNum = input('请输入运单号码：')  # 输入运单号码，注意，只有正在途中的快递才可以查到！
    # 用 url_1 查询运单号对应的快递公司，如中通，返回：zhongtong。
    url_1 = 'http://www.kuaidi100.com/autonumber/autoComNum?resultv2=1&text=' + packageNum # 这个接口好像需要鉴权了
    response = requests.get(url_1) # 调用接口，并获得返回值
    companyName = json.loads(response.text)['auto'][0]['comCode']
    print("\n快递公司：" + companyName + "\n")
    # 用 url_2 查询和运单号、快递公司来查询快递详情，结果是一个json字符串
    url_2 = 'http://www.kuaidi100.com/query?type=' + companyName + '&postid=' + packageNum  # 还有个可选字段temp，如：'&temp=0.9829438147420106'
    print('时间↓                    快递进度↓\n')
    for item in json.loads(requests.get(url_2).text)['data']:  # 解析 Json 字符串
        print(item['time'], "----", item['context'])


while 1:
    searchPackage()
    print("\n")

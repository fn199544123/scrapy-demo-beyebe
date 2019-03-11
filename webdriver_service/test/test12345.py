import requests
import json

headers = {"Content-Type": "application/json"}
# 接口1、2测试DEMO
data12 = {
    "bill": {
        'ossPath': "http://byb-pic.oss-cn-shenzhen.aliyuncs.com/beyebe/data/20190222/d4107614554b82ff8e71a899b47d1114.pdf"
    }
}

text1 = requests.post("http://39.108.188.34:8893/QrcodeDetectV3", data=json.dumps(data12).encode(),
                      headers=headers).text
obj1 = json.loads(text1)
print("发票识别文件数(不是发票数)")
print(len(obj1['data']))
text2 = requests.post("http://39.108.188.34:9088/spider/fapiaoList.go", data=text1.encode(), headers=headers).text
obj2 = json.loads(text2)
print("发票验真结果")
print(obj2)
# 接口3，接口4测试DEMO
data34 = {
    "companyName": "沈阳北方建设股份有限公司",
    "billNums": ["01287153", "01238774"],
    "afterDate": "19000101"
}
text3 = requests.post("http://39.108.188.34:9089/spider/zhongdeng.go", data=json.dumps(data34).encode(),
                      headers=headers).text
obj3 = json.loads(text3)
print("中登网查询PDF数量", len(obj3['pdfs']))
text4 = requests.post("http://39.108.188.34:8891/BatchPdfCode", data=text3.encode(), headers=headers).text
obj4 = json.loads(text4)
print("交叉验证结果", obj4)
input = {
    "timelimit": "1年",
    "title": "测试归档号",
    "maincontractno": "转让合同编码",
    "maincontractcurrency": "人民币",
    "maincontractsum": "10000",
    "description": "我是可爱的小描述",
    "addDebtorList": [
        {
            # 企业
            "debtorType": "企业",
            "debtorName": "可爱的比一比",
            "orgCode": "abcd",
            "businessCode": "1234",
            "lei": "777",
            "responsiblePerson": "毛泽东",
            "industryCode": "农、林、牧、渔业",
            "scale": "大型企业",
            "country": "中国",
            "province": "广东省",
            "city": "深圳市",
            "address": "可爱的南山区",
        }
    ],
    "ossPathList": [
        {
            "filename": "东莞民兴YT20190228002.jpg",
            "path": "http://boss.yintaifac.com:8888/obpm/uploads/item/2019/070c9b11-61b4-4d81-a2c6-f9343eddc5bd.jpg"
        }
    ]
}
headers = {"Content-Type": "application/json"}
text5 = requests.post("http://39.108.188.34:9090/spider/zhongdengdengji.go", data=json.dumps(input).encode(),
                      headers=headers).text
print("预览测试")
print(json.loads(text5))

# testAccount = [{'account': 'ytbl0011', 'keyword': 'ytbl0011aDmin'}]
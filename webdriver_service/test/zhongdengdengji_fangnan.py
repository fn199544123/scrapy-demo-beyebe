import requests
import json
url = "http://localhost:9090/spider/zhongdengdengji.go"
input = {
    "timelimit": "1年",
    "title": "测试归档号",
    "maincontractno": "转让合同编码",
    "maincontractcurrency": "人民币",
    "maincontractsum": "10000",
    "description": "我是可爱的小描述",
    "addDebtorList": [
        {
            # 金融机构
            "debtorType": "金融机构",
            "debtorName": "出让人名称",
            "financeCode": "abc123abc123abc123",
            "businessCode": "abc",
            "lei": "123",
            "responsiblePerson": "江泽民",
            "country": "中国",
            "province": "黑龙江省",
            "city": "哈尔滨市",
            "address": "美丽的松花江",
        }, {
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
        }, {
            # 机关事业单位
            "debtorType": "机关事业单位",
            "debtorName": "可爱的比一比",
            "orgCode": "abcd",
            "legalCertificateNo": "1234",
            "lei": "777",
            "responsiblePerson": "毛泽东",
            "country": "中国",
            "province": "广东省",
            "city": "深圳市",
            "address": "可爱的南山区",
        }, {
            # 个体工商户
            "debtorType": "个体工商户",
            "tradeName": "字号名称",
            "idType": "身份证",
            "idCode": "230104199504041215",
            "country": "中国",
            "province": "广东省",
            "city": "深圳市",
            "address": "可爱的南山区",
        }, {
            # 个人
            "debtorType": "个人",
            "idType": "身份证",
            "idCode": "230104199504041215",
            "country": "中国",
            "province": "广东省",
            "city": "深圳市",
            "address": "可爱的南山区",
        }, {
            # 其他
            "debtorType": "其他",
            "debtorName": "出让人名称",
            "orgCodeNoVerify": "abc123abc123abc123",
            "registrationCertificateNo": "abc",
            "lei": "123",
            "responsiblePerson": "江泽民",
            "country": "中国",
            "province": "黑龙江省",
            "city": "哈尔滨市",
            "address": "美丽的松花江",
        }
    ]
}
data = json.dumps(input)
headers = {
'User-Agent': 'User-Agent:Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
    "Content-Type": "application/json"}
response = requests.post(url,data=data,headers=headers,timeout=(500,500))
print(response.text)
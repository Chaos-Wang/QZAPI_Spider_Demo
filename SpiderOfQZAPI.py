import requests
import json
import csv

user_xh = ''
user_pwd = ''
start = 1
end = 290
url = 'http://jxgl.hainu.edu.cn/app.do?'

test_data1 = {'method':'authUser','xh':user_xh,'pwd':user_pwd}
r1 = requests.get(url,params=test_data1)
text = json.loads(r1.text)
token=text.get("token")
head={'token': token}

for str in range(start,end):
    ex = "%(s)03d"%{'s':str}
    xh = '20171684310'+ex
    test_data2 = {'method':'getUserInfo','xh':xh}
    r2 = requests.get(url,params=test_data2,headers=head)
    res = json.loads(r2.text).get('bj')

    if(res == '计算机科学与技术2017-2'):
        test_data3 = {'method':'getCjcx','xh':xh}
        r3 = requests.get(url,params=test_data3,headers=head)
        s = json.loads(r3.text)
        file = open('./grade/'+xh+'.csv','w')
        writer = csv.writer(file,s[0].keys())
        for item in s:
            writer.writerow(item.values())
        print('xh:'+xh+ ' finished!')
            
            
        
        
            
            

        



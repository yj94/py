import time
import requests
import os
import base64
import re
Loginflag=-1
while (Loginflag==-1): #登录的flag为-1时 重复登录过程
    dtime =int(round(time.time() * 1000)) #十位时间戳
    #print("login time"+str(dtime))
    LoginCode = f"https://xg.fjsdxy.com/SPCP/Web/Account/GetLoginVCode?dt={dtime}" #拼接验证码
    filefold=os.getcwd()+"\\jpgs\\"
    path=filefold+str(dtime)+".jpg"
    apiUrl="http://api.ttshitu.com/base64" #OCR的API
    LoginPostTXT=""
    postsession=""
    session = requests.Session()
    r=session.get(LoginCode)
    sessiontext=str(r.cookies)
    #print(sessiontext)
    r3="Cookie (.+?) for"
    Result3=re.findall(r3,sessiontext)
    #print(Result3)
    sessionID=str(Result3).strip('[\']')#获取ASP SESSION
    #print("first login session"+sessionID)
    header = {"User-Agent":"Mozilla/5.0(Linux;Android 6.0;Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Mobile Safari/537.36",
            "Content-Type":"application/x-www-form-urlencoded",
            "Cookie":sessionID
            }#定义header
    #print("login header"+str(header))
    apiheader = {"User-Agent":"Mozilla/5.0(Linux;Android 6.0;Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Mobile Safari/537.36",
            'Connection':'keep-alive'
            }
    r.raise_for_status() #等待响应
    if not os.path.exists(filefold):
        os.mkdir(filefold)
    with open(path,'wb') as f:
        f.write(r.content)
        f.close()
        print("RawLoginCode save success")
    # RawLoginCode =Image.open(path)
    # grayimage=RawLoginCode.convert('1')
    # grayimage.save(os.getcwd()+r'\jpgs\final.jpg')
    # src = cv2.imread(os.getcwd()+r'\jpgs\final.jpg', cv2.IMREAD_UNCHANGED)
    # kernel = np.ones((3,1), np.uint8)
    # erosion = cv2.erode(src, kernel)
    # cv2.imwrite(os.getcwd()+r'\jpgs\erosion.jpg',erosion)
	# 原验证码处理
    with open(path, 'rb') as f2:
        base64data = base64.b64encode(f2.read())#验证码转为base64进行OCR
    LoginData={
        'username': '***',
        'password': '***',
        'typeid': '7',
        'image': base64data
    }
    Apisession = requests.Session()
    response = ((Apisession.post(apiUrl,headers=apiheader, data=LoginData)).text)#查看api的返回值
    #print(response)
    r="result\":\"(.+?)\""
    Result=re.findall(r,response)
    TheCode=str(Result).strip('[\']')#返回验证码
    print(TheCode)
    StuLogin=f"https://xg.fjsdxy.com/SPCP/Web/"
    LoginPage=(requests.get(StuLogin)).text
    r2="ReSubmiteFlag\" type=\"hidden\" value=\"(.+?)\""
    Result2=re.findall(r2,LoginPage)
    ReSubmiteFlags=str(Result2).strip('[\']')#登录的flag
    #print(ReSubmiteFlag)
    with open('user.txt',encoding='utf-8') as file: #读取账号 格式：学号,身份证后六位
        content=file.read()
        user=content.rstrip()
        file.close()
    Div=content.index(',')
    Username=content[:Div]
    Rawpassword=content[Div+1:]
    Password="Fjsy@"+Rawpassword
    StuLoginData={
        'ReSubmiteFlag':ReSubmiteFlags,
        'StuLoginMode':'1',
        'txtUid':Username,
        'txtPwd':Password,
        'code':TheCode
    }#post的data
    #r=session.get(StuLogin)
    #sessiontext=str(r.cookies)
    #print("login session"+sessiontext)
    LoginPost=(session.post(StuLogin,headers=header,data=StuLoginData))#提交登录数据
    LoginPostTXT=((LoginPost).text)
    with open('text.txt','w',encoding='utf-8')as f3:
        f3.write(LoginPostTXT)#保存登录信息为txt
        f3.close()
    tempcookie=session.cookies.get_dict()
    with open('cookie.txt','w+',encoding='utf-8')as fr3:#读取保存的cookie
        fr3.write(str(tempcookie))
        fr3.close()
    #print(tempcookie)
    # sessionresult=tempcookie.replace('{','')
    # sessionresult2=sessionresult.replace('\': ','=')
    # sessionresult3=sessionresult2.replace('}','')
    # sessionresult4=sessionresult3.replace('=\'','=')
    # print(sessionresult4)
    with open('text.txt',encoding='utf-8') as Loginstate:
        content4=Loginstate.read()
        testLoginflag=content4
        #print(testflag)
        Loginflag=(testLoginflag.rfind("安全退出")) #查找是否有此字段来判断是否登录成功

print("登录成功") 
print("wait for post")

def PostTemper1():#提交表单
    dtime2 =int(round(time.time() * 1000))
    temperCode = f"https://xg.fjsdxy.com/SPCP/Web/Account/GetLoginVCodeForm?gnmc=twtb&dt={dtime2}"
    path=filefold+str(dtime2)+".jpg"
    rok=session.get(temperCode)
    m1=35
    rok.raise_for_status()
    if not os.path.exists(filefold):
        os.mkdir(filefold)
    with open(path,'wb') as ff:
        ff.write(rok.content)
        ff.close()
        print("code save success")
    with open('cookie.txt',encoding='utf-8') as cfile:
        content2=cfile.read()
        finalcookie=eval(content2)
        cfile.close()
    with open(path, 'rb') as ff2:
        base64data2 = base64.b64encode(ff2.read()) 
    LoginData2={
        'username': 'yj233',
        'password': 'yjk123456',
        'typeid': '7',
        'image': base64data2
    }
    Apisession = requests.Session()
    response2 = ((Apisession.post(apiUrl,headers=apiheader, data=LoginData2)).text)
    r4="result\":\"(.+?)\""
    PostResult=re.findall(r4,response2)
    PostCode=str(PostResult).strip('[\']')
    print(PostCode)
    StuPost=f"https://xg.fjsdxy.com/SPCP/Web/Temperature/StuTemperatureInfo"
    PostPage=(requests.get(StuPost)).text
    r5="ReSubmiteFlag\" type=\"hidden\" value=\"(.+?)\""
    FlagResult=re.findall(r5,PostPage)
    ReSubmiteFlags2=str(FlagResult).strip('[\']')
    header2 = {"User-Agent":"Mozilla/5.0(Linux;Android 6.0;Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Mobile Safari/537.36",
            "Content-Type":"application/x-www-form-urlencoded",
            "Connection":"keep-alive",
            }
    StuPostData={
        'TimeNowHour':'7',
        'TimeNowMinute':m1,
        'Temper1':'36',
        'Temper2':'3',
        'code':PostCode,
        'ReSubmiteFlag':ReSubmiteFlags2
    }
    LoginPost=((session.post(StuPost,headers=header2,cookies=finalcookie,data=StuPostData)).text)
    with open('post.txt','w',encoding='utf-8')as ff3:
        ff3.write(LoginPost)#保存post信息为txt
    with open('post.txt',encoding='utf-8') as state:
        content3=state.read()
        testflag=content3
    flag=(testflag.rfind("成功"))
    if (flag==-1):
        time.sleep(300)
        int(m1)+5
        PostTemper1()
    else:
        print("早上填报成功！")
        with open('result.txt','a',encoding='utf-8')as rs:
            rs.write(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())+" 早上填报成功！\n")
            rs.close()
        return
PostTemper1()
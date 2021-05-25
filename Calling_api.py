from requests import get
import json,os
link = 'http://saral.navgurukul.org/api/courses'
res = get(link).text
j=json.loads(res)
d=[]
for p in j:
    c=0
    for m in j[p]:
        print(str(c)+".",m['name']) 
        c+=1
        d.append(m)
inp = int(input("Enter the serial number :\n"))
for i in range(len(d)) :
    r=d[i]
    if inp==i:
        for q in r :
            link1 = "http://saral.navgurukul.org/api/courses/"+r['id']+"/exercises"
            resq = get(link1).text
            js = json.loads(resq)
lis=[]
l=1
for p in js['data']:
    jktyre=[]
    print(str(l)+".",p['name'])
    go=link1[:-1]+'/getBySlug?slug='+p['slug']
    x=p['childExercises']
    jktyre.append(go)
    s=1
    for g in x :
        god=link1[:-1]+'/getBySlug?slug='+g['slug']
        z=str(l)+'.'+str(s)
        print ('        '+z,g['name'])
        a={z:god}
        lis.append(a)
        jktyre.append(god)
        s+=1
    dicton={l:jktyre}
    lis.append(dicton)
    l+=1
inf=(input("Enter a number :\n"))
for i in lis:
    for j in i:
        try:
            if inf==j:
                fg=get(i[j]).text
                fg=json.loads(fg)
                km=json.loads(fg['content'])
                km=km[0]['value']
                print(km.strip())
            if int(inf)==j:
                df=1    
                for g in i[j] :
                    fg=get(g).text
                    fg=json.loads(fg)
                    km=json.loads(fg['content'])
                    km=km[0]['value']
                    print(str(df)+'.',km.strip())
                    df+=1
        except Exception as a:
            pass





























# def calling_an_api():    
#     page = get('http://saral.navgurukul.org/api/courses')
#     data=page.text
#     j=json.loads(data)
#     lst=[]
#     for i in j.values():
#         dic={}
#         for k in i:
#             for m in k:
#                 dic[m]=k[m]
#             lst.append(dic.copy())
#     with open('courses.json','w+') as fs:
#         fs.write(json.dumps(lst,indent=4))
#         fs.close()
#     return j
# # pprint(calling_an_api())
# def get_back():
#     with open('courses.json','r') as fs:
#         re=fs.read()
#         f=json.loads(re)
#         sec=[]
#         c=0
#         for i in f:
#             print(c,i['name'])
#             sec.append([c,i['name']])
#             c+=1
#         inp=int(input('Enter a Id:-'))
#         for i in sec:
#             if inp==i[0]:
#                 print(f[inp])       
#                 pass
# get_back()
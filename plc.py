import requests
from bs4 import BeautifulSoup

loginurl = 'https://172.31.14.4/FormLogin'

loggedinurl = 'https://172.31.14.4/Portal/Portal.mwsl?PriNav=Vartables'

username = input("Username: ")
password = input("Password: ")

access = input("Which table would you like to access: (Requested='0', RequestedName='1', AckRequested='2', AckRequestedName='3', Previous.Code='4', Previous.Name='5', Current.Code='6', Current.Name='7', Next.Code='8', NextName='9'): ")

#requestType = input("Would you like to pull data or modify the data in the table: ('pull', 'modify')")

payload = {
    'Login':username,
    'Password':password,
    'Redirection': None
}

headerlist = {
    'Host': '172.31.14.4',
    'Connection': 'keep-alive',
    'Content-Length': '36',
    'Cache-Control': 'max-age=0',
    'Origin': 'https://172.31.14.4',
    'Upgrade-Insecure-Requests': '1',
    'Content-Type': 'application/x-www-form-urlencoded',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36',
    'Sec-Fetch-Dest': 'document',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-User': '?1',
    'Referer': 'https://172.31.14.4/Portal/Portal.mwsl?intro_enter_button=ENTER&PriNav=Start&coming_from_intro=true',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.9',
    'Cookie': 'siemens_ad_session=WnIHYF/AVc+peny4wwexL2uYBxTwQzcveF3DHA==; siemens_ad_secure_session=QZicNFplSiwlMdkgg8rL1iA070FT8DGy5KqV5A=='
}

with requests.Session() as s:
    t = s.post(loginurl, data=payload, headers=headerlist, verify=False)
    print('-----------------------------------------------------------------------------------------')
    q = s.get(loggedinurl)
    print('-----------------------------------------------------------------------------------------')
    soup = BeautifulSoup(q.text, features="html.parser")
    request = 'vartable_updatable_' + access
    print(request)
    print('-----------------------------------------------------------------------------------------')    

    
    a = soup.findAll('tr', attrs={'class':'var'})
    print("a equals: ")
    print(a)

    
    for i in a:
        varValue = i.find('td', attrs={'id':request})
        if varValue != None:
            print("varValue equals: ")
            print(varValue)
            print("The Monitor Value you requested is: " + varValue.text)







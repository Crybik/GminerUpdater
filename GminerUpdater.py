import requests
import regex
import re
import os
import platform
from tqdm import tqdm
from zipfile import ZipFile
from bs4 import BeautifulSoup
url = 'https://github.com/develsoftware/GMinerRelease/'
r = requests.get(url)
soup = BeautifulSoup(r.content, 'html.parser')
thelastest = soup.find('span',{'class':'css-truncate css-truncate-target text-bold mr-2'})
LF = float(thelastest.text)
formatted = "{:.2f}".format(LF)
appxdata = os.getenv('APPDATA')
url2 = ("https://github.com/develsoftware/GMinerRelease/releases/tag/"+formatted)
r2 = requests.get(url2)
soup2 = BeautifulSoup(r2.content, 'html.parser')
if platform.system() == "windows" or platform.system() == "Windows":
    v = appxdata+'\\gversion.txt'
    if os.path.isfile(str(v)) == True:
        with open(v) as f:
            contents = f.read()
    else:
        print ("type the current version of your Gminer-Update ( First time only )\nExample : 2.60\nif you don't know your current version press enter")
        current = input()
        if not current:
            current = float(formatted)-1
        with open(appxdata+'\\gversion.txt', 'w') as f:
            f.write (str(current))
elif platform.system() == "Linux" or platform.system() == "linux":
    print ("type the current version of your Gminer-Update ( First time only )\nExample : 2.60\nif you don't know your current version press enter")
    current = input()
    print ("Check")
    v = "/tmp/gversion.txt"
    if os.path.isfile(str(v)) == True:
        with open(v) as f:
            contents = f.read()
    #with open('/tmp/gversion.txt', 'w') as f:
    elif not current:
        current = float(formatted)-1
        with open(v, 'w') as f:
            f.write (str(current))
        f.write (current)
with open(v, "r") as yyy:
     verdata = yyy.read()
     vfloat = (float(verdata))
def veryfing():
    if formatted > (f"{vfloat:.2f}"):
        print ("There is an Update and it is | Gminer",formatted)
        outdated = (bool(True))
        print("\nDo you want to Download the New-Update : Gminer : ",formatted)
        print("\nPlease type [Yes/No] or [Y/N] ")
        downloadoption = input()
        if downloadoption == "Yes" or downloadoption == "yes" or downloadoption == "y" or downloadoption == "yeah" or downloadoption == "yup" or downloadoption == "1" or downloadoption == "YeS" or downloadoption == "YES" or downloadoption == "yES" or downloadoption == "yea":
            regex = re.compile('.*windows.*')
            if platform.system() == "linux" or platform.system() == "Linux":
                regex = re.compile('.*linux.*')
            thedownloadingthing = soup2.find ('a',{'href': regex})
            relname = thedownloadingthing.text.strip()
            theentirelink = f"https://github.com/develsoftware/GMinerRelease/releases/download/{formatted}/{relname}"
            if os.path.isfile(relname):
                print("The file is already existed")
            else: 
                print("Downloading >>>")
                download_link = requests.get(theentirelink, allow_redirects=True)
                open(relname, 'wb').write(download_link.content)
                # if the downloading finished Change the current versoin to the newer
                if platform.system() == "windows" or platform.system() == "Windows":
                    if os.path.isfile(relname):
                        print("The Miner has been downloaded")
                        with open(v, "w") as myfile:
                            myfile.write(formatted)
                if platform.system() == "linux" or platform.system() == "Linux":    
                    print("The Miner has been downloaded")
                    with open("/tmp/gversion.txt", "w") as myfile:
                        myfile.write(formatted)
                # Extraction
                print ("Choose one \n-1 Extract miner.exe ( Recommended ) \n-2 Extract all files \n-3 Do not extract anything")
                exoption = input()
                if exoption == "1" or exoption == "-1" or exoption == "one":
                    path = os.getcwd()
                    minerfile = "miner.exe"
                    with ZipFile(path+"\\"+relname, 'r') as zipfilex:
                        with open(minerfile, 'wb') as f:
                            f.write(zipfilex.read(minerfile))
                            print("Miner.exe ~ Extracted")
                elif exoption == "2" or exoption == "-2" or exoption == "two":
                    zf = ZipFile(relname, 'r')
                    zf.extractall("minerfiles")
                    zf.close()
                    print("Miner Files ~ Extracted")
                elif exoption == "3" or exoption == "-3" or exoption == "three": 
                    print("Nothing ~ Extracted")
        elif downloadoption == "No" or downloadoption == "no" or downloadoption == "Nope" or downloadoption == "NOPE" or downloadoption == "nah" or downloadoption == "nO" or downloadoption == "0" or downloadoption == "n":
            print("Updates are always good btw") 
        else:
            print("Please Type [Yes] or [No]")        
    else:
        print ("You have the lastest version : )")
        outdated = (bool(False))
veryfing()
import os
import requests
import gdown


#download file
def check_is_sharing(link): #check if given link contins 'sharing' keyword.
    if 'sharing' in link: 
        return True
    else:
        return False

def get_file_id(link): #return the shared file id
    try:
        link = link[32:]
        for i in range(len(link)):
            if link[i] == '/':
                stop = i
        return link[:stop]
    except:
        return False


def download_link(link):
    prefix = 'https://drive.google.com/uc?export=download&id='

    if not check_is_sharing(link):
        print('this link is not detected as a sharing link.\nAbort process')
        return -1

def downloader(link, path):
    '''
    try:
        response = requests.get(link)
        open("instagram.html", "wb").write(response.content)
        return response.content
    except:
        return False
    '''
    gdown.download(link, path, quiet=False)

def download_file(link, path):
    if not check_is_sharing(link):
        return -1
    
    file_id = get_file_id(link)
    if not file_id:
        return -2

    version = downloader(link, path)
    if not version:
        return -3
    else:
        return version



downloader('https://drive.google.com/file/d/1Hg9Ol1ShodctpWTVfZc5jo5-SDmYXZPi/view?usp=sharing', 'version.txt')
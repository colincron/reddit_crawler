import requests
import re
from bs4 import BeautifulSoup

sub_pattern = re.compile("\\/r\/([a-zA-Z0-9-_]*)\/$")
link_list = []
done_list = []
garbage_list = []
subs_list = []

def write_to_file(href):
    with open("test.txt", "a") as myfile:
        print("File opened")
        myfile.write(href + "\n")
        print("Written to output file")
        myfile.close()
        print("File closed")

def get_site(url):
    print("Adding site %s to link_list" % url)
    link_list.append(url)
    print("%s appended to link_list" % url)
    while len(link_list) > 0:
        if link_list[0] not in garbage_list and link_list[0] not in done_list:
            print("Trying url: %s " % link_list[0])
            #r = requests.get(link_list[0], verify=False)
            r = requests.get(link_list[0])
            get_links(r)
            # can add new functionality here?
            print("Removing link_list[0] and adding to done_list: %s " % link_list[0])
            done_list.append(link_list[0])
            link_list.pop(0)
        else:
            print("Already accounted for: %s " % link_list[0])
            link_list.pop(0)

def get_links(r):
    html = r.text
    soup = BeautifulSoup(html, 'html.parser')
    for link in soup.find_all('a'):
        href = link.get('href')
        if href == None:
            pass
        elif href.startswith('https://www.reddit.com'):
            if href not in done_list and href not in garbage_list:
                print("Found link: %s" % href)
                link_list.append(href)
            else:
                print('accounted for: %s ' % href )
        else:
            print("Garbage link: %s " % href)
            if href.startswith('/r/') and sub_pattern.match(href) and href not in subs_list:
                print("Subreddit found! %s " % href)
                print("Appending to subs_list... %s" % href)
                subs_list.append(href)
                print("Writing to file... %s" % href)
                write_to_file(href)
            garbage_list.append(href)

if __name__ == "__main__":
    url = "http://www.reddit.com"
    
    get_site(url)
    print(link_list)
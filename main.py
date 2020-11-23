import requests
import re
from bs4 import BeautifulSoup

sub_pattern = re.compile("\\/r\/([a-zA-Z0-9-_]*)\/$")
topic_pattern = re.compile("\\/t\/([a-zA-Z0-9-_]*)\/$")
user_pattern = re.compile("\\/user\/([a-zA-Z0-9-_]*)\/$")
link_list = []
done_list = []
garbage_list = []
subs_list = []
users_list = []
topics_list = []
base_url = "http://www.reddit.com"

def write_to_file(href):
    if href.startswith('/r/'):
        print("Write function: sub")
        with open("subs.txt", "a") as myfile:
            print("File opened")
            full_url = base_url + href + "\n"
            print("FULL URL TEST:::::::: %s " % full_url)
            myfile.write(full_url)
            link_list.append(full_url)
            print("Written to output file")
            myfile.close()
            print("File closed")
    if href.startswith('/user/'):
        print("Write function: user")
        with open("users.txt", "a") as myfile:
            print("File opened")
            full_url = base_url + href + "\n"
            print("FULL URL TEST:::::::: %s " % full_url)
            myfile.write(full_url)
            link_list.append(full_url)
            print("Written to output file")
            myfile.close()
            print("File closed")
    if href.startswith('/t/'):
        print("Write function: topic")
        with open("topics.txt", "a") as myfile:
            print("File opened")
            full_url = base_url + href + "\n"
            print("FULL URL TEST:::::::: %s " % full_url)
            myfile.write(full_url)
            link_list.append(full_url)
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
            print("Possible garbage link: %s " % href)
            print("Deciding if it's a subreddit, a user, or a topic")
            if href.startswith('/r/') and href not in subs_list:
                if sub_pattern.match(href):
                    print("SUBREDDIT found! %s " % href)
                    print("Appending to subs_list... %s" % href)
                    subs_list.append(href)
                    print("Writing to file... %s" % href)
                    write_to_file(href)
            if href.startswith('/user/') and href not in users_list:
                if user_pattern.match(href):
                    print("USER found! %s " % href)
                    print("Appending to the users_list... %s " % href)
                    users_list.append(href)
                    print("Writing to file... %s " % href)
                    write_to_file(href)
            if href.startswith('/t/') and href not in topics_list:
                if topic_pattern.match(href):
                    print("TOPIC found! %s " % href)
                    print("Appending to the topics_list... %s " % href)
                    topics_list.append(href)
                    print("Writing to file... %s " % href)
                    write_to_file(href)
                    
            garbage_list.append(href)

if __name__ == "__main__":
    get_site(base_url)
    #print(link_list)
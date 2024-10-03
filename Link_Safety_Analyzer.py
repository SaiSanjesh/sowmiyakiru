import requests

def link_check(link):
    def expand_short_url(short_url):
        try:
            response = requests.head(short_url, allow_redirects=True)
            main_url = response.url
            return main_url
        except requests.exceptions.RequestException as e:
            print(f"Error expanding short URL: {e}")
            return None

   
    short_url = link
    return expand_short_url(short_url)


def is_phishing_link(url_list):
 
    services = [
        "paypal","facebook","google","appleid","ebay","microsoft","amazon","twitter","instagram","linkedin","pinterest","snapchat","tumblr","reddit",
        "youtube","whatsapp","telegram","wechat","line","viber","kik","skype","zoom","discord","twitch","tiktok","quora","flickr","vimeo","badoo","github",
        "myspace","meetup","soundcloud","mix","foursquare","vine","periscope","pof","okcupid","grindr","tinder","hinge","bumble","zoosk","match","eharmony","youtube"
    ]

    for i in services:
        if url_list[0]=='https:' and (url_list[1][0] == i or url_list[1][1] == i):
            return True
        else:
            continue
    return False
if __name__=='__main__':
    red = "\033[91m"
    green = "\033[92m"
    reset = "\033[0m"
    cyan = "\033[36m"
    print(cyan)
    print("""Welcome to Link Safety Analyzer
                    Created by Sanju""")
    print(reset)
    while True:
        print("1. Analysis Link.\n2. Exit.")
        ch=input("Enter Option: ")
        if ch=='1':
            url = input("Enter Url to Analysis Link: ")
            print()
            link=link_check(url)
            url_list=[]
            url_list.append(link.split('//')[0])
            url_list.append(link.split('//')[1].split('.'))
            if is_phishing_link(url_list):
                print(green,"------> The link appears to be safe.",reset)
                print("Main Url is: ", green,link,reset)
                print()
            else:
                print(red,"------> Warning: This link is anonymous.")
                print("Main Url is: ",link,reset)
                print()
        else:
            break

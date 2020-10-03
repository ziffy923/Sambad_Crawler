import bs4
from urllib.parse import urlparse


key='class'



def find_links(i,div,base_url):
    print('container id is:',i)

    spans=div.find_all('span')
    if(spans[0].text!='KATHA'):
        return ''

    for link in div.find_all('a'):
        parse_result= urlparse(link.get('href'))
        if(not bool(parse_result.netloc)):
            actual_url=base_url+parse_result.path
        else:
            actual_url=parse_result.scheme+'://'+parse_result.netloc+parse_result.path
    return actual_url


def main():
    output_list=[]
    url='https://www.sambadepaper.com/'
    file_index= open('new_sam.html','r')

    soup= bs4.BeautifulSoup(file_index.read(),'html.parser')
    all_divs=soup.find_all('div')

    for i, div in zip(range(len(all_divs)),all_divs):
        attr_set=div.__dict__['attrs']
        if key in attr_set:
            if 'papercol' in attr_set[key]:
                target_url=find_links(i,div,url)
                if target_url!='':
                    output_list.append(target_url)

    for link in output_list:
        print(link)


if __name__ == '__main__':
    main()

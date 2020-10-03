import os
import re
from PIL import Image



def sort_key(str):
    temp=re.findall(r'\d+',str)
    res = list(map(int, temp))
    val=int(res[1])
    return val



def main():
    current_dir=os.getcwd()
    full_file_list=[]
    for root, dir, files in os.walk(current_dir):
        pass

    reg_kat=re.compile('kat')
    reg_ss=re.compile('ss')

    for file in files:
        res_kat=reg_kat.findall(file)
        if res_kat:
            res_ss=reg_ss.findall(file)
            if (not res_ss):
                full_file_list.append(os.path.join(current_dir,file))

    full_file_list.sort(key=sort_key)

    Image_open_list=[]

    for file in full_file_list:
        temp=Image.open(file)
        Image_open_list.append(temp)

    Image_open_list[0].save(os.path.join(current_dir,'Katha.pdf'),save_all=True, append_images=Image_open_list[1:])




if __name__ == '__main__':
    main()

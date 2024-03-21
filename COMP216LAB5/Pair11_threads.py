#Nida Karadag
#Aiden Ireland
#Part A
import requests
import threading
import argparse
import time
#Nida Karadag Parts (A - B)
def urlTaker(url, pathname):
    r = requests.get(url)
    if r.ok:
        with open(pathname, 'wb') as fd:#ridiculously small size
            fd.write(r.content)         #write the bit to file
        print('Image downloaded')
    else:
        print('Image could not be downloaded')

urls = [
'https://th.bing.com/th/id/OIP.z-dkECmUFma29zYrb27JkwAAAA?w=264&h=180&c=7&r=0&o=5&pid=1.7',
'https://th.bing.com/th/id/OIP.MhwSzfXnBG1MpuuA6IFi-AAAAA?w=218&h=180&c=7&r=0&o=5&pid=1.7',
'https://th.bing.com/th/id/OIP.m8b7Y9-81Q4UMCBMaFkw2QAAAA?w=198&h=180&c=7&r=0&o=5&pid=1.7',
'https://th.bing.com/th/id/OIP.XN9D7tH47WNJ8h214YgqTwAAAA?w=220&h=180&c=7&r=0&o=5&pid=1.7',
'https://th.bing.com/th/id/OIP.cFvfW8dARmuVtR3zOxfTSAHaE9?w=274&h=183&c=7&r=0&o=5&pid=1.7',
'https://th.bing.com/th/id/OIP.wcEy7Ow-TaAohBCz6USqCAAAAA?w=265&h=180&c=7&r=0&o=5&pid=1.7',
'https://th.bing.com/th/id/OIP.9FWt0sWpi4UOee5o3WdI-QHaFj?w=224&h=180&c=7&r=0&o=5&pid=1.7',
'https://th.bing.com/th/id/OIP.JYXSCIpGskpiOxYTw1vuwgAAAA?w=252&h=180&c=7&r=0&o=5&pid=1.7',
'https://th.bing.com/th/id/OIP.QjWOHkojgYSz1LhaypSB-gAAAA?w=190&h=180&c=7&r=0&o=5&pid=1.7',
'https://th.bing.com/th/id/OIP.Wlfm_lF4VWlYLiPNfbmbDwHaHa?w=181&h=181&c=7&r=0&o=5&pid=1.7',
'https://th.bing.com/th/id/OIP.ZquJ_NwCCyWfvpAEeU-vngAAAA?w=142&h=180&c=7&r=0&o=5&pid=1.7',
'https://th.bing.com/th/id/OIP.C6q29lesR7-Ork5YKuI6LwAAAA?w=257&h=180&c=7&r=0&o=5&pid=1.7',
'https://th.bing.com/th/id/OIP.A7o1Bm-XNr9A_4pLPCCujgAAAA?w=252&h=180&c=7&r=0&o=5&pid=1.7',
'https://th.bing.com/th/id/OIP.oSjt2rY3YUScDY7pw3b1WAHaFj?w=236&h=180&c=7&r=0&o=5&pid=1.7',
'https://th.bing.com/th/id/OIP.AroTG9KnmisPIhICyGjoDAHaFj?w=223&h=180&c=7&r=0&o=5&pid=1.7',
'https://th.bing.com/th/id/OIP.zSyHBN9_rn_O9XBkdPx-agAAAA?w=189&h=180&c=7&r=0&o=5&pid=1.7',
'https://th.bing.com/th/id/OIP.pGTxkbwreLj7l2ORZrtA8gAAAA?w=147&h=184&c=7&r=0&o=5&pid=1.7',
'https://th.bing.com/th/id/OIP.5SaLUh616MU7KDIP2_0VCwAAAA?w=204&h=180&c=7&r=0&o=5&pid=1.7',
'https://th.bing.com/th/id/OIP.S-lrZd2TFhSEpI3VRQyKqQAAAA?w=173&h=180&c=7&r=0&o=5&pid=1.7',
'https://th.bing.com/th/id/OIP.sDmZWxXBrF329vZvDu2HrAAAAA?w=266&h=180&c=7&r=0&o=5&pid=1.7',
'https://th.bing.com/th/id/OIP.5umgRLykyWn-v_5HmOS0NAHaE7?w=243&h=180&c=7&r=0&o=5&pid=1.7',
'https://th.bing.com/th/id/OIP.MPayRq2bYdhfVUj5O9BCnwAAAA?w=125&h=184&c=7&r=0&o=5&pid=1.7',
'https://th.bing.com/th/id/OIP.OeLv1q1dEfGkl1bRHfM5awHaFj?w=240&h=180&c=7&r=0&o=5&pid=1.7',
'https://th.bing.com/th/id/OIP.MksSZEmu5Cgly2HNvRp4NQAAAA?w=180&h=163&c=7&r=0&o=5&pid=1.7',
'https://th.bing.com/th/id/OIP.HCpPn-IRV8SVidBlRoBRUwHaE7?w=287&h=191&c=7&r=0&o=5&pid=1.7'
]

# takes url and pathname as arguments and downloads the image from the url to the pathname
#pathname = './wk05_a6_download_file.py'
#urlTaker(urls, pathname)

#Part B
'''
1.	Create a function that does not require any argument and does the following:
a.	Start timer.
[import the time module
use time.perf_counter() to get the current time.]
b.	Call the function in Part A with appropriate arguments (first the supplied url list 
and the second one that you will have to generate) to sequentially each url. 
(Invoke the method after the previous download is completed).
c.	End timer. 
[again use time.perf_counter() to get the current time.]
d.	Print elapse times. 
[subtract (a) from (c).]
'''

def timeIt():
    start = time.perf_counter()
    for i, url in enumerate(urls):
        pathname = f'Images/wk05_a6_download_file_{i}.jpg'
        urlTaker(url, pathname) 
    end = time.perf_counter()
    print(f'Function urlTaker took {end-start} seconds to complete')


#Aidens Part (C - D)
#part C Create a function that does not require an argument and does the following:
def PartC():
    start = time.perf_counter() 
    threads = []
    for i, url in enumerate(urls):
        pathname = f'Images/image_{i}.jpg'
        thread = threading.Thread(target=urlTaker, args=(url, pathname)) #call the function in Part A with appropriate arguments.
        # 'threading.Thread': constructor from the import threading to be used to create a new thread.
        # 'target=urlTaker': specifies the target (urltaker) that the thread will execute.
        # 'args=([url], pathname)': These are the arguments that urlTaker function expects and will be passed through.
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()#scyronize the threads
    end = time.perf_counter()#End timer when all the threads have completed their downloads
    print(f'Part C function Used Function A \'urlTaker\' and took {end - start} seconds to complete in a elapse fashion')#print elapse times
#Run Function
#timeIt()
#PartC()
#PART D main method for code
def main():
    #Creates an ArgumentParser 
    parser = argparse.ArgumentParser(description='Download images in either serial or threaded mode.')
    #A mandatory argument that may be either serial or threaded 
    parser.add_argument("mode", choices=["serial", "threaded"], help="Execution mode: 'serial' or 'threaded'")
    #optional Arg for downloading folder
    parser.add_argument("-f", "--folder", default='./Images', help="Folder to save downloaded images (default is ./Images)") #used to pass incase someone wants a curtain file but the assignment said it dosnt take a file request I didnt edit the methods for it
    #create the phaser
    args = parser.parse_args()
    #run 'python Pair11_threads.py serial' in ps (must cd into COMP216\COMP216LAB5)
    if args.mode == "serial":
        timeIt()  # Part B
    #run 'python Pair11_threads.py threaded' in ps 
    elif args.mode == "threaded":
        PartC()  # Part C

if __name__ == "__main__":
    main()
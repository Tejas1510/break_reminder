import webbrowser
import time


breaks = int(input("How many breaks do you wish to take? :)"))
break_count = 0

if(break_count<breaks):
    time.sleep(1200)
    webbrowser.open("https://gaana.com/song/fagan-foramto-aayo-4")
    break_count = break_count+1

if(break_count==1):
    while(break_count<breaks):
        time.sleep(1500)
        webbrowser.open("https://gaana.com/song/fagan-foramto-aayo-4")
        break_count = break_count+1
        

else:
    exit 
    






    







    

    




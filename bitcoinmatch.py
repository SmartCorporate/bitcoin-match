from bitcointools import *
import sys
import os
import re
from time import sleep
from urllib.request import urlopen
import winsound
import time

print( "\n-------||---||---------------------------------" );
print( "\n---===============-----------------------------" );
print( "\n---==||===========-----------------------------" );
print( "\n-----||--      ---==---------------- ----------" );
print( "\n-----||--      ---==---------------------------" );
print( "\n-----||----- ---==-----------------------------" );
print( "\n-----||---------==-----------------------------" );
print( "\n-----||----- ---=====--------------------------" );
print( "\n-----||--       ----===------------------------" );
print( "\n-----||--        -----==-----------------------" );
print( "\n-----||--       ----===------------------------" );
print( "\n---==||=============---------------------------" );
print( "\n---===============----------BITCOIN  MATCH-----" );
print( "\n-------||---||--------------------2022---------" );
print( "\n----------------------------------2140---------" );

time.sleep(3)



while True:

  print('===========[]==[] BTC MATCH... []==[]================')
  #billioner addres BTC
  gold = "1KUr81aewyTFUfnq4ZrpePZqXixd59ToNn"
 
  priv = random_key()
  print('Private random key is:')
  print (priv )

  
  pub = privtopub(priv)

  address = pubtoaddr(pub)
  print('Public address is:')
  print (address)


  check_address = address

  

  if check_address == gold :
            print( "MATCH!!");
            text_file = open("match.txt","a")
            text_file.write("\nMATCH!!! ")
            text_file.write("\nThis is private key: " + priv)
            text_file.write("\nThis is btc public address: " + check_address)
            text_file.write("\n$$$$$$$$$$$!!!!!!!!!!")
            text_file.close()
            winsound.Beep(440, 500)
            winsound.Beep(500, 700)
            winsound.Beep(440, 500)
            winsound.Beep(500, 700)
            winsound.Beep(440, 500)
            winsound.Beep(500, 700)

 
         



                   

            
 
          

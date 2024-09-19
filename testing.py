import matplotlib.pyplot as plt


import pymysql
import pandas as pd


from datetime import date
import time
start_time=time.time()
duration=10

tv_count=0
tv_price=0
samsung_tv_count=0
samsung_tv_price=0
lg_tv_count=0
lg_tv_price=0
sony_tv_count=0
sony_tv_price=0
redmi_tv_count=0
redmi_tv_price=0

fan_count=0
fan_price=0
usha_fan_count=0
usha_fan_price=0
crompton_fan_count=0
crompton_fan_price=0
bajaj_fan_count=0
bajaj_fan_price=0
havells_fan_count=0
havells_fan_price=0


fridge_count=0
fridge_price=0
samsung_fridge_count=0
samsung_fridge_price=0
lg_fridge_count=0
lg_fridge_price=0
whirlpool_fridge_count=0
whirlpool_fridge_price=0
bluestar_fridge_count=0
bluestar_fridge_price=0


washing_machine_count=0
washing_machine_price=0
samsung_washing_machine_count=0
samsung_washing_machine_price=0
lg_washing_machine_count=0
lg_washing_machine_price=0
whirlpool_washing_machine_count=0
whirlpool_washing_machine_price=0
bluestar_washing_machine_count=0
bluestar_washing_machine_price=0
ifb_washing_machine_count=0
ifb_washing_machine_price=0

while (time.time() - start_time)< duration:
    try:
        product=input("enter the product")
        price=int(input("enter the price"))
        if product.isalpha() and price>0:
           if (product=="tv"):
              tv_count=tv_count+1
              if (price>0):
                 tv_price=tv_price+price
              product_brand=input("enter the product brand name")   
              if (product_brand=="samsung"):
                 samsung_tv_count=samsung_tv_count+1
                 if(price>0):
                   samsung_tv_price=samsung_tv_price+price
              elif (product_brand=="lg"):
                  lg_tv_count=lg_tv_count+1
                  if(price>0):
                    lg_tv_price=lg_tv_price+price
              elif (product_brand=="sony"):
                   sony_tv_count=sony_tv_count+1
                   if(price>0):
                      sony_tv_price=sony_tv_price+price
              elif(product_brand=="redmi"):
                  redmi_tv_count=redmi_tv_count+1
                  if(price>0):
                     redmi_tv_price=redmi_tv_price+price

            
            
        
            
            
           
           elif (product=="fan"):
                fan_count=fan_count+1
                if(price>0):
                   fan_price=fan_price+price
                product_brand=input("enter the product brand name")
                if(product_brand=="usha"):
                   usha_fan_count=usha_fan_count+1
                   if(price>0):
                      usha_fan_price=usha_fan_price+price
                elif(product_brand=="crompton"):
                     crompton_fan_count=crompton_fan_count+1
                     if(price>0):
                        crompton_fan_count=crompton_fan_count+price
                elif(product_brand=="bajaj"):
                    bajaj_fan_count=bajaj_fan_count+1
                    if(price>0):
                       bajaj_fan_price=bajaj_fan_price+price
                elif(product_brand=="havells"):
                     havells_fan_count=havells_fan_count+1
                     if(price>0):
                        havells_fan_price=havells_fan_price+price

           elif(product=="fridge"):
               fridge_count=fridge_count+1
               if(price>0):
                 fridge_price=fridge_price+price
               product_brand=input("enter the product brand name")
               if(product_brand=="samsung"):
                  samsung_fridge_count=samsung_fridge_count+1
                  if(price>0):
                     samsung_fridge_price=samsung_fridge_price+price
               elif(product_brand=="lg"):
                   lg_fridge_count=lg_fridge_count+1
                   if(price>0):
                     lg_fridge_price=lg_fridge_price+price
               elif(product_brand=="whirlpool"):
                    whirlpool_fridge_count=whirlpool_fridge_count+1
                    if(price>0):
                       whirlpool_fridge_price=whirlpool_fridge_price+price
               elif(product_brand=="bluestar"):
                    bluestar_fridge_count=bluestar_fridge_count+1
                    if(price>0):
                       bluestar_fridge_price=bluestar_fridge_price+price



           elif (product=="washingmachine"):
               washing_machine_count=washing_machine_count+1
               if(price>0):
                 washing_machine_price=washing_machine_price+price
               product_brand=input("enter the product brand name")
               if(product_brand=="samsung"):
                  samsung_washing_machine_count=samsung_washing_machine_count+1
                  if(price>0):
                     samsung_washing_machine_price=samsung_washing_machine_price+price
               elif(product_brand=="lg"):
                    lg_washing_machine_count=lg_washing_machine_count+1
                    if(price>0):
                       whirlpool_washing_machine_price=whirlpool_washing_machine_price+price
               elif(product_brand=="whirlpool"):
                    whirlpool_washing_machine_count=whirlpool_washing_machine_count+1
                    if(price>0):
                       whirlpool_washing_machine_price=whirlpool_washing_machine_price+price
               elif(product_brand=="bluestar"):
                    bluestar_washing_machine_count=bluestar_washing_machine_count+1
                    if(price>0):
                       bluestar_washing_machine_price=bluestar_washing_machine_price+price
               elif(product_brand=="ifb"):
                    ifb_washing_machine_count=ifb_washing_machine_count+1
                    if(price>0):
                      ifb_washing_machine_price=ifb_washing_machine_price+price

    
    except ValueError:
        print('invalid input')
    


import mysql.connector
from datetime import date


connection = mysql.connector.connect(
    host="localhost",  
    user="root",
    password="hello",  
    database="daily_data"  
)

cursor = connection.cursor()


def insert_daily_data(daily_date,total_tv_count,total_tv_price,total_samsung_tv_count,total_samsung_tv_price,total_lg_tv_count,total_lg_tv_price,total_sony_tv_count,total_sony_tv_price,total_redmi_tv_count,total_redmi_tv_price,total_fan_count,total_fan_price,total_usha_fan_count,total_usha_fan_price,total_crompton_fan_count,total_crompton_fan_price,total_bajaj_fan_count,total_bajaj_fan_price,total_havells_fan_count,total_havells_fan_price,total_fridge_count,total_fridge_price,total_samsung_fridge_count,total_samsung_fridge_price,total_lg_fridge_count,total_lg_fridge_price,total_whirlpool_fridge_count,total_whirlpool_fridge_price,total_bluestar_fridge_count,total_bluestar_fridge_price,total_washing_machine_count,total_washing_machine_price,total_samsung_washing_machine_count,total_samsung_washing_machine_price,total_lg_washing_machine_count,total_lg_washing_machine_price,total_whirlpool_washing_machine_count,total_whirlpool_washing_machine_price,total_bluestar_washing_machine_count,total_bluestar_washing_machine_price,total_ifb_washing_machine_count,total_ifb_washing_machine_price):
    insert_query = "INSERT INTO total ( daily_date,tv_count,tv_price,samsung_tv_count,samsung_tv_price,lg_tv_count,lg_tv_price,sony_tv_count,sony_tv_price,redmi_tv_count,redmi_tv_price,fan_count,fan_price,usha_fan_count,usha_fan_price,crompton_fan_count,crompton_fan_price,bajaj_fan_count,bajaj_fan_price,havells_fan_count,havells_fan_price,fridge_count,fridge_price,samsung_fridge_count,samsung_fridge_price,lg_fridge_count,lg_fridge_price,whirlpool_fridge_count,whirlpool_fridge_price,bluestar_fridge_count,bluestar_fridge_price,washing_machine_count,washing_machine_price,samsung_washing_machine_count,samsung_washing_machine_price,lg_washing_machine_count,lg_washing_machine_price,whirlpool_washing_machine_count,whirlpool_washing_machine_price,bluestar_washing_machine_count,bluestar_washing_machine_price,ifb_washing_machine_count,ifb_washing_machine_price) VALUES (%s,%s, %s,%s,%s,%s,%s,%s,%s,%s,%s,%s, %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s, %s,%s,%s,%s,%s,%s,%s,%s,%s,%s, %s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    data = ( daily_date,main_tv_count,main_tv_price,main_samsung_tv_count,main_samsung_tv_price,main_lg_tv_count,main_lg_tv_price,main_sony_tv_count,main_sony_tv_price,main_redmi_tv_count,main_redmi_tv_price,main_fan_count,main_fan_price,main_usha_fan_count,main_usha_fan_price,main_crompton_fan_count,main_crompton_fan_price,main_bajaj_fan_count,main_bajaj_fan_price,main_havells_fan_count,main_havells_fan_price,main_fridge_count,main_fridge_price,main_samsung_fridge_count,main_samsung_fridge_price,main_lg_fridge_count,main_lg_fridge_price,main_whirlpool_fridge_count,main_whirlpool_fridge_price,main_bluestar_fridge_count,main_bluestar_fridge_price,main_washing_machine_count,main_washing_machine_price,main_samsung_washing_machine_count,main_samsung_washing_machine_price,main_lg_washing_machine_count,main_lg_washing_machine_price,main_whirlpool_washing_machine_count,main_whirlpool_washing_machine_price,main_bluestar_washing_machine_count,main_bluestar_washing_machine_price,main_ifb_washing_machine_count,main_ifb_washing_machine_price)
    
    cursor.execute(insert_query, data)
    connection.commit()
    


today_date=date.today()
main_tv_count = tv_count
main_tv_price = tv_price
main_samsung_tv_count = samsung_tv_count
main_samsung_tv_price = samsung_tv_price
main_lg_tv_count=lg_tv_count
main_lg_tv_price=lg_tv_price
main_sony_tv_count=sony_tv_count
main_sony_tv_price=sony_tv_price
main_redmi_tv_count=redmi_tv_count
main_redmi_tv_price=redmi_tv_price

main_fan_count=fan_count
main_fan_price=fan_price
main_usha_fan_count=usha_fan_count
main_usha_fan_price=usha_fan_price
main_crompton_fan_count=crompton_fan_count
main_crompton_fan_price=crompton_fan_price
main_bajaj_fan_count=bajaj_fan_count
main_bajaj_fan_price=bajaj_fan_price
main_havells_fan_count=havells_fan_count
main_havells_fan_price=havells_fan_price

main_fridge_count=fridge_count
main_fridge_price=fridge_price
main_samsung_fridge_count=samsung_fridge_count
main_samsung_fridge_price=samsung_fridge_price
main_lg_fridge_count=lg_fridge_count
main_lg_fridge_price=lg_fridge_price
main_whirlpool_fridge_count=whirlpool_fridge_count
main_whirlpool_fridge_price=whirlpool_fridge_price
main_bluestar_fridge_count=bluestar_fridge_count
main_bluestar_fridge_price=bluestar_fridge_price


main_washing_machine_count=washing_machine_count
main_washing_machine_price=washing_machine_price
main_samsung_washing_machine_count=samsung_washing_machine_count
main_samsung_washing_machine_price=samsung_washing_machine_price
main_lg_washing_machine_count=lg_washing_machine_count
main_lg_washing_machine_price=lg_washing_machine_price
main_whirlpool_washing_machine_count=whirlpool_washing_machine_count
main_whirlpool_washing_machine_price=whirlpool_washing_machine_price
main_bluestar_washing_machine_count=bluestar_washing_machine_count
main_bluestar_washing_machine_price=bluestar_washing_machine_price
main_ifb_washing_machine_count=ifb_washing_machine_count
main_ifb_washing_machine_price=ifb_washing_machine_price




insert_daily_data(today_date,main_tv_count,main_tv_price,main_samsung_tv_count,main_samsung_tv_price,main_lg_tv_count,main_lg_tv_price,main_sony_tv_count,main_sony_tv_price,main_redmi_tv_count,main_redmi_tv_price,main_fan_count,main_fan_price,main_usha_fan_count,main_usha_fan_price,main_crompton_fan_count,main_crompton_fan_price,main_bajaj_fan_count,main_bajaj_fan_price,main_havells_fan_count,main_havells_fan_price,main_fridge_count,main_fridge_price,main_samsung_fridge_count,main_samsung_fridge_price,main_lg_fridge_count,main_lg_fridge_price,main_whirlpool_fridge_count,main_whirlpool_fridge_price,main_bluestar_fridge_count,main_bluestar_fridge_price,main_washing_machine_count,main_washing_machine_price,main_samsung_washing_machine_count,main_samsung_washing_machine_price,main_lg_washing_machine_count,main_lg_washing_machine_price,main_whirlpool_washing_machine_count,main_whirlpool_washing_machine_price,main_bluestar_washing_machine_count,main_bluestar_washing_machine_price,main_ifb_washing_machine_count,main_ifb_washing_machine_price)


cursor.close()

connection.close()




                
x_axis = ['tv_count','tv_price','fan_count','fan_price','fridge_count','fridge_price','washing_machine_count','washing_machine_price']
y_axis_main = [tv_count,tv_price,fan_count,fan_price,fridge_count,fridge_price,washing_machine_count,washing_machine_price]

plt.bar(x_axis, y_axis_main)
plt.title("automatic analysis")
plt.xlabel("product and price")
plt.ylabel("values")
plt.show()

x_axis = ['samsung tv count','samsung tv price','LG tv count','lg tv price','sony tv count','sony tv price']
y_axis = [samsung_tv_count,samsung_tv_price,lg_tv_count,lg_tv_price,sony_tv_count,sony_tv_price]

plt.bar(x_axis, y_axis)
plt.title("automatic analysis")
plt.xlabel("brand and its price")
plt.ylabel("values")


plt.show()

x_axis = ['usha fan count','usha fan price','crompton fan count','crompton fan price','bajaj fan count','bajaj fan price','havells fan count','havells fan price']
y_axis = [usha_fan_count,usha_fan_price,crompton_fan_count,crompton_fan_price,bajaj_fan_count,bajaj_fan_price,havells_fan_count,havells_fan_price]

plt.bar(x_axis, y_axis)
plt.title("automatic analysis")
plt.xlabel("brand and its price")
plt.ylabel("values")


plt.show()

x_axis_main = ['samsung fridge count','samsung fridge price','LG fridge count','lg fridge price','whirlpool fridge count','whirlpool fridge price','bluestar fridge count','bluestar fridge price']
y_axis_main = [samsung_fridge_count,samsung_fridge_price,lg_fridge_count,lg_fridge_price,whirlpool_fridge_count,whirlpool_fridge_price,bluestar_fridge_count,bluestar_fridge_price]

plt.bar(x_axis, y_axis)
plt.title("automatic analysis")
plt.xlabel("brand and its price")
plt.ylabel("values")


plt.show()


x_axis = ['samsung_washing_machine_count','samsung_washing_machine_price','lg_washing_machine_count','lg_washing_machine_price','whirlpool_washing_machine_count','whirlpool_washing_machine_price','bluestar_washing_machine_count','bluestar_washing_machine_price','ifb_washing_machine_price','ifb_washing_machine_price']
y_axis = [samsung_washing_machine_count,samsung_washing_machine_price,lg_washing_machine_count,lg_washing_machine_price,whirlpool_fridge_count,whirlpool_fridge_price,bluestar_washing_machine_count,bluestar_washing_machine_price,ifb_washing_machine_price,ifb_washing_machine_price]

plt.bar(x_axis, y_axis)
plt.title("automatic analysis")
plt.xlabel("brand and its price")
plt.ylabel("values")


plt.show()





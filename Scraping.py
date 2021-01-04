#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 10:25:27 2020

@author: yefersontorresberru
"""

import time
from selenium import webdriver
import os
from pymongo import MongoClient 
try: 
    conn = MongoClient() 
    print("Connected successfully!!!") 
except:   
    print("Could not connect to MongoDB") 
  
# database 
db = conn.myDB
  
# Created or Switched to collection names: my_gfg_collection 
collection = db.data1
def leer(table):
    global carpeta,bandera
    json=[]
    cab=[]
    cont=[]
    cabi=[]
    listad=[]
    for item in table.find_elements_by_xpath(".//*[self::tr]"):
     try:   
      rows=item.find_elements_by_xpath(".//*[self::th]")
      if(len(rows)==1):
           cab1= item.find_element_by_xpath(".//*[self::th]").text
           if (len(cab1)>0):
            cab.append(cab1)
            cont1=item.find_element_by_xpath(".//*[self::td]").text
            cont.append(cont1)
      else:
          table2=item.find_element_by_id("rounded-corner")
          cab1= item.find_element_by_xpath(".//*[self::th]").text
          cab.append(cab1)
          for item1 in table2.find_elements_by_xpath(".//*[self::tr]"):
             try:
              d=[td.text for td in item1.find_elements_by_xpath(".//*[self::th]")]
              if(len(d)>0):
                cabi=d
             except Exception as e:
                 print(e)
             cont2=[td.text for td in item1.find_elements_by_xpath(".//*[self::td]")]
             if (len(cont2)>0):
              interno=dict(zip(cabi,cont2))
              listad.append(interno)
          cont.append(listad)
     except Exception as e:
          print(e)     
    json=dict(zip(cab, cont))
    return json
def leerProductos(table):
    global carpeta,bandera
    json=[]
    cabi=[]
    for item in table.find_elements_by_xpath(".//*[self::tr]"):
        d=[td.text for td in item.find_elements_by_xpath(".//*[self::th]")]
        if(len(d)>0):
            cabi=d
        cont2=[td.text for td in item.find_elements_by_xpath(".//*[self::td]")]
        if (len(cont2)>2):
            interno=dict(zip(cabi,cont2))
            json.append(interno)
    return json
def leerFechas(table):
    json=[]
    cab=[]
    cont=[]
    for item in table.find_elements_by_xpath(".//*[self::tr]"):
      cab1= item.find_element_by_xpath(".//*[self::th]").text
      cab.append(cab1.replace(".",""))
      cont1=item.find_element_by_xpath(".//*[self::td]").text
      cont.append(cont1)    
    json=dict(zip(cab, cont))
    return json
def leerParametros(table):
    json=[]
    cab=[]
    cont=[]
    for item in table.find_elements_by_xpath(".//*[self::tr]"):
      cab1= [td.text for td in item.find_elements_by_xpath(".//*[self::td]")]
      if(len(cab1)>0):
       cab.append(cab1[0])
       cont.append(cab1[2])
    json=dict(zip(cab, cont))
    return json
def leerPreguntas(table):
    json=[]
    cab1=[]
    cont=[]
    cab3=""
    for item in table.find_elements_by_xpath(".//*[self::tr]"):
     cab= [td.text for td in item.find_elements_by_class_name("tituloAzulPq")] 
     try:
      cab3=item.find_element_by_class_name("marcaRoja").text
      if(len(cab3)>0):
       cab1.append(cab3)
     except Exception as e:
         print("")
     cab2= [td.text for td in item.find_elements_by_xpath(".//*[self::p]")]
     interno=[]
     for d in cab:
       for i in cab2:
         e=i.find(d)
         if e >= 0:
             l=len(i)-len(d)
             stringpar=i[-l:]
             if(stringpar.find(":")>=0 and stringpar.find(":")<3):
              l=l-2
              stringpar=i[-l:]
             interno.append(stringpar)
     if(len(interno)>0):        
       cont.append(dict(zip(cab,interno)))
    json=dict(zip(cab1, cont))
    return json
def leerCriterios(tables):
    json=[]
    cab=[]
    cont=[]
    for table in tables:
     for item in table.find_elements_by_xpath(".//*[self::tr]"):
      cab1= [td.text for td in item.find_elements_by_xpath(".//*[self::td]")]
      if(len(cab1)>2):
       print(cab1)
       cab.append(cab1[0])
       cont.append(cab1[2])
    json=dict(zip(cab, cont))
    return json
def leeradj(tables):
    json=[]
    cab=[]
    cont=[]
    for table in tables:
     for item in table.find_elements_by_xpath(".//*[self::tr]"):
      cab1= [td.text for td in item.find_elements_by_xpath(".//*[self::td]")]
      if(len(cab1)>1):
       cab.append(cab1[0])
       cont.append(cab1[1])
    json=dict(zip(cab, cont))
    return json
def leerResumen(tables,con):
    json=[]
    interno=[]
    cab=[]
    cont=[]
    for table in tables:
     interno=[]
     if con>0:
      bandera=False
      for item in table.find_elements_by_xpath(".//*[self::tr]"):      
       if bandera==True:
        cont=[td.text for td in item.find_elements_by_xpath(".//*[self::td]")]
        json1=dict(zip(cab, cont))
        interno.append(json1)
       else:
        cab= [td.text for td in item.find_elements_by_xpath(".//*[self::td]")]
        bandera=True
      table="table"+str(con)
      test={table:interno}
     json.append(test)
     con=con+1
    return json

def tipoArchivo(table):
  for item in table.find_elements_by_xpath(".//*[self::th]"):
      ubicacion1=ubicacion+carpeta+"/"+item.text
      print(ubicacion1)
      try:
       os.mkdir(ubicacion1)
      except OSError as exc:
          print (exc)
      enable_download_headless(driver, ubicacion1)
def Archivo(table):
    json=""
    for item in table.find_elements_by_xpath(".//*[self::td]"):
      print(item.text)
    for item in table.find_elements_by_xpath(".//*[self::a]"):
      item.click()
    return json
# Printing the data inserted 
cursor = collection.find()
dfg=0
for record in cursor: 
  url=record['LINK']
  idrecord=record['_id']
  try:
   dff=record['parametros']
  except Exception as e:
   #print(e)
   dfg=dfg + 1
  if( dfg==1):
    print(url)
    dfg=0
    driver = webdriver.Chrome()
    driver.get(url)
    el1=driver.find_element_by_xpath('//button[text()="Aceptar"]')
    el1.click()
    carpeta=""
    bandera=False
    ubicacion="/Users/yefersontorresberru/Downloads/"
    time.sleep(1)
    try:
     el4=driver.find_element_by_link_text("Parámetros de Calificación")
     el4.click()
     time.sleep(1)
     table4= driver.find_element_by_id("rounded-corner")
     json4=leerParametros(table4)
     print(json4)
     doc4=collection.find_one_and_update({"_id":idrecord},{"$set":{'parametros':1}})
     doc4=collection.find_one_and_update({"_id":idrecord},{"$set":json4})
     print(json4)
    except Exception as e:
        print(e)
        
    driver.close()


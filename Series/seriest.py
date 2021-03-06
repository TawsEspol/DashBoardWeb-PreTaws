import pandas as pd
import numpy as np
import json
dataf=pd.read_csv( "/Users/User/Desktop/prueba/new.csv",sep=",")
ide=dataf.id_news;country=dataf.country ;tipos=dataf.cnn_prediction;dates=dataf.time;titles=dataf.title_trans;news=dataf.news
tipos_uni=tipos.unique() #tipos de noticias sin repetir
country_uni=country.unique()#paises sin repetir
#Extraccion de los años 
fechas=np.zeros((len(dates),), dtype=int)
for ind,fecha in enumerate(dates):
        año=fecha.split("-")[0]
        fechas[ind]=int(año)
dataf["fechas"]=fechas
#Años sin repetir#
fechasunicas=dataf.fechas.unique()

### Graficos de Serie de Tiempo ###



options= [{"text": "Crimen", "value": "crime"},{"text":"Política","value":"polit"},
{"text": "Corrupción", "value": "corrupt"},{"text":"Salud","value":"health"},
{"text": "Religion", "value": "religion"},{"text":"Educación","value":"educ"},
{"text": "Desempleo", "value": "unemploy"},{"text":"Economia","value":"economi"},
{"text":"Deportes","value":"sports"}]
for topics in options:
        d={}
        for paises in country_uni:
                if paises not in d:
                        d[paises]=[]
                for años in fechasunicas:
                        condi=(fechas==años) & (country==paises) & (tipos==topics['value'])
                        canti=fechas[condi].size     
                        d[paises].append(canti)
                        with open(topics["text"]+'.json','w') as f:
                             json.dump(d,f)
print(d)

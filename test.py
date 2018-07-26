import pandas as pd
from riotAPI import RiotAPI

file=open(__file__,"rb")
print(file.read(100))

riotAPI=RiotAPI("ka","br1","pt_BR")
champions=riotAPI.get_champions(language="pt_BR")

champions_dataframe=pd.DataFrame(champions.dict)
champions_info_dataframe=pd.DataFrame(list(champions_dataframe["info"]))
champions_dataframe=champions_dataframe.drop(columns="info")
champions_dataframe=champions_dataframe.join(champions_info_dataframe)
print(len(champions_dataframe.to_dict(orient="records")))

#champions_dataframe.to_csv("/run/media/Panda/4E226C68226C574D/Users/pandaQ/Documents/kaggle/champions_dataset.csv",index=False,index_label=False)
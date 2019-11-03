import os
import pandas as pd
from datetime import datetime
os.chdir("/Users/rameshbaskaran/Downloads/niftydata")
all_filenames=os.listdir()
cc = pd.concat([pd.read_csv(f,parse_dates=["Date"]) for f in all_filenames if f[0]=='d'])
cc.info()
cc.set_index("Date",inplace=True)
cc.sort_index(inplace=True)
print(cc)
cc.to_csv( "combined_csv.csv")

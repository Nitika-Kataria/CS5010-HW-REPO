import pandas as pd
import numpy as np

import project01.parser as parser

bfood = parser.FoodBrandObject("../dataset/FoodData_Central_csv_2020-10-30/branded_food.csv")
cornSyrup = bfood.run_on_df(parser.insert_index, "corn syrup", "ingredients")

cornSyrupIndex = cornSyrup[cornSyrup["corn_syrup_idx"] != -1]

del cornSyrupIndex["fdc_id"]
cornSyrupIndex = cornSyrupIndex.drop(cornSyrupIndex.loc[:, "gtin_upc":"discontinued_date"].columns, axis=1)

cornSyrupIndex = cornSyrupIndex.groupby(["brand_owner"]).sum()["corn_syrup_idx"]

print(cornSyrupIndex)

import pandas as pd
import random

import csv

# f = open(r"C:\Myname\Courses\Projects\MyProject\GeneratedCsvData\ingredient.csv",'r')
# ld = list(csv.DictReader(f))
# ld = list(filter(lambda i:i['ing_name'],ld))
ing =pd.read_csv(r"C:\Myname\Courses\Projects\MyProjec\GeneratedCsvData\ingredient.csv", index_col = False, skip_blank_lines = True)


ing_id = ing["ing_id"].dropna(how ="all").tolist()
ord = pd.read_csv(r"C:\Myname\Courses\Projects\MyProjec\GeneratedCsvData\Orders.csv", index_col = False, skip_blank_lines=True)
item_list = list(set(ord["sku"].dropna(how = all).tolist()))
recipe = []
for i in item_list:
    ing_needed = []
    ing_num= random.randint(1,4)
    for x in range(ing_num):
        ing_needed=random.choice(ing_id)
        quantity = random.randint(5,300)
        recipe.append([
        i,
        ing_needed,
        quantity
    ])


df = pd.DataFrame(recipe)

r = df.to_csv(r"C:\Myname\Courses\Projects\MyProjec\GeneratedCsvData\recipepython.csv")

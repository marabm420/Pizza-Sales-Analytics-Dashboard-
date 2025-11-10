import pandas as pd
from datetime import datetime, timedelta
import random
from faker import Faker

fake = Faker()
item_categories = ["Pizza - Margherita", "Pizza - Pepperoni", "Pizza - BBQ Chicken", "Pizza - Hawaiian",
    "Pizza - Meat Lovers", "Garlic Bread", "Calzone", "Mozzarella Sticks", "Pasta - Alfredo",
    "Pasta - Marinara", "Salad - Caesar", "Salad - Greek"]
size = ["small","medium","Large","regular"]

def generate_order(num_orders):
    orders = []
    base_date = datetime(2025,1,15,9,15)
    for i in range(1,num_orders):
        customer_name = fake.name()
        num_items = random.randint(1,4)
        address = fake.address().replace("/n",", ")
        created_at = base_date + timedelta(days = 25, hours= 5,minutes = random.randint(1,1000))
        # item_category = []
        # item_size = []
        # for x in range(num_items):
        #     item_category.append(random.choice(item_categories))
        #     item_size.append(random.choice(size))
        quantity = random.randint(1,3)
        unit_price = round(random.uniform(5,16),2)
        price = round(unit_price*quantity,2)
        for x in range(num_items):
            item_category = random.choice(item_categories)
            item_size = random.choice(size)
            orders.append([
                f"100{i}",
                customer_name,
                f"item00{i}",
                item_category,
                item_size,
                quantity,
                address,
                created_at.strftime("%Y-%m-%d %I:%M %p"),
                price
                ])
    return orders

order_data = generate_order(150)
columns = ["Order ID", "Customer Name","item_id", "Item Category", "Size", "Quantity", "Address", "Created At",
           "Price$"]
df = pd.DataFrame(order_data, columns=columns)

excelFile = r"C:\Myname\Courses\Projects\ProjectName\GeneratedCsvData\MyPizzaOrdersPython.xlsx"
df.to_excel(excelFile, index = False)

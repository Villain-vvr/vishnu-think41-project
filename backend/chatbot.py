import pandas as pd
import os

# Base directory of the chatbot.py file (inside backend/)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Data folder is inside backend/data
DATA_DIR = os.path.join(BASE_DIR, "data")

# Load the CSVs from backend/data
orders = pd.read_csv(os.path.join(DATA_DIR, "orders.csv"))
products = pd.read_csv(os.path.join(DATA_DIR, "products.csv"))
inventory = pd.read_csv(os.path.join(DATA_DIR, "inventory_items.csv"))
order_items = pd.read_csv(os.path.join(DATA_DIR, "order_items.csv"))

def handle_query(question: str) -> str:
    q = question.lower()

    if "top 5 most sold products" in q:
        top_products = order_items["product_id"].value_counts().head(5).index
        product_names = products[products["id"].isin(top_products)]["name"]
        return "Top 5 sold products:\n" + "\n".join(product_names)

    elif "status of order id" in q:
        order_id = ''.join(filter(str.isdigit, question))
        status = orders[orders["order_id"] == int(order_id)]["status"]
        return f"Status: {status.values[0]}" if not status.empty else "Order not found."

    elif "how many" in q and "in stock" in q:
        product_name = question.split("How many")[-1].split("are")[0].strip()
        in_stock = inventory[
            (inventory["product_name"].str.lower() == product_name.lower())
            & (inventory["sold_at"].isna())
        ]
        return f"{len(in_stock)} '{product_name}' left in stock."

    # 🧠 Simulated LLM response
    else:
        return (
            f"I'm a smart assistant, but I can't yet understand that question.\n"
            f"You asked: \"{question}\".\n"
            f"Try rephrasing or ask about products, orders, or stock."
        )

        




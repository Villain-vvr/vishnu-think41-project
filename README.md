# 🧠 Conversational AI Chatbot with FastAPI

A simple chatbot backend that answers supply chain-related queries like:
- Top 5 most sold products
- Order status by ID
- Remaining stock for a product

## 🚀 Features

- FastAPI-based backend
- Data from CSV (orders, inventory)
- Frontend chat UI (HTML + JS)
- Clean API design with `/query` endpoint

## 📦 Setup Instructions

```bash
git clone https://github.com/yourusername/vishnu-think41-project.git
cd vishnu-think41-project
pip install -r requirements.txt
uvicorn main:app --reload

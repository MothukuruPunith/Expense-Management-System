from fastapi import FastAPI,HTTPException
from datetime import date
from typing import List
from pydantic import BaseModel
import db_helper
from logging_setup import logging_set
app = FastAPI()
logger = logging_set('server')
class Expense(BaseModel):
    amount:float
    category:str
    notes:str
class Summary(BaseModel):
    start_date:date
    end_date:date
@app.get("/expenses/{expense_date}",response_model=List[Expense])
def get_expense_for_date(expense_date:date):
    logger.info('ok')
    expenses = db_helper.fetch_expenses_for_date(expense_date)
    return expenses

@app.post("/expenses/{expense_date}")
def add_or_update_expense(expense_date:date,expenses:List[Expense]):
    db_helper.delete_expenses_for_date(expense_date)
    for expense in expenses:
        db_helper.insert_expense(expense_date,expense.amount,expense.category,expense.notes)
    return {"message":"Successful bro"}

@app.post("/analytics")
def get_analytics(date_range:Summary):
    data = db_helper.fetch_expense_summary(date_range.start_date,date_range.end_date)
    # if data is None:
    #     raise HTTPException(status_code=500,detail="Failed to retrieve Summary")
    total = sum([row['total'] for row in data])
    breakdown={}
    for row in data:
        percentage = (row['total']/total)*100 if total != 0 else 0
        breakdown[row['category']]={
            "total":row['total'],
            "percentage":percentage
        }
    return breakdown

@app.get("/analytics_month")
def get_analytics_by_month():
    expenses = db_helper.fetch_summary_by_month()
    return expenses
from datetime import datetime
from typing import Tuple
#pydantic does data validation
from pydantic import BaseModel, EmailStr, PositiveFloat, PositiveInt, validator
from enum import Enum

class ProductEnum(str, Enum):
    product_category1 = "ZapFlow com Gemini"
    product_category2 = "ZapFlow com chatGPT"
    product_category3 = "ZapFlow com Llama3.0"

class Sales(BaseModel):
    email: EmailStr
    date_time: datetime
    value: PositiveFloat
    product_qty: PositiveInt
    product_category: ProductEnum

    @validator('date_time')
    def validate_date_interval(cls, v):
        # Set the allowed date range
        start_interval = datetime(2024, 9, 1) #01/09/2024
        end_interval = datetime(2025, 2, 26, 23, 59, 59) # 26/02/2025 até 23:59:59

        #Check if the date is within allowed date range
        if not (start_interval <= v <= end_interval):
            raise ValueError("The date of sale must be between 01/09/2024 and 26/02/2025")
        return v

    @validator('product_category')
    def category_must_be_in_enum(cls, v):
        return v
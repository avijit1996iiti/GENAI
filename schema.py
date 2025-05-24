from pydantic import BaseModel, Field
from typing import Optional


class ProductPriceResponse(BaseModel):
    product: str = Field(..., description="Name of the product")
    price_usd: int = Field(..., description="Price of the product in USD")
    source: Optional[str] = Field(None, description="Source of the price information")

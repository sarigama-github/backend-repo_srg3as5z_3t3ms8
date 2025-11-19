"""
Database Schemas

Define your MongoDB collection schemas here using Pydantic models.
These schemas are used for data validation in your application.

Each Pydantic model represents a collection in your database.
Model name is converted to lowercase for the collection name:
- User -> "user" collection
- Product -> "product" collection
- BlogPost -> "blogs" collection
"""

from pydantic import BaseModel, Field, EmailStr
from typing import Optional
from datetime import datetime

# Example schemas (retain examples, plus add our app-specific ones)

class User(BaseModel):
    """
    Users collection schema
    Collection name: "user" (lowercase of class name)
    """
    name: str = Field(..., description="Full name")
    email: str = Field(..., description="Email address")
    address: str = Field(..., description="Address")
    age: Optional[int] = Field(None, ge=0, le=120, description="Age in years")
    is_active: bool = Field(True, description="Whether user is active")

class Product(BaseModel):
    """
    Products collection schema
    Collection name: "product" (lowercase of class name)
    """
    title: str = Field(..., description="Product title")
    description: Optional[str] = Field(None, description="Product description")
    price: float = Field(..., ge=0, description="Price in dollars")
    category: str = Field(..., description="Product category")
    in_stock: bool = Field(True, description="Whether product is in stock")

# App-specific schemas for the salon website

class Appointment(BaseModel):
    """Hair salon appointment booking
    Collection name: "appointment"
    """
    name: str = Field(..., description="Customer full name")
    contact: str = Field(..., description="Phone number or email")
    service: str = Field(..., description="Requested service")
    appointment_time: datetime = Field(..., description="Desired date & time (ISO 8601)")
    notes: Optional[str] = Field(None, description="Optional notes")
    status: str = Field("pending", description="Booking status: pending, confirmed, cancelled")

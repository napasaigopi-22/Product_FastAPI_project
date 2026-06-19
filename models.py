# we are defining the products table a models which will be including of class and objects.
# we are defining the constructor for the class to make sure it works fine.

from pydantic import BaseModel

class product(BaseModel):
    item_no : int
    name : str
    price : float
    quantity : int
    Description : str
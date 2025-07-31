from fastapi import FastAPI,HTTPException
from pydantic import BaseModel

app = FastAPI(

    title="Practice API"
)

@app.get("/")
def productsone():
    return {"data": "products"}

@app.get("/shoes")
def shoes():
    return{
        "first":"sports",
        "second":"formal"
    }

@app.get("/gender")
def gender():
    return{"first":"male","second":"female"}

# DYNAMIC VALUES PASSING THROUGH ENPOINTS

@app.get("/details/{name}")
def details(name):
    return {"My name is :"+ name}

@app.get("/users/{name}/{age}/{location}")
def users(name:str,age:int,location:str):
    return {"name": name,
             "age":age,
             "location":location
           }

# DATA TYPE VALIDATION WHEN PASSING END POINTS

@app.get("/detail/{age}")
def detail(age:int):
        # return{age}
        return{f"I am {age} years old"}

# POST METHOD IN FASTAPI


class students(BaseModel):
    name:str
    age:int
    marks:int

@app.post("/student")
def new_students(student:students):
    return student

item=[
    {"name":"apple","price":100},
    {"name":"banana","price":200},
    {"name":"orange","price":300},
    {"name":"mango","price":400},
    {"name":"pineapple","price":500},
    {"name":"strawberry","price":600},
    {"name":"watermelon","price":700},
    {"name":"grapes","price":800},
]
class products(BaseModel):
    name:str
    price:int

@app.post("/products",status_code=201)
def create_new_products(pro:products):
    item_list={"name":pro.name,"price":pro.price}
    item.append(item_list)
    return {"Product created successfully"}

@app.get("/view_all_products")
def view_all_products():
    return item

@app.get("/view_filtered_products/{price}")
def view_filtered_products(price:int):
    for i in item:
        if(i["price"]==price):
            return i["name"]
    else:
        return {"No products found"}

# PUT METHOD IN FASTAPI

@app.put("/update_products/{pricing_value}")
def update_products(pro:products,pricing_value:int):
    for i in item:
        if (i["price"]== pricing_value):
             i["name"]=pro.name
             i["price"]=pro.price
             return {"product update successfully"}
        raise HTTPException(status_code=404,detail="Product not found")


# DELETE METHOD IN FASTAPI

@app.delete("/delete_products/{pricing_value}",status_code=204)
def delete_products(pricing_value:int):
    for i in item:
        if (i["price"]== pricing_value):
            item.remove(i)
            return {"product update successfully"}
        raise HTTPException(status_code=404,detail="Product not found")
    

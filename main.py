from datetime import datetime

from fastapi import FastAPI, Path, Query, Body, Header
from fastapi.encoders import jsonable_encoder
from pyexpat.errors import messages
from starlette import status

from starlette.responses import HTMLResponse, JSONResponse, Response, PlainTextResponse, RedirectResponse, FileResponse
from starlette.staticfiles import StaticFiles
from pydantic import BaseModel

from schemas.person_schemas import Person

app=FastAPI()
# @app.get("/")
# def root():
#     data = {"message": "Hello Aboba.COM"}
#     json_data = jsonable_encoder(data)
#     return JSONResponse(content=json_data)
#
# @app.get("/about")
# def get_about():
#     return {"message":"О сайте"}
# @app.get("/contact")
# def contact():
#     data="Вы попали на страницу контакты"
#     return Response(content=data,media_type="text/plain")
# @app.get("/text",response_class=PlainTextResponse)
# def root_text():
#     return "Lev Ban"
# @app.get("/users/admin")
# def get_admin():
#     return {"Hello":"Admin"}
# @app.get("/users")
# def get_admin(phone:str|None=Query(default=None,min_length=3,max_length=20)):
#     if phone==None:
#         return {"phone":"NONE"}
#     else:
#         return {"phone":phone}
# @app.get("/users/{name}")
# def get_user(name:str=Path(min_length=3,max_length=20),
#              age: int=Query(ge=18,lt=111)):
#     return {"user_name":name,"age_users":age }
#
# @app.get("/categories/{category_id}/products")
# def get_admin(category_id:int):
#     categories = [
#         {"id": 1, "name": "hleb"},
#         {"id": 2, "name": "eda"},
#         {"id": 3, "name": "voda"}
#     ]
#     return {
#         "category_id": category_id,
#         "categories": categories[category_id-1]
#     }
# @app.get("/notfound")
# def notfound():
#     return JSONResponse(content={"message": "Resource Not Found"}, status_code=404)
# products=[{"id":1,"name":"Product1","category":"Category1"},
#           {"id":2,"name":"Product2","category":"Category2"},
#           {"id":3,"name":"Product3","category":"Category3"}]
#
# @app.get("/products/{product_id}")
# def read_product(response: Response,product_id:int= Path()):
#     if product_id is None:
#         response.status_code = status.HTTP_200_OK
#         return {"products":products}
#     for product in products:
#         if product["id"] == product_id:
#             response.status_code = status.HTTP_200_OK
#             return {"product":product}
#     response.status_code = status.HTTP_404_NOT_FOUND
#     return {"product":"NOT FOUND"}

# @app.get("/")
# def new():
#     data="hello bro"
#     return Response(content=data,media_type="text/html",headers={"Secret-Code":"123456789"})
@app.get("/")
def root():
    now=datetime.now()
    response=JSONResponse(content={"message":"куки уств"})
    response.set_cookie(key="last_visit",value=now)


    return response



# @app.post("/hello")
# def hello(person: Person):
#     if person.age ==None:
#
#         return {"message":f"{person.name}"}
#     else:
#         return {"message":f"{person.name}{person.age}"}
# @app.post("/hello")
# def hello(person:Person):
#     return {"message":f"Hello,{person.name}!Company{person.company.name}"}


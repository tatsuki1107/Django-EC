# Django-EC

## ER diagram

![image](https://user-images.githubusercontent.com/79680980/210130353-713ed911-4148-485f-a407-effb3a9d8108.png)


## end point

### /api/create_user
・ body: {"user_name": str, "user_address": str}  
・ response: {"user_id": str}  
・ method: POST  
　　   
### /api/login
・ body: {"user_name": str, "user_address": str}  
・ response: {"user_id": str}  
・ method: POST  
  
### /api/register_company  
・ body: {"company_name": str}  
・ response: {"status": "ok"}  
・ method: POST  
  
### /api/register_item  
・ body: {"item_name": str, "item_type": str, "company_id": str, "price": int}  
・ response: {"status": "ok"}  
・ method: POST  

### /api/items
・ response: [{"item_id": str}]  
・ method: GET  
  
### /api/items/{item_id}
・ response: {"item_id": str, "item_name": str, "item_type": str, "company_id": str, "populality": int, "price": int}  
・ method: GET  
  
### /api/companies  
・ response: [{"company_id": str}]  
・ method: GET  
  
### /api/companies/{company_id}
・ response: {"company_id": str, "company_name": str, "populality": int}  
・ method: GET  
  
### /api/order
・ body: {"user_id": str, "item_id": str, "quantity": int}  
・ response: {"shiped_date": date}  
・ method: POST  
  
### /api/order_history  
・ body: {"user_id": str}  
・ response: [{"item_name": str, "order_date": date, "price": int, "quantity": int}]  
・ method: POST  
  
### /api/push_like
・ body: {"user_id": str, "item_id": str}  
・ response: {"status": "ok"}  
・ method: POST  
  
### /api/likes
・ body: {"user_id": str}  
・ response: [{"item_id": str}]  
・ method: POST  
  
### /api/delete_like
・ body: {"user_id": str, "item_id": str}  
・ response: {"status": "ok"}  
・ method: DELETE  
  
### /api/recommend_items
・ body: {"user_id": str}  
・ response: [{"item_id": str}]  
・ method: POST 


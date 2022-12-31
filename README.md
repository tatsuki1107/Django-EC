# Django-EC

## ER diagram

![image](https://user-images.githubusercontent.com/79680980/210130365-cd495393-def2-462b-95a1-721f697fd68f.png)



## end point

### /api/create_user
・ body: {"user_name": str, "user_address": str}  
・ response: {"user_id": int}  
・ method: POST  
　　   
### /api/login
・ body: {"user_name": str, "user_address": str}  
・ response: {"user_id": int}  
・ method: POST  

### /api/delete_user  
・ body: {"user_id": int}  
・ response: {"status": "ok"}  
・ method: DELETE  

### /api/register_company  
・ body: {"company_name": str}  
・ response: {"status": "ok"}  
・ method: POST  
  
### /api/delete_company  
・ body: {"company_id": int}  
・ response: {"status": "ok"}  
・ method: DELETE  
  
### /api/register_item  
・ body: {"item_name": str, "item_type": str, "company_id": str, "price": int}  
・ response: {"status": "ok"}  
・ method: POST  

### /api/delete_item  
・ body: {"item_id": int}  
・ response: {"status": "ok"}  
・ method: DELETE  

### /api/items
・ response: [{"item_id": int}]  
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


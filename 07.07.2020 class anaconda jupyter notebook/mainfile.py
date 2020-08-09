import sys
sys.path.insert(1,"D:\\sql files\\") #1= absolute path, complete path

import select_products
import select_product
from insert_product import insert
import update_product
import delete_product

def menu():
    print("=======MENU======")
    print("1. Add Product")
    print("2. Update Product")
    print("3. Delete Product")
    print("4. Display Products")
    print("5. Display Product By Id")

    ch=int(input("Enter your choice"))

    if(ch==1):
        insert()
    elif(ch==2):
        update_product.update()
    elif(ch==3):
        delete_product.delete()
    elif(ch==4):
        select_products.selectproducts()
    elif(ch==5):
        select_product.selectproductsbyid()
    else:
        print("Invalid option!!!")


    c=input("Do you want to continue with this app?").lower()
    if(c=="yes"):
        menu()


menu()  
        

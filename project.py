restaurent=["food plaza"]
food_list=["pizza","burger","pasta","chicken","motton","chicken biryani"]
price=["80","120","100","90","200","150"]
cart=[]
sales=[]
orders=[]
password=1234
while True:
    print('='*25)
    print("1.Admin")
    print("2.User")
    print("3.Exit")
    ch=int(input('enter for choice:'))
    if ch==1:
        pin=int(input('enter your pin:'))
        if password==pin:
            print('successfully admin login')
            while True:
                print('='*25)
                print("1.dashboard")
                print("2.manage restaurent")
                print("3.manage food items")
                print("4.view orders")
                print("5.manage users")
                print("6.reports")
                print("7.logout")
            

                choice=int(input('enter your choice:'))
                if choice==1:
                    print('orders is',orders)
                elif choice==2:
                    print('manage restaurent:')
                    print("1.add")
                    print("2.update")
                    print("3.remove")
                    print("4.exit")
                    choose=int(input('you choose:'))
                    if choose==1:
                        name=input('enter a restaurent name')
                        if name in restaurent:
                            print('restaurent is already existed')
                        else:
                            restaurent.append(name)
                            print('sucessfully added to restarunt')
                    elif choose==2:
                        new_restaurent="food_court"
                        old_restaurent="food plaza"
                        res=restaurent.index(old_restaurent)
                        restaurent[res]=new_restaurent
                        print(restaurent)
                    elif choose==3:
                        res=restaurent.remove('food plaza')
                        print(res)
                    else:
                        choose==4
                        print('4.exit')
                elif choice==3:
                    print('manage food items:')
                    food_list.append('ice cream')
                    food_list.remove('pasta')
                    print('food_list',food_list)
                elif choice==4:
                    print('view orders',orders)
                elif choice==5:
                    print('manage customers and riders')
                elif choice==6:
                    print('sales,orders,analysics')
                elif choice==7:
                    print('logout')
                    print('thank you visit again')
                    break
                else:
                    print('you are not admin:')
                    break
               
    elif ch==2:
        while True:
            print('='*25)
            print("1.browse restaurent")
            print("2.view menu")
            print("3.add to cart")
            print("4.place order")
            print("5.track order")
            print("6.order history")
            print("7.logout")
            
            choices = int(input('enter choice: '))
            
            if choices == 1:
                print('restaurent:', restaurent)
                
            elif choices == 2:
                print('--- Menu ---')
                for i in range(len(food_list)):
                    print(f"{food_list[i]} - {price[i]}")
                    
            elif choices == 3:
                food = input('enter food name: ')
                if food in food_list:
                    print('food is available')
                    addcart = input('add to cart (yes/no): ')
                    
                    if addcart == 'yes':
                        cart.append(food)
                        print(f'{food} added to cart')
                    else:
                        print('food is not added to cart')
                else:
                    print('food is not available')
                    
            elif choices == 4:
                if not cart:
                    print('cart is empty! add items first.')
                else:
                    details = input('enter details (address/name): ')
                    phone_no = int(input('enter number: '))
                    orders.append(cart.copy())
                    sales.extend(cart.copy())
                    cart.clear()
                    print('='*45)
                    print('          food bill            ')
                    print('='*45)
                    print(f"customer name/address:{details}")
                    print(f"phone number:{phone_no}")
                    print('=' * 45)
                    print(f"{'item name':<20}{'price':>15}")
                    print('=' * 45)

                    
            elif choices == 5:
                print('your order is:', orders)
                print('your details:', details, phone_no)
                
            elif choices == 6:
                print('order history:')
                for o in orders:
                    print(o)
                    
            elif choices == 7:
                print('successfully logout')
                break
            
            else:
                print('invalid choice')

    
    elif ch == 3:
        print('exit')
        break
    else:
        print('invalid option, please try again')

            
                              

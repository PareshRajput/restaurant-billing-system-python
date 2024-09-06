dishname={1:"Poha",2:"Samosa",3:"Tea",4:"VadaPav",5:"Idali",6:"Coffe",7:"PaniPuri",8:"Dosa"}
dishprice={1:20,2:15,3:12,4:15,5:30,6:25,7:34,8:55}
itemkey=[]
q=[]
final_price=0
"""
itemkey[i]= when we pass the dishnamae
dishname[itemkey[i]] =
"""
print("_"*80)
print(f"{" "*30} Taj Hotel")
print("_"*80)
while True:
    print(f""" 
                Menu
        1.Poha          2.Samosa
        3.Tea           4.VadaPav
        5.Idali         6.Coffe
        7.PaniPuri      8.Dosa
    {'-'*70}
        """)
    itemname=eval(input("Enter The Your Choice :- "))
    qunt=eval(input("Enter The Quantity :- "))
    itemkey.append(itemname)
    q.append(qunt)
    # print(itemkey)
    # print(q)
    ch=input("Do You Wnat To Continue(y/n) :").lower()
    if ch=='n':
        print("-"*90)
        print("|{:^20}|{:^20}|{:^20}|{:^20}|".format("ItemName","Quantity","Price","Amount"))
        # :^20   it is used for space in center 
        print("-"*90)
        
        for i in range(len(itemkey)):
                    print("-"*90)
                    print("|{:^20}|{:^20}|{:^20}|{:^20}|".format(dishname[itemkey[i]],q[i],dishprice[itemkey[i]],q[i]*dishprice[itemkey[i]]))
                    # :^20   it is used for space in center 
                    print("-"*90)
                    
                    final_price=final_price+q[i]*dishprice[itemkey[i]]    
        break
print("-"*85)   
print(f"Final Price : -\t\t\t\t\t\t\t\t{final_price}\n" )
print("-"*85)   

print("Thank You ! ... Visit Again ... !")



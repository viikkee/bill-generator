dtr={1:"Cooking Oil",2:"Rice",3:"Dal",4:"Sugar",5:"Aata",6:"Turmeric",7:"Coffee",8:"Tea",9:"Dry Fruits Mix",10:"Green Peas"}
p={1:120,2:60,3:100,4:45,5:40,6:200,7:2500,8:155,9:850,10:120}
f=list(dtr.keys())
de={}
lst_it=[]
amt=[]
print("*"*30)
print("\tLIST OF ITEMS AND PRISE")
print("*"*30)
print("""\t1 Cooking Oil    ₹120/litre
    2 Rice  	     ₹60/kg
    3 Dal	         ₹100/kg
    4 Sugar	         ₹45/kgl
    5 Aata	         ₹40/kg
    6 Turmeric	     ₹200/kg
    7 Coffee	     ₹2500/kg
    8 Tea	         ₹155/kg
    9 Dry Fruits Mix ₹850/kg
    10 Green Peas	 ₹120/kg
    11 Exit""")
print("*"*30)
while(True):
    ite=input("which item u need :")
    if(ite=="" or ite.isalpha() or ite.isspace()):
        print("Invalid opction")
        continue
    if(int(ite)==1):
        quan=input("kg :")
        de[dtr.get(1)]=p.get(1)
        amt.append(p.get(1)*int(quan))
        continue
    elif(int(ite)==2):
        quan=input("kg :")
        de[dtr.get(2)]=p.get(2)
        amt.append(p.get(1)*int(quan))
        continue
    elif(int(ite)==3):
        quan=input("kg :")
        de[dtr.get(3)]=p.get(3)
        amt.append(p.get(1)*int(quan))
        continue
    elif(int(ite)==4):
        quan=input("kg :")
        de[dtr.get(4)]=p.get(4)
        amt.append(p.get(1)*int(quan))
        continue
    elif(int(ite)==5):
        quan=input("kg :")
        de[dtr.get(5)]=p.get(5)
        amt.append(p.get(1)*int(quan))
        continue
    elif(int(ite)==6):
        quan=input("kg :")
        de[dtr.get(6)]=p.get(6)
        amt.append(p.get(1)*int(quan))
        continue
    elif(int(ite)==7):
        quan=input("kg :")
        de[dtr.get(7)]=p.get(7)
        amt.append(p.get(1)*int(quan))
        continue
    elif(int(ite)==8):
        quan=input("kg :")
        de[dtr.get(8)]=p.get(8)
        amt.append(p.get(1)*int(quan))
        continue
    elif(int(ite)==9):
        quan=input("kg :")
        de[dtr.get(9)]=p.get(9)
        amt.append(p.get(1)*int(quan))
        continue
    elif(int(ite)==10):
        quan=input("kg :")
        de[dtr.get(10)]=p.get(10)
        amt.append(p.get(1)*int(quan))
        continue
    else:
        if(int(ite)==11):break
    print(de)
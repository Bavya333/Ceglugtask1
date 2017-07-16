import csv
class billsys:
	def display(self):
		f=open('product.csv',"rb")
		reader=csv.reader(f)
		pdt=list(reader)
		head=0
		rno=0
		for i in pdt:
		        if rno==0:
		        	head=i
			cno=0
			for j in i:
        	        	if rno != 0:	  		
					print '%s:%s'%(head[cno],i[cno])
				cno+=1
		  	rno+=1
		f.close()
	def add(self):
		f=open('product.csv',"a")
		print("Enter the item info...")
		line=[]
		name=0        
 		for i in range(5):
			name=raw_input() 
   			line=line+[name]
		writer=csv.writer(f)
		writer.writerow(line)
		f.close()

	def categ_search(self):
		f=open('product.csv',"rb")
		reader=csv.reader(f)
	        pdt=list(reader)
		head=0
		rno=0
		print("Enter the category to be searched:")
		cat=raw_input()
		for i in pdt:
		        if rno==0:
		        	head=i
			cno=0
			for j in i:
	                	if rno != 0 and i[0]==cat:
					print '%s:%s'%(head[cno],i[cno])
				cno+=1
		  	rno+=1
		f.close()
		
	def item_search(self):
		f=open('product.csv',"rb")
		reader=csv.reader(f)
	        pdt=list(reader)
		head=0
		rno=0
		print("Enter the item to be searched:")
		cat=raw_input()
		for i in pdt:
		        if rno==0:
		        	head=i
			cno=0
			for j in i:
	                	if rno != 0 and i[2]==cat:
					print '%s:%s'%(head[cno],i[cno])
				cno+=1
		  	rno+=1
		f.close()
	
	def update(self):
		print("Enter the item name:")
		it=0;
		it=raw_input()
		print("Enter the item for price and quantity update using csv:")
	      	with open('product.csv') as f1:
			reader=csv.reader(f1.readlines())
		reader=list(reader)
		with open('product.csv','w') as f2:
			writer=csv.writer(f2)
			for line in reader:
				if line[2]==it:
					l=[]
					name=0
					for i in range(5):
						name=raw_input()
						l=l+[name]
					writer.writerow(l)			
				else:
					writer.writerow(line)
		
		
	
	def billing(self):
		
			print("Enter 1 to continue billing...0 to exit")
			a=raw_input()
			dicts=[]	
			while int(a)==1:
				with open("product.csv","rb") as f:
					reader=csv.reader(f)
					pdt=list(reader)
					head=0
					rno=0
					mydict=[]
					print("Enter the item to be searched:")
					item=raw_input()
					for i in pdt:
					        if rno==0:
					        	head=i
						cno=0
						for j in i:
	        			        	if rno != 0 and i[2]==item:
								mydict=mydict+[{head[cno]:i[cno]}] 				
								cno+=1
					  	rno+=1	
					dicts=dicts+[mydict]
					print("Enter 1 to continue billing...0 to exit")
					a=raw_input()
			Total=0
			for i in dicts:
				Amount=0
				print("Enter the quantity for "+str(i[2]))
				n=raw_input()
				i[3]['Qty']=n
				Amount=int(i[3]['Qty'])*int(i[4]['Price'])
				Total+=Amount
			print(dicts)
			print("Total="+str(Total))
			
				
	
	
	def delete(self):
		with open("product.csv","rb") as f1:
			reader=csv.reader(f1)
		  	reader=list(reader)	
			with open("product.csv","wb") as f2:
				writer=csv.writer(f2)
				print("Enter the item to be deleted:")
				item=raw_input()
				for row in reader:
					if row[2]!=item:
						writer.writerow(row)
	
a=billsys()
print("Menu...1.Display.2.Add.3.Update.4.Item Search.5.Category Search.6.Delete.7.Billing.0.Exit...")
c=raw_input()
c=int(c)
while c!=0:
	if c==1:
		a.display()
	elif c==2:
		a.add()
	elif c==3:
		a.update()
	elif c==4:
		a.item_search()
	elif c==5:
		a.categ_search()
	elif c==6:
		a.delete()
	elif c==7:
		a.billing()
	else:
		print("Invalid input")
        print("Enter your choice...")
	c=raw_input()
	c=int(c)

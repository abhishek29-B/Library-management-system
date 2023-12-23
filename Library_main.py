'''
Library Management system
Copyrights abhishek
Abhishek B
AI/ML developer
github link:https://github.com/abhishek29-B
linkedin: https://www.linkedin.com/in/abhishek-b-abhi-472052220
'''

class Library:
    def __init__(self,book,lender_data):
        self.books=book
        self.lender=lender_data

        
    def show(self):
        try:
            show_status=input('''If you want to Show all books : Enter as a 'book'\nIf you want to Show all Lender details : Enter as a 'lend'\n''')
            if show_status=='book':
                print('********************** Show all the Books *************************')
                iter_data_is=self.books.items()
            elif show_status=='lend':
                print('********************** Show all the Lender *************************')
                iter_data_is=self.lender.items()
            for (k,v) in  (iter_data_is):
                for i in (v):
                    print(i,' : ',v[i])
                print('\n====================================')
                
        except TypeError:
            print("Enter the Valid data 'book' or 'lend'\n")
        except Exception as e:
            print(e)

         
     #Add book to Dict       
    def add_book(self):
        try:
            self.book_name=input('Enter a Book Name : ')

            self.book_price=int(input('Enter a Book Price : '))
            
            self.book_auth=input('Enter a Book Author name : ')
            print(self.book_name,self.book_price,self.book_auth)
            self.books.update({len(self.books):{'name':self.book_name,'price':self.book_price,'Author':self.book_auth}})
            print('The {self.book_name} is Added')
        except Exception as e:
            print(e)
            
        
    def lend_book(self,ids):
        user_status=input('If you lend Book: Enter Lend\nReturn the Book: Enter Return\n')
        try:
            if user_status=='Lend':
                print('=====================The Book is Lended===================')
                status=True
            elif user_status=='Return':
                print("======================The Book is Return==================")
                status=None
            for (lk,lv) in  (self.lender.items()):
                if ids == lv['ids']:
                    lendId=lv['ids']
                    self.status_data=lv
                    break
                else:
                    lendId=False
            if lendId:
                bookId=int(input("Enter The Book Id : "))
                print("Status : ",self.books[bookId])
                self.status_data['book']=status
                print("Status : ",self.status_data)

        except TypeError:
            print('This is the type Error')
        except:
            print('Invalid')
        

                
            

if __name__=='__main__':
    print('++++++++++++++++++++ Library Management sytem +++++++++++++++++++++\n')
    
    book={
        0:{'name':'Python','price':200,'Author':'Guido van Rossum'},
        1:{'name':'java','price':150,'Author':'James Gosling'}
        }
    lender_data={
        0:{'ids':1000,'Name':'abcd','book':None},
        1:{'ids':1001,'Name':'efgh','book':None}
        }
    obj1=Library(book,lender_data)

    while True:
        print('==========User Guide Line==================\n')
        print('''Show the all Books : 1\nAdd Books :\t2\nLend a Books :\t3\nExit :\t\t4''')
        user_input=int(input('\nEnter a number for display the window : \n'))
        
        if user_input==1:
            print('========================== Show the Details ===================\n')
            obj1.show()
        elif user_input==2:
            print('========================== Add New Books ===================\n')
            obj1.add_book()
        elif user_input==3:
            print('========================== Lend Books ===================\n')
            ids=int(input('\nEnter a Lender Id : \n'))
            obj1.lend_book(ids)
        elif user_input==4:
            print('Thank you for visit Abhisek Library\nCome again...!')
            exit()





            


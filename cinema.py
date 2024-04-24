class Star_Cinema:
    hall_list = []
    def entry_hall(self,hall):
        Star_Cinema.hall_list.append(hall)
class Hall(Star_Cinema):
    def __init__(self,rows,cols,hall_no) -> None:
        self.seats = {}
        self.show_list =[]
        self.__rows = rows
        self.cols = cols
        self.hall_no = hall_no
        self.entry_hall(self)
    def entry_show(self,id,movie_name,time):
        
        tu_le = (id,movie_name,time)
        self.show_list.append(tu_le)
        seatAvailable=[]
        for row in range(self.__rows):
            rowInfo=[]
            for x in range(self.cols):
                   rowInfo.append(0)
            seatAvailable.append(rowInfo)
        self.seats[id] = seatAvailable
    def book_seats(self,id,listt):
        # print(listt)
        for key,values in self.seats.items():
            # print(values)
            if  id ==key:   
                if values[listt[0]][listt[1]]==1:
                    print("Seat are Already booked")
                    return
                else:
                    print("Seat booked Succesfully!!")
                    values[listt[0]][listt[1]] = 1
                    return
            else :
                print("Invalid")
                return       
    def view_show_list(self):
       for view in self.show_list:
           print(view)   
    def view_available_seats(self,id):
        for key,value in self.seats.items():
                # print(key,value)
                if id  != key:
                    print("Invalid ID")
                    return                  
                else :
                    for x in value:
                        print(x)
                    return
hall1 = Hall(5,5,121)
hall1.entry_show(111,'Jawan Maji(111)','25/10/2023 11.00 AM')
hall1.entry_show(333,'Sujon Maji(333)','25/10/2023 2.00 PM')
run = True
while run:
    print("----------Welcome to Our Cinema Hall---------")
    print('1.\tView all show today')
    print('2.\tView available seats')
    print('3.\tBook Ticket')
    print('4.\tExit')
    option = int(input("Enter Options: "))
    if(option==1):
        hall1.view_show_list()
        print('-----------------------------------------------------')    
    elif(option==2):
        id = int(input('Enter Show Id: '))
        hall1.view_available_seats(id)
    elif(option==3):
        id = int(input("Enter Id:"))
        rows = int(input("Enter rows: "))
        cols = int(input("Enter Cols: "))
        listt = (rows,cols)
        A = hall1.book_seats(id,listt)
    elif option==4:
        break
    
        
        







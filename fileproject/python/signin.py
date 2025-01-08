users={}
def status_user():
    while True:
        status=input('Are you member Y/N : ')
        if status.upper()=='Y':
            login()
            break
        elif status.upper()=='N':
            signin()
            break
        else:
            print("Enter only Y or N")

def login():
    while True:
        try:
            name=input('Username :')
            password=int(input('Password :'))
            if name in users:
                while users[name]!=password:
                    password=int(input('Password :'))
                print('Login Successful')
                break
            else:
                i=0
                while i<=3:
                    i+=1
                    print('Member information not found.')
                    if i>3:
                        signin()
                        break
                    name=input('Username :')
                    if name in users:
                        while users[name]!=password:
                            password=int(input('Password :'))
                        print('Login Successful.')
                        break
            break
                    
        except:
            print('Please enter password to number only.')

def signin():
    createID=input('Create username :')
    if createID in users:
        print('ID online.')
    else:
        while True:
            try:
                createpassword=int(input('Create Password :'))
                confirm=int(input('Confirm Password :'))
                while confirm!=createpassword:
                    print('Password do not match.')
                    createpassword=int(input('Create Password :'))
                    confirm=int(input('Confirm Password :'))
                break
            except:
                print('Please set password to number only.')
        users[createID]=createpassword
        print('Successful account creation.')
        login()





    


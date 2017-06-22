from spy_details import spy,friends,chatmessage
from datetime import datetime
from steganography.steganography import Steganography


print 'Welcome to SpyChat Application'

#Existed Status
status=['Busy','Urgent Calls Only']


# function to add status
def add_status(current_status):

    updated_status=None

    if current_status!=None:
        print'Your current status is %s'%(current_status)
    else:
        print'You don\'t have any current status'


    status_selection=raw_input("Do you want to update your status or use the existed statuses y/n?\n")
    if status_selection.upper()=="Y":
        new_status=raw_input("what is your new status?")

        if len(new_status)>0:
            print 'your updated status is %s'%(new_status)
            status.append(new_status)
            updated_status=new_status
        else:
            print 'Please enter valid status'

    elif status_selection.upper()=="N":
        print 'your older status are as following:-'
        item_number=1
        for message in status:
            print '%d = %s'%(item_number,message)
            item_number=item_number+1

        item_number_selection=int(raw_input("Select your message by providing the required item number\n"))
        if len(status)>=item_number_selection:
            print 'your selected message is %s'%(status[item_number_selection-1])
            updated_status=status[item_number_selection-1]
        else:
            print 'entered number is invalid'

    return updated_status

#Function to add new friend
def add_friend():
    new_friend={
        'name':"",
        'salutation':"",
        'age':0,
        'rating':0.0,
        'chats':[]
    }
    print 'Please provide the details of your new friend'
    new_friend['name']=raw_input("What is the name of your friend?\n")
    new_friend['salutation'] = raw_input("what should i call your friend Mr. or Ms.\n")
    new_friend['age']=int(raw_input("Enter age of your friend\n"))
    new_friend['rating']=float(raw_input("Rating of your friend\n"))


    if (len(new_friend['name']) > 0) and (new_friend['age'] > 12) and (new_friend['rating'] >= spy['rating']):
        friends.append(new_friend)
        print'Friend Added'
    else:
        print "Entered friend\'s details are invalid"


    return len(friends)


#function to select a particular friend
def friend_selection():
    item_number=0
    for friend in friends:
        print " %d)name: %s %s  age:%d  rating:%.2f" %(item_number+1,friend['salutation'],\
                                                       friend['name'],friend['age'],friend['rating'])
        item_number=item_number+1
    selection_number=int(raw_input("which friend you want to select\n"))
    selected_friend_position=selection_number-1
    return selected_friend_position


#function for sending message to a  selected friend
def send_message():

    friend_choice = friend_selection()

    original_image = raw_input('What is the name of image? \n >')
    output_path = 'fidel.jpg'
    text = raw_input('what do you want to encode \n >')
    Steganography.encode(original_image, output_path, text)

    new_chat = chatmessage(text, True)

    friends[friend_choice]['chats'].append(new_chat)
    print'Your secret image is ready!'


# function for reading message from selected friend
def read_message():

    sender = friend_selection()
    output_path = raw_input("What's the name of file?")
    secret_text = Steganography.decode(output_path)

    new_chat = chatmessage(secret_text,False)

    friends[sender]['chats'].append(new_chat)
    print'your secret image has been saved'









def start_chat(spy_name,spy_age,spy_rating):
    current_status=None


    if spy_age>12 and spy_age<50 and len(spy_name)>0:
        spy_name = spy['salutation'] + " " + spy_name
        print "Based on Your Rating"
        if spy_rating>4.5:
            print 'Great ace!'
        elif spy_rating > 3.5 and spy_rating <= 4.5:
            print 'You are one of the good ones.'
        elif spy_rating >= 2.5 and spy_rating <= 3.5:
            print 'You can always do better'
        else:
            print 'We can always use somebody to help in the office.'


        print 'Sucessfully Authenticated Welcome %s aged %d and rating of %.2f to SpyChat'%(spy_name,spy_age,spy_rating)
        flag=True
        while flag:
             choice=raw_input("Choose from the following option\n 1. Add a status \n 2. Add a friend \n "
                              "3. Send a secret message \n 4. Read a secret message\n 5.Close Application")
             choice=int(choice)
             if choice==1:
                current_status=add_status(current_status)
                print 'your current status is %s '%(current_status)
             elif choice==2:
                number_of_friends=add_friend()
                print "Total number of Friends in your list are %d"%(number_of_friends)
             elif choice==3:
                send_message()
             elif choice==4:
                read_message()
             else:
                flag=False


    else:
        print "Entered Data is  invalid"




existing=raw_input("Want to continue as a default user Y/N? ")
#user wants to work as a default user
if existing.upper()=='Y':
    start_chat(spy['name'],spy['age'],spy['rating'])

#if user wants to create a new profile
else:
    spy={
        'name':"",
        'salutation':"",
        'age':0,
        'rating':0.0,
        'is_online':False

    }
    spy['name'] = raw_input("What is your name? ")

    spy['salutation'] = raw_input("what should i call you?")

    spy['age'] = int(raw_input("What is your age?"))

    spy['rating'] = float(raw_input("What is your spy rating?"))

    spy_is_online = True

    start_chat(spy['name'], spy['age'], spy['rating'])

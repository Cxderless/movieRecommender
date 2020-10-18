#-----------------------------IMPORTS-----------------------------------#
from tkinter import *           # Importing the tkinter module for a GUI
import datetime                 # Importing the datetime module 
from datetime import timedelta  # Import timedelta from the datetime module

#-----------------------------FUNCTIONS------------------------------------#

#----------A Error message---------#

def Error(string):              # Making a function which excepts a string
    Error = Tk()                # Making a new window called Error
    Error.title("Error")        # Calling the new window Error
    Error.config(background = "#ccdeff")                                            # Making the window background #ccdeff/light blue
    Label(Error, text = string, fg = "red", bg = "#ccdeff").grid()                  # Making a label which outputs the string that is sent to the Error, and make the text red and placing it on the GUI window
    Button(Error, text = "return", command =lambda:close(Error)).grid(sticky = W)   # Making a button called return that runs the close function

def close(window):
    window.destroy()
#----Recommend Window-----Part 1-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
    
def recommendor(old, username): # Creating a new function called recommendor which recieves a tkinter and a username
    movies = [line.rstrip('\n') for line in open("lists.txt")]      # Opening a the lists text file and splitting it into a list at every new line
    profile = [line.rstrip('\n') for line in open(username+".txt")] # Opening the text file for the username given and split into a list at every new line
    odds = []                                                       # Creating a empty list called odds
    directors_disliked =[]                                          # Creating a empty list called directors_disliked
    for i in range(len(profile[8].split())):                        # Making a for loop that runs for the length of the list in the 8th place in the the username text file
        if i ==0:                                                   # A conditional which checks if i is 0 
            mov_data = [line.rstrip('\n') for line in open(username+" "+profile[8].split(",")[i]+".txt")]   # Opening a file that is made for each user and making it a list
        else:                                                                                               # The second part of the conditional that runs if i isn't 0
            mov_data = [line.rstrip('\n') for line in open(profile[8].split(",")[i]+".txt")]                # Opening the a text file that is already made before 
        directors_disliked.append(mov_data[3])          # This adds the director of the movie text file opened 
    today = datetime.datetime.now()                     # Use the datetime module to get the current time of the PC running the program
    profile4 = [profile[4].split()[0].split("-")[0], profile[4].split()[0].split("-")[1],profile[4].split()[0].split("-")[2]]   # Getting the users Dob
    profile4 = datetime.datetime(int(profile4[0]),int(profile4[1]),int(profile4[2]))                                            # Make a datetime var from the date of birth entered by the use
    age = int(int((today-profile4).total_seconds())/60/60/24/365)                                                               # Working out their age to the lowest year
    for i in range(len(movies)):                                            # A for loop which runs for the length of the all the movies in the lists.txt file
        mov_data = [line.rstrip('\n') for line in open(movies[i]+".txt")]   # Opening the movie text file and splits it into a list at every new line
        if  mov_data[4] == "R":                                             # A conditional which checks wether the age rating of the movie is R
            age_rating = 17                                                 # Setting the variable age_rating to 17
        elif mov_data[4] == "PG":
            age_rating = 8
        elif mov_data[4] == "PG-13":
            age_rating = 13
        elif mov_data[4] == "-":
            age_rating = 0
        if movies[i] not in profile[9] or age_rating <=age:                 # A condition that checks wether the movie has been watched and the wether they are old enough for the movie
            number = 0                                                      # Makes a place holder variable called number and sets it to 0
            if mov_data[0].split()[0] in profile[6]:                        # If the first genre the movies is in the genres liked
                number = number+1                                           # Adds one to the variable number
            if mov_data[0].split()[1] in profile[6]:
                number = number+1
            if mov_data[0].split()[2] in profile[6]:
                number = number +1
            if mov_data[3] in directors_disliked:                           # A conditional wether checks if movie director is a director they don't like
                number =number -1                                           # Minuses one from the variable number
            odds.append(number)                                             # Adds the variable number to the end of the list odds
    movies_data = []                                                        # Makes a emty list called movies_data
    for i in range(len(movies)-1):                                          # A for loop that runs as long as the length of movies
        movies_data.append([odds[int(i)],movies[int(i)]])                   # Fills the list movies_data with odds and movies
    for passnum in range(len(movies_data)-1,0,-1):                          # This bubble sorts the list movies_data by the odds
        for i in range(passnum):                    
            if movies_data[i][0]<movies_data[i+1][0]:
                temp = movies_data[i]
                movies_data[i] = movies_data[i+1]
                movies_data[i+1] = temp
    movies_recommend = []                                                   # This is another list
    for i in range(9):                                                      # This for loop runs 9 times which adds the top 9 movies to movies_recommend
        movies_recommend.append(movies_data[i][1])                          
    recommend_window(old, movies_recommend,username)                        # This runs the recommend_window function and sends it the old window, the list, as well as the username

#--------------Change Password Function-----Part 1---------------------------------------------------------------------------------------------------------------------------------------------------

def change_password(old, username, movies_recommend):   # This creates a new function that recieves a tkinter window, a list and a username
    old.destroy()                                       # This deletes the old window
    window = Tk()                                       # This creates a new tkinter window
    window.title("Change Password")                     # This names the window 'change password'
    window.config(background = "#ccdeff")               # This sets the background of the tkinter window to light blue 
    passwords = [StringVar(),StringVar(),StringVar()]   # This makes a new list called passwords and places StringVar() 3 times inside
    Label(window,text = "Current Password", bg = "#ccdeff").grid(sticky = W)            # This makes a label that outputs 'current password' and places it on the window using grid
    Label(window,text = "New Password", bg = "#ccdeff").grid(sticky = W)                # This makes a label with a light blue background and places it on the window using grid
    Label(window,text = "Re-enter Password", bg = "#ccdeff").grid()     
    Entry(window, textvariable = passwords[0], show = "*").grid(row = 0, column = 1)    # This makes a entry box that is tied to the the 1st place in the passwords list and shows only '*' and places it on the window
    Entry(window, textvariable = passwords[1], show = "*").grid(row = 1, column = 1)
    Entry(window, textvariable = passwords[2], show = "*").grid(row = 2, column = 1)
    Button(window, text = "Submit", command = lambda : change_password_1(window, username, movies_recommend,passwords)).grid(sticky = W)        # This makes a button that runs the next part of the change password code when clicked
    Button(window, text = "Back", command = lambda : recommend_window(window,movies_recommend,username)).grid(row = 3, column = 1, sticky = E)  # This goes back to the recommend window

#--------------Change Password Function-----Part 2------------------------------------------------------------------------------------------------------------------------------------

def change_password_1(window, username, movies_recommend,passwords):    # This creates a function called change_password_1 
    for i in range(3):                                                  # A for loop that runs 3 times
        passwords[i] = passwords[i].get()                               # This gets the passwords entered into the entry boxes
    profile = [line.rstrip('\n') for line in open(username+".txt")]     # This opens the text file for the logged in user and gets all their data
    if passwords[0] == profile[1]:                                      # This checks if the first password entered is the same as their original password
        if passwd_check(passwords[1]) == True:                          # This runs the passwd_check function that check how secure the password is
            if passwords[1] == passwords[2]:                            # This checks if the last 2 entered passwords are the same
                profile[1] = passwords[1]                               # This makes the original password the new password
                with open(username+".txt","w") as file:                 # This opens the users file  as file then rewrite their file with the new data
                    file.writelines(profile[0]+"\n"+profile[1]+"\n"+profile[2]+"\n"+profile[3]+"\n"+profile[4]+"\n"+profile[5]+"\n"+profile[6]+"\n"+profile[7]+"\n"+profile[8]+"\n"+profile[9])
                file.close()                                            # This closes the window
                recommend_window(window,movies_recommend,username)      # This runs the recommend_window function

#--------------Add Genres Function-----Part 1--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def add_genres(old,movies_recommend,username):      # This creates a new function called add_genres
    old.destroy()                                   # This closes the old window
    window = Tk()                                   # This makes a new tkinter window called window
    window.title("Add Genres")                      # This line names the window 'Add genres'
    window.config(background = "#ccdeff")           # This makes the windows background light blue
    Label (window, text = "Which genres of movies do you like",bg = "#ccdeff").grid(columnspan = 5, sticky = W, row = 6, column = 0)# This makes a label with a light blue background and places it on the window
    genres = ["Action","Romance","Horror","Sci-Fi","Drama","Fantasy","Family","Musical","History","Comedy","Adventure","Thriller"]  # This makes a list filled with all the genres
    profile = [line.rstrip('\n') for line in open(username+".txt")]                                                                 # This opens the users file
    Data = [IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar()]            # This makes a list and fills it with IntVar() for the checkboxes
    for i in range(len(profile[6].split())):                            # A for loop for runs for the amount of spaces in the line with the liked genres
        Data[genres.index(profile[6].split()[i])] = IntVar(value = 1)   # This makes the check boxes for all the liked genres already activated,  below is a list of all the check buttons
    check_buttons = [Checkbutton(window, variable = Data[0], text = "Action", bg = "#ccdeff"),Checkbutton(window, variable = Data[1], text = "Romance", bg = "#ccdeff"),Checkbutton(window, variable = Data[2], text = "Horror", bg = "#ccdeff"),Checkbutton(window, variable = Data[3], text = "Sci_fi", bg = "#ccdeff"),Checkbutton(window, variable = Data[4], text = "Drama", bg = "#ccdeff"),Checkbutton(window, variable = Data[5], text = "Fantasy", bg = "#ccdeff"),Checkbutton(window, variable = Data[6], text = "Family", bg = "#ccdeff"),Checkbutton(window, variable = Data[7], text = "Musical", bg = "#ccdeff"),Checkbutton(window, variable = Data[8], text = "History", bg = "#ccdeff"),Checkbutton(window, variable = Data[9], text = "Comedy", bg = "#ccdeff"),Checkbutton(window, variable = Data[10], text = "Adventure", bg = "#ccdeff"),Checkbutton(window, variable = Data[11], text = "Thriller", bg = "#ccdeff")]
    nums_column = [0,2,4,0,2,4,0,2,4,0,2,4]         # This list has all coloumn positions for all the check buttons
    nums_row =    [7,7,7,8,8,8,9,9,9,10,10,10]      # A list that has all row positions for all the check buttons
    for i in range(12):                             # A for loop that runs 12 times
        check_buttons[i].grid(columnspan = 2, row = nums_row[i], column = nums_column[i], sticky = W)       # This places the check buttons in thier correct position using the 3 lists
    Button(window, text = "Submit", command = lambda : add_genre(movies_recommend,username,Data,genres,window)).grid(row =11, column = 0,sticky = W)    # This makes a button that continues to the next part and places it on the window
    Button(window, text = "Back", command = lambda : recommend_window(window,movies_recommend,username)).grid(row =11, column = 5, sticky = E)          # This button goes back to the recommend_window

#--------------Add Genre Function-----Part 2-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def add_genre(movies_recommend,username,data,genres,window):            # A function called add_genre to be activated by a button
    profile = [line.rstrip('\n') for line in open(username+".txt")]     # This opens the file for the user and splits it by line
    for i in range(12):                                                 # A for loop that runs 12 times
        data[i] = data[i].get()                                         # This gets wether the check buttons have been checked or unchecked
    genres_liked = ""                                                   # A variable called genres_liked which is a string
    for i in range(len(data)):                                          # A for loop thats runs the same amount of times as the length of data
        if data[i] == 1:                                                # This checks wether the check button is activated
            genres_liked = genres_liked+" "+str(genres[i])              # This adds the activated genre as a list with lots of spaces
    with open(username+".txt","w") as file:                             # This opens the user file as file, the next line writes it to the new line
        file.writelines(profile[0]+"\n"+profile[1]+"\n"+profile[2]+"\n"+profile[3]+"\n"+profile[4]+"\n"+profile[5]+"\n"+genres_liked+"\n"+profile[7]+"\n"+profile[8]+"\n"+profile[9])
    recommend_window(window,movies_recommend,username)                  # This returns to the recommend_window function

#--------------Change Infomation Function-----Part 1-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def change_info(old, movies_recommend, username):                   # Creating a new function which recieves a window, a list as well as a username
    old.destroy()                                                   # This closes the old window
    su = Tk()                                                       # Making a new tkinter window
    su.config(background = "#ccdeff")                               # Making the window's background light blue
    su.title("Change Infomation")                                   # Naming the window
    profile = [line.rstrip('\n') for line in open(username+".txt")] # Opening the users file as a list split at every line and saves it as profile
    Data = [StringVar(),StringVar(),[IntVar(),IntVar(),IntVar()],IntVar()]                              # Making a list to hold all the imports for this function
    Label(su, text = "Name",bg = "#ccdeff").grid(columnspan = 2, sticky = W, row = 1, column = 0)       # Making a label that outputs Name with a blue background
    Entry(su, textvariable = Data[0]).grid(columnspan = 2, sticky = W, row = 1, column = 2)             # Making an entry that is linked to the data list
    Label(su, text = "Address",bg = "#ccdeff").grid(columnspan = 2, sticky = W, row = 2, column = 0)    #
    Entry(su, textvariable = Data[1]).grid(columnspan = 2, sticky = W, row = 2, column = 2)             #
    Label(su, text = "Date of birth Day / Month / Year",bg = "#ccdeff").grid(columnspan = 4, sticky = W, row = 3, column = 0)
    Entry(su, textvariable = Data[2][0]).grid(columnspan = 2, sticky = W, row = 4, column = 0)
    Entry(su, textvariable = Data[2][1]).grid(columnspan = 2, sticky = W, row = 4, column = 2)
    Entry(su, textvariable = Data[2][2]).grid(columnspan = 2, sticky = W, row = 4, column = 4)
    Radiobutton(su, text = "Male", variable = Data[3], value = 1,bg = "#ccdeff").grid(columnspan = 2, sticky = W, row = 5, column = 0)      # A radio button meaning that that only one can be activated
    Radiobutton(su, text = "Female", variable = Data[3], value = 2,bg = "#ccdeff").grid(columnspan = 2, sticky = W, row = 5, column = 1)    #
    Radiobutton(su, text = "Other", variable = Data[3],value = 3,bg = "#ccdeff").grid(columnspan = 2, sticky = W, row = 5, column = 3)      #
    Button(su, text = "Back", command = lambda:recommend_window(old, movies_recommend, username)).grid(column = 5, row = 6, sticky = E)     #
    Button(su, text = "Submit", command = lambda:changeinfo(su, movies_recommend, username,Data)).grid(row = 6, sticky = W)                 #

#--------------Change Infomation Function-----Part 2------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def changeinfo(su, movies_recommend, username,data):    # Creating a new function that recieves a window, two lists and a string
    try:                                                # Using try to get all the data without crashes
        data[0] = data[0].get()                         # Getting the texts in the entry boxes or radio buttons
        data[1] = data[1].get()                         #
        data[2][0] = data[2][0].get()                   #   
        data[2][1] = data[2][1].get()                   #
        data[2][2] = data[2][2].get()                   #
        data[3] = data[3].get()                         #
    except:                                             # This will run if there is an error with the try
        Error("Please enter a valid date of birth")     # This runs the Error function that outputs the string
    if data[0].isalpha() == True:                       # A conditional that checks if the name is only letters
        profile = [line.rstrip('\n') for line in open(username+".txt")] # Opening the users file and saves it as a list in the variable profile
        file = open(username+".txt","w")                # This opens the users file with write permissions, then rewrites the profile with the edited profile
        file.writelines([str(profile[0])+"\n",str(profile[1])+"\n",str(data[0])+"\n",str(data[1])+"\n",str(datetime.datetime(int(data[2][2]),int(data[2][1]),int(data[2][0])))+"\n",str(data[3])+"\n",str(profile[6])+"\n",str(profile[7])+"\n",str(profile[8])+"\n",str(profile[9])+"\n"])
        recommend_window(su, movies_recommend, username)# This runs the recommend_window
    else:                                               # The second part of the conditional that runs everything
        Error("Please enter a valid name")              # This runs the Error function which outputs the string in a new window

#--------------Recommend Window-----Part 2----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    
def recommend_window(old,movies_recommend,username):    # Starting a function called recommend_window
    movies = []                                         # Making a empty list called movies
    for i in range(9):                                  # A for loop that runs 9 times
        mov = list(movies_recommend[i])                 # This splits the movie into letters
        while True:                                     # This While loop runs indefinitly until broken
            if "_" in mov:                              # This checks if there are underscores in the list
                mov[mov.index("_")] = " "               # This replaces the underscore with a splace
            else:                                       # The second part of the conditional that run if the first part isn't run
                break                                   # Breaking the while loop
        movies.append("".join(mov))                     # Making the list back into a string then adds it to the endt of the movies list
    old.destroy()                                       # Deleting the old window
    window = Tk()                                       # Creating a new window
    window.title("Movie Recommendor")                   # Naming the window 'Movie Recommendor'
    window.config(background = "#8ca8da")               # Setting the window's Background to a light blue, then making a list of buttons
    buttons = [Button(window, text = "Log out", command = lambda : back(window), bg = "#c8c8c8"),Button(window, text = "Change Infomation", bg = "#c8c8c8", command = lambda: change_info(window,movies_recommend,username)),Button(window, text = "Change Password", command = lambda : change_password(window, username, movies_recommend), bg = "#c8c8c8"),Button(window, text = movies[0], command = lambda : Movie(movies_recommend[0],window,movies_recommend,username),bg = "#ccdeff"),Button(window, text = movies[1], command = lambda : Movie(movies_recommend[1],window,movies_recommend,username),bg = "#ccdeff"),Button(window, text = movies[2], command = lambda : Movie(movies_recommend[2],window,movies_recommend,username),bg = "#ccdeff"),Button(window, text = movies[3], command = lambda : Movie(movies_recommend[3],window,movies_recommend,username),bg = "#ccdeff"),Button(window, text = movies[4], command = lambda : Movie(movies_recommend[4],window,movies_recommend,username),bg = "#ccdeff"),Button(window, text = movies[5], command = lambda : Movie(movies_recommend[5],window,movies_recommend,username),bg = "#ccdeff"),Button(window, text = movies[6], command = lambda : Movie(movies_recommend[6],window,movies_recommend,username),bg = "#ccdeff"),Button(window, text = movies[7], command = lambda : Movie(movies_recommend[7],window,movies_recommend,username),bg = "#ccdeff"),Button(window, text = movies[8], command = lambda : Movie(movies_recommend[8],window,movies_recommend,username),bg = "#ccdeff")]
    for i in range(12):                                                 # A for loop that runs 12 time
        buttons[i].config(width = 20)                                   # Making the button 20 wide
    column_place = [0,1,2,0,1,2,0,1,2,0,1,2]                            # Making a list of all the column positions
    row_place = [0,0,0,2,2,2,3,3,3,4,4,4]                               # Making a list of all the row positions
    label = Label(window, text = "Recommended movies", bg = "#8ca8da")  # Making a label that output Recommend movies with a blue background when put on the window
    label.config(height =2)                                             # Making the label 2 wide
    label.grid(columnspan = 2, row = 1, column = 0, sticky = W)         # Putting the Label on the window
    button = Button(window, text = "Add Genre", command = lambda:add_genres(window,movies_recommend,username), bg = "#c8c8c8") # Creating a button that runs the add_genres function when clicked
    button.config(width = 20)                                           # Making the button 20 wide
    button.grid(row = 1, column = 2, sticky = NW)                       # Putting the button on the window
    for i in range(12):                                                 # A for loop that runs 12 times
        buttons[i].grid(row = row_place[i], column = column_place[i])   # Placing a button on the window
        
#--------------Movie - Infomation / Like / Dislike-----Part 1-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def Movie(movie,old,movies_recommend,username):                     # Creating a function called movie which runs when you click on a movie in the recommend_movie
    mov_data =[line.rstrip('\n') for line in open(movie+".txt")]    # Opening the text file for the movie with all the data
    old.destroy()                                                   # Deleting the old window
    window = Tk()                                                   # Creating a new window called window
    window.title(movie)                                             # Calling the window the current movie opened
    window.config(background = "#ccdeff")                           # Making the window's background light blue
    photo = PhotoImage(file = movie+"_Image.gif")                   # Opening the gif for the movie as a tkinter PhotoImage file
    label = Label(window, image = photo)                            # Creating a label which displays the photo
    label.image = photo                                             # Making the image photo
    label.grid(rowspan = 10, column = 11,columnspan = 10,row = 1)   # Placing the image on the window
    mov_list = list(movie)                                          # Making the movies name into a list of seperate letters and saving it as mov_list
    while True:                                                     # A while loop that runs infinitly until it was broken
        if "_" in mov_list:                                         # A conditional that checks if a underscore in the list
            mov_list[mov_list.index("_")] = " "                     # Replacing a underscore with spaces
        else:                                                       # The second part of the conditonal
            break                                                   # Breaking the while loop
    movie2 = "".join(mov_list)                                      # Joining the list together and saving it together
    Button(window, text = "Back", command = lambda: recommend_window(window,movies_recommend,username)).grid(row = 0, sticky = W)               # A button that runs the recommend_window then placing it on the window
    Button(window, text = "Log out", command  = lambda : back(window)).grid(row = 0, column = 1, sticky = W)                                    # A button that closes the window and then the start function then putting it on the window
    Button(window, text = "Like", fg = "red", command = lambda : like(movie,movies_recommend,username)).grid(row = 0, column = 9, sticky = E)   # A button that runs the like function then places it on the window
    Button(window, text = "Dislike", command = lambda : dislike(movie,movies_recommend,username)).grid(row = 0, column = 8, sticky = E)         # A button that runs the dislike function then places it on the window
    Label(window, text = movie2,font=(None,20), bg = "#ccdeff").grid(row = 1,sticky = W, columnspan = 10)                                       # A label that outputs the name and outputs it as size 20 font then puts it on the window
    Label(window, text = "Age rating : "+mov_data[4], bg = "#ccdeff").grid(row = 2,sticky = W, columnspan = 10)                                 
    Label(window, text = "Length : "+mov_data[6]+" hours", bg = "#ccdeff").grid(row = 3,sticky = W, columnspan = 10)                             
    Label(window, text = "Director : "+mov_data[3], bg = "#ccdeff").grid(row = 4,sticky = W, columnspan = 10)                                    
    Label(window, text = "Actors : "+mov_data[2], bg = "#ccdeff").grid(row = 5,sticky = W, columnspan = 10)                                      
    Label(window, text = str(mov_data[5].replace('\\n','\n')),justify = 'left', bg = "#ccdeff").grid(row = 6,sticky = W, columnspan = 10)        
    photo = PhotoImage(file = "Star_Image.gif")                                 # Opens the Star_Image.gif file
    label = Label(window, image = photo)                                        # Puts the image in a label
    label.image = photo                                                         # Sets the image to label
    label.grid(column = 11, row = 0)                                            # Placing the label in the image
    Label(window, text = mov_data[1], bg = "#ccdeff").grid(column = 12, row =0) # Putting the Imdb rating on the window

#--------------Movie - Infomation / Like / Dislike-----Part 2----------------------------------------------------------------------------------------------------------------------------------------------------
    
def like(movie,movies_recommend,username):                          # Creating a function called like 
    profile = [line.rstrip('\n') for line in open(username+".txt")] # Opening the users text file as profile
    profile[7] = str(profile[7])+" "+str(movie)                     # Adds the new movie to the previous list of liked movies
    profile[9] = str(profile[9])+" "+str(movie)                     # Adds the new movie to the previous list of watched movies
    with open(username+".txt") as file:                             # Opening the users file as the variable file, rewriting the new lines
        file.writelines([profile[0]+"\n",profile[1]+"\n",profile[2]+"\n",profile[3]+"\n",profile[4]+"\n",profile[5]+"\n",profile[6]+"\n", profile[7]+"\n",profile[8]+"\n",profile[9]])
    file.close()                                                    # Closing the file

#--------------Movie - Infomation / Like / Dislike-----Part 3-----------------------------------------------------------------------------------------------------------------------------------------------------
    
def dislike(movie,movies_recommend,username):                       # Creating a function called dislike
    profile = [line.rstrip('\n') for line in open(username+".txt")] # Opening the users text file as profile
    profile[8] = str(profile[7])+str(movie)                         # Adds the new movie to the previous list of disliked movies
    profile[9] = str(profile[9])+str(movie)                         # Adds the new movie to the previous list of watched movies
    with open(username+".txt") as file:                             # Opening the users file as the variable file, rewriting the new lines
        file.writelines([profile[0]+"\n",profile[1]+"\n",profile[2]+"\n",profile[3]+"\n",profile[4]+"\n",profile[5]+"\n",profile[6]+"\n", profile[7]+"\n",profile[8]+"\n",profile[9]])
    file.close()                                                    # Closing the file

#--------------Back Function---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def back(window):       # Creating a new function which reciees a tkinter window
    window.destroy()    # Deleting the old window
    Start()             # Running the Start function

#--------------Password Check---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def passwd_check(password):         # Creating a function called passwd_check that gets password
    List = []                       # creating an empty list called List
    for i in range(len(password)):  # A for loop that runs for the length of the password sent
        letter = list(password)[i]  # Spliting the list into letters and sets the letter to ith places
        if letter.isalpha() == True and letter.islower() == True:   # A conditional that checks if it is alphabetical and if it is lowercase
            List.append(1)          # This adds 1 to the list
        elif letter in ["A","B","C","D","E","F","G","H","I","J","K","L","M","O","P","Q","R","S","T","U","V","W","X","Y","Z"]:   # A conditional checking if it is in a list
            List.append(2)          # This adds 2 to the list List 
        elif letter in ['0','1','2','3','4','5','6','7','8','9']:   # A conditional checking if it is a number
            List.append(3)          # Adding 3 to the list
        elif letter in ["`","¬","!",'"',"£","$","%","^","&","*","(",")","_","+","-","=","[","]",";","'","#",",",".","/","<",">","?",":","@","~","{","}",'\\',"|"]:  # Checking if it is a special character
            List.append(4)          # Adding 4 to the list
        else:                       # If it is anything else it will run this
            List.append(0)          # This adds 0 to the list
    if 1 in List and 2 in List and 3 in List and 4 in List: # This checks if 1,2,3,4 is in the list List
        return(True)                # This sends back True to the function that called it
    else:                           # If the other conditional isn't activated
        return(False)               # This sends back False to the function that called it

#--------------Login Function-----Part 1---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def Login(start):                           # Creating a new function call Login
    start.destroy()                         # Deleting the old window
    login = Tk()                            # Creating a new tkinter window
    login.title("Login")                    # Naming the window Login
    login.config(background = "#ccdeff")    # Making the background of the tkinter window light blue
    data = [StringVar(),StringVar()]        # Making a list for StringVar()
    Label(login, text= "Username", bg = "#ccdeff").grid()           # Making a light blue label which outputs Username and puting it on the grid
    Label(login, text= "Password", bg = "#ccdeff").grid()           #
    Entry(login, textvariable = data[0]).grid(row = 0, column = 2)  # Making an entry that is tied to the variable data[0] and places it on the grid
    Entry(login, textvariable = data[1], show = "*").grid(row = 1, column = 2)                      # An entry box tied to the variable data[1] and shows only *
    Button(login, text = "Submit", command = lambda: login_2(data, login)).grid()                   # A button which runs the next section of the login code
    Button(login, text = "Back", command = lambda: back(login)).grid(column = 2,row = 2,sticky = E) # A button which runs the start function

#--------------Login Function-----Part 2---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def login_2(data,login):        # Creating a new function called login_2
    username = data[0].get()    # Getting the text in the entry boxes
    password = data[1].get()    # Getting the text in the entry boxes
    try:                        # Using try to check if the username actually exists
        content = [line.rstrip('\n') for line in open(username+".txt")]     # Opening the users text file and splitting it into a list at every line
        if password == content[1]:                                          # A conditional that checks if password and original password
            recommendor(login,username)                                     # Running the recommendor function
        else:                                                               # The other part of the previous conditional
            Error("Password incorrect")                                     # Running the Error function which outputs the string in a new window
    except:                                                                 # This runs if their are Errors occuring in the try par
        Error("Username not recognised")                                    # Running the Error function which outputs the string in a new window

#---------------Sign Up Function-----Part 1---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def sign_up(start):                     # Creating a function called sign up
    start.destroy()                     # Deleting the previous window
    su = Tk()                           # Creating a new tkinter window called su
    su.title("Sign up")                 # Naming the window sign up
    su.config(background = "#ccdeff")   # Making the background light blue, Below is a list of all the data needed for 
    Data = [StringVar(),StringVar(),[IntVar(),IntVar(),IntVar()],IntVar(),[IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar()],StringVar(),StringVar(),StringVar()]
    Label(su, text = "Name",bg = "#ccdeff").grid(columnspan = 2, sticky = W, row = 1, column = 0)   # A label which outputs Name over a light blue background 
    Entry(su, textvariable = Data[0]).grid(columnspan = 2, sticky = W, row = 1, column = 2)         # A Entry box connected to Data[0]
    Label(su, text = "Address",bg = "#ccdeff").grid(columnspan = 2, sticky = W, row = 2, column = 0)
    Entry(su, textvariable = Data[1]).grid(columnspan = 2, sticky = W, row = 2, column = 2)         
    Label(su, text = "Date of birth Day / Month / Year",bg = "#ccdeff").grid(columnspan = 4, sticky = W, row = 3, column = 0)
    Entry(su, textvariable = Data[2][0]).grid(columnspan = 2, sticky = W, row = 4, column = 0)      
    Entry(su, textvariable = Data[2][1]).grid(columnspan = 2, sticky = W, row = 4, column = 2)      
    Entry(su, textvariable = Data[2][2]).grid(columnspan = 2, sticky = W, row = 4, column = 4)      
    Radiobutton(su, text = "Male", variable = Data[3], value = 1,bg = "#ccdeff").grid(columnspan = 2, sticky = W, row = 5, column = 0)  # A radio button to get the users gender
    Radiobutton(su, text = "Female", variable = Data[3], value = 2,bg = "#ccdeff").grid(columnspan = 2, sticky = W, row = 5, column = 1)
    Radiobutton(su, text = "Other", variable = Data[3],value = 3,bg = "#ccdeff").grid(columnspan = 2, sticky = W, row = 5, column = 2)  
    Label (su, text = "Which genres of movies do you like",bg = "#ccdeff").grid(columnspan = 5, sticky = W, row = 6, column = 0)        # Below is a list of checkbuttons       
    check_buttons = [Checkbutton(su, variable = Data[4][0], text = "Action", bg = "#ccdeff"),Checkbutton(su, variable = Data[4][1], text = "Romance", bg = "#ccdeff"),Checkbutton(su, variable = Data[4][2], text = "Horror", bg = "#ccdeff"),Checkbutton(su, variable = Data[4][3], text = "Sci_fi", bg = "#ccdeff"),Checkbutton(su, variable = Data[4][4], text = "Drama", bg = "#ccdeff"),Checkbutton(su, variable = Data[4][5], text = "Fantasy", bg = "#ccdeff"),Checkbutton(su, variable = Data[4][6], text = "Family", bg = "#ccdeff"),Checkbutton(su, variable = Data[4][7], text = "Musical", bg = "#ccdeff"),Checkbutton(su, variable = Data[4][8], text = "History", bg = "#ccdeff"),Checkbutton(su, variable = Data[4][9], text = "Comedy", bg = "#ccdeff"),Checkbutton(su, variable = Data[4][10], text = "Adventure", bg = "#ccdeff"),Checkbutton(su, variable = Data[4][11], text = "Thriller", bg = "#ccdeff")]
    nums_column = [0,2,4,0,2,4,0,2,4,0,2,4]     # The column location for each checkbutton
    nums_row =    [7,7,7,8,8,8,9,9,9,10,10,10]  # The row location for each checkbutton
    for i in range(12):                         # A for loop that runs 12 times
        check_buttons[i].grid(columnspan = 2, row = nums_row[i], column = nums_column[i], sticky = W)           # Placing the respective checkbutton in the respective column and row
    Label(su, text = "Username",bg = "#ccdeff").grid(columnspan = 2, sticky = W, row = 11, column = 0)          # Making a label which outputs username and places it on the window
    Label(su, text = "Password",bg = "#ccdeff").grid(columnspan = 2, sticky = W, row = 12, column = 0)          
    Label(su, text = "Password re-entry", bg = "#ccdeff").grid(columnspan = 2, sticky = W, row = 13, column = 0)
    Entry(su, textvariable = Data[5]).grid(columnspan = 2, sticky = W, row = 11, column = 2)                    # A entry box tied to data[5] and is place on the window
    Entry(su, textvariable = Data[6], show = "*").grid(columnspan = 2, sticky = W, row = 12, column = 2)        
    Entry(su, textvariable = Data[7], show = "*").grid(columnspan = 2, sticky = W, row = 13, column = 2)        
    Button (su, text = "Next", command = lambda : signup(su,Data)).grid(columnspan = 2, sticky = W, row = 14, column = 0)   # A button that runs the next part of the sign up section and placed on the window
    Button (su, text = "Back", command = lambda: back(su)).grid(columnspan = 2, sticky = E, row = 14,column = 5)

#--------------Sign up Function-----Part 2--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    
def signup(su, data):                       # Creating a new function called sighnup
    try:                                    # Using a try statement to make the code more robust
        data[0] = data[0].get()             # Getting what is in the entry Boxes
        data[1] = data[1].get()             
        data[2][0] = data[2][0].get()       
        data[2][1] = data[2][1].get()       
        data[2][2] = data[2][2].get()       
        data[3] = data[3].get()             
        for i in range(12):                 # Using a for loop to increase the efficiency
            data[4][i] = data[4][i].get()   
        data[5] = data[5].get()             
        data[6] = data[6].get()             
        data[7] = data[7].get()             
    except:                                 # The second part of the try which runs if there is an error
        Error("Please enter a valid Date of Birth") # Running the Error function outputting the string in a new window
    if data[2][0] == "":                    # If the entry boxes are empty
        data[2][0] = 1                      # Sets it to 1
    if data[2][1] == "":                    
        data[2][1] = 1                      
    if data[2][2] == "":                    
        data[2][2] = 1                      
    if data[6] != "":                       # If the password is not empty, then it check that name is alphabetical, and that the address isn't empty, and that the DoB is less than the current time, and gender has been entered and that username is empty 
        if data[0].isalpha() == True and data[1] != "" and datetime.datetime(int(data[2][2]),int(data[2][1]),int(data[2][0]))<datetime.datetime.now() and data[3] != 0 and data[5] != "":
            try:                                    # A try statement to check if the username exists
                open(data[5]+".txt")                # Opens the text file for username
                Error("Username already in use")    # Runs the Error function outputing the string in a new window
            except:                                 # If there is an error happens, this runs
                if passwd_check(data[6]) == True:   # A conditional that checks the outcome of running the passwd_check function comes back True
                    if data[6] == data[7]:          # If two passwords are the same 
                        genres = ["Action","Romance","Horror","Sci-Fi","Drama","Fantasy","Family","Musical","History","Comedy","Adventure","Thriller"]  # A list filled with the genres
                        for i in range(12):         # A for loop that runs 12 times
                            genres_liked = ""       # Makes a string and ties it to variable genres_liked
                            for i in range(12):     # A for loop that runs 12 times
                                if data[4][i] == 1: # A conditonal that checks if the checkbox is activate
                                    genres_liked = genres_liked+" "+str(genres[i])  # Adding the genre to the list of genres liked
                        data[4] = genres_liked      # Makes data[4] the same as genres_liked
                        su.destroy()                # Deleting the su window
                        su = Tk()                   # Recreating the window
                        su.title("Sign up")         # Naming the window Sign up
                        su.config(background = "#ccdeff")   # Making the window background light blue
                        movie_liked = [StringVar(),StringVar(su),StringVar()]       # Making a list of 3 StringVar() for called movie_liked
                        movie_disliked = [StringVar(),StringVar(su),StringVar()]    # Making a list of 3 StringVar() for called movie_disliked
                        movie_liked[1].set("Genre")                                 # Making the variable for the option menu to genre
                        movie_disliked[1].set("Genre")                              # Making the variable for the option menu to genre
                        Label(su, text = "Optional", bg = "#ccdeff").grid(columnspan = 2, sticky = W)
                        Label(su, text = "Please enter a movie that you like", bg = "#ccdeff").grid(row = 1, column = 0,columnspan = 2, sticky = W)     # Making a label then placing it on the window
                        Label (su, text = "Please enter it's genre", bg = "#ccdeff").grid(row = 2, column = 0,columnspan = 2, sticky = W)               # Making a label then placing it on the window
                        Label (su, text = "Please enter it's director", bg = "#ccdeff").grid(row = 3, column = 0,columnspan = 2, sticky = W)            # Making a label then placing it on the window
                        Entry (su, textvariable = movie_liked[0]).grid(row = 1, column = 2,columnspan = 2, sticky = W)                                  # Making an entry box tied to the movie_liked[0] then placing it on the window
                        OptionMenu(su,movie_liked[1],"Genre","Action","Romance","Horror","Sci-Fi","Drama","Fantasy","Family","Musical","Biography","History","Comedy","Adventure","Thriller").grid(row = 2, column = 2,columnspan = 2, sticky = W)
                        Entry (su, textvariable = movie_liked[2]).grid(row = 3, column = 2,columnspan = 2, sticky = W)                                  # Making an entry box tied to the movie_liked[2] then places it on the window, above is an option menu
                        Label(su, text = "Please enter a movie that you dislike", bg = "#ccdeff").grid(row = 4, column = 0,columnspan = 2, sticky = W)  # Making a label then placing it on the window
                        Label (su, text = "Please enter it's genre", bg = "#ccdeff").grid(row = 5, column = 0,columnspan = 2, sticky = W)               # Making a label then placing it on the window
                        Label (su, text = "Please enter it's director", bg = "#ccdeff").grid(row = 6, column = 0,columnspan = 2, sticky = W)            # Making a label then placing it on the window
                        Entry (su, textvariable = movie_disliked[0]).grid(row = 4, column = 2,columnspan = 2, sticky = W)                               # Making an entry box tied to the movie_disliked[0] then placing it on the window
                        OptionMenu(su,movie_disliked[1],"Genre","Action","Romance","Horror","Sci-Fi","Drama","Fantasy","Family","Musical","Biography","History","Comedy","Adventure","Thriller").grid(row = 5, column = 2,columnspan = 2, sticky = W)
                        Entry (su, textvariable = movie_disliked[2]).grid(row = 6, column = 2,columnspan = 2, sticky = W)                               # Making an entry box tied to the movie_disliked[0] then placing it on the window
                        Button(su, text = "Submit", command = lambda : signup_2(movie_liked, movie_disliked, su, data)).grid(sticky = W)                # A button that runs the signup_2 function when clicked 
                        Button(su, text = "Back", command = lambda : sign_up(su)).grid(sticky = E, column = 4, row = 7)                                 # A button that runs the sign_up function when clicked
                    else:                                   # This runs if the passwords aren't the same
                        Error("The passwords don't match")  # Running the Error which outputs the string on a new window
                else:                                       # This runs if the password doesn't pass the passwd_check function
                    Error("Please enter a password with:\n    - A capital\n    - A lowercase letter\n    - A number\n   - A special character") # Running the Error which outputs the string on a new window
        else:                                       # This runs if the infomation is not possible
            Error("Please enter valid infomation")  # Running the Error which outputs the string on a new window
    else:                                           # This runs if a password wasn't entered
        Error("Please enter something a password") # Running the Error which outputs the string on a new window

#--------------Sign Up Function-----Part 3---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def signup_2(Movie_liked, Movie_disliked, su, data):    # Creating a new function called signup_2
    movie_liked = []                                    # Creating a list under the variable movie_liked
    movie_disliked = []                                 # Creating a list under the variable movie_disliked
    for i in range(3):                                  # A for loop that runs 3 times
        movie_liked.append(Movie_liked[i].get())        # Appending what the user entered for the movie liked in the sign up function part 2
        movie_disliked.append(Movie_disliked[i].get())  # Appending what the user entered for the movie disliked in the sign up function part 2
    num = 0
    if Movie_liked[0] != "" or Movie_liked[2] != "":
        if Movie_liked[1] != "Genre":
            num = 1
        else:
            Error("Please enter a valid genre")
    else:
        num = 1
    if num == 1:
        file = open(data[5]+".txt","w+")            # Creating a text file for the username, then writing all the data collected 
        file.writelines([str(data[5])+"\n",str(data[6])+"\n",str(data[0])+"\n",str(data[1])+"\n",str(datetime.datetime(int(data[2][2]),int(data[2][1]),int(data[2][0])))+"\n",str(data[3])+"\n", str(data[4])+"\n",str(movie_liked[0])+"\n",str(movie_disliked[0])+"\n","\n"])
        file.close()                                                        # Closing the text file
        file = open(data[5]+" "+movie_liked[0]+".txt","w+")                 # Creating a text file for the movie they like
        file.writelines(str(movie_liked[1])+"\n\n\n"+movie_liked[2])        # Writing the data collected to it
        file.close()                                                        # Closing the text file
        file = open(data[5]+" "+movie_disliked[0]+".txt","w+")              # Creating a text file for the movie they dislike
        file.writelines(str(movie_disliked[1])+"\n\n\n"+movie_disliked[2])  # Writing to the text file
        file.close()                                                        # Closing the text file
    recommendor(su,data[5])                                             # Running to the recommendor function

#--------------Start---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def Start():                                # A function called Start
    start = Tk()                            # Creating a new window
    start.title("Start")                    # Naming the window Start
    start.config(background = "#ccdeff")    # Making the background light blue
    Label (start, text = "Would you like to:",bg = "#ccdeff").grid(row = 0, columnspan = 3,sticky = W)  # Making a label then placing it on the window
    Button(start, text = "Login", command = lambda : Login(start)).grid(row = 1, column = 0)            # Making a label which outputs Login then places on the window
    Button(start, text = "Sign up", command = lambda : sign_up(start)).grid(row = 1, column = 1)        # Making a label which outputs Sign up then places on the window


Start() # Starting the code

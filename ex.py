import streamlit as st
import streamlit as st
import mysql.connector 
import time as t
import pandas as pd 
placeholder = st.empty()

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    database="faculty"
)
mycursor=mydb.cursor()
valid=[]
def valid_pass(u,p,utype):
    mydb=mysql.connector.connect(host='localhost',user='root',database='faculty')
    mycursor=mydb.cursor()
    print(utype)
    if utype=="Admin":
        mycursor.execute(f"select name from administrator where email='{p}' ;")
        out_u=mycursor.fetchall()
        mycursor.execute(f"select email from administrator where email='{p}' ;")
        out_p=mycursor.fetchall()
        
    else:    
        mycursor.execute(f"select faculty_id from faculty where faculty_id='{u}';")
        out_u=mycursor.fetchall()
        mycursor.execute(f"select password from faculty where faculty_id='{u}';")
        out_p=mycursor.fetchall()
        
        
    for i in range(len(out_u)):
        print(p==out_p[0][0],u==out_u[0][0])
        print(u,p)
        print(out_p[0][0],out_u[0][0])
        if u==out_u[0][0] and p==out_p[0][0] :
            print(out_p,out_u)
            if utype=="Admin":
                st.session_state['login']= True
                st.session_state['type']="Admin"
                st.success("Login success")
                print(st.session_state)
                
                return 1
            else:
                st.session_state['login']= True
                st.session_state['type']="faculty"
                st.session_state['user']=out_u[0][0]


                st.success("Login success")    
        else:
            return 0
    return 1

def login():
    # interface codes for the login screen
    # with st.form(key='myform',clear_on_submit=True):
        st.write("Welcome to the login screen")

        st.markdown("<h1 style='text-align: center; color: blue;'>Login</h1>", unsafe_allow_html=True)
        utype=st.radio("Login Type",("Admin","Faculty"))
        st.markdown("#### Enter your credentials")    
        user=st.text_input("User Name")
        password=st.text_input("Password",type='password')
        # if user:
        #     valid_pass(user,password,utype)
        
        st.button("login",valid_pass(user,password,utype))
        # st.button("Login",valid_pass(user,password,utype))
    





def main():
    print(st.session_state)
    if st.session_state['login']== True and st.session_state['type']=="Admin":
        # interface codes for the main screen
        st.header("Welcome to Faculty Achivement Portal")
        #st.button("Logout",on_click=login)
        menu=["Faculty Registration","Faculty profile updation","Add Achivement","Achivement Updation","Experience","Qualification","Query"]
        option=st.sidebar.selectbox("Menu",menu)
        if option == "Faculty Registration":
            st.markdown("<h1 style='text-align: center; color: blue;'>Faculty Registration</h1>", unsafe_allow_html=True)
            with st.form(key="Insert_form",clear_on_submit=True):
                c1,c2=st.columns(2)
                with c1:
                    i1=st.text_input("First Name")
                    i2=st.text_input("Middle Name")
                    i3=st.text_input("Last Name")
                    i7=st.text_input("faculty_id")
                with c2:
                    i4=st.text_input("Department Name")
                    i5=st.text_input("Email")
                    i6=st.text_input("Password")  
                submission = st.form_submit_button(label="Add Faculty")
                if submission==True:
                    mycursor.execute(f"Insert into faculty values ('{i1}','{i2}','{i3}','{i5}','{i7}','{i6}','{i4}');")
                    mydb.commit()
                    st.success("Insertion successfull")
                st.write("\n")
                i8=st.text_input("faculty id")
                submission1 = st.form_submit_button(label="Delete Faculty")
                if submission1==True:
                    mycursor.execute(f"delete from faculty where faculty_id='{i8}' ;")
                    mycursor.execute(f"delete from achievement where faculty_id='{i8}';")
                    mycursor.execute(f"delete from qualification where faculty_id='{i8}';")

                    mycursor.execute(f"delete from experience where faculty_id='{i8}';")

                    mydb.commit()
                    st.success("Deletion successfull")

                st.write("\n")
                st.subheader("Present Records")
                query = "select * from faculty"
                mycursor.execute(query)
                last=mycursor.fetchall()
                last = pd.DataFrame(last,columns=["Fname",	"Mname",	"Lname"	,"Email",	"faculty_id"	,"password",	"department_id"	])
                st.write(last)
        elif option == "Faculty profile updation":
            st.markdown("<h1 style='text-align: center; color: blue;'>Faculty profile updation</h1>", unsafe_allow_html=True)
            with st.form(key="Insert_form",clear_on_submit=True):
                c3,c4=st.columns(2)
                with c3:
                    i1=st.text_input("Update First Name")
                    i2=st.text_input("Update Middle Name")
                    i3=st.text_input("Update Last Name")
                    i7=st.text_input("faculty_id")
                with c4:
                    i4=st.text_input("Update Email")
                    i5=st.text_input("Update Password")    
                submission = st.form_submit_button(label="Update Faculty")
                if submission==True:
                    mycursor.execute(f"update faculty set Fname='{i1}', Mname='{i2}'	,Lname='{i3}',	Email='{i4}',	password='{i5}' where faculty_id='{i7}';")
                    mydb.commit()
                    st.success("Updation successfull")
                st.write("\n")
                st.write("\n")
                st.subheader("Present Records")
                query = "select * from faculty"
                mycursor.execute(query)
                last=mycursor.fetchall()
                last = pd.DataFrame(last,columns=["Fname",	"Mname",	"Lname"	,"Email",	"faculty_id"	,"password",	"department_id"	])
                st.write(last)  
        elif option == "Add Achivement":   
            st.markdown("<h1 style='text-align: center; color: blue;'>Add Achivement </h1>", unsafe_allow_html=True)
            with st.form(key="Insert_form",clear_on_submit=True):
                c5,c6=st.columns(2)
                with c5:
                    i1=st.text_input("Achivement ID")
                    i2=st.text_input("Faculty ID")
                    i3=st.date_input("Date")
                with c6:
                    i4=st.text_input("Achivement")
                    i5=st.text_input("Proof for Achivement") 
                    i6=st.text_input("Manager ID") 

                submission = st.form_submit_button(label="Add Achivement")
                if submission==True:
                    mycursor.execute(f"insert into  achievement (`achievement_id`, `faculty_id`, `Date`, `Description`, `prof_of_doc`, `val_manager_id`) values ('{i1}','{i2}','{i3}','{i4}','{i5}','{i6}');")
                    mydb.commit()
                    st.success("Insertion successfull")
                st.write("\n")
                i8=st.text_input("faculty id")
                i9=st.text_input("achievement Id")
                submission1 = st.form_submit_button(label="Delete achievement")
                i11=st.text_input("Faculty Id")
                i13=st.text_input("achievement ID")
                i12=st.text_input("Approval Status")
                upp=st.form_submit_button(label="Approve Achivement")
                if upp == True:
                    mycursor.execute(f"update  achievement set approval_status='{i12}' where faculty_id='{i11}' and achievement_id='{i13}';")
                    mydb.commit()
                    st.success("Approval status changed")
                if submission1==True:
                    mycursor.execute(f"delete from achievement where faculty_id='{i8}' and achievement_id='{i9}';")
                    mydb.commit()
                    st.success("Deletion successfull")
                st.write("\n")
                st.subheader("Present Records")
                query = "select * from achievement;"
                mycursor.execute(query)
                last=mycursor.fetchall()
                last = pd.DataFrame(last,columns=["achievement_id"	,"faculty_id"	,"Date"	,"Description"	,"prof_of_doc","val_manager_id","approval status"])
                st.write(last)  
        elif option == "Achivement Updation":  
            st.markdown("<h1 style='text-align: center; color: blue;'> Achivement Updation </h1>", unsafe_allow_html=True)
            with st.form(key="Insert_form",clear_on_submit=True): 
                c7,c8=st.columns(2)
                with c7:
                    i1=st.text_input("Achivement ID")
                    i2=st.text_input("Faculty ID")
                with c8:
                    i3=st.text_input("Update Achivement")
                    i4=st.text_input("update Proof for Achivement")         
                submission = st.form_submit_button(label="Update Faculty")
                if submission==True:
                    mycursor.execute(f"update  achievement set prof_of_doc='{i4}',Description='{i3}' where faculty_id='{i2}' ;")
                    mydb.commit()
                    st.success("Updation successfull")
                st.write("\n")
                st.write("\n")
                st.subheader("Present Records")
                query = "select * from achievement;"
                mycursor.execute(query)
                last=mycursor.fetchall()
                last = pd.DataFrame(last,columns=["achievement_id"	,"faculty_id"	,"Date"	,"Achivements "		,"prof_of_doc","val_manager_id","approval status"])
                st.write(last)  

        elif option == "Experience":  
            st.markdown("<h1 style='text-align: center; color: blue;'> Faculty  Experience </h1>", unsafe_allow_html=True)
            st.write("\n")
            i4=st.text_input("Experience Type")
            i5=st.text_input("Faculty Id ")    

            i6=st.text_input(" Number Of Years ")    
            submission = st.button(label="Add Experience ")
            if submission==True:
                mycursor.execute(f"INSERT INTO `experience` (`faculty_id`, `Experience_type`, `number_of_years`) VALUES ('{i5}', '{i4}', '{i6}');")
                mydb.commit()
                st.success("Updation successfull")
            st.subheader("Present Records")
            query = "select * from experience;"
            mycursor.execute(query)
            last=mycursor.fetchall()
            last = pd.DataFrame(last,columns=["faculty_id",	"Experience_type"	,"number_of_years"])
            st.write(last)   
        elif option == "Qualification":  
            st.markdown("<h1 style='text-align: center; color: blue;'> Add Qualification </h1>", unsafe_allow_html=True)
            i4=st.text_input("Qualification  ")
            i5=st.text_input("Faculty Id ")    
            submission = st.button(label="Add Qualification ")
            if submission==True:
                mycursor.execute(f"INSERT INTO `qualification` (`Qualification_name`, `faculty_id`) VALUES ('{i4}', '{i5}');;")
                mydb.commit()
                st.success(" successfull")
            st.subheader("Present Records")


            query = "select * from qualification;"
            mycursor.execute(query)
            last=mycursor.fetchall()
            last = pd.DataFrame(last,columns=["Qualification_name",	"Faculty Id"])
            st.write(last)                 
        else:
            with st.form(key="Query_form",clear_on_submit=False):
                query = st.text_area("Enter your query : ")
                queries = query.split(";")
                submission = st.form_submit_button(label="Submit")
                if submission==True:
                    for query in queries:
                        if query==" \n" or query=="\n" or query==" ":
                            st.write()
                        else:
                            mycursor.execute(query)
                            if 'select' in query or 'Select' in query or "SELECT" in query or 'desc' in query or 'Desc' in query or 'DESC' in query or 'show' in query or 'Show' in query or 'SHOW' in query:
                                output=mycursor.fetchall()
                                output=pd.DataFrame(output,columns=[i[0] for i in mycursor.description])
                                out = 'Results of your query ( '+ query + ')'
                                st.write(out)
                                st.write(output)
                            else:
                                mydb.commit()
                                st.success("Query executed successfully..")

    elif st.session_state['login']== True and st.session_state['type']=="faculty":
        menu=["Faculty profile updation","Add Achivement","Achivement Updation","Experience","Qualification","Query"]
        option=st.sidebar.selectbox("Menu",menu)
        
        if option == "Faculty profile updation" :
            st.markdown("<h1 style='text-align: center; color: blue;'>Faculty profile updation</h1>", unsafe_allow_html=True)
            with st.form(key="Insert_form",clear_on_submit=True):
                c3,c4=st.columns(2)
                with c3:
                    i1=st.text_input("Update First Name")
                    i2=st.text_input("Update Middle Name")
                    i3=st.text_input("Update Last Name")
                    i7=st.text_input("faculty_id")
                with c4:
                    i4=st.text_input("Update Email")
                    i5=st.text_input("Update Password")    
                submission = st.form_submit_button(label="Update Faculty")
                if submission==True and st.session_state['user']==i7:
                    mycursor.execute(f"update faculty set Fname='{i1}', Mname='{i2}'	,Lname='{i3}',	Email='{i4}',	password='{i5}' where faculty_id='{i7}';")
                    mydb.commit()
                    st.success("Updation successfull")
                else:
                    st.warning("You cannot update other faculty details, please contact admin")                
                st.write("\n")
                st.write("\n")
                st.subheader("Present Records")
                query = "select Fname,	Mname,	Lname	,Email,department_id from faculty"
                mycursor.execute(query)
                last=mycursor.fetchall()
                last = pd.DataFrame(last,columns=["Fname",	"Mname",	"Lname"	,"Email",		"department_id"	])
                st.write(last)  
        elif option == "Add Achivement":   
            st.markdown("<h1 style='text-align: center; color: blue;'>Add Achivement </h1>", unsafe_allow_html=True)
            with st.form(key="Insert_form",clear_on_submit=True):
                c5,c6=st.columns(2)
                with c5:
                    i1=st.text_input("Achivement ID")
                    i2=st.text_input("Faculty ID")
                    i3=st.date_input("Date")
                with c6:
                    i4=st.text_input("Achivement")
                    i5=st.text_input("Proof for Achivement") 
                    i6=st.text_input("Manager ID") 

                submission = st.form_submit_button(label="Add Achivement")
                if submission==True and st.session_state['user']==i2:
                    mycursor.execute(f"insert into  achievement (`achievement_id`, `faculty_id`, `Date`, `Description`, `prof_of_doc`, `val_manager_id`)values ('{i1}','{i2}','{i3}','{i4}','{i5}','{i6}');")
                    mydb.commit()
                    st.success("Insertion successfull")
                else:
                    st.warning("You cannot update other faculty details, please contact admin")                
    
                st.write("\n")
                i8=st.text_input("Faculty id")
                i9=st.text_input("achievement Id")
                submission1 = st.form_submit_button(label="Delete achievement")
                if submission1==True:
                    mycursor.execute(f"delete from achievement where faculty_id='{i8}' and achievement_id='{i9}';")
                    mydb.commit()
                    st.success("Deletion successfull")
                st.write("\n")
                st.subheader("Present Records")
                query = "select * from achievement;"
                mycursor.execute(query)
                last=mycursor.fetchall()
                last = pd.DataFrame(last,columns=["achievement_id"	,"faculty_id"	,"Date"	,"Achievements"	,"prof_of_doc","val_manager_id","approval status"])
                st.write(last)  
        elif option == "Achivement Updation":  
            st.markdown("<h1 style='text-align: center; color: blue;'> Achivement Updation </h1>", unsafe_allow_html=True)
            with st.form(key="Insert_form",clear_on_submit=True): 
                c7,c8=st.columns(2)
                with c7:
                    i1=st.text_input("Achivement ID")
                    i2=st.text_input("Faculty ID")
                with c8:
                    i3=st.text_input("Update Achivement")
                    i4=st.text_input("update Proof for Achivement") 
                print(i2,st.session_state['user'])            
                submission = st.form_submit_button(label="Update Faculty")
                if submission==True and st.session_state['user']==i2:
                    mycursor.execute(f"update  achievement set prof_of_doc='{i4}',Description='{i3}' where faculty_id='{i2}' ;")
                    mydb.commit()
                    st.success("Updation successfull")
                else:
                    st.warning("You cannot update other faculty details, please contact admin")                
    
                st.write("\n")
                st.write("\n")
                st.subheader("Present Records")
                query = "select * from achievement;"
                mycursor.execute(query)
                last=mycursor.fetchall()
                last = pd.DataFrame(last,columns=["achievement_id"	,"faculty_id"		,"Date"	,	"Achievements ","prof_of_doc","val_manager_id","approval status"])
                st.write(last)  

        elif option == "Experience":  
            st.markdown("<h1 style='text-align: center; color: blue;'> Faculty  Experience </h1>", unsafe_allow_html=True)
            st.write("\n")
            i4=st.text_input("Experience Type")
            i5=st.text_input("Faculty ID ")    

            i6=st.text_input(" Number Of Years ")    
            submission = st.button(label="Add Experience ")
            if submission==True and st.session_state['user']==i5:
                mycursor.execute(f"INSERT INTO `experience` (`faculty_id`, `Experience_type`, `number_of_years`) VALUES ('{i5}', '{i4}', '{i6}');")
                mydb.commit()
                st.success("Updation successfull")
            else:
                st.warning("You cannot add other faculty details, please contact admin")    
            i8=st.text_input("Updating Number of years")
            i7=st.text_input("Faculty Id ")
            up=st.button("Update")
            if up :
                mycursor.execute(f"update  experience set number_of_years='{i8}' where faculty_id='{i7}' ;")
                mydb.commit()
            st.subheader("Present Records")
            query = "select * from experience;"
            mycursor.execute(query)
            last=mycursor.fetchall()
            last = pd.DataFrame(last,columns=["faculty_id",	"Experience_type"	,"number_of_years"])
            st.write(last)   
        elif option == "Qualification":  
            st.markdown("<h1 style='text-align: center; color: blue;'> Add Qualification </h1>", unsafe_allow_html=True)
            i4=st.text_input("Qualification  ")
            i5=st.text_input("Faculty Id ")    
            submission = st.button(label="Add Qualification ")
            if submission==True and st.session_state['user']==i5:
                mycursor.execute(f"INSERT INTO `qualification` (`Qualification_name`, `faculty_id`) VALUES ('{i4}', '{i5}');;")
                mydb.commit()
                st.success(" successfull")
            else:
                st.error("You cannot update please contact admin")                 
            st.subheader("Present Records")


            query = "select * from qualification;"
            mycursor.execute(query)
            last=mycursor.fetchall()
            last = pd.DataFrame(last,columns=["Qualification_name",	"Faculty Id"])
            st.write(last)                 
        else:
            with st.form(key="Query_form",clear_on_submit=False):
                query = st.text_area("Enter your query : ")
                queries = query.split(";")
                submission = st.form_submit_button(label="Submit")
                if submission==True:
                    for query in queries:
                        if query==" \n" or query=="\n" or query==" ":
                            st.write()
                        else:
                            mycursor.execute(query)
                            if 'select' in query or 'Select' in query or "SELECT" in query or 'desc' in query or 'Desc' in query or 'DESC' in query or 'show' in query or 'Show' in query or 'SHOW' in query:
                                output=mycursor.fetchall()
                                output=pd.DataFrame(output,columns=[i[0] for i in mycursor.description])
                                out = 'Results of your query ( '+ query + ')'
                                st.write(out)
                                st.write(output)
                            else:
                                mydb.commit()
                                st.success("Query executed successfully..")
    else:
        st.warning("Please login ")    
        print(valid)                              
def logout():
    if st.session_state['login']==True:
        st.session_state["login"] = False
        st.session_state['type']="fac"
        st.session_state['user']="x"
    else:
        st.error("please login")    


page_names_to_funcs = {
    "Main Page": login,
    "Page 2": main,
    "logout":logout
    
}

selected_page = st.sidebar.selectbox("Select a page", page_names_to_funcs.keys())
page_names_to_funcs[selected_page]()

if 'login' not in st.session_state:
    st.session_state['login'] = False
    st.session_state['type']="fac"
    st.session_state['utype']="facd"
    st.session_state['user']="x"


# if st.session_state["page"] == "login":
#     login()
# elif st.session_state["page"] == "main":
#     main()
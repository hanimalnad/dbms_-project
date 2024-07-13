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

def valid_pass(u,p):
    mydb=mysql.connector.connect(host='localhost',user='root',database='faculty')
    mycursor=mydb.cursor()
    mycursor.execute('select name from administrator;')
    out_u=mycursor.fetchall()
    mycursor.execute('select email from administrator;')
    out_p=mycursor.fetchall()
    for i in range(len(out_u)):
        if u==out_u[i][0] and p==out_p[i][0]:
            return 1
        else:
            return 0
    return 1
     

# st.header("Welcome to Faculty Management Portal")
# log=placeholder.form("login")
# with log:
#     st.markdown("<h1 style='text-align: center; color: blue;'>Login</h1>", unsafe_allow_html=True)
#     utype=st.radio("Login Type",("Admin","Faculty"))
#     st.markdown("#### Enter your credentials")
#     username = st.text_input("Username")
#     password = st.text_input("Password", type="password")
#     submit = st.form_submit_button("Login")

# if submit and valid_pass(username,password)==1:
#     log.empty()
#     menu=["Faculty Registration","Faculty profile updation","Add Achivement","Achivement Updation","Query"]
#     option=st.sidebar.selectbox("Menu",menu)
#     if option == "Faculty Registration":

#         st.markdown("<h1 style='text-align: center; color: blue;'>Faculty Registration</h1>", unsafe_allow_html=True)
#         with st.form(key="Insert_form",clear_on_submit=True):

#             c1,c2=st.columns(2)
#             with c1:
#                 i1=st.text_input("First Name")
#                 i2=st.text_input("Middle Name")
#                 i3=st.text_input("Last Name")
#                 i7=st.text_input("faculty_id")



#             with c2:
#                 i4=st.text_input("Department ID")
#                 i5=st.text_input("Email")
#                 i6=st.text_input("Password")  
#             submission = st.form_submit_button(label="Add Faculty")

#             if submission==True:
#                 mycursor.execute(f"Insert into faculty values (%s,%s,%s,%s,%s,%s,%s),({i1},{i2},{i3},{i5},{i6},{i6},{i6});")
#                 mydb.commit()
#                 st.success("Insertion successfull")

#             st.write("\n")
#             st.write("\n")
#             st.subheader("Present Records")
#             query = "select * from faculty"
#             mycursor.execute(query)
#             last=mycursor.fetchall()
#             last = pd.DataFrame(last,columns=["Fname",	"Mname",	"Lname"	,"Email",	"faculty_id"	,"password",	"department_id"	])
#             st.write(last)
#     elif option == "Faculty profile updation":
#         st.markdown("<h1 style='text-align: center; color: blue;'>Faculty profile updation</h1>", unsafe_allow_html=True)
#         with st.form(key="Insert_form",clear_on_submit=True):

#             c3,c4=st.columns(2)
#             with c3:
#                 i1=st.text_input("Update First Name")
#                 i2=st.text_input("Update Middle Name")
#                 i3=st.text_input("Update Last Name")
#                 i7=st.text_input("faculty_id")

#             with c4:
#                 i4=st.text_input("Update Email")
#                 i5=st.text_input("Update Password")    
#             submission = st.form_submit_button(label="Update Faculty")
#             if submission==True:
#                 mycursor.execute(f"update faculty set Fname={i1} Mname={i2}	Lname={i2}	Email={i2}	password={i5} where faculty_id={i7};")
#                 mydb.commit()
#                 st.success("Insertion successfull")

#             st.write("\n")
#             st.write("\n")
#             st.subheader("Present Records")
#             query = "select * from faculty"
#             mycursor.execute(query)
#             last=mycursor.fetchall()
#             last = pd.DataFrame(last,columns=["Fname",	"Mname",	"Lname"	,"Email",	"faculty_id"	,"password",	"department_id"	])
#             st.write(last)  

#     elif option == "Add Achivement":   
#         st.markdown("<h1 style='text-align: center; color: blue;'>Add Achivement </h1>", unsafe_allow_html=True)
#         with st.form(key="Insert_form",clear_on_submit=True):
#             c5,c6=st.columns(2)
#             with c5:
#                 i1=st.text_input("Achivement ID")
#                 i2=st.text_input("Faculty ID")
#                 i3=st.date_input("Date")
#             with c6:
#                 i4=st.text_input("Description")
#                 i5=st.text_input("Proof for Achivement") 
#             submission = st.form_submit_button(label="Add Achivement")
#             if submission==True:
#                 mycursor.execute(f"insert into  faculty values (%s,%s,%s,%s,%s),({i1},{i2},{i3},{i4},{i5});")
#                 mydb.commit()
#                 st.success("Insertion successfull")

#             st.write("\n")
#             st.write("\n")
#             st.subheader("Present Records")
#             query = "select * from faculty"
#             mycursor.execute(query)
#             last=mycursor.fetchall()
#             last = pd.DataFrame(last,columns=["achievement_id"	,"faculty_id"	,"field"	,"Date"	,"Description"	,"prof_of_doc","val_manager_id"])
#             st.write(last)  

#     elif option == "Achivement Updation":  
#         st.markdown("<h1 style='text-align: center; color: blue;'> Achivement Updation </h1>", unsafe_allow_html=True)
#         with st.form(key="Insert_form",clear_on_submit=True): 
#             c7,c8=st.columns(2)
#             with c7:
#                 i1=st.text_input("Achivement ID")
#                 i2=st.text_input("Faculty ID")
#             with c8:
#                 i3=st.text_input("Update Description")
#                 i4=st.text_input("update Proof for Achivement")         
#             submission = st.form_submit_button(label="Update Faculty")
#             if submission==True:
#                 mycursor.execute(f"update  faculty set prof_of_doc={i4},Description={i3} where faculty_id={i2};")
#                 mydb.commit()
#                 st.success("Insertion successfull")

#             st.write("\n")
#             st.write("\n")
#             st.subheader("Present Records")
#             query = "select * from faculty"
#             mycursor.execute(query)
#             last=mycursor.fetchall()
#             last = pd.DataFrame(last,columns=["achievement_id"	,"faculty_id"	,"field"	,"Date"	,"Description"	,"prof_of_doc","val_manager_id"])
#             st.write(last)  

#     else:
#         with st.form(key="Query_form",clear_on_submit=False):
#             query = st.text_area("Enter your query : ")
#             queries = query.split(";")
#             submission = st.form_submit_button(label="Submit")
#             if submission==True:
#                 for query in queries:
#                     if query==" \n" or query=="\n" or query==" ":
#                         st.write()
#                     else:
#                         mycursor.execute(query)
#                         if 'select' in query or 'Select' in query or "SELECT" in query or 'desc' in query or 'Desc' in query or 'DESC' in query or 'show' in query or 'Show' in query or 'SHOW' in query:
#                             output=mycursor.fetchall()
#                             output=pd.DataFrame(output,columns=[i[0] for i in mycursor.description])
#                             out = 'Results of your query ( '+ query + ')'
#                             st.write(out)
#                             st.write(output)

#                         else:
#                             mydb.commit()
#                             st.success("Query executed successfully..")        
 
with st.form(key="Insert_form",clear_on_submit=True):
    st.markdown("<h1 style='text-align: center; color: blue;'>Login</h1>", unsafe_allow_html=True)
    utype=st.radio("Login Type",("Admin","Faculty"))
    st.markdown("#### Enter your credentials")
    user=st.text_input("UserName")
    passw=st.text_input("Password")
    submission = st.form_submit_button(label="Login")



st.header("Welcome to Faculty Management Portal")
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
            mycursor.execute(f"update faculty set Fname='{i1}', Mname='{i2}'	,Lname='{i2}',	Email='{i2}',	password='{i5}' where faculty_id='{i7}';")
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
            i4=st.text_input("Description")
            i5=st.text_input("Proof for Achivement") 
            i6=st.text_input("Manager ID") 

        submission = st.form_submit_button(label="Add Achivement")
        if submission==True:
            mycursor.execute(f"insert into  achievement values ('{i1}','{i2}','{i3}','{i4}','{i5}','{i6}');")
            mydb.commit()
            st.success("Insertion successfull")
        st.write("\n")
        st.write("\n")
        st.subheader("Present Records")
        query = "select * from achievement;"
        mycursor.execute(query)
        last=mycursor.fetchall()
        last = pd.DataFrame(last,columns=["achievement_id"	,"faculty_id"	,"Date"	,"Description"	,"prof_of_doc","val_manager_id"])
        st.write(last)  
elif option == "Achivement Updation":  
    st.markdown("<h1 style='text-align: center; color: blue;'> Achivement Updation </h1>", unsafe_allow_html=True)
    with st.form(key="Insert_form",clear_on_submit=True): 
        c7,c8=st.columns(2)
        with c7:
            i1=st.text_input("Achivement ID")
            i2=st.text_input("Faculty ID")
        with c8:
            i3=st.text_input("Update Description")
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
        last = pd.DataFrame(last,columns=["achievement_id"	,"Description "		,"Date"	,"faculty_id"	,"prof_of_doc","val_manager_id"])
        st.write(last)  

elif option == "Experience":  
    st.markdown("<h1 style='text-align: center; color: blue;'> Faculty  Experience </h1>", unsafe_allow_html=True)
    st.write("\n")
    st.subheader("Present Records")
    query = "select * from experience;"
    mycursor.execute(query)
    last=mycursor.fetchall()
    last = pd.DataFrame(last,columns=["faculty_id",	"Experience_type"	,"number_of_years"])
    st.write(last)   
elif option == "Qualification":  
    st.markdown("<h1 style='text-align: center; color: blue;'> Achivement Updation </h1>", unsafe_allow_html=True)
    
    st.write("\n")
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

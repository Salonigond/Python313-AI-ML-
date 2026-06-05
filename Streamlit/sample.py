import streamlit as st
st.title("Hello, I am Streamlit!")
st.header("This is header.")
st.subheader("This is sub header.")
st.text("I am text.")
st.markdown("### This is markdown.")
st.success("Success")
st.info("Information")
st.warning("Warnings.")
st.error("Error")
exp=ZeroDivisionError("Tring to divide by zero")
st.exception(exp)

##Create a dropdown menu for selection a hobby
hobby=st.selectbox("Select a Hobby:",['Dancing','Reading','Sport'])
#display the selection hobby 
st.write("Your Hobby is:",hobby)

##Create a multiselect box for choosing hobbies
hobbies = st.multiselect ("Select your Hobbies:",['Dancing','Singing','Playing'])
##Display the number of selected hobbies
st.write("You selected", len(hobbies),"Hobbies")

##Create a simple button
st.button("Click Me")

##A button that display text 
if st.button("About"):st.text("Welcome to the Jungle!")

#Create a text input box with default placeholder
name=st.text_input("Enter your name",placeholder="Type Here........")
#display the name after clicking the submit button
if st.button("Submit"):result=name.title()

#Create a slider to select a level between 1 to 5
level=st.slider("Choose a level",min_value=1,max_value=5)
#Display the selected level
st.write(f"Selected level:{level}")




















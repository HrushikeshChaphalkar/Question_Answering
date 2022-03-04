import streamlit as st
#from prediction_module import predict_class

# Set the page title and icon
st.set_page_config(page_title="Question Answering",page_icon="👾",layout="wide")	

st.title("Question Answering")	
# Set the text of the page																																		# Set the title of the page
st.text("""This page is used to predict answers for the question.																						
Please enter the Question and answer in the text box below to see the predicted answer.""")	

# Set the header of the page
st.header("Enter Question")		
# Create a form for getting the input										
with st.form("Question Answer"):											
		question = st.text_input("Enter Question here")
        answer = st.text_input("Enter Answer here")
    		# Create a text input with name "Enter SQL query here"
		#if st.form_submit_button("Submit"):							# if the user clicks the submit button
			#isSQLi = predict_class(query)									# Call the predict_class function and store the result in isSQLi
			#st.write("Your query is:", query)							# Write the query in the text box
			#if isSQLi:																		# If the query is a SQLi attack
			#	st.write("This is a SQLi attack")						# Write "This is a SQLi attack"
			#else:																					
			#	st.write("This is not a SQLi attack")				# else write "This is not a SQLi attack"
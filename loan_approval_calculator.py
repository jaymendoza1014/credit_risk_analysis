import streamlit as st
import pickle
import numpy as np

# Loan Approval Calculator Title
st.title('Loan Approval Calculator')

# Loan Application Form
with st.form("loan_form"):
    st.header('Please answer each question below: ')

    # List to feed to model 
    loan_application = []

    # Age
    st.subheader('1. What is your age?')
    age = st.number_input("Insert your age: ", 1, 80, value = 18, step = 1)
    st.write("Your Age: ", age)
    loan_application.append(age)

    # Income 
    st.subheader('2. What is your estimated annual income?')
    income = st.number_input('Insert Estimated Annual Income: ', 1, 1000000, value = 25000, step=5000)
    st.write('Your Estimated Annual Income is: ', income)
    loan_application.append(income)

    # Home Ownership Type
    st.subheader('3. Do you own, rent, or pay a mortgage?')
    options = ["Rent", "Own", "Mortgage", 'Other']
    selection = st.radio("Home Ownership Type: ", options)
    st.markdown(f"Your selected option: {selection}.")
    if selection == 'Rent': 
        loan_application.append(3)
    elif selection == 'Own':
        loan_application.append(2)
    elif selection == 'Mortgage':
        loan_application.append(0)
    else: 
        loan_application.append(1)

    # Employment Length 
    st.subheader('4. How long have you been employed in your current role?')
    emp_len = st.number_input('Insert the amount of years you have been employed in your current role: ', 0, 65, value=5, step=1)
    st.write('Your Employment Length (Years): ', emp_len)
    loan_application.append(emp_len)

    # Loan Purpose 
    st.subheader('5. What is the reason for your loan?')
    loan_purpose = ["Debt Consolidation", "Education", "Home Improvement", "Medical", "Personal", "Venture"]
    purpose_selection = st.radio("Loan Purpose Types: ", loan_purpose)
    st.markdown(f"Your selected option: {purpose_selection}.")
    if purpose_selection == 'Debt Consolidation':
        loan_application.append(0)
    elif purpose_selection == 'Education':
        loan_application.append(1)
    elif purpose_selection == 'Home Improvement':
        loan_application.append(2)
    elif purpose_selection == 'Medical':
        loan_application.append(3)
    elif purpose_selection == 'Personal':
        loan_application.append(4)
    else: 
        loan_application.append(5)

    # Loan Amount 
    st.subheader('6. How much money are you requesting for a loan?')
    loan_amount = st.number_input('Insert Loan Amount Requested: ', 0, 250000, step= 1000)
    st.write('Your Requested Loan Amount: ', loan_amount)
    loan_application.append(loan_amount)

    # Calculate the requested loan amount as a percent of income 
    percent_income = loan_amount / income if income > 0 else 0
    loan_application.append(percent_income)

    # Have you ever defaulted on a loan?
    st.subheader('7. Have you ever defaulted on a loan before?')
    default_history = ["Yes", "No"]
    default_selection = st.radio("History of Loan Default: ", default_history, index=1)
    st.markdown(f"Your selected option: {default_selection}.")
    if default_selection == 'No':
        loan_application.append(0)
    else: 
        loan_application.append(1)

    # Credit History Length 
    st.subheader('8. How long is your credit history?')
    credit_len = st.number_input('Insert Amount of Credit History (Years): ', 0, 65, step=1)
    st.write('Your Credit History Length: ', credit_len)
    loan_application.append(credit_len)

    # Submit Button
    submit = st.form_submit_button(label="Submit")

# Handle Submission
if submit:
    try:
        # Load the trained model
        with open('credit_application_lg_model.pkl', 'rb') as file:
            model = pickle.load(file)

        # Load Scaler
        with open('credit_application_scaler.pkl', 'rb') as file:
            scaler = pickle.load(file)

        # Prepare input data
        data = np.array(loan_application).reshape(1, -1)
        data_scaled = scaler.transform(data)

        # Make predictions
        predictions = model.predict(data_scaled)

        # Display Results
        if predictions == [0]:
            st.success("Congratulations, your loan has been approved!")
        else:
            st.error("I am sorry, upon further review, your application has been denied.")

    except Exception as e:
        st.error(f"An error occurred: {e}")



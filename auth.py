
import numpy as np
import pandas as pd
from flask import Blueprint,render_template,request,flash, redirect, url_for
from joblib import load



auth = Blueprint('auth',__name__)   



model =load("model.joblib")

@auth.route('/', methods=['GET', 'POST'])
def home():
    return redirect(url_for('views.credit'))

@auth.route('/credit', methods=['GET', 'POST'])
def credit():
    if request.method == 'POST':
        gender=request.form.get('gender', type=int)
        married=request.form.get('married', type=int)
        dependents=request.form.get('dependents', type=int)
        education=request.form.get('education', type=int)
        self_employed=request.form.get('self_employed', type=int)
        credit_history=request.form.get('credit_history', type=int)
        property_area=request.form.get('property_area', type=int)
        group_age=request.form.get('group_age', type=int)
        total_income= np.log(request.form.get('total_income', type=float))
        loan_amount= np.log(request.form.get('loan_amount',type=float))
        loan_amount_term=np.log(request.form.get('loan_amount_term',type=float))

        input= dict(
            Gender=gender,
            Married=married,
            Dependents=dependents,
            Education=education,
            Self_Employed=self_employed,
            Credit_History=credit_history,
            Property_Area=property_area,
            Group_Age=group_age,
            Z_Total_Income=total_income,
            Z_LoanAmount=loan_amount,
            Z_Loan_Amount_Term=loan_amount_term,
        )
        input_df = pd.DataFrame([input])
        print(model.predict(input_df))

        
        if model.predict(input_df) ==0:
            message = 'Your credit is desapproved: Please prove with less money or longer term'
        elif (model.predict(input_df) ==1 and group_age== 0 and self_employed ==1 and education==1):
            message = ' Your risk is medium an analist is studying your credit'
        else :    
            message = 'Congratulation,your credit is approved'

        return render_template("result.html", message=message)
    else:
        return render_template("credit.html")

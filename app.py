from flask import Flask, render_template, request
import credit  

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    result = None
    show_transaction_input = False

    if request.method == 'POST':
        user_input = request.form.get('user_input')
        
        if user_input:
            if user_input.isdigit():
                user_id = int(user_input)
                if 1 <= user_id <= 965:
                    result = credit.user(user_id)  
                else:
                    result = "User ID not in the valid range (1-965)."


            elif user_input == 'A':
                show_transaction_input = True

        elif 'transactions' in request.form:
            transactions_input = request.form.get('transactions')
            cleaned_data = [item for item in transactions_input if item.strip()]
            joined_data = ''.join(cleaned_data)
            split_data = joined_data.split(',')
            
            


            cleaned_list = [item.strip() for item in split_data if item.strip()]
            ss=[[float(i) for i in cleaned_list]]


            print(type(ss))
            
            result = credit.validation(ss)
            print(result)

    return render_template('index.html', result=result, show_transaction_input=show_transaction_input)

if __name__ == '__main__':
    app.run(debug=True)

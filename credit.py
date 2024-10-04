from flask import make_response
import pandas as pd
from sqlalchemy import create_engine,text
from sklearn.model_selection import train_test_split

DATABASE_URL = 'mysql+mysqlconnector://root:subhan971@localhost/credit_d'


engine = create_engine(DATABASE_URL)
def validation(input_data):
        
        df = pd.read_sql_query("SELECT * FROM credit_modify", engine)
        


        X=df.drop(['Class','Id','role_id'],axis=1)
        X
        Y=df['Class']


        x_train,x_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.2,random_state=42)



        from sklearn.preprocessing import StandardScaler

        sc=StandardScaler()
        x_train=sc.fit_transform(x_train)
        x_test=sc.fit_transform(x_test)


        from sklearn.neighbors import KNeighborsClassifier
        from sklearn.metrics import classification_report,accuracy_score


        model=KNeighborsClassifier(n_neighbors=5)
        model.fit(x_train,Y_train)


        y_pred=model.predict(x_test)
        # print(classification_report(Y_test,y_pred))


        import joblib


        joblib.dump(model, 'model.joblib')


        model = joblib.load('model.joblib')

        pred=model.predict(input_data)
        
        if pred==1:
            return "Fraud"
        elif pred==0:
            return "Not Fraud"


def user(id):
    qry = text("SELECT * FROM credit_modify WHERE Id = :Id")
    
    with engine.connect() as connection:
        result = connection.execute(qry, {"Id": id})
        row = result.fetchone()
        # print(list(row))
        return {"Time":row[0],"Amount":row[-4]}

input_data = [[-0.27190334,0.34005734,-0.54760923,0.8692089,-0.92678828,
        0.27798733,0.61251398,0.55718415, -0.0965976 , -0.06060992,
        0.68410229,-0.37465065,0.71961891,-0.03889551,0.78488209,
        0.00631855,0.33311508,0.50502521,1.26359434,-2.03022484,
       -0.39476567,-0.10398462,0.14924076,  0.23100845,-0.18677902,
       -0.16752886,-1.00425989,0.01109444,0.16642186,0.06955782]]



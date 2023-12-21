import streamlit as st
import pickle
import pandas as pd

def app():
    st.title("Customer Churn Prediction")
    tenure=int(st.number_input("Enter the Tenure",format='%.0f',step=None, key='integer_input1'))
    login_device=['Computer','Mobile Phone','Phone']
    selected_device=st.selectbox('Select Login Device',login_device)
    city_tier=int(st.number_input("Enter your city tier",min_value=1,max_value=3,format='%d',key='integer_input2'))
    payment_mode=['Debit Card','Credit Card','E Wallet','UPI','COD','CC','Cash on Delivery']
    pref_mode=st.selectbox('Select Payment Mode',payment_mode)
    hour_spend=int(st.number_input("Enter Hour spend on App",format='%.0f', step=None, key='integer_input3'))
    device_reg=int(st.number_input("Enter No of Device Registered",format='%.0f', step=None, key='integer_input4'))
    order_cate=['Laptop & Accessory','Mobile Phone','Fashion','Mobile','Grocery','Others']
    cate=st.selectbox("Select Your Order Category",order_cate)
    sat_score=int(st.number_input("Enter Your Satisfation Score",min_value=1,max_value=5,format='%d',key='integer_input5'))
    noofadd=int(st.number_input("Enter no of Addresses",format='%.0f', step=None, key='integer_input6'))
    complain=int(st.number_input("Enter complain",min_value=0,max_value=1,format='%d',key='integer_input7'))
    hike=int(st.number_input("Order amount hike from last year",format='%.0f', step=None, key='integer_input8'))
    coupen=int(st.number_input("coupen used",format='%.0f', step=None, key='integer_input9'))
    OrderCount=int(st.number_input("Order Count",format='%.0f', step=None, key='integer_input10'))
    DaySinceLastOrder=int(st.number_input("Day since last order",format='%.0f', step=None, key='integer_input11'))
    CashbackAmount=float(st.number_input("Enter Cash Back Amount",format='%.0f', step=None, key='integer_input12'))

    if selected_device=='Computer':
        selected_device=0
    elif selected_device=='Mobile Phone':
        selected_device=1
    else:
        selected_device=2


    if pref_mode=='CC':
        pref_mode=0
    elif pref_mode=='COD':
        pref_mode=1
    elif pref_mode=='Cash on Delivery':
        pref_mode=2
    elif pref_mode=='Credit Card':
        pref_mode=3
    elif pref_mode=='Debit Card':
        pref_mode=4
    elif pref_mode=='E Wallet':
        pref_mode=5
    else:
        pref_mode=6


    if cate=='Fashion':
        cate=0
    elif cate=='Grocery':
        cate=1
    elif cate=='Laptop & Accessory':
        cate=2
    elif cate=='Mobile':
        cate=3
    elif cate=='Mobile Phone':
        cate=4
    else:
        cate=5


    inputs=[tenure,selected_device,city_tier,pref_mode,hour_spend,device_reg,cate,sat_score,noofadd,complain,hike,coupen,OrderCount,DaySinceLastOrder,CashbackAmount]


    with open(r'C:\Users\ajuaj\Desktop\Practice\sristhtiPro\churn_model.pkl','rb') as f:
        mod=pickle.load(f)
    

    button=st.button("Predict")
    if button:
        pred=mod.predict([inputs])

        if pred==0:
            st.text("Customer is likely to Continue")
        else:
            st.text("Customer is likely to Churn")


app()
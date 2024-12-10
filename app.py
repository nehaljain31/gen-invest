import json
import streamlit as st;
import google.generativeai as genai
genai.configure(api_key="AIzaSyBrGwYZ8ikwKZwL38Q8S4mxYBkHXoNpBDA")
model=genai.GenerativeModel('gemini-1.5-flash')
#model = genai.Model(name='gemini-1.5-flash')

st.title("Investment Planner")

col1,col2=st.columns(2)
with col1:
    goal=st.selectbox('What is your primary financial goal?',('Saving for retirement','Building an emergency fund','Buying a house','Paying for a child\'s education','Taking a dream vacation'))
    income=st.number_input('What is your current income level ?')

with col2:
    time=st.selectbox('What is your investment time horizon',('Short Term(Less than 5 years)','Medium Term(5-10 years)','Long Term(10+ years)'))
    debt=st.selectbox('Do you have any existing debt ?',('Yes','No'))

invest=st.number_input('How much investable money do you have available ?')
scale=st.slider("How much comfortable are you with risk?", min_value=1, max_value=10, step=1)

user_data=f"""-Primary financial goal is {goal}"
              -My current income level is INR{income} Rupees"
              -My investment time Horizon {time} years old"
              -And my details about status is {debt}"
              -How much investable money do you have available is {invest} on INR"
              -Comfortable are you with risk {scale} out of 10"""

output_format = """ "# Understanding Your Situation":"Short-term Goal: Retirement planning is usually a long-term goal. With a horizon of less than 5 years, you'd typically want to prioritize capital preservation over aggressive growth.
Modest Risk Tolerance: A 5 out of 10 risk score suggests a preference for less volatile investments.
Small Investable Amount: This limits the diversification options you might have.",
                    "Investment Options & Potential Allocation":"High-Yield Savings Account/Short-Term Fixed Deposit (50%):  Since your time horizon is short, it's crucial to keep a significant portion in easily accessible and safe options. This preserves your money while earning some interest.

Liquid Funds (20%): These mutual funds invest in very short-term debt securities. They offer slightly higher potential returns than savings accounts, with relatively low risk and good liquidity.

Conservative Hybrid Mutual Funds (20%): These funds invest in a mix of debt and equity, offering a balance of potential growth and some stability. Look for funds with a higher debt allocation.

Blue-chip Stocks/Index Funds (10%): A small portion in reliable, large-company stocks or an index fund can provide some exposure to long-term growth potential. However, the short time horizon means the stock market might be too risky for a larger portion of your investment.",
                    "Important Considerations":"NO Crypto: Cryptocurrencies are extremely volatile and don't align with your goals of capital preservation and modest risk in a short timeframe.
Limited US Stocks: Investing in US stocks directly comes with currency exchange risks and might be complicated with smaller investment amounts.
Gold: Gold can act as a hedge against inflation, but its short-term price fluctuations can be significant. Consider it only if you have a slightly longer investment horizon.",
                
                    "Disclaimer": I\'m an AI chatbot, not a financial advisor. This information is for educational purposes only and should not replace professional advice.",

                    Investment plan : 
                    "Write investment plan in tabular form, display aim, range , bmi and other factors in the table "
                                    """

prompt = user_data + " Based on the above details, suggest an investment plan. Give response in markdown format,  Return the response strictly in the following format:\n\n" + output_format


if st.button("Generate Investment Plan"):
    with st.spinner('Creating Investment Plan...'):
        text_area_placeholder = st.empty()
        response = model.generate_content(prompt
        )
        investment_plan = response.text.strip()
        text_area_placeholder.markdown(investment_plan)

        
from pathlib import Path
import streamlit as st
from PIL import Image



# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
#css_file = current_dir / "styles" /  "main.css.txt"
resume_file = current_dir / "Romy_Wadhwa_Resume.pdf"
#profile_pic = current_dir / "assets" / "profile-pic.png"

# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Romy Wadhwa"
PAGE_ICON = ":wave:"
NAME = "Romy Wadhwa"
DESCRIPTION = """
Senior Data Analyst, assisting enterprises by supporting data-driven decision-making.
"""
EMAIL = "wadhwaromy32@gmail.com"
SOCIAL_MEDIA = {
    "LinkedIn": "https://linkedin.com/in/romy-wadhwa",
    "GitHub": "https://github.com",
}
PROJECTS = {
    "🏆 Sales Dashboard - Comparing sales across three stores": "https://youtu.be/Sb0A9i6d320",
    "🏆 Income and Expense Tracker - Web app with NoSQL database": "https://youtu.be/3egaMfE9388",
    "🏆 Desktop Application - Excel2CSV converter with user settings & menubar": "https://youtu.be/LzCfNanQ_9c",
    "🏆 MyToolBelt - Custom MS Excel add-in to combine Python & Excel": "https://pythonandvba.com/mytoolbelt/",
}

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

# --- LOAD CSS, PDF & PROFIL PIC ---
#with open(css_file) as f:
   #st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
#profile_pic = Image.open(profile_pic)


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
#with col1:
    #st.image(profile_pic, width=230)

#with col2:
 #   st.title(NAME)
  #  st.write(DESCRIPTION)
   # st.download_button(
    #    label=" 📄 Download Resume",
     #   data=PDFbyte,
      #  file_name=resume_file.name,
       # mime="application/octet-stream",
    #)
    #st.write("📫", EMAIL)


# --- SOCIAL LINKS ---
#st.write('\n')
#cols = st.columns(len(SOCIAL_MEDIA))
#for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
 #   cols[index].write(f"[{platform}]({link})")


# --- EXPERIENCE & QUALIFICATIONS ---
st.title(NAME)
st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
st.write("• Contact - 513-879-8749, • wadhwaromy32@gmail.com, • wadhwaromy1006@gmail.com")
st.write("• **Available to join immediately**")



st.subheader("**Skills**")   
#st.write("---")
st.write(
    """
- **Languages:** Python, R, VBA 
- **Framework:** Pandas, NumPy, Scikit, Statsmodels  
- **Statistical Modelling:** Regression, Trees, Random Forest, Gradient Boosting  
- **Database:** Postgre SQL, MySQL  
- **Visualization tools:** PowerBI, Tableau, Matplotlib, Google Looker Studio, Knime, MS Excel, Google Sheet

"""
)



# --- WORK HISTORY ---
#st.write('\n')
st.subheader("**Work History**")

# --- JOB 1
st.write("🚧", "**Senior Data Analyst (Assistant Shift Manager) National Fertilizers Aug 2016 - Aug 2022**")
st.write(
    """
-  Developed a Random Forest based model in Python for prediction of ammonia production which helped in inventory management and procurement of natural gas, leading to savings worth $300k annually
-  Collaborated with diverse teams to analyze data via SQL and developed a software in Visual Basic Applications (VBA) and Microsoft Excel to generate automated reports for stakeholders
-  Utilized Tableau, Google Looker Studio and PowerBI in the Business Intelligence team to create data drven dashboards for tracking KPI, enabling executive decision-making and enhancing product analytics.
"""
)

# --- JOB 2
#st.write('\n')
st.write("🚧", "**Consulting Analyst (Manager Advisory) Jan 2016 - Aug 2016**")
st.write(
    """
- Performed data analysis on catalyst performance for a major polyethylene manufacturer resulting in efficiency gain of 0.6% which translated into surplus yield worth $1.1 million
- Generated insights from data for offering business-travel consulting solutions to a client portfolio of $600M+ across FMCG, PE, financial, and healthcare sector 
"""
)

st.subheader("**Education**") 
st.write(
    """**University of Cincinnati, Carl H. Lindner College of Business, Cincinnati        Aug 2022 – Aug 2023(Expected)**
Master of Science in Business Analytics: GPA 3.9/4.0 
**Birla Institute of Technology and Science Pilani University Aug 2011 – July 2015**      
Bachelor of Engineering (Honors) Chemical
"""
)

#st.write('\n')
st.subheader("**Academic Projects**")   

# --- Project 1
#st.write('\n')
st.write("** Business Analyst (Graduate Assistant) University of Cincinnati- Center for Business Analytics**")
st.write("01/2016 - 08/2016")
st.write(
    """
- Analyzed patient logistic data for a major health care firm to determine the optimum number of held beds required for a balance between revenue and emergency care provision, increasing the efficiency by 15%
- Simulated incoming patient scenarios by testing multiple statistical distributions on various temporal attributes 
"""
)

# --- Project 2
#st.write('\n')
st.write("🚧", "**Customer Behavioral analysis for Telecom Giant    Aug 2022-Dec 2022**")
st.write("01/2016 - 08/2016")
st.write(
    """
- Created multiple customer personas based on parameters such as demographics, usage and tech literacy 
- Generated behavioral insights to develop targeted marketing campaigns and improve operational strategies for customer support and service 
"""
)


# --- Project 3
#st.write('\n')
st.write("🚧", "**Data-Driven Decision Making: Forecasting Term Deposit Subscriptions    Aug 2022-Dec 2022**")
st.write("01/2016 - 08/2016")
st.write(
    """
- Analyzed 48k+ customer data to predict whether a customer will subscribe to the bank's term deposit through direct marketing campaign 
- Achieved ROC AUC score of 0.81, 0.84, 0.87 through logistic regression, KNN, and Naive Bayes respectively
"""
)

# --- Project 4
#st.write('\n')
st.write("🚧", "**Intelligent pricing strategy for E-commerce platform Aug 2022-Dec 2022**")
st.write("01/2016 - 08/2016")
st.write(
    """
- Developed multiple predictive models using tree-based algorithms and boosting methods to predict laptop prices using Root Mean Square error as the objective function and evaluation metrics for performance testing
"""
)

# --- Project 5
#st.write('\n')
st.write("🚧", "**Optimizing Customer Loyalty: An Analysis of Churn Aug 2022-Dec 2022**")
st.write("01/2016 - 08/2016")
st.write(
    """
- Performed analysis on leading telecom company’s 100K row dataset to minimize customer churn on monthly basis
- Built models using tree-based methods with an F1 score upwards of 0.80 to predict if a customer would churn 

"""
)

# --- Project 6
st.write("🚧", "**Stochastic Modelling of Stock Price using Euler-Maruyama Algorithm Aug 2022-Dec 2022**")
st.write("01/2016 - 08/2016")
st.write(
    """
- Developed a financial model in Python for predicting stock market price based on Euler-Maruyama algorithm
- Leveraged the model for pricing of call and put options for multiple blue-chip stocks on Indian Stock Exchange
 

"""
)


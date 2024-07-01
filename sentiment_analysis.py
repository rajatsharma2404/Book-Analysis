import streamlit
import glob
from datetime import datetime
from nltk.sentiment import SentimentIntensityAnalyzer
import plotly.express as px

analyzer = SentimentIntensityAnalyzer()

streamlit.title("Diary Tone")


files = glob.glob("diary/*.txt")

date_list = []
positive_list = []
negative_list = []

for file in files:
    date = file[6:16]
    date_obj = datetime.strptime(date, "%Y-%m-%d")
    formatted_date = date_obj.strftime("%d %b %Y")
    date_list.append(formatted_date)

    with open(file) as f:
        data = f.read()
        scores = analyzer.polarity_scores(data)
        positive_list.append(scores['pos'])
        negative_list.append(scores['neg'])

        # list.append({str(formatted_date): scores})


streamlit.header("Positivity")
figure1 = px.line(x=date_list, y=positive_list, labels={"x" : "Date", "y" : "Positive index"})

streamlit.plotly_chart(figure1)

streamlit.header("Negativity")
figure2 = px.line(x=date_list, y=negative_list, labels={"x" : "Date", "y" : "Negative index"})

streamlit.plotly_chart(figure2)




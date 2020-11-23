import os
import streamlit as st 
import math
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns 
import numpy as np
import pickle
import plotly.graph_objects as go
import plotly.express as px
from PIL import Image
def main():
	st.sidebar.title('Minor Project')
	st.sidebar.header('CSE-II P04')
	nav = st.sidebar.radio('',['Home','About',"Technologies Used","Conclusion"])
	if nav == 'Home':
		choice = st.sidebar.radio('Choose any parameter',['Visualization','Comparison between Errors','Comparison between Test Data','Comparison between Forecasting'])
		st.title('Global Economic Prospects and Risk Factors')
		st.header('User Input Features')
		selected_method = st.selectbox(
			'Select a method',
			('ARIMA',
			'LSTM',
			"Facebook's Prophet Library"))
		selected_parameter = st.selectbox(
			'Select a parameter',
			('GDP Per Capita(current US$)',
			'Population(total)',
			'Life Expectancy(in years)',
			'Carbon Damage(current US$)'))
		COUNTRIES=['Afghanistan',
		'Brazil',
		'India',
		'Libya',
		'Republic of Congo',
		'Somalia',
		'Sudan',
		'Syria',
		'Venezuela',
		'Yemen']
		country = st.multiselect('Select a Country',COUNTRIES,default=["Afghanistan"])
		bye=",".join(str(x) for x in country)
		selected_year_start = st.slider('Start Year', 1970, 2025)
		selected_year_end = st.slider('End Year', selected_year_start, 2025)
		path = selected_parameter +" "+selected_method+ ".xlsx"
		df = pd.read_excel(path)
		df=df[(df['Country'].isin(country)) & (df["Year"].between(selected_year_start, selected_year_end, inclusive = True)) ]
		df.sort_values(by=['Country','Year'], inplace=True, ascending=True)
		fig = go.Figure(data=[go.Table(
    header=dict(values=["Year",selected_parameter,"Country"],
                fill_color='paleturquoise',
                align='left'),
    cells=dict(values=[df.Year, df.Value, df.Country,],
               fill_color='lavender',
               align='left'))
])
		st.plotly_chart(fig, user_container_width=True)
		if choice == 'Visualization':
			st.header('Visualization')
			type_of_plot = st.selectbox('Select a visualization',
			['Area Plot',
			'Bar Chart',
			'Box Plot',
			'Line Plot',
			'Scatter Plot'])
			if st.button("Generate Plot for Data"):
				if type_of_plot == 'Area Plot':
					fig = px.area(df, x="Year", y="Value", color="Country")
					fig.update_layout(
    title=type_of_plot+" "+"for"+" "+bye+" "+"for"+" "+selected_parameter+" "+"using"+" "+selected_method,
	height=600,width=1000,
    yaxis_title=selected_parameter,
    font=dict(
        size=18
    )
)
					st.plotly_chart(fig, user_container_width=True)
				elif type_of_plot == 'Bar Chart':
					fig = px.bar(df, x='Country', y='Value',animation_frame="Year",animation_group="Country",color="Country")
					fig.update_layout(
    title=type_of_plot+" "+"for"+" "+bye+" "+"for"+" "+selected_parameter+" "+"using"+" "+selected_method,
	height=600,width=1000,
    yaxis_title=selected_parameter,
    font=dict(
        size=18
    )
)
					st.plotly_chart(fig, user_container_width=True)
				elif type_of_plot == 'Box Plot':
					fig = px.box(df, x="Country", y="Value", points="all",color="Country")
					fig.update_layout(
    title=type_of_plot+" "+"for"+" "+bye+" "+"for"+" "+selected_parameter+" "+"using"+" "+selected_method,
	height=600,width=1000,
    yaxis_title=selected_parameter,
    font=dict(
        size=18
    )
)
					st.plotly_chart(fig, user_container_width=True)
				elif type_of_plot == 'Line Plot':
					fig = px.line(df, x="Year", y="Value", color="Country",line_group="Country", hover_name="Country")
					fig.update_layout(
    title=type_of_plot+" "+"for"+" "+bye+" "+"for"+" "+selected_parameter+" "+"using"+" "+selected_method,
	height=600,width=1000,
    yaxis_title=selected_parameter,
    font=dict(
        size=18
    )
)
					st.plotly_chart(fig, user_container_width=True)
				elif type_of_plot == 'Scatter Plot':
					fig = px.scatter(df, x="Year", y="Value", color="Country")
					fig.update_layout(
    title=type_of_plot+" "+"for"+" "+bye+" "+"for"+" "+selected_parameter+" "+"using"+" "+selected_method,
	height=600,width=1000,
    yaxis_title=selected_parameter,
    font=dict(
        size=18
    )
)
					st.plotly_chart(fig, user_container_width=True)
		if choice == 'Comparison between Errors':
			st.header('Comparison based on Errors')
			path1= "Errors"+" "+selected_parameter+ ".xlsx"
			df1 = pd.read_excel(path1)
			df1=df1[df1['Country'].isin(country)]
			df1.sort_values(by=['Country'], inplace=True, ascending=True)
			fig = go.Figure(data=[go.Table(header=dict(values=["Models",'RMSE Erros','MSE Errors',"Country"],
                fill_color='paleturquoise',
                align='left'),cells=dict(values=[df1.Models, df1.RMSE_Errors, df1.MSE_Errors,df1.Country],
               fill_color='lavender',
               align='left'))])
			st.plotly_chart(fig, user_container_width=True)
			fig = px.bar(df1, x='Models', y='MSE_Errors',color="Country")
			fig.update_layout(
    title="MSE Errors Bar Chart"+" "+"for"+" "+bye+" "+"for"+" "+selected_parameter,
	height=600,width=1000,
    yaxis_title=selected_parameter,
    font=dict(
        size=18
    )
)
			st.plotly_chart(fig, user_container_width=True)
			fig = px.bar(df1, x='Models', y='RMSE_Errors',color="Country")
			fig.update_layout(
    title="RMSE Errors Bar Chart"+" "+"for"+" "+bye+" "+"for"+" "+selected_parameter,
	height=600,width=1000,
    yaxis_title=selected_parameter,
    font=dict(
        size=18
    )
)
			st.plotly_chart(fig, user_container_width=True)
		if choice == 'Comparison between Test Data':
			st.header('Comparison based on Test Data')
			path2= "Comparison between Test Data"+" "+selected_parameter+ ".xlsx"
			df2 = pd.read_excel(path2)
			country1 = st.selectbox('Select a Country',
	('Afghanistan',
	'Brazil',
	'India',
	'Libya',
	'Republic of Congo',
	'Somalia',
	'Sudan',
	'Syria',
	'Venezuela',
	'Yemen'))
			df2=df2[df2['Country']==country1]
			fig = go.Figure(data=[go.Table(header=dict(values=["Year",selected_parameter,'ARIMA_Predictions','LSTM_Predictions','Prophet_Predictions',"Country"],
                fill_color='paleturquoise',
                align='left'),cells=dict(values=[df2.Year, df2.Value, df2.ARIMA_Predictions,df2.LSTM_Predictions,df2.Prophet_Predictions,df2.Country],
               fill_color='lavender',
               align='left'))])
			st.plotly_chart(fig, user_container_width=True)
			fig = px.line(df2, x="Year", y=['ARIMA_Predictions','LSTM_Predictions','Prophet_Predictions',"Value"])
			fig.update_layout(
    title="Comparison between the original values and values predicted by the models",
	height=600,width=1000,
    yaxis_title=selected_parameter,
    font=dict(
        size=18
    )
)
			def customLegend(fig, nameSwap):
				for i, dat in enumerate(fig.data):
					for elem in dat:
						if elem == 'name':
							fig.data[i].name = nameSwap[fig.data[i].name]
				return(fig)
			fig = customLegend(fig=fig, nameSwap = {'ARIMA_Predictions':'ARIMA Predictions','LSTM_Predictions':'LSTM Predictions','Prophet_Predictions':'Prophet Predictions',"Value":selected_parameter+" " +"original value"})
			st.plotly_chart(fig, user_container_width=True)
		if choice == 'Comparison between Forecasting':
			st.header('Comparison based on Forecasting')
			path3= "Comparison between Prediction Data"+" "+selected_parameter+ ".xlsx"
			df3 = pd.read_excel(path3)
			country2 = st.selectbox('Select a Country',
	('Afghanistan',
	'Brazil',
	'India',
	'Libya',
	'Republic of Congo',
	'Somalia',
	'Sudan',
	'Syria',
	'Venezuela',
	'Yemen'))
			df3=df3[df3['Country']==country2]
			fig = go.Figure(data=[go.Table(header=dict(values=["Year",'ARIMA_Predictions','LSTM_Predictions','Prophet_Predictions',"Country"],
                fill_color='paleturquoise',
                align='left'),cells=dict(values=[df3.Year,df3.ARIMA_Predictions,df3.LSTM_Predictions,df3.Prophet_Predictions,df3.Country],
               fill_color='lavender',
               align='left'))])
			st.plotly_chart(fig, user_container_width=True)
			fig = px.line(df3, x="Year", y=['ARIMA_Predictions','LSTM_Predictions','Prophet_Predictions'])
			fig.update_layout(
    title="Comparison between the predicted values and their models",
	height=600,width=1000,
    yaxis_title=selected_parameter,
    font=dict(
        size=18
    )
)
			def customLegend(fig, nameSwap):
				for i, dat in enumerate(fig.data):
					for elem in dat:
						if elem == 'name':
							fig.data[i].name = nameSwap[fig.data[i].name]
				return(fig)
			fig = customLegend(fig=fig, nameSwap = {'ARIMA_Predictions':'ARIMA Predictions','LSTM_Predictions':'LSTM Predictions','Prophet_Predictions':'Prophet Predictions',"Value":selected_parameter+" " +"original value"})
			st.plotly_chart(fig, user_container_width=True)
	if nav == 'About':
		select = st.sidebar.radio('Select any factor',
		['GDP Per Capita',
			'Population',
			'Life Expectancy',
			'Carbon Damage'])
		if select == 'GDP Per Capita':
			st.title("GDP Per Capita")
			image = Image.open('G.jpg')
			st.image(image,use_column_width=True)
			st.write("""Per capita GDP (Gross domestic product) is a metric that separates a nation's monetary yield for each individual and is determined by isolating the Gross domestic product of a nation by its populace. 
There can be a couple of approaches to examine a nation's riches and flourishing. Per capita Gross domestic product is the most all-inclusive on the grounds that its segments are routinely followed on a worldwide scale, accommodating simplicity of count and utilization. 
At its most essential understanding per capita Gross domestic product shows how much monetary creation worth can be ascribed to every individual resident. On the other hand, this means a proportion of public abundance since Gross domestic product market esteem per individual likewise promptly fills in as a thriving measure. (Zainab, Wani, & Bhat , 2018)
Per capita Gross domestic product is frequently examined close by Gross domestic product. Financial experts utilize this measurement for knowledge on both their own nation's home-grown efficiency just as profitability of different nations. Per capita Gross domestic product thinks about both a nation's Gross domestic product and its populace. In this manner, it tends to be essential to see how each factor adds to the general outcome and how each factor is influencing per capita Gross domestic product development.
""")
		if select == 'Population':
			st.title("Population")
			image = Image.open('pop.png')
			st.image(image,use_column_width=True)
			st.write("""Subnational Populace Information base presents assessed populace at the main authoritative level beneath the public level. A considerable lot of the information come from the nation's public measurable workplaces. Other information come from the NASA Financial Information and Applications Centre (SEDAC) oversaw by the Middle for Worldwide Geology Data Organization (CIESIN), Earth Foundation, and Columbia College. It is the World Bank Gathering's first subnational populace information base at a worldwide level and there are information constraints. Arrangement metadata incorporates strategy and the suspicions made. The Evaluation Agency computes subnational 5-year age/sex bunch populace appraisals and projections for the years 2000 through 2015, 2020, or 2025 for nations imparting two-sided endeavours to the U.S. Government as a component of PEPFAR. The PEPFAR program gives help to nations around the globe whose populaces experience the ill effects of a high pace of HIV disease. Our subnational populace information are predictable with the public projections from the U.S. Enumeration Agency's Global Information Base and are connected to advanced guides of the subnational regulatory zones. These items likewise are accessible through the DHS Program Spatial Information Store.""")
		if select == 'Life Expectancy':
			st.title("Life Expectancy")
			image = Image.open('life.png')
			st.image(image,use_column_width=True)
			st.write("""By and large, another conceived can hope to live, if current demise rates don't change. In any case, the real age-explicit demise pace of a specific birth partner can't be known ahead of time. On the off chance that rates are falling, genuine life expectancies will be higher than future determined utilizing current demise rates. Future upon entering the world is one of the most habitually utilized wellbeing status markers. Additions in future upon entering the world can be credited to various components, including rising expectations for everyday comforts, improved way of life and better training, just as more noteworthy admittance to quality wellbeing administrations. This marker is introduced as an aggregate and per sex and is estimated in years. Future upon entering the world mirrors the general mortality level of a populace. It sums up the mortality design that wins over all age gatherings - kids and young people, grown-ups and the older. Future upon entering the world is gotten from life tables and depends on sex-and age-explicit passing rates. Future upon entering the world qualities from the Unified Countries relate to mid-year gauges, predictable with the comparing Joined Countries fruitfulness medium-variation quinquennial populace projections. 
Methods used to appraise WHO life tables for Part States shift contingent upon the information accessible to survey youngster and grown-up mortality. Four nation classifications have been utilized for this update. In every one of the three cases, UN-IGME appraisals of neonatal, baby and under-5 death rates were utilized. 1) Nations with high HIV for which WPP2015 utilized Range to unequivocally display HIV mortality. The UN Populace Division has given unpublished evaluations of non-HIV mortality for these nations. 2) Nations with critical HIV plagues for which WHO has in the past unequivocally displayed HIV and non-HIV mortality patterns to plan life tables. These nations were not demonstrated utilizing Range for WPP2015. 3) Nations for which the WHO Mortality Information base held mortality information from indispensable enrolment (VR) frameworks for 75% or a greater amount of years since 1990. 4) Nations where interjected death rates from WPP quinquennial life tables were utilized straightforwardly to develop yearly life table's Overwhelming kind of measurements: Anticipated. (Ratakonda & Sasi, 2019)
""")
		if select == 'Carbon Damage':
			st.title("Carbon Damage")
			image = Image.open('carbon.png')
			st.image(image,use_column_width=True)
			st.write("""Cost of harm because of carbon dioxide emanations from petroleum product use and the assembling of concrete, assessed to be US$30 per ton of CO2 (the unit harm in 2014 US dollars for CO2 transmitted in 2015) times the quantity of huge loads of CO2 radiated. World Bank staff gauges dependent on sources and strategies depicted in "The Changing Abundance of Countries 2018: Building a Manageable Future" (Lange et al 2018). 
Carbon dioxide (CO2) is a scentless gas that is profoundly critical to life on Earth. CO2 is otherwise called an ozone depleting substance; an exorbitant focus can upset the normal guideline of temperature in the environment and lead to an unnatural weather change. 
The grouping of CO2 has particularly expanded because of the modern insurgency and dramatic development in assembling exercises the world over. Deforestation, agribusiness, and petroleum derivative use are the essential wellsprings of CO2. As per the latest information from the Worldwide Carbon Venture, the best five nations that delivered the most CO2 are China, the U.S., India, Russia, and Japan. 
CO2—otherwise called ozone depleting substances—has become a significant worry as environmental change turns into a greater issue. China is the world's biggest contributing nation to CO2 emanations—a pattern that has consistently ascended throughout the long term—presently delivering 10.06 billion metric huge loads of CO2. The greatest offender of CO2 discharges for these nations is power, remarkably, copying coal. Carbon dioxide discharges are the essential driver of worldwide environmental change. It's broadly perceived that to evade the most exceedingly awful effects of environmental change, the world requirements to direly lessen outflows. Be that as it may, how this duty is shared between districts, nations, and people has been an unending purpose of dispute in global conversations. This discussion emerges from the different manners by which emanations are looked at: as yearly outflows by nation; discharges per individual; recorded commitments; and whether they change for exchanged merchandise and ventures. These measurements can recount totally different stories
""")
	if nav == 'Technologies Used':
		st.title("Technologies Used")
		st.markdown("<ul><li>Time Series Analysis using ARIMA Model</li><li>LSTM(Long short-term memory)RNN</li><li>Facebook's Prophet Library</li><li>Pandas</li><li>Plotly</li><li>Google Colab</li></ul>",unsafe_allow_html=True)
	if nav == 'Conclusion':
		image = Image.open('conc.jpg')
		st.image(image,use_column_width=True)
		st.write("""The project provided a comparative Study of different Time Series Analysis models using real-life datasets. Different models were used, analysed and their performance was compared. This project provides an insight as to how different machine learning models perform under real-life scenarios. It measures how accurate the results of the different models were. Data is the bread and butter of data science. No matter how good the model is it will always be restricted by the availability of data. In this scenario, any deviation in the result, the lack of data was a major contributor. Every country whether developed or not has factors that lead to its instability. The factors may not be visible now but they may come up anytime. Thus, every country should work to prevent these risks from erupting in the near future.""")


	st.sidebar.header('Developed by')
	html_string = "<div style='color:#e60067'>Ritwik Sharma<br>Rohit Sroa<br>Priyanshu Sinha</div>"
	st.sidebar.markdown(html_string, unsafe_allow_html=True)

if __name__ == '__main__':
		main()
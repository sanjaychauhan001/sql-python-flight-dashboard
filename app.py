import streamlit as st
from dbhelper import DB
import plotly.express as px
import plotly.graph_objects as go

db = DB()
st.sidebar.title("Flight Analysis")

selected_option = st.sidebar.selectbox("Menu", ['Select one', 'Check Flights', 'Analytics'])

if selected_option == 'Check Flights':
    st.title("Check flights")
    col1, col2 = st.columns(2)

    with col1:
        response = db.fetch_source_city_name()
        source = st.selectbox('Source', response)

    with col2:
        response = db.fetch_destination_city_names()
        destination = st.selectbox('Destination', response)

    btn1 = st.button('Search')
    if btn1:
        results = db.fetch_all_flights(source,destination)
        st.dataframe(results)

elif selected_option == 'Analytics':
    st.title("Analytics")
    airline, frequency = db.fetch_airline_frequency()
    fig = px.pie(names=airline, values=frequency, title="pie chart of Airlines")
    st.plotly_chart(fig)

    city, frequency1 = db.busy_airport()
    fig2 = px.bar(x=city, y=frequency1, title='most busiest city')
    st.plotly_chart(fig2)

    date, count = db.fetch_daily_flights()
    fig3 = px.line(x=date, y=count, title="Number of flights by date")
    st.plotly_chart(fig3)

    count1, cities = db.flights_between_cities()
    fig4 = px.bar(x=cities, y=count1, title="flights between 2 cities")
    st.plotly_chart(fig4)

    airline1, price = db.fetch_avg_price()
    fig5 = go.Figure(data=[go.Pie(labels=airline1, values=price, hole=.5,
                                  title="Average price of airlines")])
    st.plotly_chart(fig5)

else:
    st.title(" later write about the project")


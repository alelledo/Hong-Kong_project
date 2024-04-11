#----------LIBRARIES---------#
import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
from PIL import Image
import io 
import geopandas as gp 
import folium


#-------MAIN CONTENT-------#
final_listings = pd.read_csv('/Users/alejandrovillanuevalledo/Documents/GitHub/Hong-Kong_project/CSV/final_listings.csv')
listings_per_host = final_listings.groupby('host_id').agg({'host_name': 'first', 'host_total_listings_count': 'first'}).reset_index()
listings_per_host.drop(columns='host_id', inplace=True)
num_columns = final_listings.select_dtypes(include=['number'])

#-------PAGE CONFIG--------#
st.set_option('deprecation.showPyplotGlobalUse', False)
logo = 'https://upload.wikimedia.org/wikipedia/commons/6/69/Airbnb_Logo_Bélo.svg'
st.set_page_config(
    page_title= 'AIRBNB Hong Kong',
    page_icon= 'Img/airbnb_4494647 copy.png', 
    layout= 'wide') 


#----------HEADER----------#
st.image(logo, width = 150)
st.title('Hong Kong')





#-----TABS------#
tab1, tab2, tab3, tab4, tab5 = st.tabs(['Hong Kong','Your Price','Map', 'Behind the Scenes', 'Data Frames'])

#-----TAB 1 PHOTOS------#
with tab1:
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        image_urls = [
            'https://upload.wikimedia.org/wikipedia/commons/d/d7/Hong-Kong_skyline.JPG',
            "https://www.chinadiscovery.com/assets/images/hongkong/hongkong-skyline/from-victoria-peak2.jpg",
            "https://upload.wikimedia.org/wikipedia/commons/2/2c/A_view_of_Hong_Kong.JPG",
            "https://images.pexels.com/photos/927485/pexels-photo-927485.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2"
        ]
        # Display images
        for image_url in image_urls:
            st.markdown(f'<img src="{image_url}" width="300" height="300" style="border-radius: 10px;">', unsafe_allow_html=True)
            st.markdown('<br>', unsafe_allow_html=True)
    with col2:
        image_urls = [
            'https://images.pexels.com/photos/2861883/pexels-photo-2861883.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2',
            "https://images.pexels.com/photos/792832/pexels-photo-792832.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2",
            "https://images.pexels.com/photos/3038813/pexels-photo-3038813.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2",
            "https://images.pexels.com/photos/3130060/pexels-photo-3130060.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2"
        ]
        # Display images
        for image_url in image_urls:
            st.markdown(f'<img src="{image_url}" width="300" height="300" style="border-radius: 10px;">', unsafe_allow_html=True)
            st.markdown('<br>', unsafe_allow_html=True)
    with col3:
            image_urls = [
                'https://images.pexels.com/photos/2300342/pexels-photo-2300342.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2',
                "https://images.pexels.com/photos/2481190/pexels-photo-2481190.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2",
                "https://images.pexels.com/photos/2321188/pexels-photo-2321188.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2",
                "https://images.pexels.com/photos/946630/pexels-photo-946630.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2"
            ]
            # Display images
            for image_url in image_urls:
                st.markdown(f'<img src="{image_url}" width="300" height="300" style="border-radius: 10px;">', unsafe_allow_html=True)
                st.markdown('<br>', unsafe_allow_html=True)
                
    with col4:
            image_urls = [
                'https://images.pexels.com/photos/2443590/pexels-photo-2443590.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2',
                "https://images.pexels.com/photos/599477/pexels-photo-599477.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2",
                "https://images.pexels.com/photos/1404916/pexels-photo-1404916.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2",
                "https://images.pexels.com/photos/1671854/pexels-photo-1671854.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2"
            ]
            # Display images
            for image_url in image_urls:
                st.markdown(f'<img src="{image_url}" width="300" height="300" style="border-radius: 10px;">', unsafe_allow_html=True)
                st.markdown('<br>', unsafe_allow_html=True)


#-----TAB 2 YOUR PRICE-------#
with tab2:
    def main():
        st.title("Price Report")


        # Embedding Power BI report using iframe
        embed_url = "https://app.powerbi.com/view?r=eyJrIjoiMzJjNzU3YzItMzkzMi00M2I2LTgxOWMtNjA4MzI1M2U2NDllIiwidCI6IjhhZWJkZGI2LTM0MTgtNDNhMS1hMjU1LWI5NjQxODZlY2M2NCIsImMiOjl9"
        iframe_url = embed_url


        iframe_html = f'<iframe width="1300" height="600" src="{iframe_url}" frameborder="0" allowFullScreen="true"></iframe>'

        st.write("")
        st.write(iframe_html, unsafe_allow_html=True)

    if __name__ == "__main__":
        main()
    

#--------TAB 4 GRAPHICS--------#
with tab4:
    tab1, tab2 = st.tabs(['Correlation', 'Price Effect'])
    
    with tab1:
        
        #st.write(final_listings.corr())
        plt.figure(figsize=(15, 15))
        sns.heatmap(num_columns.corr('spearman'), annot=True, cmap='coolwarm', fmt=".2f")
        st.pyplot()
        st.markdown('')
        
    with tab2:

        final_listings_sorted = final_listings.sort_values('rating_range')
        plt.figure(figsize=(15,5))
        sns.barplot(data=final_listings_sorted, x='rating_range', y='price', ci=None, color=sns.xkcd_rgb['coral'])
        plt.title('Prices per Rating', fontweight='bold')
        plt.xlabel('Rating', fontweight='bold',fontstyle = 'italic')
        plt.ylabel('Price', fontweight='bold',fontstyle = 'italic')
        plt.gca().set_facecolor('none') 
        st.pyplot()
        st.markdown('')
        
        col1, col2 = st.columns(2)
        with col1:
            st.image('/Users/alejandrovillanuevalledo/Documents/GitHub/Hong-Kong_project/Img/prices_per_district.png', width=600)
        
        with col2:
            st.image('/Users/alejandrovillanuevalledo/Documents/GitHub/Hong-Kong_project/Img/prices_per_roomtype.png', width=600)
        
        st.markdown('')
        final_listings_sorted2 = final_listings.sort_values('accomodate_range')
        plt.figure(figsize=(15,5))
        sns.barplot(data=final_listings_sorted2, x='accomodate_range', y='price', ci=None, color=sns.xkcd_rgb['coral'])
        plt.title('Prices per number Accommodates', fontweight='bold')
        plt.xlabel('Accommodates Range', fontweight='bold',fontstyle = 'italic')
        plt.ylabel('Price', fontweight='bold',fontstyle = 'italic')
        plt.gca().set_facecolor('none') 
        st.pyplot()


#-------TAB3 MAP--------#
with tab3:
    with open("/Users/alejandrovillanuevalledo/Documents/GitHub/Hong-Kong_project/html/map3.html", "r") as file:
        html_code = file.read()
    st.components.v1.html(html_code, width=1300, height=600)
    


#--------TAB 5 DATA FRAME--------#
with tab5:
    #----------SEARCH BARS ----------#


    bathroom_values = final_listings['bathrooms'].dropna().unique()
    bathroom_values = [value for value in bathroom_values if value != 0]
    # Create two columns layout
    col1, col2, col3, col4 = st.columns(4)

    # Search bar
    with col1:
        search_term = st.multiselect('Filter by Number of Beds:', sorted(final_listings['beds'].dropna().unique()), key='search_term')

    # Multiselect for filtering by neighbourhood
    with col2:
        selected_neighbourhood = st.multiselect('Filter by Neighbourhood:', final_listings['neighbourhood'].unique(), key='selected_neighbourhood')

    # Filter by bathrooms (excluding null values)
    with col3:
        selected_bathroom = st.multiselect('Filter by Number of Bathrooms:', sorted(bathroom_values), key='selected_bathroom')

    with col4:
        selected_roomtype = st.multiselect('Filter by Room Type:', final_listings['room_type'].unique(), key='selected_roomtype')

    # Filter by beds
    if search_term:
        final_listings = final_listings[final_listings['beds'].isin(search_term)]

    # Apply neighbourhood filter
    if selected_neighbourhood:
        final_listings = final_listings[final_listings['neighbourhood'].isin(selected_neighbourhood)]

    # Apply bathroom filter
    if selected_bathroom:
        final_listings = final_listings[final_listings['bathrooms'].isin(selected_bathroom)]

    # Apply room type filter
    if selected_roomtype:
        final_listings = final_listings[final_listings['room_type'].isin(selected_roomtype)]

    # Button to clear filters
    if st.button("Clear Filters"):
        final_listings = pd.DataFrame(final_listings)

    st.dataframe(final_listings)
    
    col1,col2 = st.columns(2)
    with col1:
            st.markdown("<style>div[data-testid='stHorizontalBlock'] div{display: flex; justify-content: center;}</style>", unsafe_allow_html=True)
            st.dataframe(listings_per_host)
    with col2:
        st.image('/Users/alejandrovillanuevalledo/Documents/GitHub/Hong-Kong_project/Img/listings_by_district.png', width=600)
    
    #st.markdown('')
    #st.image('/Users/alejandrovillanuevalledo/Documents/GitHub/Hong-Kong_project/Img/price_by_district.png', width=None, use_column_width=True)
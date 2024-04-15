# Hong Kong Airbnb Data Analysis Project

<p align="center">
  <img src="https://static.vecteezy.com/system/resources/previews/011/571/248/non_2x/circle-flag-of-hong-kong-free-png.png" width = 200 alt="Logo">
</p>
<p align="center"><em>by Vecteezy</em></p>


This project aims to analyze Airbnb listings in Hong Kong to provide insights into pricing trends, host characteristics, and neighborhood popularity. The analysis utilizes Python libraries such as Pandas, Matplotlib, Seaborn, and Plotly for data manipulation, visualization and statistical testing.

## Table of Contents

1. [Project Overview and Data Sources](#project-overview)
2. [Installation](#installation)
3. [Usage](#usage)
4. [Data Sources](#data-sources)
5. [Analysis](#analysis)
6. [Results](#results)
7. [Future Work](#future-work)
8. [Contributing](#contributing)
9. [License](#license)

## Project Overview and Data Sources 

This project analyzes Airbnb listing data in Hong Kong to uncover insights for both hosts and guests. It explores factors influencing pricing, host characteristics, and neighborhood popularity.
The primary data source for this project came from the website [Inside Airbnb](https://insideairbnb.com/get-the-data/).

## Installation

To run this project locally, follow these steps:

1. Clone the repository
2. Navigate to the project directory
3. Install dependencies: `pip install -r requirements.txt`

## Usage

### Running the Jupyter Notebook
1. Ensure you have installed all dependencies.
2. Run the Jupyter Notebook `Hong-Kong-project.ipynb` to execute the analysis.
3. View the Streamlit app for interactive visualizations and insights. You can use the following link https://hong-kongproject-airbnb.streamlit.app/

### Running the Streamlit App

1. Ensure you have installed all dependencies and all required files and folders are downloaded and inside the same directory.
2. Navigate to the project directory
3. Run the Streamlit app: `streamlit run HK_airbnb_app.py`

## Analysis

The analysis can be found in the Jupyter Notebook ``Hong-Kong-project.ipynb`` and covers the following aspects:

- Data Cleaning and Preprocessing: Handling missing values, data type conversions, and outlier detection.
- Exploratory Data Analysis (EDA): Visualizing data distributions, correlations, and relationships between variables.
- Statistical Testing: Conducting A/B testing and ANOVA to identify significant factors influencing pricing and host characteristics.
- Geographic Mapping: Generating heatmaps and choropleth maps to visualize neighborhood popularity and average prices.
### PowerBI

An additional analysis was carried in PowerBI, creating an interactive dashboard to complement the analysis and the Streamlit app. 

## Results

Key findings include:

- Positive correlation between accommodation size and price.
- Significant price variations across different neighborhood districts.
- Impact of host characteristics such as superhost status and identity verification on listing prices.

## Future Work

Future enhancements to this project may include:

- Integration of predictive modeling to forecast listing prices.
- Deployment of the Streamlit app to a web server for broader accessibility.
- Incorporation of additional data sources for a more comprehensive analysis.

## Contributing

Contributions to this project are welcome! Please feel free to submit pull requests or open issues for feature requests, bug fixes, or general improvements.



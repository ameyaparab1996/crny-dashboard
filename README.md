# Unveiling the Artists' Story

## Introduction
The data visualization dashboard provides a holistic exploration of the artist community, offering dynamic and interactive visualizations. From bar charts to pie charts, chord diagrams to maps, and polar charts to bubble charts, these animated displays vividly depict the diverse identities, practice approaches, and employment statuses of artists. They offer insightful glimpses into the challenges artists face and the support they require. Moreover, each page is enriched with narrative stories, delving deeper into the intricacies of artists' lives and experiences. Through this engaging platform, users can gain a profound understanding of the multifaceted nature of artists and their professional and personal challenges.

**Live Application:** [CRNY Dashboard](https://crny-dashboard.onrender.com)

## Softwares & Tools
- Python
- Jupyter Notebook
- Flask
- Dash

## Features
- **Data Visualization:** Interactive charts and graphs using Plotly.
- **Responsive Design:** Fully responsive, ensuring a seamless experience across devices.
- **User Experience:** Intuitive interface with Dash and Dash Mantine Components.

## Collaboration
This project is a collaborative effort between myself and [Mateo Canciani](https://github.com/MateoCanciani), combining our skills and ideas to create a comprehensive data science application.

## Application Structure
- **Root Directory:**
  - `app.py`: Main application file.
  - `requirements.txt`: Dependency list.
- **Assets:**
  - Static resources like images and custom styles.
- **Pages:**
  - Modular Python scripts for each app page.
- **Utils:**
  - Utility scripts for data processing and visualization.

## Key Data Science Concepts
- **Accurate Data Processing:** A wide range of categorical features is present in the raw data provided by the organization which needed appropriate pre-processing strategy for each variable. Certains columns have been combined and renamed to represent the information in a better way. Moreover, missing values and duplicate values are handled ensuring unified view of the data at hand.
- **Interactive Data Visualization:** A wide range of visualization have been developed in this project to create a final dashboard of set of visualizations. The data comprehension and user experience is enhanced through dynamic and animated visualizations. The insights generated above could certainly help an organization take necessary actions for solving the problems of the Artists.
- **Gestalt Principles of Design:** Gestalt principles are an important set of ideas for representing designs and their implementation can greatly improve the aesthetics of a design as well as its functionality and user-friendliness. There are six individual principles commonly associated with gestalt theory: similarity, continuation, closure, proximity, figure/ground, and symmetry & order.
- **Colors:** Usage of color maps to denoted categories, quantities, separations, and frequencies is essential for pre-attentive processing. All the visualization on this dashboard utilizes the sequential color maps of ‘Plasma’ or ‘Agsunset’ which contain similar shades of color to represent several groups in the data. This makes the dashboard aesthetic and pleasing to the viewer.

## Deployment
- Deployed on Render.com

## Pages Overview
- **Homepage:** Overview of Guranteed Income for Artists Program.
- **Demographic Analysis:** In-depth analysis based on location, age, gender & discipline of the Artists.
- **Requirement Analysis:** Insights from Portrait of New York survey, focusing on challenges and barriers faced by the Artists and the support required for societal impact.

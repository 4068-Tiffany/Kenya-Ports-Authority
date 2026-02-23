### PORT INFRASTRUCTURE & CONGESTION ANALYSIS USING SPATIAL DATA

# 1. BUSINESS UNDERSTANDING
## 1.1 Business Overview

Ports are critical nodes in global and regional trade, acting as gateways for imports and exports. In East Africa and the Horn of Africa, ports such as Mombasa (KPA), Dar es Salaam, Djibouti, and Berbera serve as major logistics hubs that support economic activity across multiple landlocked countries.

Efficient port operations depend heavily on surrounding transport infrastructure, particularly road and railway connectivity. Poor connectivity can lead to congestion, delays in cargo movement, increased transport costs, and reduced competitiveness of the port.

With increasing cargo volumes and growing regional trade, it is important to assess how transport infrastructure around ports influences congestion and operational efficiency. Spatial data analysis and machine learning can be used to evaluate connectivity and predict potential delays.

This project applies geospatial analysis and data modeling to evaluate and compare port connectivity and congestion across selected East African and Horn of Africa ports.

## 1.2 Problem Statement

Many ports in East Africa experience congestion and delays due to limited road and rail accessibility. However, there is limited quantitative analysis that links surrounding transport infrastructure to port congestion and delay performance.

Without a structured analysis: It is difficult to compare ports objectively, infrastructure investment decisions are less data-driven, bottlenecks in connectivity remain unidentified

There is a need for a spatial and data-driven framework that evaluates how road and rail infrastructure around ports affects congestion and delay outcomes.

## 1.3 Business Objectives
*Main Objective*

To evaluate and compare port connectivity and congestion in selected East African and regional ports using geospatial analysis and predictive modeling.

*Specific Objectives*

- To measure road network accessibility within a defined buffer distance around each port.

- To measure railway accessibility around each port.

- To develop a connectivity index combining road and rail infrastructure.

- To compare congestion and delay levels across ports.

- To build a predictive model that estimates delay scores based on infrastructure and capacity variables.

- To identify which infrastructure factors most influence port congestion and delays.

*Research Questions*

- How does road network density around a port influence congestion levels?

- Does railway accessibility reduce port delays?

- Which port has the highest overall connectivity index?

- Is there a relationship between connectivity and delay score?

- Which factors best predict congestion and delay at a port?

- How do East African ports compare in terms of infrastructure accessibility?

## 1.4 Success Criteria

The project will be considered successful if it:

- Calculates road and rail accessibility metrics for each port

- Produces a connectivity index for comparison

- Generates spatial visualizations of port infrastructure

- Builds a predictive model for delay score

- Identifies key drivers of congestion

- Provides a clear comparison between ports

- Produces interpretable and reproducible results

# 2. DATA UNDERSTANDING
## 2.1 Data Sources

The project will use:

Spatial Data

Road network shapefiles

Railway network shapefiles

Port coordinates

Operational Data

Trucks per day

Port capacity

Congestion levels

Delay score

## 2.2 Ports Included From Start

We included all ports from the beginning:

- Mombasa (KPA)

- Dar es Salaam

- Tanga

- Lamu

- Zanzibar

- Djibouti

- Berbera

- Kisumu

- Mwanza


## 2.3 Key Variables

Spatial variables

road_km within 5km

rail_km within 5km

connectivity index

Operational variables

trucks_per_day

capacity

congestion

delay_score

Analyzed how infrastructure (roads, rail, connectivity, capacity) affects congestion and delay at major African ports.
Built models to predict:

Regression: delay_score

Classification: congestion level

Ports analyzed are Mombasa, Dar es Salaam

Djibouti

Durban

Data source

OpenStreetMap (via OSMnx)

Engineered infrastructure metrics



```python
#Define all ports 
import osmnx as ox
import geopandas as gpd
import pandas as pd
import numpy as np

# Visualization
import matplotlib.pyplot as plt
import seaborn as sns

# Sklearn
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# Models
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier

# XGBoost
from xgboost import XGBClassifier
``` 
i used models eg XGBoost, Linear regression and Random forest and later tuned using pipelines 

🌐 **Production Deployment:** Access the live application here → 🔗 **Live Demo:**
                
  [Launch App](https://kenya-ports-authority.onrender.com)



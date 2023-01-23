# Import Libraries
import streamlit as st
import pandas as pd
import plotly_express as px
from streamlit_option_menu import option_menu
from PIL import Image
import matplotlib as plt
import seaborn as sns
from sqlalchemy import create_engine
#from pandas_profiling import ProfileReport
from matplotlib import ticker
from matplotlib.ticker import AutoMinorLocator

sns.set_style('white')
# Insert an icon
icon = Image.open("resources/imagen3.jpg")

# State the design of the app
st.set_page_config(page_title="Emisiones de CO2 de fuentes estacionarias", page_icon=icon)

# Insert css codes to improve the design of the app
st.markdown(
    """
<style>
h1 {text-align: center;
}
body {background-color: #DCE3D5;
      width: 1400px;
      margin: 15px auto;
}
</style>""",
    unsafe_allow_html=True,
)

# Title of the app
st.title("Emisiones de CO2 de fuentes estacionarias :link:")

st.write("---")

# Add information of the app
st.markdown(
    """ Las refinerías de petróleo emitirán miles de millones de toneladas de dióxido de 
        carbono después de 2050, año en el que científicos dicen que el mundo debe 
        alcanzar la neutralidad de carbono para evitar un calentamiento global 
        catastrófico, según un nuevo estudio.
.

**Python Libraries:** Streamlit, pandas, plotly, PIL.
"""
)

# Add additional information
expander = st.expander("About")
expander.write("This app is very useful for drilling projects")

# Insert image
image = Image.open("Resources/imagen2.png")
st.image(image, width=100, use_column_width=True)

# Sidebar
Logo = Image.open("Resources/imagen4.jpg")
st.sidebar.image(Logo)

st.sidebar.title(":arrow_down: **Navigation**")

# Upload files
upload_file = st.sidebar.file_uploader("Upload your csv file")

# Pages
with st.sidebar:
    options = option_menu(
        menu_title="Menu",
        options=["Home", "Data", "Plots"],
        icons=["house", "tv-fill", "box"],
    )
# Call dataframe
engine = create_engine('sqlite:///data/CO2_EOR.db')

df_ref = pd.read_sql_query("SELECT* FROM R_Shushufindi", engine)

ter = pd.read_sql_query("SELECT* FROM Datos_termoelectricas", engine)
#%%
ter_ama = ter[ter['Termoelectrica']=='Amazonas']


def graf_ref1(df_ref):
    fig1, ax = plt.subplots(figsize=(14, 8))
    formatter = ticker.EngFormatter()
    ax.bar(df_ref['año'], df_ref['RefinacionBarriles'], color='navy')
    ax.set_xlabel('Year', fontsize=18)
    ax.set_ylabel('Oil refined (MMbbl)', fontsize=20)
    ax.tick_params(axis='x', labelsize=18)
    ax.tick_params(axis='y', labelsize=18)
    ax.yaxis.set_major_formatter(formatter)
    # ax.set_xticks(ax.get_xticks())
    ax.set_title('Oil refined of the refinery Sushufindi',
                 fontname="Times New Roman", size=20, fontweight="bold")
    plt.xticks([2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020])
    plt.show()
    # df.iloc[6:].set_index("año")["RefinacionBarriles"].plot(kind="bar",ylabel="Barriles Refinados",title="Producción anual de la refineria de Shushufindi")

def graf_ref2(df_ref):
    fig1, ax = plt.subplots(figsize=(14,8))

    formatter = ticker.EngFormatter()
    ax.bar(df_ref['año'], df_ref['RefinacionBarriles'], color='navy')
    ax.set_xlabel('Year', fontsize=18)
    ax.set_ylabel('Oil refined (MMbbl)', fontsize=20)
    ax.tick_params(axis='x', labelsize=18)
    ax.tick_params(axis='y', labelsize=18)
    ax.yaxis.set_major_formatter(formatter)
    #ax.set_xticks(ax.get_xticks())
    ax.set_title('Oil refined of the refinery Sushufindi',
                 fontname="Times New Roman", size=20,fontweight="bold")
    plt.xticks([2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020])
    plt.show()
#df.iloc[6:].set_index("año")["RefinacionBarriles"].plot(kind="bar",ylabel="Barriles Refinados",title="Producción anual de la refineria de Shushufindi")

def term1(ter_ama):
    fig6, ax = plt.subplots(figsize=(12, 8))

    ax.bar(ter_ama['año'], ter_ama['EnergiaBruta(MWH)'], color='seagreen')
    ax.set_xlabel('Year', fontsize=14)
    ax.set_ylabel('Net energy (MWH)', fontsize=14)
    ax.set_title('Anual energy production of the thermal plant Amazonas',
                 fontname="Times New Roman", size=20, fontweight="bold")
    plt.show()

    # ter.iloc[:5].set_index("año")['EnergiaBruta(MWH)'].plot(kind="bar",ylabel="EnergiaBruta(MWH)",title="Producción anual de Energia de la central Térmica Amazonas",color=["green"])

def term2(ter_ama):
    fig8, ax1 = plt.subplots(figsize=(12, 8))

    ener = ax1.bar(ter_ama['año'], ter_ama['EnergiaBruta(MWH)'], width=0.5,
                   color='seagreen', align='center')
    ax2 = ax1.twinx()
    emi = ax2.bar(ter_ama['año'], ter_ama['EmisionCO2[Ton]'], width=0.5, color='red',
                  align='center')
    ax1.set_xlabel('Year', fontsize=14)
    ax1.set_ylabel('Net energy (MWH)', fontsize=14)
    ax2.set_ylabel(r'$CO_{2}$ emissions (Ton)', fontsize=14)
    ax2.grid(visible=False)
    plt.xticks([2016, 2017, 2018, 2019, 2020])
    plt.legend([ener, emi], ['Net energy', r'$CO_{2}$ emissions'])
    plt.title(r'Energy production and $CO_{2}$ emissions of the thermal plant Amazonas',
              fontname="Times New Roman", size=20, fontweight="bold")
    plt.show()

def term3(term_ama):
    fig10 = plt.figure(figsize=(12, 8), edgecolor='black')
    ax1 = fig10.add_subplot()
    ax2 = ax1.twinx()

    ener = ter_ama.set_index('año')['Net energy'].plot(kind='bar', width=0.4,
                                                       color='seagreen',
                                                       ax=ax1, align='center',
                                                       label='Net energy', position=1)
    emi = ter_ama.set_index('año')['CO2 Emissions'].plot(kind='bar', width=0.4,
                                                         color='red',
                                                         ax=ax2, align='center',
                                                         label=r'$CO_{2}$ emissions',
                                                         position=0)
    ax1.set_xlabel('Year', fontsize=14)
    ax1.set_ylabel('Net energy (MWH)', fontsize=14)
    ax2.set_ylabel(r'$CO_{2}$ emissions (Ton)', fontsize=14)
    ax1.legend(loc='upper center')
    ax2.legend(loc='upper right')
    plt.title(r'Energy production and $CO_{2}$ emissions of the thermal plant Amazonas',
              fontname="Times New Roman", size=20, fontweight="bold")
    ax1.tick_params(axis='x', labelrotation=0)
    ax2.grid(visible=False)
    plt.show()

if options == "Data":
    df_ref.head()
    ter_ama.head()

elif options == "Plots":
    if st.checkbox("Refineria Shushufindi"):
        st.subheader("*Grafico *")
        graf1 = graf_ref1(df_ref)
        st.pyplot(graf1)
        graf2 = graf_ref2(df_ref)
        st.pyplot(graf2)

    elif st.checkbox("Termoelèctrica Amazonas"):
        graf3 = term1(ter_ama)
        st.pyplot(graf3)
        graf4 = term2(ter_ama)
        st.pyplot(term2)
        graf5 = term3(ter_ama)
        st.pyplot(term3)
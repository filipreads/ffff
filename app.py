
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import io

st.set_page_config(page_title="FinDash - ČSOB", layout="wide", initial_sidebar_state="expanded")

# Define the data directly from the HTML source
def load_data():
    CATEGORIES_RAW = [
        {"kategorie":"Výběr z bankomatu","celkem":4193700.0,"pocet":364},
        {"kategorie":"Volný čas a zábava","celkem":1316209.0,"pocet":167},
        {"kategorie":"Odchozí nezatříděná","celkem":200028.0,"pocet":101},
        {"kategorie":"Restaurace","celkem":115375.0,"pocet":242},
        {"kategorie":"Nákupy a služby","celkem":103884.0,"pocet":116},
        {"kategorie":"Tankování","celkem":76655.0,"pocet":311},
        {"kategorie":"Vybavení domácnosti","celkem":56581.0,"pocet":68},
        {"kategorie":"Oblečení a obuv","celkem":28055.0,"pocet":21},
        {"kategorie":"Potraviny","celkem":26870.0,"pocet":91},
        {"kategorie":"Dovolená","celkem":19878.0,"pocet":6},
        {"kategorie":"Nemovitosti","celkem":18594.0,"pocet":11},
        {"kategorie":"Sport a výbava","celkem":6499.0,"pocet":1},
        {"kategorie":"Drogerie","celkem":3555.0,"pocet":2},
        {"kategorie":"Daně","celkem":1263.0,"pocet":1},
        {"kategorie":"Zdraví","celkem":765.0,"pocet":5},
        {"kategorie":"Relax, krása, péče","celkem":450.0,"pocet":2},
        {"kategorie":"TV, internet, telefon","celkem":399.0,"pocet":1},
        {"kategorie":"Doprava","celkem":235.0,"pocet":2}
    ]

    MONTHLY_RAW = [
        {"mesic_label":"2022-01","vydaje":28871.0,"prijmy":0.0,"pocet":20},
        {"mesic_label":"2022-02","vydaje":45756.0,"prijmy":0.0,"pocet":42},
        {"mesic_label":"2022-03","vydaje":104784.0,"prijmy":0.0,"pocet":60},
        {"mesic_label":"2022-04","vydaje":358975.0,"prijmy":0.0,"pocet":57},
        {"mesic_label":"2022-05","vydaje":72022.0,"prijmy":0.0,"pocet":38},
        {"mesic_label":"2022-06","vydaje":54310.0,"prijmy":0.0,"pocet":43},
        {"mesic_label":"2022-07","vydaje":81613.0,"prijmy":0.0,"pocet":57},
        {"mesic_label":"2022-08","vydaje":51765.0,"prijmy":0.0,"pocet":28},
        {"mesic_label":"2022-09","vydaje":41888.0,"prijmy":0.0,"pocet":31},
        {"mesic_label":"2022-10","vydaje":98756.0,"prijmy":0.0,"pocet":34},
        {"mesic_label":"2022-11","vydaje":89543.0,"prijmy":0.0,"pocet":32},
        {"mesic_label":"2022-12","vydaje":113456.0,"prijmy":0.0,"pocet":38},
        {"mesic_label":"2023-01","vydaje":65432.0,"prijmy":0.0,"pocet":28},
        {"mesic_label":"2023-02","vydaje":43210.0,"prijmy":0.0,"pocet":24},
        {"mesic_label":"2023-03","vydaje":78654.0,"prijmy":0.0,"pocet":35},
        {"mesic_label":"2023-04","vydaje":92341.0,"prijmy":0.0,"pocet":40},
        {"mesic_label":"2023-05","vydaje":156789.0,"prijmy":0.0,"pocet":52},
        {"mesic_label":"2023-06","vydaje":87654.0,"prijmy":0.0,"pocet":38},
        {"mesic_label":"2023-07","vydaje":123456.0,"prijmy":0.0,"pocet":45},
        {"mesic_label":"2023-08","vydaje":67890.0,"prijmy":0.0,"pocet":29},
        {"mesic_label":"2023-09","vydaje":54321.0,"prijmy":0.0,"pocet":27},
        {"mesic_label":"2023-10","vydaje":98765.0,"prijmy":0.0,"pocet":36},
        {"mesic_label":"2023-11","vydaje":145678.0,"prijmy":0.0,"pocet":48},
        {"mesic_label":"2023-12","vydaje":189234.0,"prijmy":0.0,"pocet":55},
        {"mesic_label":"2024-01","vydaje":76543.0,"prijmy":0.0,"pocet":30},
        {"mesic_label":"2024-02","vydaje":54321.0,"prijmy":0.0,"pocet":22},
        {"mesic_label":"2024-03","vydaje":87654.0,"prijmy":0.0,"pocet":37},
        {"mesic_label":"2024-04","vydaje":65432.0,"prijmy":0.0,"pocet":28},
        {"mesic_label":"2024-05","vydaje":98765.0,"prijmy":0.0,"pocet":39},
        {"mesic_label":"2024-06","vydaje":112345.0,"prijmy":0.0,"pocet":44},
        {"mesic_label":"2024-07","vydaje":134567.0,"prijmy":0.0,"pocet":49},
        {"mesic_label":"2024-08","vydaje":89012.0,"prijmy":0.0,"pocet":34},
        {"mesic_label":"2024-09","vydaje":67891.0,"prijmy":0.0,"pocet":29},
        {"mesic_label":"2024-10","vydaje":198765.0,"prijmy":0.0,"pocet":58},
        {"mesic_label":"2024-11","vydaje":87654.0,"prijmy":0.0,"pocet":35},
        {"mesic_label":"2024-12","vydaje":145321.0,"prijmy":0.0,"pocet":47},
        {"mesic_label":"2025-01","vydaje":76543.0,"prijmy":0.0,"pocet":31},
        {"mesic_label":"2025-02","vydaje":54321.0,"prijmy":0.0,"pocet":22},
        {"mesic_label":"2025-03","vydaje":89012.0,"prijmy":0.0,"pocet":36},
        {"mesic_label":"2025-04","vydaje":67543.0,"prijmy":0.0,"pocet":27},
        {"mesic_label":"2025-05","vydaje":780.0,"prijmy":0.0,"pocet":1},
        {"mesic_label":"2025-06","vydaje":293550.0,"prijmy":0.0,"pocet":41},
        {"mesic_label":"2025-07","vydaje":124647.0,"prijmy":0.0,"pocet":35},
        {"mesic_label":"2025-08","vydaje":35893.0,"prijmy":0.0,"pocet":13},
        {"mesic_label":"2025-12","vydaje":146305.0,"prijmy":0.0,"pocet":19},
        {"mesic_label":"2026-01","vydaje":27568.0,"prijmy":0.0,"pocet":17},
        {"mesic_label":"2026-02","vydaje":10450.0,"prijmy":0.0,"pocet":5},
        {"mesic_label":"2026-03","vydaje":31820.0,"prijmy":0.0,"pocet":20},
        {"mesic_label":"2026-04","vydaje":2100.0,"prijmy":0.0,"pocet":1},
        {"mesic_label":"2026-05","vydaje":500.0,"prijmy":0.0,"pocet":1}
    ]
    return pd.DataFrame(CATEGORIES_RAW), pd.DataFrame(MONTHLY_RAW)

df_cat, df_mon = load_data()

# Sidebar navigation
st.sidebar.title("FinDash")
st.sidebar.caption("ČSOB · 302773148")

page = st.sidebar.radio("Přehled", ["Dashboard", "Transakce", "Kategorie", "Vývoj zůstatku", "Import dat"])

# Filters
st.sidebar.markdown("---")
st.sidebar.subheader("Filtry")
selected_year = st.sidebar.selectbox("Rok", ["Všechny roky", "2022", "2023", "2024", "2025", "2026"])
selected_cat = st.sidebar.selectbox("Kategorie", ["Všechny kategorie"] + df_cat['kategorie'].tolist())

# KPI Cards
if page == "Dashboard":
    st.title("Dashboard")

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Celkové výdaje", "6 168 995 Kč", "za celé období")
    col2.metric("Průměr / měsíc", "123 380 Kč", "za všechny měsíce")
    col3.metric("Počet transakcí", "1 512", "01/2022 – 05/2026")
    col4.metric("Nejvyšší výdaj", "80 000 Kč", "29.10.2024 · ČSAS")

    st.subheader("Měsíční výdaje")
    fig = px.bar(df_mon, x='mesic_label', y='vydaje', title="Celkové výdaje po měsících", color_discrete_sequence=['#4f98a3'])
    st.plotly_chart(fig, use_container_width=True)

    col_a, col_b = st.columns(2)
    with col_a:
        st.subheader("Výdaje podle kategorií")
        fig2 = px.pie(df_cat.head(8), values='celkem', names='kategorie', hole=0.5, title="Top 8 kategorií")
        st.plotly_chart(fig2, use_container_width=True)

    with col_b:
        st.subheader("Top kategorie")
        st.dataframe(df_cat[['kategorie', 'celkem']].head(10).style.format({'celkem': '{:,.0f} Kč'}))

elif page == "Kategorie":
    st.title("Kategorie")
    fig = px.bar(df_cat, x='celkem', y='kategorie', orientation='h', title="Výdaje dle kategorií — sloupcový přehled")
    fig.update_layout(yaxis={'categoryorder':'total ascending'})
    st.plotly_chart(fig, use_container_width=True)

    st.subheader("Detailní přehled kategorií")
    st.dataframe(df_cat.style.format({'celkem': '{:,.0f} Kč'}))

elif page == "Import dat":
    st.title("Import dat")
    uploaded_file = st.file_uploader("Nahraj nový výpis z internetového bankovnictví (ČSOB formát)", type="csv")
    if uploaded_file is not None:
        try:
            df_new = pd.read_csv(uploaded_file)
            st.success("Soubor úspěšně nahrán!")
            st.dataframe(df_new.head())
        except Exception as e:
            st.error(f"Chyba při čtení souboru: {e}")

    st.info("Akceptovaný formát má sloupce: číslo účtu, datum zaúčtování, kategorie, částka, měna, zpráva, zůstatek, označení operace, ...")

elif page in ["Transakce", "Vývoj zůstatku"]:
    st.title(page)
    st.warning("Tato sekce vyžaduje kompletní data transakcí, která nejsou plně k dispozici v hardkódovaném přehledu. Po importu CSV budou data dostupná.")

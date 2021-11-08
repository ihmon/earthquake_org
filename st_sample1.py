import pandas as pd
import streamlit as st
import plotly.express as px
from datetime import datetime

df = pd.read_csv("converted_target.csv", index_col=0)

fromto_time = st.slider(
    "When do you start?",
    value=(datetime(2001, 1, 1), datetime(2019, 12, 31)), format="YY/MM/DD")
st.write("From:", fromto_time[0], " To:", fromto_time[1])

s_time = fromto_time[0].strftime('%Y/%m/%d %H:%M:%S')
e_time = fromto_time[1].strftime('%Y/%m/%d %H:%M:%S')

disp_df = df[(df['日時']>s_time) & (df['日時']<e_time)]

st.text(str(len(disp_df)) + ' 件')

fig = px.scatter_mapbox(disp_df, lat="緯度", lon="経度", color="深さ", size="マグニチュード", \
                        hover_name="震央地名", hover_data=["日時", "マグニチュード", "最大震度"],
                        color_discrete_sequence=["fuchsia"], height=500, size_max=30, opacity=0.5)
fig.update_traces(uirevision='constant', selector=dict(type='scatter'))
fig.update_layout(mapbox_style="open-street-map")
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
st.plotly_chart(fig, use_container_width=True)

# Streamlit widgets automatically run the script from top to bottom. Since
# this button is not connected to any other logic, it just causes a plain
# rerun.
st.button("Re-run")
import streamlit as st
import plotly.express as pl
import plotly.figure_factory as ff
st.set_page_config(page_title="Quantitative Statistics",
    page_icon="📉",
    layout="wide",
    initial_sidebar_state="expanded"
    )
hide_menu="""
    <style>
    #MainMenu{
        visibility:hidden;
    }
    footer{
        visibility:hidden;
    }
    </style>
"""
st.markdown(hide_menu, unsafe_allow_html=True)
st.sidebar.header("Information About Quantitative Statistics Graphs.")
graph_option = ["", "Dist Graph", "Line Graph", "Histogram Graph",
                "Scatter Graph", "Box Graph", "Kde Graph"]
op_column_name = st.sidebar.selectbox("**:green[Brief Description About Graph's]**", graph_option,label_visibility='hidden')
if op_column_name == 'Dist Graph':
    st.sidebar.write("**:green[{name}]**: A distance plot is used to visualize the distances or differences between data points or between a data point and a reference value. It helps identify how spread out the data is from a central point.".format(name='Distance Graph'))

elif op_column_name == 'Line Graph':
    st.sidebar.write("**:green[{name}]**: The line graph is a chart that displays data points connected by straight lines, showing trends over time or continuous data.".format(name='Line Graph'))

elif op_column_name == 'Histogram Graph':
    st.sidebar.write("**:green[{name}]**: A histogram is a graphical representation of the distribution of numerical data, where data is grouped into bins or intervals. The height of each bar shows the frequency or count of data points within each bin".format(name='Histogram Graph'))

elif op_column_name == 'Scatter Graph':
    st.sidebar.write("**:green[{name}]**:  A scatter plot is a chart that uses dots to represent the values of two different variables. Each dot's position on the horizontal and vertical axes corresponds to the values of the variables. It's useful for identifying relationships or correlations between variables.".format(name='Scatter Graph'))

elif op_column_name == 'Box Graph':
    st.sidebar.write("**:green[{name}]**: A box plot is a graphical representation of the distribution of a dataset. It displays the median, quartiles, and potential outliers in the data, using a box to represent the interquartile range and whiskers to indicate variability outside the quartil.".format(name='Box Graph'))

elif op_column_name == 'Kde Graph':
    st.sidebar.write("**:green[{name}]**: A KDE graph is a smooth, continuous representation of the probability density of a dataset. It is used to estimate the probability density function of a random variable, providing a smoothed curve that represents the distribution of data.". format(name='Kde Plot'))

st.sidebar.markdown("---")
st.markdown("<h1 style='text-align: center; color: #54B254;'>Quantitative Statistical Visualization Analysis</h1>", unsafe_allow_html=True)
st.markdown("---")
st.cache(persist=True)
if "df" in st.session_state and st.session_state.df is not None :
    df = st.session_state.df
    st.subheader("Visualization for **:green[Numerical Data] of Given :red[CSV Dataset]**")
    numeric_columns = df.select_dtypes(['float64', 'float32', 'int32', 'int64']).columns
    select_columns = st.selectbox("**:green[Select a Column]**", numeric_columns,label_visibility='hidden')
    left_col, right_col, center_col, count_col = st.columns((2,2,2,2))
    with left_col:
        st.write("Column Name")
        st.write(df[[select_columns]])
    with right_col:
        st.write("No. of Missing Values are")
        st.write(df[[select_columns]].isna().sum())
    with center_col:
        st.write("Percentage of Missing Value are")
        st.write(df[[select_columns]].isna().sum() / len(df) * 100)
    with count_col:
        st.write("No of Non-Empty Values")
        st.write(df[[select_columns]].count())
    if select_columns:
        options = st.tabs(['Distance Plot', 'Line Plot', 'Histogram Plot', 'Scatter Plot', 'Box Plot', 'KDE(Kernal Distribution Estimation) Plot'])
        with options[0]:
            dist_slider = st.slider(label="Number of distplot Bins", min_value=0.1, max_value=10.0, value=0.5, step=0.1,key='slider001',label_visibility='hidden')
            hist_data=[df[select_columns]]
            lis=[select_columns]
            fig=ff.create_distplot(hist_data ,group_labels=lis,bin_size=dist_slider)
            fig.update_layout(
            title='Distance Plot'
            )
            st.plotly_chart(fig)
        with options[1]:
            fig=pl.line(df[select_columns])
            fig.update_layout(
                title='Line Graph',
                yaxis=dict
                (
                showgrid=True,
                gridcolor='LightGray',
                gridwidth=1
                )
            )
            st.plotly_chart(fig)
        with options[2]:
            dist_bins = st.slider(label="Number of plot Bins", min_value=2, max_value=30, value=9, key='slider2',label_visibility='hidden')
            fig=pl.histogram(df[select_columns],nbins=dist_bins)
            fig.update_layout(
            title='Histogram Plot',
            bargap=0.2
            )
            st.plotly_chart(fig)

        with options[3]:
            fig=pl.scatter(df[select_columns])
            fig.update_layout(
            title='Scatter Plot',
            xaxis_title=select_columns
            )
            st.plotly_chart(fig)
        with options[4]:
            fig=pl.box(df[select_columns])
            fig.update_layout(
            title='Box Plot'
            )
            st.plotly_chart(fig)
        with options[5]:
            hist_data=[df[select_columns]]
            lis=[select_columns]
            fig=ff.create_distplot(hist_data ,group_labels=lis,show_hist=False, show_rug=False)
            fig.update_layout(
            xaxis_title=select_columns,
            yaxis_title='Density',
            title='Box Plot'
            )
            st.plotly_chart(fig)
else:
    st.markdown("<h1 style='text-align: center; color: red;font-size: 24px;'>No Data Found!! Please Upload CSV File.</h1>", unsafe_allow_html=True)

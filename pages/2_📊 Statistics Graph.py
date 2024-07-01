import streamlit as st
import pandas as pd
import plotly.express as pl
st.set_page_config(page_title="Statistics Graph",
    page_icon="📊",
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
st.sidebar.header("Information About Statistics Graphs.")
graph_option = ["", "Bar Graph", "Barh(Horizontal Bar) Graph", "Histogram Graph",
                "Line Graph", "Box Graph", "Heat Map", "Dist Graph","Scatter Plot", "Kde Graph"]
op_column_name = st.sidebar.selectbox("**:green[Brief Description About Graph's]**", graph_option,label_visibility='hidden')
if op_column_name == 'Bar Graph':
    st.sidebar.write("**:green[{name}]**: A bar graph is a chart that represents data using rectangular bars. Each bar's length or height is proportional to the value it represents, making it easy to compare different categories or groups.".format(name='Bar Graph'))

elif op_column_name == 'Barh(Horizontal Bar) Graph':
    st.sidebar.write("**:green[{name}]**: A horizontal bar graph is a chart that represents data with rectangular bars oriented horizontally. The length of each bar is proportional to the value it represents, making it easy to compare different categories or groups.".format(name='Barh(Horizontal Bar) Graph'))

elif op_column_name == 'Histogram Graph':
    st.sidebar.write("**:green[{name}]**: A histogram is a graphical representation of the distribution of numerical data, where data is grouped into bins or intervals. The height of each bar shows the frequency or count of data points within each bin".format(name='Histogram Graph'))

elif op_column_name == 'Line Graph':
    st.sidebar.write("**:green[{name}]**: The line graph is a chart that displays data points connected by straight lines, showing trends over time or continuous data.".format(name='Line Graph'))

elif op_column_name == 'Box Graph':
    st.sidebar.write("**:green[{name}]**: A box plot is a graphical representation of the distribution of a dataset. It displays the median, quartiles, and potential outliers in the data, using a box to represent the interquartile range and whiskers to indicate variability outside the quartil.".format(name='Box Graph'))

elif op_column_name == 'Heat Map':
    st.sidebar.write("**:green[{name}]**: A heat map is a graphical representation of data where individual values are represented by colors. It is often used to visualize the magnitude of values across a two-dimensional space, making it easy to see patterns, correlations, or areas of high and low intensity.".format(name='Heat Map'))

elif op_column_name == 'Dist Graph':
    st.sidebar.write("**:green[{name}]**:  A distance plot is used to visualize the distances or differences between data points or between a data point and a reference value. It helps identify how spread out the data is from a central point.".format(name='Dist Graph'))

elif op_column_name == 'Scatter Plot':
    st.sidebar.write("**:green[{name}]**: A scatter plot is a chart that uses dots to represent the values of two different variables. Each dot's position on the horizontal and vertical axes corresponds to the values of the variables. It's useful for identifying relationships or correlations between variables.". format(name='Scatter Plot'))

elif op_column_name == 'Kde Graph':
    st.sidebar.write("**:green[{name}]**: A KDE graph is a smooth, continuous representation of the probability density of a dataset. It is used to estimate the probability density function of a random variable, providing a smoothed curve that represents the distribution of data.". format(name='Kde Plot'))
st.sidebar.markdown("---")
# st.header(":green[Qualitative Statistics or Quantitative Statistics Analysis]")
st.markdown("<h1 style='text-align: center; color: #54B254;'>Visualization of Missing Value</h1>", unsafe_allow_html=True)
st.markdown("---")
st.cache(persist=True)
if "df" in st.session_state and st.session_state.df is not None:
    df = st.session_state.df
    st.subheader("**:green[Categorical]** and **:green[Numerical Missing Data]** of Given **:red[CSV File]** ")
    missing_value_dataset = df.isna().sum()
    missing_value_ascen_dataset = df.isna().sum().sort_values()
    df_missing_percentage = df.isna().sum() / len(df) * 100
    df_missing_percentage_Ascending = df.isna().sum().sort_values() / len(df) * 100
    df_missing_percentage_Descending = df.isna().sum().sort_values(ascending=False) / len(df) * 100
    missing_value_descen_dataset = df.isna().sum().sort_values(ascending=False)
    empty_value = df.count(axis=0)
    df_missing_non_empty_ascending = df.count().sort_values()
    df_missing_non_empty_descending = df.count().sort_values(ascending=False)
    visual_tabs = st.tabs(['Visualization for Missing Value', 'Visualization for Percentage of Missing Value', 'Visualization for Non-Empty Value'])
    with visual_tabs[0]:
        # empty_dataset = df.isnull()
        # st.write(empty_dataset)
        inner_tabs = st.tabs(['Bar Graph', 'Horizontal Bar Graph', 'Histogram Graph', 'Line Graph', 'Box Plot', 'Heat Map'])
        with inner_tabs[0]:
            missing_val = missing_value_dataset[missing_value_dataset !=0 ]
            left_col, right_col = st.columns((2,5))
            with left_col:
                missing_val_df=missing_val.to_frame()
                st.write(":green[Column Name of Missing Value  ]")
                st.write(missing_val_df)
            with right_col:
                st.write(":green[Summary of Missing Value]")
                st.write(missing_val.describe())
            st.markdown("---")
            fig=pl.bar(missing_val_df)
            fig.update_layout(
            xaxis_title='Column Names  ',
            yaxis_title='Missing \t Values',
            )
            st.plotly_chart(fig)
            tab = st.tabs(['Sorted in Ascending Order', 'Sorted in Descending Order'])
            with tab[0]:
                sort_ascen = missing_value_ascen_dataset[missing_value_ascen_dataset != 0]
                sort_ascen_df=sort_ascen.to_frame()
                fig=pl.bar(sort_ascen_df)
                fig.update_layout(
                xaxis_title='Column Names  ',
                yaxis_title='Missing \t Values',
                )
                st.plotly_chart(fig)
            with tab[1]:
                sort_desen = missing_value_descen_dataset[missing_value_descen_dataset != 0]
                sort_desen_df=sort_desen.to_frame()
                fig=pl.bar(sort_desen_df)
                fig.update_layout(
                xaxis_title='Column Names  ',
                yaxis_title='Missing \t Values',
                )
                st.plotly_chart(fig)
        with inner_tabs[1]:
            missing_val = missing_value_dataset[missing_value_dataset !=0 ]
            left_col, right_col = st.columns((2,5))
            with left_col:
                missing_val_df=missing_val.to_frame()
                st.write(":green[Column Name of Missing Value  ]")
                st.write(missing_val_df)
            with right_col:
                st.write(":green[Summary of Missing Value]")
                st.write(missing_val.describe())
            st.markdown("---")
            fig=pl.bar(missing_val_df, orientation='h')
            fig.update_layout(
            xaxis_title='Missing \t Values',
            yaxis_title='Column Names',
            )
            st.plotly_chart(fig)
            tab = st.tabs(['Sorted in Ascending Order', 'Sorted in Descending Order'])
            with tab[0]:
                sort_ascen = missing_value_ascen_dataset[missing_value_ascen_dataset != 0]
                sort_ascen_df=sort_ascen.to_frame()
                fig=pl.bar(sort_ascen_df, orientation='h')
                fig.update_layout(
                xaxis_title='Missing \t Values',
                yaxis_title='Column Names',
                )
                st.plotly_chart(fig)
            with tab[1]:
                sort_desen = missing_value_descen_dataset[missing_value_descen_dataset != 0]
                sort_desen_df=sort_desen.to_frame()
                fig=pl.bar(sort_desen_df, orientation='h')
                fig.update_layout(
                xaxis_title='Missing \t Values',
                yaxis_title='Column Names',
                )
                # fig.update_traces(marker=dict(color='red'))
                st.plotly_chart(fig)
        with inner_tabs[2]:
            missing_val = missing_value_dataset[missing_value_dataset != 0]
            left_col, right_col = st.columns((2,5))
            with left_col:
                missing_val_df=missing_val.to_frame()
                st.write(":green[Column Name of Missing Value  ]")
                st.write(missing_val_df)
            with right_col:
                st.write(":green[Summary of Missing Value]")
                st.write(missing_val.describe())
            st.markdown("---")
            dist_bins = st.slider(label="Number of plot Bins", min_value=5, max_value=100, value=10, key='slider 1',label_visibility='hidden')
            fig=pl.histogram(missing_val_df,nbins=dist_bins)
            fig.update_layout(
            title='Histogram Plot',
            bargap=0.2
            )
            st.plotly_chart(fig)
        with inner_tabs[3]:
            missing_val = missing_value_dataset[missing_value_dataset != 0]
            left_col, right_col = st.columns((2,5))
            with left_col:
                missing_val_df=missing_val.to_frame()
                st.write(":green[Column Name of Missing Value  ]")
                st.write(missing_val_df)
            with right_col:
                st.write(":green[Summary of Missing Value]")
                st.write(missing_val.describe())
            st.markdown("---")
            fig=pl.line(missing_val_df)
            fig.update_layout(
                title='Line Graph',
                xaxis_title='Column Name ',
                yaxis_title='Missing \t Values',
                yaxis=dict
                (
                showgrid=True,
                gridcolor='LightGray',
                gridwidth=1
                )
            )
            st.plotly_chart(fig)
        with inner_tabs[4]:
            missing_val = missing_value_dataset[missing_value_dataset != 0]
            left_col, right_col = st.columns((2,5))
            with left_col:
                missing_val_df=missing_val.to_frame()
                st.write(":green[Column Name of Missing Value  ]")
                st.write(missing_val_df)
            with right_col:
                st.write(":green[Summary of Missing Value]")
                st.write(missing_val.describe())
            st.markdown("---")
            fig=pl.box(missing_val_df)
            fig.update_layout(
            title="Box Plot"
            )
            st.plotly_chart(fig)
        with inner_tabs[5]:
            missing_val = missing_value_dataset[missing_value_dataset != 0]
            left_col, right_col = st.columns((2,5))
            with left_col:
                missing_val_df=missing_val.to_frame()
                st.write(":green[Column Name of Missing Value  ]")
                st.write(missing_val_df)
            with right_col:
                st.write(":green[Summary of Missing Value]")
                st.write(missing_val.describe())
            st.markdown("---")
            fig=pl.imshow(df.corr(),color_continuous_scale='Viridis')
            fig.update_layout(
            title="Heat Map"
            )
            fig.layout.height = 1100
            fig.layout.width = 1100
            # fig.update_xaxes(side="top")
            fig.update_traces(texttemplate="%{z:.1f}%")
            st.plotly_chart(fig)
    with visual_tabs[1]:
        inner_tabs = st.tabs(['Bar Graph', 'Horizontal Bar Graph', 'Histogram Graph', 'Line Graph', 'Box Plot'])
        with inner_tabs[0]:
            missing_percent = df_missing_percentage[df_missing_percentage != 0]
            left_col, right_col = st.columns((2,5))
            with left_col:
                missing_percent_frame=missing_percent.to_frame()
                st.write(":green[Column Name of Missing Value (%) ]")
                st.write(missing_percent_frame)
            with right_col:
                st.write(":green[Summary of Missing Value (%)]")
                st.write(missing_percent.describe())
            st.markdown("---")
            fig=pl.bar(missing_percent_frame)
            fig.update_layout(
            xaxis_title='Column Names  ',
            yaxis_title='Missing \t Values',
            )
            st.plotly_chart(fig)
            inner_tab_percent = st.tabs(['Sorted in Ascending Order', 'Sorted in Descending Order'])
            with inner_tab_percent[0]:
                set_sort_ascen = df_missing_percentage_Ascending[df_missing_percentage_Ascending != 0]
                sort_ascen_df=set_sort_ascen.to_frame()
                fig=pl.bar(sort_ascen_df)
                fig.update_layout(
                xaxis_title='Column Names  ',
                yaxis_title='Missing \t Values',
                )
                st.plotly_chart(fig)
            with inner_tab_percent[1]:
                set_sort_descen = df_missing_percentage_Descending[df_missing_percentage_Descending != 0]
                sort_desen_df=set_sort_descen.to_frame()
                fig=pl.bar(sort_desen_df)
                fig.update_layout(
                xaxis_title='Column Names  ',
                yaxis_title='Missing \t Values',
                )
                st.plotly_chart(fig)
        with inner_tabs[1]:
            missing_percent = df_missing_percentage[df_missing_percentage != 0]
            left_col, right_col = st.columns((2,5))
            with left_col:
                missing_percent_frame=missing_percent.to_frame()
                st.write(":green[Column Name of Missing Value (%) ]")
                st.write(missing_percent_frame)
            with right_col:
                st.write(":green[Summary of Missing Value (%)]")
                st.write(missing_percent.describe())
            st.markdown("---")
            fig=pl.bar(missing_percent_frame, orientation='h')
            fig.update_layout(
            xaxis_title='Missing \t Value  ',
            yaxis_title='Column Names',
            )
            st.plotly_chart(fig)
            inner_tab_percent = st.tabs(['Sorted in Ascending Order', 'Sorted in Descending Order'])
            with inner_tab_percent[0]:
                set_sort_ascen = df_missing_percentage_Ascending[df_missing_percentage_Ascending != 0]
                sort_ascen_df=set_sort_ascen.to_frame()
                fig=pl.bar(sort_ascen_df, orientation='h')
                fig.update_layout(
                xaxis_title='Missing \t Value  ',
                yaxis_title='Column Names',
                )
                st.plotly_chart(fig)
            with inner_tab_percent[1]:
                set_sort_descen = df_missing_percentage_Descending[df_missing_percentage_Descending != 0]
                sort_descen_df=set_sort_descen.to_frame()
                fig=pl.bar(sort_descen_df, orientation='h')
                fig.update_layout(
                xaxis_title='Missing \t Value  ',
                yaxis_title='Column Names',
                )
                st.plotly_chart(fig)
        with inner_tabs[2]:
            percentage_missing_value= df_missing_percentage[df_missing_percentage != 0]
            left_col, right_col = st.columns((2,5))
            with left_col:
                percentage_missing_value_df=percentage_missing_value.to_frame()
                st.write(":green[Column Name of Missing Value  ]")
                st.write(percentage_missing_value_df)
            with right_col:
                st.write(":green[Summary of Missing Value]")
                st.write(percentage_missing_value_df.describe())
            st.markdown("---")
            dist_bins = st.slider(label="Number of plot Bins", min_value=5, max_value=100, value=10, key='slider2',label_visibility='hidden')
            fig=pl.histogram(percentage_missing_value_df,nbins=dist_bins)
            fig.update_layout(
            title='Histogram Plot',
            bargap=0.2
            )
            st.plotly_chart(fig)
        with inner_tabs[3]:
            percentage_missing_value= df_missing_percentage[df_missing_percentage != 0]
            left_col, right_col = st.columns((2,5))
            with left_col:
                percentage_missing_value_df=percentage_missing_value.to_frame()
                st.write(":green[Column Name of Missing Value  ]")
                st.write(missing_val_df)
            with right_col:
                st.write(":green[Summary of Missing Value]")
                st.write(missing_val.describe())
            st.markdown("---")
            fig=pl.line(missing_val_df)
            fig.update_layout(
                title='Line Graph',
                xaxis_title='Column Name ',
                yaxis_title='Missing \t Values ',
                yaxis=dict
                (
                showgrid=True,
                gridcolor='LightGray',
                gridwidth=1
                )
            )
            st.plotly_chart(fig)
        with inner_tabs[4]:
            percentage_missing_value= df_missing_percentage[df_missing_percentage != 0]
            left_col, right_col = st.columns((2,5))
            with left_col:
                percentage_missing_val=percentage_missing_value.to_frame()
                st.write(":green[Column Name of Missing Value  ]")
                st.write(percentage_missing_val)
            with right_col:
                st.write(":green[Summary of Missing Value]")
                st.write(percentage_missing_val.describe())
            st.markdown("---")
            fig=pl.box(percentage_missing_val)
            fig.update_layout(
            title="Box Plot"
            )
            st.plotly_chart(fig)
    with visual_tabs[2]:
        inner_tabs = st.tabs(['Bar Graph', 'Horizontal Bar Grah', 'Histogram Graph', 'Line Graph', 'Box Plot'])
        with inner_tabs[0]:
            left_col, right_col = st.columns((2,5))
            with left_col:
                # missing_percent_frame=missing_percent.to_frame()
                st.write(":green[Column Name of Non-Empty Value ]")
                st.write(empty_value)
            with right_col:
                st.write(":green[Summary of Non-Empty Value]")
                st.write(empty_value.describe())
            st.markdown("---")
            fig=pl.bar(empty_value)
            fig.update_layout(
            xaxis_title='Column Names  ',
            yaxis_title='Non-Empty\t Values',
            title='Bar Graph'
            )
            st.plotly_chart(fig)
            inner_tab_count = st.tabs(['Sorted in Ascending Order', 'Sorted in Descending Order'])
            with inner_tab_count[0]:
                fig=pl.bar(df_missing_non_empty_ascending)
                fig.update_layout(
                xaxis_title='Column Names  ',
                yaxis_title='Non-Empty \t Values',
                )
                st.plotly_chart(fig)
            with inner_tab_count[1]:
                fig=pl.bar(df_missing_non_empty_descending)
                fig.update_layout(
                xaxis_title='Column Names  ',
                yaxis_title='Non-Empty \t Values',
                )
                st.plotly_chart(fig)
        with inner_tabs[1]:
            left_col, right_col = st.columns((2,5))
            with left_col:
                missing_percent_frame=empty_value.to_frame()
                st.write(":green[Column Name of Missing Value (%) ]")
                st.write(missing_percent_frame)
            with right_col:
                st.write(":green[Summary of Missing Value (%)]")
                st.write(missing_percent_frame.describe())
            st.markdown("---")
            fig=pl.bar(empty_value, orientation='h')
            fig.update_layout(
            xaxis_title='Missing \t Value  ',
            yaxis_title='Column Names',
            )
            st.plotly_chart(fig)
            inner_tab_count = st.tabs(['Sorted in Ascending Order', 'Sorted in Descending Order'])
            with inner_tab_count[0]:
                fig=pl.bar(df_missing_non_empty_ascending, orientation='h')
                fig.update_layout(
                xaxis_title='Missing \t Value  ',
                yaxis_title='Column Names',
                )
                st.plotly_chart(fig)
            with inner_tab_count[1]:
                fig=pl.bar(df_missing_non_empty_descending, orientation='h')
                fig.update_layout(
                xaxis_title='Missing \t Value  ',
                yaxis_title='Column Names',
                )
                st.plotly_chart(fig)

        with inner_tabs[2]:
            left_col, right_col = st.columns((2,5))
            with left_col:
                non_empty_values=empty_value.to_frame()
                st.write(":green[Column Name of Missing Value  ]")
                st.write(non_empty_values)
            with right_col:
                st.write(":green[Summary of Missing Value]")
                st.write(non_empty_values.describe())
            st.markdown("---")
            dist_bins = st.slider(label="Number of plot Bins", min_value=5, max_value=100, value=10, key='slider5',label_visibility='hidden')
            fig=pl.histogram(non_empty_values,nbins=dist_bins)
            fig.update_layout(
            title='Histogram Plot',
            bargap=0.2
            )
            st.plotly_chart(fig)
        with inner_tabs[3]:
            left_col, right_col = st.columns((2,5))
            with left_col:
                empmty_value_df=empty_value.to_frame()
                st.write(":green[Column Name of Missing Value  ]")
                st.write(empmty_value_df)
            with right_col:
                st.write(":green[Summary of Missing Value]")
                st.write(empmty_value_df.describe())
            st.markdown("---")
            fig=pl.line(empmty_value_df)
            fig.update_layout(
                title='Line Graph',
                xaxis_title='Column Name ',
                yaxis_title='Missing \t Values',
                yaxis=dict
                (
                showgrid=True,
                gridcolor='LightGray',
                gridwidth=1
                )
            )
            st.plotly_chart(fig)
        with inner_tabs[4]:
            left_col, right_col = st.columns((2,5))
            with left_col:
                non_value_df=empty_value.to_frame()
                st.write(":green[Column Name of Missing Value  ]")
                st.write(non_value_df)
            with right_col:
                st.write(":green[Summary of Missing Value]")
                st.write(non_value_df.describe())
            st.markdown("---")
            fig=pl.box(non_value_df)
            fig.update_layout(
            title="Box Plot"
            )
            st.plotly_chart(fig)
else:
        st.markdown("<h1 style='text-align: center; color: red;font-size: 24px;'>No Data Found!! Please Upload CSV File.</h1>", unsafe_allow_html=True)

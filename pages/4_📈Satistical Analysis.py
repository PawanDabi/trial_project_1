import streamlit as st
import matplotlib.pyplot as plt
from io import BytesIO
import pandas as pd
import seaborn as sns
import plotly.express as pl
st.set_page_config(page_title="Statistical Analysis",
    page_icon="📈",
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
st.sidebar.header("Summarizing Statistics Analysis and Graphs.")
options = ["", "Univariate Analysis", "Bivariate Analysis", "Outlier Analysis", "Z-Score Analysis", "IQR Analysis", "Count Graph",
            "Histogram Graph", "Box Graph", "Scatter Graph", "Regression Graph"]
analysis_column = st.sidebar.selectbox("Information About **:green[Univariate]**, **:green[Bivariate]**, **:green[Outlier Analysis]** and   **:green[Graphs]**", options,label_visibility='hidden')

if analysis_column == 'Univariate Analysis':
    st.sidebar.write("**:green[{name}]**: The :red[Univariate Analysis] refers to the analysis of a single variable. "
                     "In other words, it examines the distribution, central tendency, and variability of a "
                     "single variable in isolation. Examples of univariate analysis include calculating the mean, "
                     "median, and mode of a variable  "
                     "the distribution of a variable.".format(name='Univariate Analysis'))

elif analysis_column == 'Bivariate Analysis':
    st.sidebar.write("**:green[{name}]**: The :red[Bivariate Analysis] refers to the analysis of two variables at the same time. "
                     "It examines the relationship between two variables and how they are associated with each other."
                     " Examples of bivariate analysis include calculating the correlation coefficient between two variables".format(name='Bivariate Analysis'))

elif analysis_column == 'Outlier Analysis':
    st.sidebar.write("**:green[{name}]**: The :red[Outliers] are the extreme values within the dataset. "
                     "That means the outlier data points vary greatly from the expected values—either being much larger"
                     " or significantly smaller. For data that follows a normal distribution, the values that fall more "
                     "than three standard deviations from the mean are typically considered outliers.".format(name='Outlier Analysis'))

elif analysis_column == 'Z-Score Analysis':
    st.sidebar.write("**:green[{name}]**: The :red[Z-Score] is the signed number of standard deviations by which the value of an observation "
                     "or data point is above the mean value of what is being observed or measured. These data points which are"
                     " way too far from zero will be treated as the outliers.".format(name='Z-Score Analysis'))

elif analysis_column == 'IQR Analysis':
    st.sidebar.write("**:green[{name}]**: The :red[Inter-Quartile Range] (IQR) is a measure of statistical dispersion, representing the range within which the central 50% of data points lie. It is calculated as the difference between the third quartile (Q3) and the first quartile (Q1) of a dataset: IQR=Q3−Q1.".format(name='IQR Analysis'))

elif analysis_column == "Count Graph":
    st.sidebar.write("**:green[{name}]**: The :red[Count PLot] is a univariate plot that shows "
                        "the comparison of different groups in categorical variables. "
                        "It shows the number of observations per category using bins.". format(name='Count Graph'))

elif analysis_column == "Histogram Graph":
    st.sidebar.write("**:green[{name}]**: A histogram is a graphical representation of the distribution of numerical data, where data is grouped into bins or intervals. The height of each bar shows the frequency or count of data points within each bin.". format(name='Histogram Graph'))

elif analysis_column == 'Box Graph':
    st.sidebar.write("**:green[{name}]**:  A box plot is a graphical representation of the distribution of a dataset. It displays the median, quartiles, and potential outliers in the data, using a box to represent the interquartile range and whiskers to indicate variability outside the quartil.".format(name='Box Plot'))

elif analysis_column == 'Scatter Graph':
    st.sidebar.write("**:green[{name}]**: A scatter plot is a chart that uses dots to represent the values of two different variables. Each dot's position on the horizontal and vertical axes corresponds to the values of the variables. It's useful for identifying relationships or correlations between variables.". format(name='Scatter Graph'))

elif analysis_column == 'Regression Graph':
    st.sidebar.write("**:green[{name}]**: The :red[Regression Graph] creates a regression line between 2 parameters and helps to visualize their linear  relationships. ".format(name='Regression Graph'))

st.sidebar.markdown("---")
st.markdown("<h1 style='text-align: center; color: #54B254;'>Univariate, Bivariate and Outlier Analysis</h1>",unsafe_allow_html=True)
st.markdown("---")
st.cache(persist=True)
if "df" in st.session_state and st.session_state.df is not None:
    df = st.session_state.df

    analysis = st.tabs(['Univariate Analysis (UA)', 'Bivariate Analysis (BA)', 'Outlier Analysis (OA)'])
    with analysis[0]:
        inner_analysis = st.tabs(['Univariate Analysis for Categorical Data', 'Univariate Analysis for Numerical Data'])
        with inner_analysis[0]:
            categorical_columns = df.select_dtypes(include=['object']).columns
            column = st.selectbox("**:green[Select Column ]**", categorical_columns,label_visibility='hidden')
            right_col, left_col = st.columns((2,6))
            with right_col:
                st.write("Column Name")
                st.write(df[[column]])
            with left_col:
                st.write("Frequency Table")
                freq_table = pd.crosstab(index=df[column], columns="count")
                st.write(freq_table)
            st.markdown("---")
            custom_colors = ['#636EFA', '#EF553B', '#00CC96', '#AB63FA', '#FFA15A',
                            '#19D3F3', '#FF6692', '#B6E880', '#FF97FF', '#FECB52']
            custom_color = pl.colors.qualitative.Set1
            fig=pl.histogram(df, x=column,color=column,barmode='group',color_discrete_sequence=custom_colors)
            fig.update_layout(
            title="Count Plot"
            )
            fig.layout.height=500
            fig.layout.width=900
            fig.update_layout(
            title="Count Plot"
            )
            st.plotly_chart(fig)
        with inner_analysis[1]:
            numeric_columns = df.select_dtypes(['float64', 'float32', 'int32', 'int64']).columns
            column = st.selectbox("**:green[Select Column ]**", numeric_columns,label_visibility='hidden')
            right_col, left_col = st.columns((2,5))
            with right_col:
                st.write("Column Name")
                st.write(df[[column]])
            with left_col:
                st.write("Summary Statistics")
                st.write(df[column].describe())
            inner_plot = st.tabs(['Histogram Plot', 'Box Plot'])
            with inner_plot[0]:
                slid = st.slider(label="Number of Plots Bins", min_value=5, max_value=50, value=15,key='slider007',label_visibility='hidden')
                fig=pl.histogram(df[column], nbins=slid)
                fig.update_layout(
                title="Histogram Plot"
                )
                st.plotly_chart(fig)
            with inner_plot[1]:

                fig=pl.box(df[column])
                fig.update_layout(
                title='Box Plot',
                yaxis=dict(showgrid=True)
                )
                st.plotly_chart(fig)
    with analysis[1]:
        inner_ba_analysis = st.tabs(['Numerical Data V/S Numerical Data', 'Numerical Data V/S Categorical Data',
                                     'Categorical Data V/S Categorical Data  '])
        with inner_ba_analysis[0]:
            inner_nn_plot = st.tabs(['Scatter Plot', 'Regression Plot'])
            with inner_nn_plot[0]:
                right_col_1, left_col_1=st.columns((5,5))
                with right_col_1:
                    column1 = st.selectbox("**:green[Select X-Axis Column]**", numeric_columns,label_visibility='hidden')
                    st.write(df[[column1]])
                with left_col_1:
                    column2 = st.selectbox("**:green[Select Y-Axis Column]**", numeric_columns,label_visibility='hidden')
                    st.write(df[[column2]])
                st.markdown("---")
                fig=pl.scatter(x=df[column1], y=df[column2])
                fig.layout.height=500
                fig.layout.width=800
                fig.update_layout(
                title='Scatter Plot',
                xaxis_title=column1,
                yaxis_title=column2
                )
                st.plotly_chart(fig)
            with inner_nn_plot[1]:
                right_col_1, left_col_1=st.columns((5,5))
                with right_col_1:
                    column1 = st.selectbox("**:green[Select X-Axis Column]**", numeric_columns, key='slider5',label_visibility='hidden')
                    st.write(df[[column1]])
                with left_col_1:
                    column2 = st.selectbox("**:green[Select Y-Axis Column]**", numeric_columns,key='slider 6',label_visibility='hidden')
                    st.write(df[[column2]])
                st.markdown("---")
                right_column, left_column=st.columns((5,5))
                with right_column:
                    width = st.slider(":green[Plot Width]", 1, 45, 10,key='slider001',label_visibility='hidden')
                with left_column:
                    height = st.slider(":green[Plot Height]", 1, 30, 4,key='slider002',label_visibility='hidden')
                reg_size, ax = plt.subplots(figsize=(width, height))
                sns.regplot(x=column1, y=column2, data=df)
                plt.title("Regression Plot")
                buffer = BytesIO()
                st.pyplot(reg_size)
                reg_size.savefig(buffer, format='png')
                st.download_button(
                    label='Download as PNG',
                    data=buffer.getvalue(),
                    file_name='regression chart.png',
                    mime='image/png'
                )
        with inner_ba_analysis[1]:
            right_col_1,left_col_1=st.columns((5,5))
            with right_col_1:
                column1 = st.selectbox("**:green[Select Y-Axis Column]**  ", numeric_columns,label_visibility='hidden')

            with left_col_1:
                column2 = st.selectbox("**:green[Select X-Axis Column]**  ", categorical_columns,label_visibility='hidden')
            right_col, center_col, left_col = st.columns((2,5,3))
            with right_col:
                st.write("Y-Axis Column Name")
                st.write(df[[column1]])
            with center_col:
                st.write("Summary Statistics by Category")
                summary = df.groupby(column2)[column1].describe()
                st.write(summary)

            with left_col:
                st.write("X-Axis Column Name")
                st.write(df[[column2]])
            st.markdown("---")
            custom_colors = ['#636EFA', '#EF553B', '#00CC96', '#AB63FA', '#FFA15A',
                            '#19D3F3', '#FF6692', '#B6E880', '#FF97FF', '#FECB52']
            fig=pl.box(df, x=df[column2], y=df[column1],color=column2, color_discrete_sequence=custom_colors)
            fig.update_layout(
            title='Box Plot',
            xaxis_title=column2,
            yaxis_title=column1
            )
            st.plotly_chart(fig)
        with inner_ba_analysis[2]:
            right_col_1, left_col_1=st.columns((5,5))
            with right_col_1:
                column1 = st.selectbox("**:green[Select X-Axis Column]** ", categorical_columns,label_visibility='hidden')
            with left_col_1:
                column2 = st.selectbox("**:green[Select Y-Axis  Column]** ", categorical_columns,label_visibility='hidden')

            contingency_table = pd.crosstab(index=df[column1], columns=df[column2])
            right_col, center_col, left_col = st.columns((2,3,3))
            with right_col:
                st.write("X Column Name")
                st.write(df[[column1]])
            with center_col:
                st.write("Contingency Table")
                st.write(contingency_table)
            with left_col:
                st.write("Y Column Name")
                st.write(df[[column2]])
            st.markdown("---")
            fig=pl.bar(contingency_table)
            fig.update_layout(
            title='Stacked Bar Plot'
            )
            st.plotly_chart(fig)

    with analysis[2]:
        outlier_tab = st.tabs(['Z-Score Outlier', 'Inter-Quartile Range  (IQR)  Outlier'])
        with outlier_tab[0]:
            outer_column = st.selectbox(":green[Select a Column]", numeric_columns,label_visibility='hidden')
            zscore = (df[outer_column] - df[outer_column].mean()) / df[outer_column].std()
            threshold_value = st.slider(":green[Select a threshold value for finding outlier]", min_value=0.0, max_value=3.0, value=1.0,key='slid',label_visibility='hidden')
            outliers = df[zscore.abs() >= threshold_value][outer_column]
            right_col, left_col = st.columns((2,2))
            with right_col:
                st.write("Column Name")
                st.write(df[[outer_column]])
            with left_col:
                st.write("No. of :green[Outlier's] in column")
                st.write(outliers.to_frame())
            inner_zscore = st.tabs(['Histogram Z-Score Plot', 'Scatter Z-Score Plot'])
            with inner_zscore[0]:
                right_col,left_col=st.columns((5,5))
                with right_col:
                    threshold = st.slider(":green[Select a threshold value]", min_value=0.0, max_value=3.0, value=1.0, key='slider005',label_visibility='hidden')
                with left_col:
                    bin_size = st.slider(":green[Select bin size]", min_value=2, max_value=30, value=15, step=1,key='slider006',label_visibility='hidden')
                st.markdown("---")
                right_column, left_column=st.columns((5,5))
                with right_column:
                    width = st.slider(":green[Plot Width]", 1, 45, 10,key='slider003',label_visibility='hidden')
                with left_column:
                    height = st.slider(":green[Plot Height]", 1, 30, 4,key='slider004',label_visibility='hidden')
                outlier_plot, ax = plt.subplots(figsize=(width, height))
                sns.histplot(df[outer_column], kde=True, ax=ax, bins=bin_size)
                ax.axvline(df[outer_column].mean(), color='r', linestyle='dashed', linewidth=2)
                ax.axvline(df[outer_column].mean() + (threshold * df[outer_column].std()), color='g', linestyle='dashed', linewidth=2)
                ax.axvline(df[outer_column].mean() - (threshold * df[outer_column].std()), color='g', linestyle='dashed', linewidth=2)
                ax.set_title(f"Histogram of {outer_column}")
                ax.set_xlabel(outer_column)
                ax.set_ylabel("Frequency")
                buffer = BytesIO()
                st.pyplot(outlier_plot)
                outlier_plot.savefig(buffer, format='png')
                st.download_button(
                    label='Download as PNG',
                    data=buffer.getvalue(),
                    file_name='histogram z-score chart.png',
                    mime='image/png'
                )
            with inner_zscore[1]:
                fig=pl.scatter(df, x=range(len(df)), y=outer_column)
                fig.add_scatter(x=outliers.index, y=outliers, marker=dict(color='red', size=9),
                name='Outliers', text='Outlier', textposition='top center',mode='markers')
                fig.update_layout(
                title='Scatter Plot',
                xaxis_title=(f"length of {outer_column}"),
                height=500,
                width=900
                )
                st.plotly_chart(fig)
    with outlier_tab[1]:
        iqr_column = st.selectbox(":green[ Select a Column]", numeric_columns,label_visibility='hidden')
        q1 = df[iqr_column].quantile(0.25)
        q3 = df[iqr_column].quantile(0.75)
        iqr = q3 - q1
        lower_bound = q1 - (1.5 * iqr)
        upper_bound = q3 + (1.5 * iqr)
        outliers = df[(df[iqr_column] < lower_bound) | (df[iqr_column] > upper_bound)][iqr_column]
        right_col, left_col, center = st.columns((5,5,5))
        with right_col:
            st.write("Feature Name")
            st.write(df[[iqr_column]])
        with left_col:
            st.write("Values of :green[Outliers] ")
            st.write("q1: ",q1)
            st.write("q3: ",q3)
            st.write("iqr: ",iqr)
        with center:
            st.write("No. of :green[Outlier's] in column")
            st.write(outliers.to_frame())
        inner_zscore = st.tabs(['Box IQR Plot', 'Scatter IQR Plot'])
        with inner_zscore[0]:
            outlier_iqr, ax1 = plt.subplots(figsize=(width, height))
            fig=pl.box(df[iqr_column])
            fig.update_layout(
            title='Box Plot'
            )
            st.plotly_chart(fig)
        with inner_zscore[1]:
            fig=pl.scatter(df, x=range(len(df)), y=iqr_column)
            fig.add_scatter(x=outliers.index, y=outliers, marker=dict(color='red', size=9),
            name='Outliers', text='Outlier', textposition='top center',mode='markers')
            fig.update_layout(
            title='Scatter Plot',
            xaxis_title=(f"length of {iqr_column}"),
            height=500,
            width=900
            )
            st.plotly_chart(fig)
else:
    st.markdown("<h1 style='text-align: center; color: red;font-size: 24px;'>No Data Found!! Please Upload CSV File.</h1>", unsafe_allow_html=True)

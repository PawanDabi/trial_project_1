import pandas as pd
import streamlit as st
from streamlit_extras.colored_header import colored_header
from streamlit_extras.mention import mention
st.set_page_config(page_title="Exploratory Data Analysis . Streamlit",
    page_icon="https://cdn-icons-png.flaticon.com/512/3090/3090011.png",
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

st.cache(persist=True)
st.sidebar.header("Operations on Given DataSet.")
option_name = ["", "Head", "Tail", "Summery", "Column Name", "Row No", "Column No",
               "Numeric Data", "Missing Values", "Missing Values per Column", "Percentage of Missing Values", "Non-Empty Values"]

op_column_name = st.sidebar.selectbox("**:green[Information About Operations on Given DataSet]**", option_name, label_visibility='hidden')
if op_column_name == 'Head':
    st.sidebar.write("**:green[{name}]**:  This method returns the first 5 rows if a number is not specified."
                    " if any number has been given the it will written number of rows that you have been given".format(name='Head'))
elif op_column_name == 'Tail':
    st.sidebar.write("**:green[{name}]**: This method returns the last 5 rows if a number is not specified. "
                     " if any number has been given the it will written number of rows that you have been given".format(name='Tail'))
elif op_column_name == 'Summery':
    st.sidebar.write("**:green[{name}]**:  This method returns description of the data in the DataFrame. "
                     "If the DataFrame contains numerical data " .format(name='Summary'))
elif op_column_name == 'Column Name':
    st.sidebar.write("**:green[{name}]**: It returns the column name of the data.".format(name='Column Name'))
elif op_column_name == 'Row No':
    st.sidebar.write("**:green[{name}]**: This shows the number of rows in DataSet.".format(name='Row No'))
elif op_column_name == 'Column No':
    st.sidebar.write("**:green[{name}]**: This shows the number of columns in dataset".format(name='Column No'))
elif op_column_name == 'Numeric Data':
    st.sidebar.write("**:green[{name}]**: This method display the numeric column form the data set".format(name='Numeric Data'))
elif op_column_name == 'Missing Values':
    st.sidebar.write("**:green[{name}]**: This method returns the record of missing values in the data set.".format(name='Missing Values'))
elif op_column_name == 'Missing Values per Column':
    st.sidebar.write("**:green[{name}]**: This method returns the number of missing values in each column."
                     .format(name='Missing Values per Column'))
elif op_column_name == 'Missing Value(Column %)':
    st.sidebar.write("**:green[{name}]**: This method will shows the percentage of missing value of each column. "
                     .format(name='Missing Value(Column %)'))
elif op_column_name == 'Non-Empty Values':
    st.sidebar.write("**:green[{name}]**: This method counts the number of not empty values for each row, or column".format(name='Count'))
st.cache(persist=True)
st.title(":green[Streamlit EDA] : A :red[WebApp] for Efficient :green[Data Analysis .] ")
st.markdown("---")
st.markdown("<h1 style='text-align: center; color: #54B254;font-size: 36px;'>Upload CSV File...</h1>", unsafe_allow_html=True)
# file_upload = st.file_uploader("", type=['CSV'])
@st.cache_data
def read_csv_file(uploaded_file):
    encodings = ['utf-8', 'latin1', 'ISO-8859-1', 'cp1252']
    for encoding in encodings:
        try:
            uploaded_file.seek(0)
            df = pd.read_csv(uploaded_file, encoding=encoding)
            if df.empty:
                st.error("The uploaded file is empty.")
                return None
            return df
        except UnicodeDecodeError:
            continue
        except pd.errors.EmptyDataError:
            st.error("The uploaded file contains no data.")
            return None
        except pd.errors.ParserError:
            st.error("The uploaded file could not be parsed.")
            return None
    st.error("Unable to read the file with available encodings.")
    return None
file_upload = st.file_uploader("", type=['csv'])
st.markdown("---")
if 'df' not in st.session_state:
    st.session_state.df = None
# st.cache(persist=True)
if file_upload is not None:
    df = read_csv_file(file_upload)
    if df is not None:
        st.session_state.df = df
        st.session_state.file_upload=file_upload
        st.subheader("**:red[{}]** DataSet are . . ".format(file_upload.name))
else:
    if st.session_state.df is not None:
        st.subheader("**:red[{}]** DataSet are . .  ".format(st.session_state.file_upload.name))
        st.markdown(" ")
    else:
        st.markdown("<h1 style='text-align: center; color: red;font-size: 24px;'>No File Uploaded Yet.</h1>", unsafe_allow_html=True)


if st.session_state.df is not None:
    df = st.session_state.df
    file_upload=st.session_state.file_upload
    st.write(df)
    # st.write(file_upload.name)
    st.markdown("---")
    st.header("Basic Information on Given **:green[CSV]** DataSet File and more  . . . ")
    tabs = st.tabs(["Top DataSet", "Bottom DataSet", "Summary", "Column Names", "Row/Column No.", "Numeric Data Column",
    "Missing Values", "Missing Values per Column", "Percentage of Missing Values", "Non-Empty Values"])
    with tabs[0]:
        number_head = st.number_input(":green[Enter the No. of Top DataSet] ",step=0, format='%d',key='slid1',label_visibility='hidden')
        head_dataset = df.head(number_head)
        st.write(head_dataset)
        st.download_button("Download Data as .CSV",
        head_dataset.to_csv(),
        file_name='head_dataset.csv',
        mime='csv', key='slid2')
    with tabs[1]:
        number_tail = st.number_input(":green[Enter the No. of Bottom DataSet]  ", step=0, format='%d',label_visibility='hidden')
        tail_dataset = df.tail(number_tail)
        st.write(tail_dataset)
        st.download_button("Download Data as .CSV",
        tail_dataset.to_csv(),
        file_name='tail_dataset.csv',
        mime='text/csv')
    with tabs[2]:
        inner_tabs = st.tabs(['Summary for Numeric Columns', 'Summary of Categorical Column'])
        with inner_tabs[0]:
            num = ['float64', 'int64']
            numeric_summary = df.describe(include=num)
            st.write(numeric_summary)
            st.download_button("Download Data as .CSV",
            numeric_summary.to_csv(),
            file_name='numeric_dataset.csv',
            mime='text/csv')
        with inner_tabs[1]:
            cat = 'object'
            cat_summary = df.describe(include=cat)
            st.write(cat_summary)
            st.download_button("Download Data as .CSV",
            cat_summary.to_csv(),
            file_name='catgorical_dataset.csv',
            mime='text/csv')
    with tabs[3]:
        st.write(":green[Name of Columns] in DataSet: ")
        st.write(df.columns)
    with tabs[4]:
        st.write("No. of :green[Row] in DataSet: ")
        st.write(df.shape[0])
        st.write("No. of :green[Columns] in DataSet: ")
        st.write(df.shape[1])
    with tabs[5]:
        numerics = ['int16', 'int32', 'int64', 'float16', 'float32', 'float64']
        no_of_numeric = df.select_dtypes(include=numerics)
        st.write("No of :green[Numeric Data] in DataSet: ")
        st.write(len(no_of_numeric.columns))
        st.write(no_of_numeric)
        st.download_button("Download Data as .CSV", no_of_numeric.to_csv(), file_name='numeric_dataset.csv', mime='text/csv')
    with tabs[6]:
        miss_col = df.columns[df.isnull().any()]
        st.write(":green[Column Name Contains Missing Value : ]")
        right_col, left_col=st.columns((2,9))
        with right_col:
            st.write(len(miss_col))
            st.write(miss_col, "")
        with left_col:
            for i in range(0,2):
                st.text("")
                print("\n")
            empty_dataset = df.isnull()
            st.dataframe(empty_dataset)
            st.download_button("Download Data as .CSV", empty_dataset.to_csv(), file_name='missing_dataset.csv', mime='text/csv')
    with tabs[7]:
        st.write("Shows the :green[Missing Values Per Columns] in DataSet: ")
        missing_value_dataset = df[df.columns].isna().sum()
        st.write(missing_value_dataset)
        st.download_button("Download Data as .CSV",
        missing_value_dataset.to_csv(),
        file_name='missing_column_dataset.csv',
        mime='text/csv')
        sort_data = st.tabs(["Sort in Ascending Order", "Sort in Descending Order"])
        with sort_data[0]:
            st.write("Sorted in :green[Ascending Order] from DataSet ")
            missing_value_ascen_dataset = df.isna().sum().sort_values()
            st.write(missing_value_ascen_dataset)
            st.download_button("Download Data as .CSV", missing_value_ascen_dataset.to_csv(), file_name='missing_column_ascen_dataset.csv',
                               mime='text/csv')
        with sort_data[1]:
            st.write("Sorted in :green[Descending Order] from DataSet ")
            missing_value_descen_dataset = df.isna().sum().sort_values(ascending=False)
            st.write(missing_value_descen_dataset)
            st.download_button("Download Data as .CSV", missing_value_descen_dataset.to_csv(), file_name='missing_column_descen_dataset.csv',
                               mime='text/csv')
    with tabs[8]:
        st.write("Show the :green[Percentage] of Missing Values of Each Column: ")
        df_missing_percentage = df.isna().sum() / len(df) * 100
        st.write(df_missing_percentage)
        st.download_button("Download Data as .CSV", df_missing_percentage.to_csv(), file_name='percentage_column_dataset.csv',
                           mime='text/csv')
        missing_value_sorted = st.tabs(["Sort in Ascending Order", "Sort in Descending Order"])
        with missing_value_sorted[0]:
            df_missing_percentage_Ascending = df.isna().sum().sort_values() / len(df) * 100
            st.write("Shows the Sorted :green[Percentage Missing Value] in :green[Ascending Order]:")
            st.write(df_missing_percentage_Ascending)
            st.download_button("Download Data as .CSV", df_missing_percentage_Ascending.to_csv(),
                               file_name='percentage_column_ascending_dataset.csv',
                               mime='text/csv')
        with missing_value_sorted[1]:
            df_missing_percentage_Descending = df.isna().sum().sort_values(ascending=False) / len(df) * 100
            st.write("Shows the Sorted :green[Percentage Missing Value] in :green[Descending Order]: ")
            st.write(df_missing_percentage_Descending)
            st.download_button("Download Data as .CSV", df_missing_percentage_Descending.to_csv(),
                               file_name='percentage_column_descending_dataset.csv',
                               mime='text/csv')

    with tabs[9]:
        st.write("Shows the :green[Non Empty Values] of Each Column and Row in DataSet:")
        empty_value = df.count(axis=0)
        st.write(empty_value)
        st.download_button("Download Data as .CSV", empty_value.to_csv(),
                           file_name='empty_value.csv',
                           mime='text/csv')
        missing_value_sort = st.tabs(['Sort in Ascending Order', 'Sort in Descending Order'])
        with missing_value_sort[0]:
            df_missing_non_empty_ascending = df.count().sort_values()
            st.write("Shows the Sorted :green[Non Empty Value] in :green[Ascending Order]: ")
            st.write(df_missing_non_empty_ascending)
            st.download_button("Download Data as .CSV", df_missing_non_empty_ascending.to_csv(),
                               file_name='df_missing_non_empty_ascending.csv',
                               mime='text/csv')
        with missing_value_sort[1]:
            df_missing_non_empty_descending = df.count().sort_values(ascending=False)
            st.write("Shows teh Sorted :green[Non Empty Value] in :green[Descending Order]: ")
            st.write(df_missing_non_empty_descending)
            st.download_button("Download Data as .CSV", df_missing_non_empty_descending.to_csv(),
                               file_name='df_missing_non_empty_descending.csv',
                               mime='text/csv')

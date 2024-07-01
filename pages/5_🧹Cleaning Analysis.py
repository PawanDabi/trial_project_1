import pandas as pd
import streamlit as st
from streamlit_extras.mention import mention
st.set_page_config(page_title="Cleaning Analysis",
    page_icon="🧹",
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
st.sidebar.header(":green[Information about Cleaning Analysis.]")
st.sidebar.write("The Cleaning Analysis perform's some operation that remove or drop the missing value "
                "that are present in given dataset files. This Analysis gives three option to user to remove missing "
                "values in Dataset. This option's are:")
st.sidebar.write("1). Remove Missing Value's by :green[Column's]")
st.sidebar.write("2). Remove Missing Value's by :green[Row's]")
st.sidebar.write("3). Remove Missing Value's by both :green[Column] and :green[Row]")
st.markdown("<h1 style='text-align: center; color: #54B254;'>Cleaning Analysis on DataSet</h1>", unsafe_allow_html=True)
st.markdown("---")
if 'df' in st.session_state and st.session_state.df is not None:
    df=st.session_state.df
    file_upload=st.session_state.file_upload
    st.subheader("**:red[{}]** DataSet are . . ".format(file_upload.name))
    st.write(df)
    st.write("The :green[Row No.] of Dataset is: ",df.shape[0])
    st.write("The :green[Column No.] of Dataset is: ",df.shape[1])
    st.markdown("---")
    st.header("New DataSet with **:green[Missing Values]** Removed / :green[Cleaned DataSet]")
    missing_values_count = df.columns[df.isnull().any()]
    st.write("### Droping Missing Value by :green[Columns]")
    columns_to_drop = st.multiselect("", missing_values_count,label_visibility='hidden')
    if len(columns_to_drop) > 0:
        df = df.drop(columns_to_drop, axis=1)
        st.write(df)
        st.write("The :green[Row No.] of Dataset is: ",df.shape[0])
        st.write("The :green[Column No.] of Dataset is: ",df.shape[1])
        st.download_button("Download Data as .CSV", df.to_csv(index=False), file_name='cleaned_data.csv', mime='text/csv')
    st.markdown("---")
    st.write("### Droping Missing Value by :green[Rows]")
    if st.checkbox("Click here to Drop the missing value Rows"):
        df_cleaned  = df.dropna()
        st.write(df_cleaned)
        st.write("The :green[Row No.] of Dataset is: ",df_cleaned.shape[0])
        st.write("The :green[Column No.] of Dataset is: ",df_cleaned.shape[1])
        st.download_button("Download Data as .CSV", df.to_csv(index=False), file_name='cleaned_data.csv', mime='text/csv',key='slid1')
        df=df_cleaned
    st.markdown("---")
    if not df.empty:
        missing = df.columns[df.isnull().any()].tolist()
        st.write("### Droping Missing Value for both :green[Column and Row]")
        columns_for_both = st.multiselect(":red[First Select Columns. . . .] ", missing,label_visibility='hidden')
        if len(columns_for_both) > 0:
            df = df.drop(columns_for_both, axis=1)
        if st.checkbox("Click here to Show Cleaned data"):
            df_cleaned = df.dropna()
            st.write(df_cleaned)
            st.write("The :green[Row No.] of Dataset is: ", df_cleaned.shape[0])
            st.write("The :green[Column No.] of Dataset is: ", df_cleaned.shape[1])
            st.download_button("Download Data as .CSV", df_cleaned.to_csv(index=False), file_name='cleaned_data.csv', mime='text/csv')
        st.markdown("---")
    else:
        st.warning("The DataFrame is empty after dropping rows with missing values. No data to display.")
else:
    st.markdown("<h1 style='text-align: center; color: red;font-size: 24px;'>No Data Found!! Please Upload CSV File.</h1>", unsafe_allow_html=True)
for i in range(0,10):
    st.text(" ")
    print("\n")
st.subheader("Reach out to me for any :red[Suggestion/Feedback]")
left, right = st.columns((2,8))
with left:
    mention(
    label="LinkedIn",
    icon="https://img.freepik.com/premium-vector/linkedin-logo_578229-227.jpg?w=740",
    url="https://www.linkedin.com/in/pawan-dabi-a42a081b7/",
    )
with right:
    mention(
    label="Instagram",
    icon="https://www.freepnglogos.com/uploads/logo-ig-png/logo-ig-instagram-new-logo-vector-download-13.png",
    url="https://www.instagram.com/pawan_dabi_001/",
    )

st.title('Customer Review Labeling App')

uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    reviews_df = pd.read_csv(uploaded_file)

    # Convert the 'Review' column to string data type
    reviews_df['Review'] = reviews_df['Review'].astype(str)

    # Apply the classify_review function to the 'Review' column
    reviews_df['Label'] = reviews_df['Review'].apply(classify_review)

    # Display the labeled reviews
    st.write(reviews_df)

    # Allow the user to download the labeled reviews
    st.download_button(
        label="Download labeled reviews as CSV",
        data=reviews_df.to_csv(index=False),
        file_name='labeled_reviews.csv',
        mime='text/csv'
    )
else:
    st.write("Please upload a CSV file to get started.")

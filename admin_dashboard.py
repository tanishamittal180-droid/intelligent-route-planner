import streamlit as st
import pandas as pd


class AdminDashboard:

    def show(
        self,
        routes
    ):

        st.subheader(
            "Admin Analytics"
        )

        df = pd.DataFrame(

            routes,

            columns=[
                "ID",
                "Source",
                "Destination",
                "Algorithm",
                "Distance",
                "ETA"
            ]
        )

        st.dataframe(
            df,
            width="stretch"
        )

        st.bar_chart(
            df["Distance"]
        )
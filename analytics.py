# frontend/analytics.py

import pandas as pd
import streamlit as st


class Analytics:

    def show_route_comparison(
        self,
        routes_data
    ):

        df = pd.DataFrame(
            routes_data
        )

        st.subheader(
            "📊 Route Comparison"
        )

        st.dataframe(
            df,
            width="stretch"
        )

        st.bar_chart(
            df.set_index(
                "Route"
            )[["ETA (min)"]]
        )
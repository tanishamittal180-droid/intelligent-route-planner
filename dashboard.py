# frontend/dashboard.py

import streamlit as st


class Dashboard:

    def route_cards(
        self,
        summary
    ):

        c1, c2, c3, c4 = st.columns(4)

        with c1:

            st.metric(
                "Distance",
                f"{summary['distance_km']} km"
            )

        with c2:

            st.metric(
                "ETA",
                f"{summary['eta_min']} min"
            )

        with c3:

            st.metric(
                "Tolls",
                summary["tolls"]
            )

        with c4:

            st.metric(
                "Nodes",
                summary["nodes"]
            )
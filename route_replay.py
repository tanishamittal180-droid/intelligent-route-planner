import time
import streamlit as st


class RouteReplay:

    def play(
        self,
        coordinates
    ):

        st.subheader(
            "Route Replay"
        )

        progress = st.progress(
            0
        )

        total = len(
            coordinates
        )

        for i in range(total):

            progress.progress(
                (i + 1) / total
            )

            time.sleep(
                0.02
            )
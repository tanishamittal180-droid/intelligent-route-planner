# backend/export_engine.py

import pandas as pd


class ExportEngine:

    def export_route(
        self,
        directions,
        filename
    ):

        df = pd.DataFrame({

            "Directions":
                directions

        })

        df.to_csv(
            filename,
            index=False
        )

        return filename
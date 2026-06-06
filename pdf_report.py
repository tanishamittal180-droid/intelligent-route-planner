from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

from reportlab.lib.styles import (
    getSampleStyleSheet
)


class PDFReport:

    def generate(
        self,
        filename,
        source,
        destination,
        summary
    ):

        doc = SimpleDocTemplate(
            filename
        )

        styles = (
            getSampleStyleSheet()
        )

        story = []

        story.append(
            Paragraph(
                "Route Report",
                styles["Title"]
            )
        )

        story.append(
            Spacer(1, 20)
        )

        story.append(
            Paragraph(
                f"Source: {source}",
                styles["Normal"]
            )
        )

        story.append(
            Paragraph(
                f"Destination: {destination}",
                styles["Normal"]
            )
        )

        story.append(
            Paragraph(
                f"Distance: {summary['distance_km']} km",
                styles["Normal"]
            )
        )

        story.append(
            Paragraph(
                f"ETA: {summary['eta_min']} min",
                styles["Normal"]
            )
        )

        doc.build(story)

        return filename
    
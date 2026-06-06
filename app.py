import streamlit as st
from streamlit_folium import folium_static

# Backend
from backend.graph_loader import GraphLoader
from backend.geocoder import Geocoder
from backend.traffic_engine import TrafficEngine
from backend.routing_engine import RoutingEngine
from backend.route_geometry import RouteGeometry
from backend.directions_engine import DirectionsEngine
from backend.route_history import RouteHistory
from backend.export_engine import ExportEngine
from backend.sqlite_manager import DatabaseManager
from backend.pdf_report import PDFReport
from backend.ev_routing import EVRouting
from backend.traffic_heatmap import TrafficHeatmap

# Frontend
from frontend.map_view import MapView
from frontend.dashboard import Dashboard
from frontend.analytics import Analytics
from frontend.admin_dashboard import AdminDashboard
from frontend.route_replay import RouteReplay


# ====================================================
# PAGE CONFIG
# ====================================================

st.set_page_config(
    page_title="Intelligent Route Planner Pro",
    layout="wide"
)

st.title("🚀 Intelligent Route Planner Pro")

# ====================================================
# SIDEBAR
# ====================================================

st.sidebar.title("Navigation Control")

show_alternatives = st.sidebar.checkbox(
    "Show Alternative Routes",
    value=True
)

show_history = st.sidebar.checkbox(
    "Show Route History",
    value=True
)

show_heatmap = st.sidebar.checkbox(
    "Traffic Heatmap",
    value=False
)

# ====================================================
# CITY INPUT
# ====================================================

city = st.text_input(
    "City",
    "New Delhi, India"
)

# ====================================================
# LOAD ROAD NETWORK
# ====================================================

if st.button("Load Road Network"):

    with st.spinner(
        "Downloading OpenStreetMap Data..."
    ):

        loader = GraphLoader()

        G = loader.load_city(city)

        traffic = TrafficEngine()

        G = traffic.apply_traffic(G)

        st.session_state["graph"] = G

        st.success(
            "Road Network Loaded Successfully"
        )

# ====================================================
# ROUTING SECTION
# ====================================================

if "graph" in st.session_state:

    G = st.session_state["graph"]

    geocoder = Geocoder()

    routing = RoutingEngine(G)

    source_place = st.text_input(
        "Source Location",
        "India Gate New Delhi"
    )

    destination_place = st.text_input(
        "Destination Location",
        "IGI Airport New Delhi"
    )

    algorithm = st.selectbox(

        "Route Type",

        [
            "A*",
            "Dijkstra",
            "Shortest",
            "Eco"
        ]
    )

    if st.button("Find Route"):

        with st.spinner(
            "Calculating Route..."
        ):

            src = geocoder.search(
                source_place
            )

            dst = geocoder.search(
                destination_place
            )

            if src and dst:

                route = routing.route_from_places(

                    src["latitude"],
                    src["longitude"],

                    dst["latitude"],
                    dst["longitude"],

                    algorithm
                )

                # ====================
                # SUMMARY
                # ====================

                summary = routing.route_summary(
                    route
                )

                dashboard = Dashboard()

                dashboard.route_cards(
                    summary
                )

                # ====================
                # DATABASE
                # ====================

                db = DatabaseManager()

                db.save_route(

                    source_place,

                    destination_place,

                    algorithm,

                    summary["distance_km"],

                    summary["eta_min"]
                )

                # ====================
                # HISTORY
                # ====================

                history = RouteHistory()

                history.save_route(

                    source_place,

                    destination_place,

                    algorithm,

                    summary["distance_km"],

                    summary["eta_min"]
                )

                # ====================
                # MAP
                # ====================

                geometry = RouteGeometry(G)

                coordinates = geometry.extract(
                    route
                )

                map_view = MapView()

                fmap = map_view.draw_route(
                    coordinates
                )

                st.subheader(
                    "Route Map"
                )

                folium_static(
                    fmap,
                    width=1200,
                    height=600
                )

                # ====================
                # DIRECTIONS
                # ====================

                st.subheader(
                    "Turn By Turn Directions"
                )

                direction_engine = (
                    DirectionsEngine(G)
                )

                directions = (
                    direction_engine.generate(
                        route
                    )
                )

                for step in directions:

                    st.write(
                        "➡️",
                        step
                    )

                # ====================
                # CSV EXPORT
                # ====================

                exporter = ExportEngine()

                if st.button(
                    "Export CSV"
                ):

                    filename = (
                        exporter.export_route(

                            directions,

                            "outputs/route.csv"
                        )
                    )

                    st.success(
                        f"Saved: {filename}"
                    )

                # ====================
                # PDF REPORT
                # ====================

                pdf = PDFReport()

                if st.button(
                    "Generate PDF Report"
                ):

                    pdf_file = pdf.generate(

                        "outputs/report.pdf",

                        source_place,

                        destination_place,

                        summary
                    )

                    st.success(
                        f"Saved: {pdf_file}"
                    )

                # ====================
                # ALTERNATIVE ROUTES
                # ====================

                if show_alternatives:

                    st.subheader(
                        "Alternative Routes"
                    )

                    source_node = (
                        routing.nearest_node(

                            src["latitude"],

                            src["longitude"]
                        )
                    )

                    target_node = (
                        routing.nearest_node(

                            dst["latitude"],

                            dst["longitude"]
                        )
                    )

                    alternatives = (

                        routing.alternative_routes(

                            source_node,

                            target_node,

                            k=3
                        )
                    )

                    for i, alt in enumerate(

                        alternatives,

                        start=1
                    ):

                        st.write(
                            f"Route {i}"
                        )

                        st.json(

                            routing.route_summary(
                                alt
                            )
                        )

                # ====================
                # ANALYTICS
                # ====================

                analytics = Analytics()

                analytics.show_route_comparison(

                    [
                        {

                            "Route":
                                algorithm,

                            "Distance (km)":
                                summary[
                                    "distance_km"
                                ],

                            "ETA (min)":
                                summary[
                                    "eta_min"
                                ],

                            "Tolls":
                                summary[
                                    "tolls"
                                ]
                        }
                    ]
                )

                # ====================
                # EV STATIONS
                # ====================

                ev = EVRouting()

                st.subheader(
                    "EV Charging Stations"
                )

                st.json(
                    ev.get_charging_stations()
                )

                # ====================
                # TRAFFIC HEATMAP
                # ====================

                if show_heatmap:

                    st.subheader(
                        "Traffic Heatmap"
                    )

                    heatmap = (
                        TrafficHeatmap()
                    )

                    heat_map = (
                        heatmap.create(
                            coordinates
                        )
                    )

                    folium_static(
                        heat_map,
                        width=1200,
                        height=500
                    )

                # ====================
                # ROUTE REPLAY
                # ====================

                replay = RouteReplay()

                if st.button(
                    "Replay Route"
                ):

                    replay.play(
                        coordinates
                    )

            else:

                st.error(
                    "Location Not Found"
                )

# ====================================================
# ROUTE HISTORY
# ====================================================

if show_history:

    st.sidebar.subheader(
        "Recent Routes"
    )

    history = RouteHistory()

    routes = history.get_history()

    for item in reversed(
        routes[-10:]
    ):

        st.sidebar.write(

            f"{item['source']}"

            f" ➜ "

            f"{item['destination']}"
        )

    if st.sidebar.button(
        "Clear History"
    ):

        history.clear_history()

        st.rerun()

# ====================================================
# ADMIN DASHBOARD
# ====================================================

st.divider()

st.header(
    "📊 Admin Analytics Dashboard"
)

db = DatabaseManager()

admin = AdminDashboard()

admin.show(
    db.get_routes()
)
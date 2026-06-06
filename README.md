🚗 Intelligent Route Planner

An AI-powered route optimization and navigation system that computes the most efficient paths between locations using graph-based algorithms, real-world map data, and geospatial analysis. The system is built using Python and leverages libraries like OSMnx, NetworkX, and geospatial routing techniques.

📌 Features

🗺️ Real-world road network extraction using OpenStreetMap

📍 Convert latitude/longitude into nearest graph nodes

🚀 Fast shortest path computation (Dijkstra / A*)

⏱️ Optimized route selection based on distance or time

📊 Graph-based visualization of routes

🔄 Dynamic routing support (can extend for traffic data)

🧠 Modular backend for API integration

💾 Route history tracking (optional extension)

🏗️ Tech Stack

Python 3.x

OSMnx

NetworkX

NumPy

Pandas

Matplotlib

Flask / FastAPI (optional backend API layer)

📁 Project Structure
intelligent-route-planner/
│
├── backend/
│   ├── routing_engine.py      # Core routing logic
│   ├── graph_builder.py       # Road network loader
│   ├── route_history.py       # Stores past routes
│
├── app.py                     # Main API / application entry point
├── config.py                  # Configuration settings
├── requirements.txt          # Dependencies
├── README.md                 # Project documentation
└── utils/
    ├── geo_utils.py         # Location utilities
    └── helpers.py           # Helper functions

    
⚙️ Installation


1. Clone Repository
git clone https://github.com/your-username/intelligent-route-planner.git
cd intelligent-route-planner

2. Create Virtual Environment
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows

3. Install Dependencies
pip install -r requirements.txt

▶️ Running the Project


Run Backend

python app.py

Example API Request (if using Flask/FastAPI)

POST /route

{
  "source_lat": 28.6139,
  "source_lon": 77.2090,
  "dest_lat": 28.4595,
  "dest_lon": 77.0266
}
Response
{
  "distance": "24.5 km",
  "time_estimate": "45 min",
  "route": [[lat, lon], [lat, lon], ...]
}

🧠 How It Works

Load map data from OpenStreetMap

Build a graph using OSMnx

Convert coordinates into nearest graph nodes

Apply shortest path algorithm (Dijkstra / A*)

Return optimized route
(Optional) Visualize route on map

📊 Algorithms Used

Dijkstra’s Algorithm (Shortest Path)

A* Search Algorithm (Heuristic Optimization)

Graph Traversal (BFS/DFS concepts)

 screenshots

 <img width="1305" height="580" alt="Screenshot 2026-06-05 230046" src="https://github.com/user-attachments/assets/15e706e1-4011-4001-aa7c-3cee2a5a4de9" />
<img width="1333" height="622" alt="Screenshot 2026-06-05 230142" src="https://github.com/user-attachments/assets/72ad6fde-032d-406a-90fd-1f4afcf20661" />
<img width="1366" height="689" alt="Screenshot 2026-06-05 230206" src="https://github.com/user-attachments/assets/e921abc1-87a8-475a-bbd7-450affa2cc86" />
<img width="1354" height="682" alt="Screenshot 2026-06-05 230226" src="https://github.com/user-attachments/assets/a83c95ea-8804-4212-9cd6-ec2b882276cb" />
<img width="1332" height="673" alt="Screenshot 2026-06-05 230307" src="https://github.com/user-attachments/assets/57cb75e3-435a-49e8-8013-0a44eb2e5aee" />


🚀 Future Improvements

🔴 Real-time traffic integration

🚌 Multi-modal transport routing

📡 Live GPS tracking

🤖 AI-based congestion prediction

📱 Mobile app integration

🗺️ Map UI using Leaflet / Mapbox

🧑‍💻 Author

Tanisha Mittal
Project: Intelligent Route Planner
Field: Data Structures + Geospatial AI System

# auto_fetch_geo.py

import os
try:
    import osmnx as ox
except ImportError:
    raise ImportError(
        "Please pip install osmnx to auto-download the Riyadh GeoJSON:\n"
        "    pip install osmnx"
    )

def ensure_riyadh_geojson(path: str = "data/riyadh_neighborhoods.geojson"):
    """
    Downloads admin_level=8 boundaries for Riyadh from OpenStreetMap
    and writes to `path` if it does not already exist.
    """
    if not os.path.exists(path):
        os.makedirs(os.path.dirname(path), exist_ok=True)
        # Fetch all admin boundaries of level 8 in Riyadh
        gdf = ox.geometries_from_place(
            "Riyadh, Saudi Arabia",
            tags={"boundary": "administrative", "admin_level": "8"},
        )
        # Keep only polygons
        gdf = gdf[gdf.geometry.type.isin(["Polygon", "MultiPolygon"])]
        gdf.to_file(path, driver="GeoJSON")
        print(f"✅ Downloaded {len(gdf)} polygons → {path}")
    else:
        print(f"ℹ️ Using existing geojson at {path}")

from dataclasses import dataclass, field
from typing import Dict, Tuple

@dataclass
class Config:
    # Pre-defined lat/lon for each Riyadh region
    region_coords: Dict[str, Tuple[float, float]] = field(
        default_factory=lambda: {
            "North":   (24.865, 46.716),
            "South":   (24.658, 46.712),
            "East":    (24.722, 46.820),
            "West":    (24.700, 46.670),
            "Central": (24.7136, 46.6753),
        }
    )

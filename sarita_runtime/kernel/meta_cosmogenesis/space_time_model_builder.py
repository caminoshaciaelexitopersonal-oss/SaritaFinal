import random

class SpaceTimeModelBuilder:
    """
    Defines the dimensionality and temporal structure of a cosmos.
    """
    def build_model(self, dim_seed, temp_seed):
        spatial_dims = int(dim_seed * 10) + 1 # 1 to 11 dims
        temporal_dims = 1 if temp_seed < 0.8 else 2 # Rare multi-temporal cosmos

        return {
            "spatial_dimensions": spatial_dims,
            "temporal_dimensions": temporal_dims,
            "topology": random.choice(["FLAT", "SPHERICAL", "TOROIDAL", "FRACTAL"]),
            "metric_expansion": round(random.uniform(0.01, 1.0), 4)
        }

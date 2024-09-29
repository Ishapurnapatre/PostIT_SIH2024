# distribution_optimizer.py
from sklearn.cluster import KMeans
import numpy as np

class DistributionOptimizer:
    def __init__(self, letters):
        self.letters = letters

    def convert_to_coordinates(self, pin):
        # For simplicity, convert pin codes into numerical data (pseudo-coordinates)
        return [int(pin[:3]), int(pin[3:])]

    def optimize_distribution(self, num_clusters=3):
        coordinates = [self.convert_to_coordinates(pin) for _, _, _, pin in self.letters]
        coordinates = np.array(coordinates)
        
        # Cluster letters based on their pseudo-coordinates (pin codes)
        kmeans = KMeans(n_clusters=num_clusters)
        kmeans.fit(coordinates)
        clusters = kmeans.predict(coordinates)
        
        # Return clustered letters with their corresponding cluster number
        optimized_distribution = [(letter, cluster) for letter, cluster in zip(self.letters, clusters)]
        return optimized_distribution

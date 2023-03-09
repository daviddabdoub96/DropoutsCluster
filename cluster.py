# Requires BigML Python bindings
#
# Install via: pip install bigml
#
# or clone it:
#   git clone https://github.com/bigmlcom/python.git
from bigml.cluster import Cluster
from bigml.api import BigML
# Downloads and generates a local version of the cluster, if it
# hasn't been downloaded previously.
cluster = Cluster('cluster/6400e6f88f679a72f0177364',
                  api=BigML("daviddabdoub96412",
                            "d28cf9091fefa471997db810683e7437e6993fb8",
                            domain="bigml.io"))
# To predict centroids fill the desired input_data
# in next line. Numeric fields are compulsory.
input_data = {
    "Curricular units 1st sem (evaluations)": 1,
    "Curricular units 1st sem (enrolled)": 1,
    "Curricular units 1st sem (grade)": 1,
    "Curricular units 1st sem (approved)": 1,
    "Age at enrollment": 1,
    "Curricular units 1st sem (credited)": 1,
    "Curricular units 2nd sem (credited)": 1,
    "Curricular units 1st sem (without evaluations)": 1,
    "Inflation rate": 1,
    "GDP": 1,
    "Application order": 1,
    "Curricular units 2nd sem (without evaluations)": 1,
    "Curricular units 2nd sem (grade)": 1,
    "Unemployment rate": 1,
    "Curricular units 2nd sem (enrolled)": 1,
    "Curricular units 2nd sem (approved)": 1,
    "Curricular units 2nd sem (evaluations)": 1}
cluster.centroid(input_data)
# The result is a dict with three keys: distance, centroid_name and
# centroid_id

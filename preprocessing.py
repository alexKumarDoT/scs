# read in main csv file

# make dictionary: key = node id, value = node properties
# use dictionary to create ties

# export into multiple csvs organized under main dir -> labels, relationships -> ... csvs ...

# TODO: csv input to specify types of relationships?


import pandas as pd
import uuid

main_csv = pd.read_csv("SCS.csv")

id2node_dict = {}                   # lookup id by proj
node2prop_dict = {}                 # lookup node props by id
id2label_dict = {}                  # lookup node class by id

def make_id():
    """generates unique key in id2node_dict when called

    Returns:
        node_id: UUID object
    """
    node_id = uuid.uuid4()
    if node_id in id2node_dict.keys():
        node_id = make_id()
    
    return node_id

def make_nodes():
    # take col
        # get unique values
        # associate props with each unique value
        # add to dicts
    return

# save main csv data in dicts
for i, row in main_csv.iterrows():
    node_id = make_id()
    id2node_dict[row["VolpeProjTitle"]] = i
    node2prop_dict[i] = [row["CustAgency"], row["CustOffice"], 
                                        row["CustOverlay"], row["CustSupportingOffice"],
                                        row["CustLead"], row["VolpeProjTitle"], 
                                        row["VolpeProjStaff"], row["VolpeProjDesc"],
                                        row["VolpeProjTaskNum"], row["VolpeProjTheme"]]

# print(main_csv.columns)

# make agency label csv
agencies = pd.unique(main_csv["CustAgency"])
agency_dict = {"Id": [], "CustAgency": [], "Type": []}
# for a in agencies:

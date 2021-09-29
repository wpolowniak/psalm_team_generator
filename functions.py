import numpy as np
import random
import pandas as pd
from io import BytesIO

def split_teams(community_dict, n_teams):
    members = list(community_dict.keys())
    random.shuffle(members)
    teams = np.array_split(members, n_teams)
    sizes = [sum([community_dict[member] for member in team]) for team in teams]
    spread = max(sizes) - min(sizes)
    if spread > 3:
        return split_teams(community_dict, n_teams)

    return format_output(teams)

def format_output(teams):
    consolidated_output = []
    for i, team in enumerate(teams, start=1):
        consolidated_output += [f'Team {i}']
        consolidated_output += list(team)
    return pd.DataFrame(consolidated_output, columns=['Psalm Teams'])

community_members = {
    'Wojtek & Gaba':2,
    'Ryan & Natalie':2,
    'Keone':1,
    'Steve':1,
    'Luke':1,
    'Lucas & Raquel':1,
    'Maria & Manny':2,
    'Dan & Anne':2,
    'Ken & Susan':2,
    'Patrick & Emma':2,
    'Angelica':1,
    'Fr. Jakov':1,
    'Mary A.':1,
    'John & Sadie':2,
    'Mark & Dana':2,
    'Fr. Joe':1,
    'Fr. John':1,
    'Rob & Julie':2,
    'Gianina':1,
    'Mark & Tara':2,
    'Brendan':1,
    'Simone & Laurie':2,
    'Anthony':1,
    'Ed & Mary':2,

}

def copy_to_clipboard(df, index=False):
    df.to_clipboard(index=index)

# Function to convert csv to xlsx
def to_excel(df):
    output = BytesIO()
    writer = pd.ExcelWriter(output, engine='xlsxwriter')
    df.to_excel(writer, sheet_name='Sheet1',index=False)
    writer.save()
    processed_data = output.getvalue()
    return processed_data
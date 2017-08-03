import petl as etl

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#   METHODS FOR CLEANING & DEFINING DB TABLE'S STRUCTURE
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #


def clean_table_headers(table):

    # CLEAN UP COLUMN HEADERS FOR DATABASE TABLE
    table = etl.rename(table, {'Day': 'DAY',
                               'Customer ID': 'CUSTOMER_ID',
                               'Campaign ID': 'CAMPAIGN_ID',
                               'Campaign': 'CAMPAIGN',
                               'Campaign state': 'CAMPAIGN_STATE',
                               'Campaign serving status': 'CAMPAIGN_SERVING_STATUS',
                               'Clicks': 'CLICKS',
                               'Start date': 'START_DATE',
                               'End date': 'END_DATE',
                               'Budget': 'BUDGET',
                               'Budget ID': 'BUDGET_ID',
                               'Budget explicitly shared': 'BUDGET_EXPLICITLY_SHARED',
                               'Label IDs': 'LABEL_IDS',
                               'Labels': 'LABELS',
                               'Invalid clicks': 'INVALID_CLICKS',
                               'Conversions': 'CONVERSIONS',
                               'Conv. rate': 'CONV_RATE',
                               'Cost': 'COST',
                               'Impressions': 'IMPRESSIONS',
                               'Search Lost IS (rank)': 'SEARCH_LOST_IS_RANK',
                               'Avg. position': 'AVG_POSITION',
                               'Interaction Rate': 'INTERACTION_RATE',
                               'Interactions': 'INTERACTIONS'
                               })
    return table


def clean_table_data(table):

    # CLEAN UP NULL VALUES
    table = etl.convert(table, 'LABEL_IDS', 'replace', '--', None)
    table = etl.convert(table, 'LABELS', 'replace', '--', None)

    isodate = etl.dateparser('%Y-%m-%d')

    # SPECIFY DATA TYPES FOR EACH COLUMN OF DATABASE
    table = etl.convert(table, {'DAY': isodate,
                                  'CUSTOMER_ID': int,
                                  'CAMPAIGN_ID': int,
                                  'CLICKS': int,
                                  'START_DATE': isodate,
                                  'END_DATE': isodate,
                                  'BUDGET': int,
                                  'BUDGET_ID': int,
                                  'INVALID_CLICKS': int,
                                  'CONVERSIONS': float,
                                  'CONV_RATE': float,
                                  'CTR': float,
                                  'COST': int,
                                  'IMPRESSIONS': int,
                                  'SEARCH_LOST_IS_RANK': float,
                                  'AVG_POSITION': float,
                                  'INTERACTION_RATE': float,
                                  'INTERACTIONS': int
                                })

    # CONVERT PERCENTAGES TO DECIMAL/RATIO FORMAT
    table = etl.convert(table, 'CONV_RATE', lambda v: v / 100)
    table = etl.convert(table, 'CTR', lambda v: v / 100)
    table = etl.convert(table, 'SEARCH_LOST_IS_RANK', lambda v: v / 100)
    table = etl.convert(table, 'INTERACTION_RATE', lambda v: v / 100)

    return table

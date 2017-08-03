## Interview Coding Exercise
#### Completed by Dustin Fay

##### Tasks:
* Parse the included delimited file.
    * Results saved to `example_report_clean.csv.gz`
* Insert the results into a database.
	* PETL was used for data definitions. See: `table_manipulation.py`
* Display the results.
    * Ideally would have displayed table using Jinja2 with Flask but built my own html structure within a loop instead. See: `database.py`
    * _Before_ & _after_ tables are printed to the console

##### Files requested in prompt:
* `example_report_clean.csv.gz`
* `postgresql_table_dump.csv`

_Note: Most all of this was new to me so I didn't have much time to focus on object oriented design and PEP8 standards. In hindsight there is a lot I would do differently but this was a fantastic learning experience. Thanks for your consideration!_

-------------------
Database Table Info:

```bash
postgres-# \d+ digi_data
```

```
                                       Table "public.digi_data"
          Column          |         Type          | Modifiers | Storage  | Stats target | Description
--------------------------+-----------------------+-----------+----------+--------------+-------------
 DAY                      | date                  | not null  | plain    |              |
 CUSTOMER_ID              | integer               | not null  | plain    |              |
 CAMPAIGN_ID              | integer               | not null  | plain    |              |
 CAMPAIGN                 | character varying(9)  | not null  | extended |              |
 CAMPAIGN_STATE           | character varying(7)  | not null  | extended |              |
 CAMPAIGN_SERVING_STATUS  | character varying(5)  | not null  | extended |              |
 CLICKS                   | integer               | not null  | plain    |              |
 START_DATE               | date                  | not null  | plain    |              |
 END_DATE                 | date                  | not null  | plain    |              |
 BUDGET                   | integer               | not null  | plain    |              |
 BUDGET_ID                | integer               | not null  | plain    |              |
 BUDGET_EXPLICITLY_SHARED | character varying(5)  | not null  | extended |              |
 LABEL_IDS                | character varying(32) |           | extended |              |
 LABELS                   | character varying(32) |           | extended |              |
 INVALID_CLICKS           | integer               | not null  | plain    |              |
 CONVERSIONS              | double precision      | not null  | plain    |              |
 CONV_RATE                | double precision      | not null  | plain    |              |
 CTR                      | double precision      | not null  | plain    |              |
 COST                     | integer               | not null  | plain    |              |
 IMPRESSIONS              | integer               | not null  | plain    |              |
 SEARCH_LOST_IS_RANK      | double precision      | not null  | plain    |              |
 AVG_POSITION             | double precision      | not null  | plain    |              |
 INTERACTION_RATE         | double precision      | not null  | plain    |              |
 INTERACTIONS             | integer               | not null  | plain    |              |
```




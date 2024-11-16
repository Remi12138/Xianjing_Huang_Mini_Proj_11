The operation is load data

The truncated output is: 

|    | country           |   beer_servings |   spirit_servings |   wine_servings |   total_litres_of_pure_alcohol |
|---:|:------------------|----------------:|------------------:|----------------:|-------------------------------:|
|  0 | Afghanistan       |               0 |                 0 |               0 |                            0   |
|  1 | Albania           |              89 |               132 |              54 |                            4.9 |
|  2 | Algeria           |              25 |                 0 |              14 |                            0.7 |
|  3 | Andorra           |             245 |               138 |             312 |                           12.4 |
|  4 | Angola            |             217 |                57 |              45 |                            5.9 |
|  5 | Antigua & Barbuda |             102 |               128 |              45 |                            4.9 |
|  6 | Argentina         |             193 |                25 |             221 |                            8.3 |
|  7 | Armenia           |              21 |               179 |              11 |                            3.8 |
|  8 | Australia         |             261 |                72 |             212 |                           10.4 |
|  9 | Austria           |             279 |                75 |             191 |                            9.7 |

The operation is describe data

The truncated output is: 

|    | summary   | country     |   beer_servings |   spirit_servings |   wine_servings |   total_litres_of_pure_alcohol |
|---:|:----------|:------------|----------------:|------------------:|----------------:|-------------------------------:|
|  0 | count     | 193         |         193     |          193      |        193      |                       193      |
|  1 | mean      |             |         106.161 |           80.9948 |         49.4508 |                         4.7171 |
|  2 | stddev    |             |         101.143 |           88.2843 |         79.6976 |                         3.7733 |
|  3 | min       | Afghanistan |           0     |            0      |          0      |                         0      |
|  4 | max       | Zimbabwe    |         376     |          438      |        370      |                        14.4    |

The operation is query data

The query is 
        SELECT country, total_litres_of_pure_alcohol
        FROM DrinkData
        ORDER BY total_litres_of_pure_alcohol
        DESC
        LIMIT 5
        

The truncated output is: 

|    | country   |   total_litres_of_pure_alcohol |
|---:|:----------|-------------------------------:|
|  0 | Belarus   |                           14.4 |
|  1 | Lithuania |                           12.9 |
|  2 | Andorra   |                           12.4 |
|  3 | Grenada   |                           11.9 |
|  4 | France    |                           11.8 |

The operation is transform data

The truncated output is: 

|    | country           |   beer_servings |   spirit_servings |   wine_servings |   total_litres_of_pure_alcohol |   total_alcohol_servings |   average_servings |
|---:|:------------------|----------------:|------------------:|----------------:|-------------------------------:|-------------------------:|-------------------:|
|  0 | Afghanistan       |               0 |                 0 |               0 |                            0   |                        0 |               0    |
|  1 | Albania           |              89 |               132 |              54 |                            4.9 |                      275 |              91.67 |
|  2 | Algeria           |              25 |                 0 |              14 |                            0.7 |                       39 |              13    |
|  3 | Andorra           |             245 |               138 |             312 |                           12.4 |                      695 |             231.67 |
|  4 | Angola            |             217 |                57 |              45 |                            5.9 |                      319 |             106.33 |
|  5 | Antigua & Barbuda |             102 |               128 |              45 |                            4.9 |                      275 |              91.67 |
|  6 | Argentina         |             193 |                25 |             221 |                            8.3 |                      439 |             146.33 |
|  7 | Armenia           |              21 |               179 |              11 |                            3.8 |                      211 |              70.33 |
|  8 | Australia         |             261 |                72 |             212 |                           10.4 |                      545 |             181.67 |
|  9 | Austria           |             279 |                75 |             191 |                            9.7 |                      545 |             181.67 |

The operation is load data

The truncated output is: 

|    | country           |   beer_servings |   spirit_servings |   wine_servings |   total_litres_of_pure_alcohol |
|---:|:------------------|----------------:|------------------:|----------------:|-------------------------------:|
|  0 | Afghanistan       |               0 |                 0 |               0 |                            0   |
|  1 | Albania           |              89 |               132 |              54 |                            4.9 |
|  2 | Algeria           |              25 |                 0 |              14 |                            0.7 |
|  3 | Andorra           |             245 |               138 |             312 |                           12.4 |
|  4 | Angola            |             217 |                57 |              45 |                            5.9 |
|  5 | Antigua & Barbuda |             102 |               128 |              45 |                            4.9 |
|  6 | Argentina         |             193 |                25 |             221 |                            8.3 |
|  7 | Armenia           |              21 |               179 |              11 |                            3.8 |
|  8 | Australia         |             261 |                72 |             212 |                           10.4 |
|  9 | Austria           |             279 |                75 |             191 |                            9.7 |

The operation is load data

The truncated output is: 

|    | country           |   beer_servings |   spirit_servings |   wine_servings |   total_litres_of_pure_alcohol |
|---:|:------------------|----------------:|------------------:|----------------:|-------------------------------:|
|  0 | Afghanistan       |               0 |                 0 |               0 |                            0   |
|  1 | Albania           |              89 |               132 |              54 |                            4.9 |
|  2 | Algeria           |              25 |                 0 |              14 |                            0.7 |
|  3 | Andorra           |             245 |               138 |             312 |                           12.4 |
|  4 | Angola            |             217 |                57 |              45 |                            5.9 |
|  5 | Antigua & Barbuda |             102 |               128 |              45 |                            4.9 |
|  6 | Argentina         |             193 |                25 |             221 |                            8.3 |
|  7 | Armenia           |              21 |               179 |              11 |                            3.8 |
|  8 | Australia         |             261 |                72 |             212 |                           10.4 |
|  9 | Austria           |             279 |                75 |             191 |                            9.7 |

The operation is describe data

The truncated output is: 

|    | summary   | country     |   beer_servings |   spirit_servings |   wine_servings |   total_litres_of_pure_alcohol |
|---:|:----------|:------------|----------------:|------------------:|----------------:|-------------------------------:|
|  0 | count     | 193         |         193     |          193      |        193      |                       193      |
|  1 | mean      |             |         106.161 |           80.9948 |         49.4508 |                         4.7171 |
|  2 | stddev    |             |         101.143 |           88.2843 |         79.6976 |                         3.7733 |
|  3 | min       | Afghanistan |           0     |            0      |          0      |                         0      |
|  4 | max       | Zimbabwe    |         376     |          438      |        370      |                        14.4    |

The operation is load data

The truncated output is: 

|    | country           |   beer_servings |   spirit_servings |   wine_servings |   total_litres_of_pure_alcohol |
|---:|:------------------|----------------:|------------------:|----------------:|-------------------------------:|
|  0 | Afghanistan       |               0 |                 0 |               0 |                            0   |
|  1 | Albania           |              89 |               132 |              54 |                            4.9 |
|  2 | Algeria           |              25 |                 0 |              14 |                            0.7 |
|  3 | Andorra           |             245 |               138 |             312 |                           12.4 |
|  4 | Angola            |             217 |                57 |              45 |                            5.9 |
|  5 | Antigua & Barbuda |             102 |               128 |              45 |                            4.9 |
|  6 | Argentina         |             193 |                25 |             221 |                            8.3 |
|  7 | Armenia           |              21 |               179 |              11 |                            3.8 |
|  8 | Australia         |             261 |                72 |             212 |                           10.4 |
|  9 | Austria           |             279 |                75 |             191 |                            9.7 |

The operation is query data

The query is SELECT * FROM DrinkData WHERE country = 'Angola'

The truncated output is: 

|    | country   |   beer_servings |   spirit_servings |   wine_servings |   total_litres_of_pure_alcohol |
|---:|:----------|----------------:|------------------:|----------------:|-------------------------------:|
|  0 | Angola    |             217 |                57 |              45 |                            5.9 |

The operation is load data

The truncated output is: 

|    | country           |   beer_servings |   spirit_servings |   wine_servings |   total_litres_of_pure_alcohol |
|---:|:------------------|----------------:|------------------:|----------------:|-------------------------------:|
|  0 | Afghanistan       |               0 |                 0 |               0 |                            0   |
|  1 | Albania           |              89 |               132 |              54 |                            4.9 |
|  2 | Algeria           |              25 |                 0 |              14 |                            0.7 |
|  3 | Andorra           |             245 |               138 |             312 |                           12.4 |
|  4 | Angola            |             217 |                57 |              45 |                            5.9 |
|  5 | Antigua & Barbuda |             102 |               128 |              45 |                            4.9 |
|  6 | Argentina         |             193 |                25 |             221 |                            8.3 |
|  7 | Armenia           |              21 |               179 |              11 |                            3.8 |
|  8 | Australia         |             261 |                72 |             212 |                           10.4 |
|  9 | Austria           |             279 |                75 |             191 |                            9.7 |

The operation is transform data

The truncated output is: 

|    | country           |   beer_servings |   spirit_servings |   wine_servings |   total_litres_of_pure_alcohol |   total_alcohol_servings |   average_servings |
|---:|:------------------|----------------:|------------------:|----------------:|-------------------------------:|-------------------------:|-------------------:|
|  0 | Afghanistan       |               0 |                 0 |               0 |                            0   |                        0 |               0    |
|  1 | Albania           |              89 |               132 |              54 |                            4.9 |                      275 |              91.67 |
|  2 | Algeria           |              25 |                 0 |              14 |                            0.7 |                       39 |              13    |
|  3 | Andorra           |             245 |               138 |             312 |                           12.4 |                      695 |             231.67 |
|  4 | Angola            |             217 |                57 |              45 |                            5.9 |                      319 |             106.33 |
|  5 | Antigua & Barbuda |             102 |               128 |              45 |                            4.9 |                      275 |              91.67 |
|  6 | Argentina         |             193 |                25 |             221 |                            8.3 |                      439 |             146.33 |
|  7 | Armenia           |              21 |               179 |              11 |                            3.8 |                      211 |              70.33 |
|  8 | Australia         |             261 |                72 |             212 |                           10.4 |                      545 |             181.67 |
|  9 | Austria           |             279 |                75 |             191 |                            9.7 |                      545 |             181.67 |

The operation is load data

The truncated output is: 

|    | country           |   beer_servings |   spirit_servings |   wine_servings |   total_litres_of_pure_alcohol |
|---:|:------------------|----------------:|------------------:|----------------:|-------------------------------:|
|  0 | Afghanistan       |               0 |                 0 |               0 |                            0   |
|  1 | Albania           |              89 |               132 |              54 |                            4.9 |
|  2 | Algeria           |              25 |                 0 |              14 |                            0.7 |
|  3 | Andorra           |             245 |               138 |             312 |                           12.4 |
|  4 | Angola            |             217 |                57 |              45 |                            5.9 |
|  5 | Antigua & Barbuda |             102 |               128 |              45 |                            4.9 |
|  6 | Argentina         |             193 |                25 |             221 |                            8.3 |
|  7 | Armenia           |              21 |               179 |              11 |                            3.8 |
|  8 | Australia         |             261 |                72 |             212 |                           10.4 |
|  9 | Austria           |             279 |                75 |             191 |                            9.7 |

The operation is load data

The truncated output is: 

|    | country           |   beer_servings |   spirit_servings |   wine_servings |   total_litres_of_pure_alcohol |
|---:|:------------------|----------------:|------------------:|----------------:|-------------------------------:|
|  0 | Afghanistan       |               0 |                 0 |               0 |                            0   |
|  1 | Albania           |              89 |               132 |              54 |                            4.9 |
|  2 | Algeria           |              25 |                 0 |              14 |                            0.7 |
|  3 | Andorra           |             245 |               138 |             312 |                           12.4 |
|  4 | Angola            |             217 |                57 |              45 |                            5.9 |
|  5 | Antigua & Barbuda |             102 |               128 |              45 |                            4.9 |
|  6 | Argentina         |             193 |                25 |             221 |                            8.3 |
|  7 | Armenia           |              21 |               179 |              11 |                            3.8 |
|  8 | Australia         |             261 |                72 |             212 |                           10.4 |
|  9 | Austria           |             279 |                75 |             191 |                            9.7 |

The operation is describe data

The truncated output is: 

|    | summary   | country     |   beer_servings |   spirit_servings |   wine_servings |   total_litres_of_pure_alcohol |
|---:|:----------|:------------|----------------:|------------------:|----------------:|-------------------------------:|
|  0 | count     | 193         |         193     |          193      |        193      |                       193      |
|  1 | mean      |             |         106.161 |           80.9948 |         49.4508 |                         4.7171 |
|  2 | stddev    |             |         101.143 |           88.2843 |         79.6976 |                         3.7733 |
|  3 | min       | Afghanistan |           0     |            0      |          0      |                         0      |
|  4 | max       | Zimbabwe    |         376     |          438      |        370      |                        14.4    |

The operation is load data

The truncated output is: 

|    | country           |   beer_servings |   spirit_servings |   wine_servings |   total_litres_of_pure_alcohol |
|---:|:------------------|----------------:|------------------:|----------------:|-------------------------------:|
|  0 | Afghanistan       |               0 |                 0 |               0 |                            0   |
|  1 | Albania           |              89 |               132 |              54 |                            4.9 |
|  2 | Algeria           |              25 |                 0 |              14 |                            0.7 |
|  3 | Andorra           |             245 |               138 |             312 |                           12.4 |
|  4 | Angola            |             217 |                57 |              45 |                            5.9 |
|  5 | Antigua & Barbuda |             102 |               128 |              45 |                            4.9 |
|  6 | Argentina         |             193 |                25 |             221 |                            8.3 |
|  7 | Armenia           |              21 |               179 |              11 |                            3.8 |
|  8 | Australia         |             261 |                72 |             212 |                           10.4 |
|  9 | Austria           |             279 |                75 |             191 |                            9.7 |

The operation is query data

The query is SELECT * FROM DrinkData WHERE country = 'Angola'

The truncated output is: 

|    | country   |   beer_servings |   spirit_servings |   wine_servings |   total_litres_of_pure_alcohol |
|---:|:----------|----------------:|------------------:|----------------:|-------------------------------:|
|  0 | Angola    |             217 |                57 |              45 |                            5.9 |

The operation is load data

The truncated output is: 

|    | country           |   beer_servings |   spirit_servings |   wine_servings |   total_litres_of_pure_alcohol |
|---:|:------------------|----------------:|------------------:|----------------:|-------------------------------:|
|  0 | Afghanistan       |               0 |                 0 |               0 |                            0   |
|  1 | Albania           |              89 |               132 |              54 |                            4.9 |
|  2 | Algeria           |              25 |                 0 |              14 |                            0.7 |
|  3 | Andorra           |             245 |               138 |             312 |                           12.4 |
|  4 | Angola            |             217 |                57 |              45 |                            5.9 |
|  5 | Antigua & Barbuda |             102 |               128 |              45 |                            4.9 |
|  6 | Argentina         |             193 |                25 |             221 |                            8.3 |
|  7 | Armenia           |              21 |               179 |              11 |                            3.8 |
|  8 | Australia         |             261 |                72 |             212 |                           10.4 |
|  9 | Austria           |             279 |                75 |             191 |                            9.7 |

The operation is transform data

The truncated output is: 

|    | country           |   beer_servings |   spirit_servings |   wine_servings |   total_litres_of_pure_alcohol |   total_alcohol_servings |   average_servings |
|---:|:------------------|----------------:|------------------:|----------------:|-------------------------------:|-------------------------:|-------------------:|
|  0 | Afghanistan       |               0 |                 0 |               0 |                            0   |                        0 |               0    |
|  1 | Albania           |              89 |               132 |              54 |                            4.9 |                      275 |              91.67 |
|  2 | Algeria           |              25 |                 0 |              14 |                            0.7 |                       39 |              13    |
|  3 | Andorra           |             245 |               138 |             312 |                           12.4 |                      695 |             231.67 |
|  4 | Angola            |             217 |                57 |              45 |                            5.9 |                      319 |             106.33 |
|  5 | Antigua & Barbuda |             102 |               128 |              45 |                            4.9 |                      275 |              91.67 |
|  6 | Argentina         |             193 |                25 |             221 |                            8.3 |                      439 |             146.33 |
|  7 | Armenia           |              21 |               179 |              11 |                            3.8 |                      211 |              70.33 |
|  8 | Australia         |             261 |                72 |             212 |                           10.4 |                      545 |             181.67 |
|  9 | Austria           |             279 |                75 |             191 |                            9.7 |                      545 |             181.67 |

The operation is load data

The truncated output is: 

|    | country           |   beer_servings |   spirit_servings |   wine_servings |   total_litres_of_pure_alcohol |
|---:|:------------------|----------------:|------------------:|----------------:|-------------------------------:|
|  0 | Afghanistan       |               0 |                 0 |               0 |                            0   |
|  1 | Albania           |              89 |               132 |              54 |                            4.9 |
|  2 | Algeria           |              25 |                 0 |              14 |                            0.7 |
|  3 | Andorra           |             245 |               138 |             312 |                           12.4 |
|  4 | Angola            |             217 |                57 |              45 |                            5.9 |
|  5 | Antigua & Barbuda |             102 |               128 |              45 |                            4.9 |
|  6 | Argentina         |             193 |                25 |             221 |                            8.3 |
|  7 | Armenia           |              21 |               179 |              11 |                            3.8 |
|  8 | Australia         |             261 |                72 |             212 |                           10.4 |
|  9 | Austria           |             279 |                75 |             191 |                            9.7 |

The operation is load data

The truncated output is: 

|    | country           |   beer_servings |   spirit_servings |   wine_servings |   total_litres_of_pure_alcohol |
|---:|:------------------|----------------:|------------------:|----------------:|-------------------------------:|
|  0 | Afghanistan       |               0 |                 0 |               0 |                            0   |
|  1 | Albania           |              89 |               132 |              54 |                            4.9 |
|  2 | Algeria           |              25 |                 0 |              14 |                            0.7 |
|  3 | Andorra           |             245 |               138 |             312 |                           12.4 |
|  4 | Angola            |             217 |                57 |              45 |                            5.9 |
|  5 | Antigua & Barbuda |             102 |               128 |              45 |                            4.9 |
|  6 | Argentina         |             193 |                25 |             221 |                            8.3 |
|  7 | Armenia           |              21 |               179 |              11 |                            3.8 |
|  8 | Australia         |             261 |                72 |             212 |                           10.4 |
|  9 | Austria           |             279 |                75 |             191 |                            9.7 |

The operation is describe data

The truncated output is: 

|    | summary   | country     |   beer_servings |   spirit_servings |   wine_servings |   total_litres_of_pure_alcohol |
|---:|:----------|:------------|----------------:|------------------:|----------------:|-------------------------------:|
|  0 | count     | 193         |         193     |          193      |        193      |                       193      |
|  1 | mean      |             |         106.161 |           80.9948 |         49.4508 |                         4.7171 |
|  2 | stddev    |             |         101.143 |           88.2843 |         79.6976 |                         3.7733 |
|  3 | min       | Afghanistan |           0     |            0      |          0      |                         0      |
|  4 | max       | Zimbabwe    |         376     |          438      |        370      |                        14.4    |

The operation is load data

The truncated output is: 

|    | country           |   beer_servings |   spirit_servings |   wine_servings |   total_litres_of_pure_alcohol |
|---:|:------------------|----------------:|------------------:|----------------:|-------------------------------:|
|  0 | Afghanistan       |               0 |                 0 |               0 |                            0   |
|  1 | Albania           |              89 |               132 |              54 |                            4.9 |
|  2 | Algeria           |              25 |                 0 |              14 |                            0.7 |
|  3 | Andorra           |             245 |               138 |             312 |                           12.4 |
|  4 | Angola            |             217 |                57 |              45 |                            5.9 |
|  5 | Antigua & Barbuda |             102 |               128 |              45 |                            4.9 |
|  6 | Argentina         |             193 |                25 |             221 |                            8.3 |
|  7 | Armenia           |              21 |               179 |              11 |                            3.8 |
|  8 | Australia         |             261 |                72 |             212 |                           10.4 |
|  9 | Austria           |             279 |                75 |             191 |                            9.7 |

The operation is query data

The query is SELECT * FROM DrinkData WHERE country = 'Angola'

The truncated output is: 

|    | country   |   beer_servings |   spirit_servings |   wine_servings |   total_litres_of_pure_alcohol |
|---:|:----------|----------------:|------------------:|----------------:|-------------------------------:|
|  0 | Angola    |             217 |                57 |              45 |                            5.9 |

The operation is load data

The truncated output is: 

|    | country           |   beer_servings |   spirit_servings |   wine_servings |   total_litres_of_pure_alcohol |
|---:|:------------------|----------------:|------------------:|----------------:|-------------------------------:|
|  0 | Afghanistan       |               0 |                 0 |               0 |                            0   |
|  1 | Albania           |              89 |               132 |              54 |                            4.9 |
|  2 | Algeria           |              25 |                 0 |              14 |                            0.7 |
|  3 | Andorra           |             245 |               138 |             312 |                           12.4 |
|  4 | Angola            |             217 |                57 |              45 |                            5.9 |
|  5 | Antigua & Barbuda |             102 |               128 |              45 |                            4.9 |
|  6 | Argentina         |             193 |                25 |             221 |                            8.3 |
|  7 | Armenia           |              21 |               179 |              11 |                            3.8 |
|  8 | Australia         |             261 |                72 |             212 |                           10.4 |
|  9 | Austria           |             279 |                75 |             191 |                            9.7 |

The operation is transform data

The truncated output is: 

|    | country           |   beer_servings |   spirit_servings |   wine_servings |   total_litres_of_pure_alcohol |   total_alcohol_servings |   average_servings |
|---:|:------------------|----------------:|------------------:|----------------:|-------------------------------:|-------------------------:|-------------------:|
|  0 | Afghanistan       |               0 |                 0 |               0 |                            0   |                        0 |               0    |
|  1 | Albania           |              89 |               132 |              54 |                            4.9 |                      275 |              91.67 |
|  2 | Algeria           |              25 |                 0 |              14 |                            0.7 |                       39 |              13    |
|  3 | Andorra           |             245 |               138 |             312 |                           12.4 |                      695 |             231.67 |
|  4 | Angola            |             217 |                57 |              45 |                            5.9 |                      319 |             106.33 |
|  5 | Antigua & Barbuda |             102 |               128 |              45 |                            4.9 |                      275 |              91.67 |
|  6 | Argentina         |             193 |                25 |             221 |                            8.3 |                      439 |             146.33 |
|  7 | Armenia           |              21 |               179 |              11 |                            3.8 |                      211 |              70.33 |
|  8 | Australia         |             261 |                72 |             212 |                           10.4 |                      545 |             181.67 |
|  9 | Austria           |             279 |                75 |             191 |                            9.7 |                      545 |             181.67 |

The operation is load data

The truncated output is: 

|    | country           |   beer_servings |   spirit_servings |   wine_servings |   total_litres_of_pure_alcohol |
|---:|:------------------|----------------:|------------------:|----------------:|-------------------------------:|
|  0 | Afghanistan       |               0 |                 0 |               0 |                            0   |
|  1 | Albania           |              89 |               132 |              54 |                            4.9 |
|  2 | Algeria           |              25 |                 0 |              14 |                            0.7 |
|  3 | Andorra           |             245 |               138 |             312 |                           12.4 |
|  4 | Angola            |             217 |                57 |              45 |                            5.9 |
|  5 | Antigua & Barbuda |             102 |               128 |              45 |                            4.9 |
|  6 | Argentina         |             193 |                25 |             221 |                            8.3 |
|  7 | Armenia           |              21 |               179 |              11 |                            3.8 |
|  8 | Australia         |             261 |                72 |             212 |                           10.4 |
|  9 | Austria           |             279 |                75 |             191 |                            9.7 |

The operation is load data

The truncated output is: 

|    | country           |   beer_servings |   spirit_servings |   wine_servings |   total_litres_of_pure_alcohol |
|---:|:------------------|----------------:|------------------:|----------------:|-------------------------------:|
|  0 | Afghanistan       |               0 |                 0 |               0 |                            0   |
|  1 | Albania           |              89 |               132 |              54 |                            4.9 |
|  2 | Algeria           |              25 |                 0 |              14 |                            0.7 |
|  3 | Andorra           |             245 |               138 |             312 |                           12.4 |
|  4 | Angola            |             217 |                57 |              45 |                            5.9 |
|  5 | Antigua & Barbuda |             102 |               128 |              45 |                            4.9 |
|  6 | Argentina         |             193 |                25 |             221 |                            8.3 |
|  7 | Armenia           |              21 |               179 |              11 |                            3.8 |
|  8 | Australia         |             261 |                72 |             212 |                           10.4 |
|  9 | Austria           |             279 |                75 |             191 |                            9.7 |

The operation is describe data

The truncated output is: 

|    | summary   | country     |   beer_servings |   spirit_servings |   wine_servings |   total_litres_of_pure_alcohol |
|---:|:----------|:------------|----------------:|------------------:|----------------:|-------------------------------:|
|  0 | count     | 193         |         193     |          193      |        193      |                       193      |
|  1 | mean      |             |         106.161 |           80.9948 |         49.4508 |                         4.7171 |
|  2 | stddev    |             |         101.143 |           88.2843 |         79.6976 |                         3.7733 |
|  3 | min       | Afghanistan |           0     |            0      |          0      |                         0      |
|  4 | max       | Zimbabwe    |         376     |          438      |        370      |                        14.4    |

The operation is load data

The truncated output is: 

|    | country           |   beer_servings |   spirit_servings |   wine_servings |   total_litres_of_pure_alcohol |
|---:|:------------------|----------------:|------------------:|----------------:|-------------------------------:|
|  0 | Afghanistan       |               0 |                 0 |               0 |                            0   |
|  1 | Albania           |              89 |               132 |              54 |                            4.9 |
|  2 | Algeria           |              25 |                 0 |              14 |                            0.7 |
|  3 | Andorra           |             245 |               138 |             312 |                           12.4 |
|  4 | Angola            |             217 |                57 |              45 |                            5.9 |
|  5 | Antigua & Barbuda |             102 |               128 |              45 |                            4.9 |
|  6 | Argentina         |             193 |                25 |             221 |                            8.3 |
|  7 | Armenia           |              21 |               179 |              11 |                            3.8 |
|  8 | Australia         |             261 |                72 |             212 |                           10.4 |
|  9 | Austria           |             279 |                75 |             191 |                            9.7 |

The operation is query data

The query is SELECT * FROM DrinkData WHERE country = 'Angola'

The truncated output is: 

|    | country   |   beer_servings |   spirit_servings |   wine_servings |   total_litres_of_pure_alcohol |
|---:|:----------|----------------:|------------------:|----------------:|-------------------------------:|
|  0 | Angola    |             217 |                57 |              45 |                            5.9 |

The operation is load data

The truncated output is: 

|    | country           |   beer_servings |   spirit_servings |   wine_servings |   total_litres_of_pure_alcohol |
|---:|:------------------|----------------:|------------------:|----------------:|-------------------------------:|
|  0 | Afghanistan       |               0 |                 0 |               0 |                            0   |
|  1 | Albania           |              89 |               132 |              54 |                            4.9 |
|  2 | Algeria           |              25 |                 0 |              14 |                            0.7 |
|  3 | Andorra           |             245 |               138 |             312 |                           12.4 |
|  4 | Angola            |             217 |                57 |              45 |                            5.9 |
|  5 | Antigua & Barbuda |             102 |               128 |              45 |                            4.9 |
|  6 | Argentina         |             193 |                25 |             221 |                            8.3 |
|  7 | Armenia           |              21 |               179 |              11 |                            3.8 |
|  8 | Australia         |             261 |                72 |             212 |                           10.4 |
|  9 | Austria           |             279 |                75 |             191 |                            9.7 |

The operation is transform data

The truncated output is: 

|    | country           |   beer_servings |   spirit_servings |   wine_servings |   total_litres_of_pure_alcohol |   total_alcohol_servings |   average_servings |
|---:|:------------------|----------------:|------------------:|----------------:|-------------------------------:|-------------------------:|-------------------:|
|  0 | Afghanistan       |               0 |                 0 |               0 |                            0   |                        0 |               0    |
|  1 | Albania           |              89 |               132 |              54 |                            4.9 |                      275 |              91.67 |
|  2 | Algeria           |              25 |                 0 |              14 |                            0.7 |                       39 |              13    |
|  3 | Andorra           |             245 |               138 |             312 |                           12.4 |                      695 |             231.67 |
|  4 | Angola            |             217 |                57 |              45 |                            5.9 |                      319 |             106.33 |
|  5 | Antigua & Barbuda |             102 |               128 |              45 |                            4.9 |                      275 |              91.67 |
|  6 | Argentina         |             193 |                25 |             221 |                            8.3 |                      439 |             146.33 |
|  7 | Armenia           |              21 |               179 |              11 |                            3.8 |                      211 |              70.33 |
|  8 | Australia         |             261 |                72 |             212 |                           10.4 |                      545 |             181.67 |
|  9 | Austria           |             279 |                75 |             191 |                            9.7 |                      545 |             181.67 |

The operation is load data

The truncated output is: 

|    | country           |   beer_servings |   spirit_servings |   wine_servings |   total_litres_of_pure_alcohol |
|---:|:------------------|----------------:|------------------:|----------------:|-------------------------------:|
|  0 | Afghanistan       |               0 |                 0 |               0 |                            0   |
|  1 | Albania           |              89 |               132 |              54 |                            4.9 |
|  2 | Algeria           |              25 |                 0 |              14 |                            0.7 |
|  3 | Andorra           |             245 |               138 |             312 |                           12.4 |
|  4 | Angola            |             217 |                57 |              45 |                            5.9 |
|  5 | Antigua & Barbuda |             102 |               128 |              45 |                            4.9 |
|  6 | Argentina         |             193 |                25 |             221 |                            8.3 |
|  7 | Armenia           |              21 |               179 |              11 |                            3.8 |
|  8 | Australia         |             261 |                72 |             212 |                           10.4 |
|  9 | Austria           |             279 |                75 |             191 |                            9.7 |

The operation is load data

The truncated output is: 

|    | country           |   beer_servings |   spirit_servings |   wine_servings |   total_litres_of_pure_alcohol |
|---:|:------------------|----------------:|------------------:|----------------:|-------------------------------:|
|  0 | Afghanistan       |               0 |                 0 |               0 |                            0   |
|  1 | Albania           |              89 |               132 |              54 |                            4.9 |
|  2 | Algeria           |              25 |                 0 |              14 |                            0.7 |
|  3 | Andorra           |             245 |               138 |             312 |                           12.4 |
|  4 | Angola            |             217 |                57 |              45 |                            5.9 |
|  5 | Antigua & Barbuda |             102 |               128 |              45 |                            4.9 |
|  6 | Argentina         |             193 |                25 |             221 |                            8.3 |
|  7 | Armenia           |              21 |               179 |              11 |                            3.8 |
|  8 | Australia         |             261 |                72 |             212 |                           10.4 |
|  9 | Austria           |             279 |                75 |             191 |                            9.7 |

The operation is describe data

The truncated output is: 

|    | summary   | country     |   beer_servings |   spirit_servings |   wine_servings |   total_litres_of_pure_alcohol |
|---:|:----------|:------------|----------------:|------------------:|----------------:|-------------------------------:|
|  0 | count     | 193         |         193     |          193      |        193      |                       193      |
|  1 | mean      |             |         106.161 |           80.9948 |         49.4508 |                         4.7171 |
|  2 | stddev    |             |         101.143 |           88.2843 |         79.6976 |                         3.7733 |
|  3 | min       | Afghanistan |           0     |            0      |          0      |                         0      |
|  4 | max       | Zimbabwe    |         376     |          438      |        370      |                        14.4    |

The operation is load data

The truncated output is: 

|    | country           |   beer_servings |   spirit_servings |   wine_servings |   total_litres_of_pure_alcohol |
|---:|:------------------|----------------:|------------------:|----------------:|-------------------------------:|
|  0 | Afghanistan       |               0 |                 0 |               0 |                            0   |
|  1 | Albania           |              89 |               132 |              54 |                            4.9 |
|  2 | Algeria           |              25 |                 0 |              14 |                            0.7 |
|  3 | Andorra           |             245 |               138 |             312 |                           12.4 |
|  4 | Angola            |             217 |                57 |              45 |                            5.9 |
|  5 | Antigua & Barbuda |             102 |               128 |              45 |                            4.9 |
|  6 | Argentina         |             193 |                25 |             221 |                            8.3 |
|  7 | Armenia           |              21 |               179 |              11 |                            3.8 |
|  8 | Australia         |             261 |                72 |             212 |                           10.4 |
|  9 | Austria           |             279 |                75 |             191 |                            9.7 |

The operation is query data

The query is SELECT * FROM DrinkData WHERE country = 'Angola'

The truncated output is: 

|    | country   |   beer_servings |   spirit_servings |   wine_servings |   total_litres_of_pure_alcohol |
|---:|:----------|----------------:|------------------:|----------------:|-------------------------------:|
|  0 | Angola    |             217 |                57 |              45 |                            5.9 |

The operation is load data

The truncated output is: 

|    | country           |   beer_servings |   spirit_servings |   wine_servings |   total_litres_of_pure_alcohol |
|---:|:------------------|----------------:|------------------:|----------------:|-------------------------------:|
|  0 | Afghanistan       |               0 |                 0 |               0 |                            0   |
|  1 | Albania           |              89 |               132 |              54 |                            4.9 |
|  2 | Algeria           |              25 |                 0 |              14 |                            0.7 |
|  3 | Andorra           |             245 |               138 |             312 |                           12.4 |
|  4 | Angola            |             217 |                57 |              45 |                            5.9 |
|  5 | Antigua & Barbuda |             102 |               128 |              45 |                            4.9 |
|  6 | Argentina         |             193 |                25 |             221 |                            8.3 |
|  7 | Armenia           |              21 |               179 |              11 |                            3.8 |
|  8 | Australia         |             261 |                72 |             212 |                           10.4 |
|  9 | Austria           |             279 |                75 |             191 |                            9.7 |

The operation is transform data

The truncated output is: 

|    | country           |   beer_servings |   spirit_servings |   wine_servings |   total_litres_of_pure_alcohol |   total_alcohol_servings |   average_servings |
|---:|:------------------|----------------:|------------------:|----------------:|-------------------------------:|-------------------------:|-------------------:|
|  0 | Afghanistan       |               0 |                 0 |               0 |                            0   |                        0 |               0    |
|  1 | Albania           |              89 |               132 |              54 |                            4.9 |                      275 |              91.67 |
|  2 | Algeria           |              25 |                 0 |              14 |                            0.7 |                       39 |              13    |
|  3 | Andorra           |             245 |               138 |             312 |                           12.4 |                      695 |             231.67 |
|  4 | Angola            |             217 |                57 |              45 |                            5.9 |                      319 |             106.33 |
|  5 | Antigua & Barbuda |             102 |               128 |              45 |                            4.9 |                      275 |              91.67 |
|  6 | Argentina         |             193 |                25 |             221 |                            8.3 |                      439 |             146.33 |
|  7 | Armenia           |              21 |               179 |              11 |                            3.8 |                      211 |              70.33 |
|  8 | Australia         |             261 |                72 |             212 |                           10.4 |                      545 |             181.67 |
|  9 | Austria           |             279 |                75 |             191 |                            9.7 |                      545 |             181.67 |


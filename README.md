dydra-py
================

<!-- WARNING: THIS FILE WAS AUTOGENERATED! DO NOT EDIT! -->

Tools for working with Dydra.com’s SPARQL endpoint.

## Install

``` sh
pip install git+https://github.com/nakamura196/dydra-py
```

## How to use

[See the documentation](https://nakamura196.github.io/dydra-py/api.html)
for full details of the Dydra Client.

``` txt:.env
DYDRA_ENDPOINT=https://dydra.com/ut-digital-archives/db/sparql
DYDRA_API_KEY=xxxxxx
```

``` python
from dydra_py.api import DydraClient
endpoint, api_key = DydraClient.load_env("../.env")
client = DydraClient(endpoint, api_key)
endpoint
```

    'https://dydra.com/ut-digital-archives/db/sparql'

### Without graph uri

import data from a file

``` python
client.import_by_file("./data.rdf", "xml")
```

    Triple count:  5

    100%|██████████| 5/5 [00:00<00:00, 39053.11it/s]

    Number of chunks:  1

    100%|██████████| 1/1 [00:00<00:00,  1.20it/s]

    Data successfully inserted.

delete data from a file

``` python
client.delete_by_file("./data_delete.rdf", "xml")
```

    Triple count:  1

    100%|██████████| 1/1 [00:00<00:00, 13706.88it/s]

    Number of chunks:  1

      0%|          | 0/1 [00:00<?, ?it/s]

delete data by subjects

``` python
client.delete_by_subjects(["http://example.org/BOB"], verbose=True)
```

    1it [00:00,  1.09it/s]

    Data for URIs successfully deleted.

search by SPARQL query

``` python
query = """
    SELECT ?s ?v ?o
    WHERE { 
      { ?s ?v ?o }
    }
"""

df = client.query(query)
df
```

    {'head': {'vars': ['s', 'v', 'o']},
     'results': {'bindings': [{'s': {'type': 'uri',
         'value': 'http://example.org/Alice'},
        'v': {'type': 'uri', 'value': 'http://example.org/type'},
        'o': {'type': 'uri', 'value': 'http://xmlns.com/foaf/0.1/Person'}},
       {'s': {'type': 'uri', 'value': 'http://example.org/Alice'},
        'v': {'type': 'uri', 'value': 'http://example.org/knows'},
        'o': {'type': 'uri', 'value': 'http://example.org/BOB'}}]}}

clear the graph

``` python
client.clear()
```

    Data successfully cleared.

### With graph uri

``` python
graph_uri = "http://example.org/graph"
```

import data from a file

``` python
client.import_by_file("./data.rdf", "xml", graph_uri=graph_uri)
```

    Triple count:  5

    100%|██████████| 5/5 [00:00<00:00, 44715.39it/s]

    Number of chunks:  1

    100%|██████████| 1/1 [00:00<00:00,  1.25it/s]

    Data successfully inserted.

search by SPARQL query

``` python
query = """
    SELECT ?g ?s ?v ?o
    WHERE { 
      graph ?g { ?s ?v ?o }
    }
"""

df = client.query(query)
df
```

    {'head': {'vars': ['g', 's', 'v', 'o']},
     'results': {'bindings': [{'g': {'type': 'uri',
         'value': 'http://example.org/graph'},
        's': {'type': 'uri', 'value': 'http://example.org/Alice'},
        'v': {'type': 'uri', 'value': 'http://example.org/type'},
        'o': {'type': 'uri', 'value': 'http://xmlns.com/foaf/0.1/Person'}},
       {'g': {'type': 'uri', 'value': 'http://example.org/graph'},
        's': {'type': 'uri', 'value': 'http://example.org/Alice'},
        'v': {'type': 'uri', 'value': 'http://example.org/knows'},
        'o': {'type': 'uri', 'value': 'http://example.org/BOB'}},
       {'g': {'type': 'uri', 'value': 'http://example.org/graph'},
        's': {'type': 'uri', 'value': 'http://example.org/BOB'},
        'v': {'type': 'uri', 'value': 'http://xmlns.com/foaf/0.1/topic_interest'},
        'o': {'type': 'uri',
         'value': 'https://jpsearch.go.jp/entity/chname/葛飾北斎'}},
       {'g': {'type': 'uri', 'value': 'http://example.org/graph'},
        's': {'type': 'uri', 'value': 'http://example.org/BOB'},
        'v': {'type': 'uri', 'value': 'http://example.org/type'},
        'o': {'type': 'uri', 'value': 'http://xmlns.com/foaf/0.1/Person'}},
       {'g': {'type': 'uri', 'value': 'http://example.org/graph'},
        's': {'type': 'uri', 'value': 'http://example.org/BOB'},
        'v': {'type': 'uri', 'value': 'http://example.org/knows'},
        'o': {'type': 'uri', 'value': 'http://example.org/Alice'}}]}}

clear the graph

``` python
client.clear(graph_uri=graph_uri)
```

    Data successfully cleared.

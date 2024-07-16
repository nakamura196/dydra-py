# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/00_core.ipynb.

# %% auto 0
__all__ = ['DydraClient']

# %% ../nbs/00_core.ipynb 3
import requests
import rdflib
from dotenv import load_dotenv
import os
from SPARQLWrapper import SPARQLWrapper, JSON

# %% ../nbs/00_core.ipynb 4
class DydraClient():

    @staticmethod
    def load_env(path):

        load_dotenv(path)

        return os.getenv("DYDRA_ENDPOINT"), os.getenv("DYDRA_API_KEY")


    def __init__(self, endpoint, api_key):

        self.endpoint = endpoint
        self.api_key = api_key

    def import_by_file(self, file_path, format, graph_uri=None):

        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/sparql-update"
        }

        # RDFファイルの読み込み
        graph = rdflib.Graph()
        graph.parse(file_path, format=format)  # フォーマットはファイルに応じて変更

        nt_data = graph.serialize(format='nt')

        if graph_uri is None:
            query = f"""
            INSERT DATA {{
            {nt_data}
            }}
            """

        else:
            query = f"""
            INSERT DATA {{
            GRAPH <{graph_uri}> {{
                {nt_data}
            }}
            }}
            """

        

        response = requests.post(self.endpoint, data=query, headers=headers)
        if response.status_code == 200:
            print("データが正常に登録されました")
        else:
            print("エラー:", response.status_code, response.text)

    def query(self, query):

        # SPARQLエンドポイントの設定
        sparql = SPARQLWrapper(self.endpoint)

        # クエリの設定
        sparql.setQuery(query)

        # 返される結果のフォーマットをJSONに設定
        sparql.setReturnFormat(JSON)

        # クエリを実行し、結果を取得
        results = sparql.query().convert()

        return results
    
    def clear(self, graph_uri=None):

        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/sparql-update"
        }

        if graph_uri is None:
            query = """
            DELETE {
            ?s ?p ?o
            }
            WHERE {
            ?s ?p ?o
            }
            """

        else:
            query = f"""
            DELETE {{
            GRAPH <{graph_uri}> {{
                ?s ?p ?o
            }}
            }}
            WHERE {{
            GRAPH <{graph_uri}> {{
                ?s ?p ?o
            }}
            }}
            """

        response = requests.post(self.endpoint, data=query, headers=headers)

        if response.status_code == 200:
            print("データが正常に削除されました")
        else:
            print("エラー:", response.status_code, response.text)

"""
Extract a dataset from a URL like Kaggle or data.gov.
JSON or CSV formats tend to work well

Jeopardy dataset
"""
import requests


def extract(
    url="https://pkgstore.datahub.io/core/glacier-mass-balance/glaciers_csv/data/c04ec0dab848ef8f9b179a2cca11b616/glaciers_csv.csv",
    file_path="data/glaciers.csv",
):
    """ "Extract a url to a file path"""
    with requests.get(url) as r:
        with open(file_path, "wb") as f:
            f.write(r.content)
    return file_path

extract()

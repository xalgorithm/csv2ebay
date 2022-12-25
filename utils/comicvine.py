from simyan.comicvine import Comicvine
from simyan.sqlite_cache import SQLiteCache
from utils.config import read_config
cfg = read_config()
cvineapi = cfg['cv_api_key']

session = Comicvine(api_key=cvineapi, cache=SQLiteCache())

# Search for Publisher
results = session.publisher_list(params={"filter": "name:DC Comics"})
for publisher in results:
    print(f"{publisher.publisher_id} | {publisher.name} - {publisher.site_url}")

# Get details for a Volume
result = session.volume(volume_id=26266)
print(result.summary)
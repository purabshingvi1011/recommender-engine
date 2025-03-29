import pandas as pd
import time
import redis
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

def info(msg, app=None):
    if app:
        app.logger.info(msg)
    else:
        print(msg)

class ContentEngine(object):
    SIMKEY = 'p:smlr:%s'

    def __init__(self, app):
        self.app = app
        self._r = redis.StrictRedis.from_url(self.app.config['REDIS_URL'])

    def train(self, data_source):
        start = time.time()
        ds = pd.read_csv(data_source)
        info("Training data ingested in %s seconds." % (time.time() - start), self.app)
        self._r.flushdb()
        start = time.time()
        self._train(ds)
        info("Engine trained in %s seconds." % (time.time() - start), self.app)

    def _train(self, ds):
        tf = TfidfVectorizer(analyzer='word',
                             ngram_range=(1, 3),
                             min_df=1,  # fixed here
                             stop_words='english')
        tfidf_matrix = tf.fit_transform(ds['description'])
        cosine_similarities = linear_kernel(tfidf_matrix, tfidf_matrix)

        for idx, row in ds.iterrows():
            similar_indices = cosine_similarities[idx].argsort()[:-100:-1]

            # Build a dictionary for Redis with {item_id: similarity_score}
            similar_items_dict = {
                str(ds['id'][i]): float(cosine_similarities[idx][i])
                for i in similar_indices[1:]  # skip self
            }

            self._r.zadd(self.SIMKEY % row['id'], mapping=similar_items_dict)

    def predict(self, item_id, num):
        return self._r.zrange(self.SIMKEY % item_id,
                              0,
                              num-1,
                              withscores=True,
                              desc=True)

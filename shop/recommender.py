import redis
from django.conf import settings
from .models import Product

r = redis.StrictRedis(host=settings.REDIS_HOST,
                      port=settings.REDIS_PORT,
                      db=settings.REDIS_DB)

class Recommender(object):
    # 检索商品对象的id
    def get_product_key(self,id):
        return 'product:{}:purchased_with'.format(id)

    #
    def products_bought(self,products):
        # 得到所有product对象的产品ID
        product_ids = [p.id for p in products]
        # 迭代所有产品id
        for product_id in product_ids:
            # 迭代所有产品id
            for with_id in product_ids:
                # 跳过所有相同的商品,得到每个产品一起购买的产品
                if product_id != with_id:
                    r.zincrby(self.get_product_key(
                            product_id),
                            with_id,
                            amount=1)

    # 建议购买的商品
    def suggest_products_for(self,products,max_results=6):
        product_ids = [p.id for p in products]
        if len(products) == 1:
            suggertions = r.zrange(
                            self.get_product_key(product_ids[0]),
                            0,-1,desc=True)[:max_results]
        else:
            flat_ids = ''.join([str(id) for id in product_ids])
            tmp_key = 'tmp_{}'.format(flat_ids)
            keys = [self.get_product_key(id) for id in product_ids]
            r.zunionstore(tmp_key,keys)
            r.zrem(tmp_key,*product_ids)
            suggertions = r.zrange(tmp_key,0,-1,desc=True)[:max_results]
        suggested_products_ids = [int(id) for id in suggertions]
        suggested_products = list(Product.objects.filter(id__in=suggested_products_ids))
        suggested_products.sort(key=lambda x:suggested_products_ids.index(x.id))
        return suggested_products

    # 清除推荐
    def clear_purchases(self):
        for id in Product.objects.values_list('id',flat=True):
            r.delete(self.get_product_key(id))

from django_mongoengine import Document, EmbeddedDocument, fields, DynamicDocument


class Tmall(DynamicDocument):
    title = fields.StringField()
    store_id = fields.StringField()
    url = fields.URLField()
    price = fields.FloatField()
    sale_num = fields.IntField()
    image_urls = fields.ListField()
    scrapy_mongodb = fields.DictField(db_field='scrapy-mongodb')

    def __str__(self):
        return self.title

    @property
    def cover(self):
        return self.image_urls[0]

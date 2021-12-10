# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface

from sqlalchemy.orm import session, sessionmaker

from animelist.models import Items, creat_items_table, db_connect


class AnimelistPipeline:
    def __init__(self) -> None:
        engine = db_connect()
        creat_items_table(engine)
        self.session = sessionmaker(bind=engine)


    def process_item(self, item, spider):
        
        session = self.Session()
        instance = session.query(Items).filter_by(**item).one_or_none()
        if instance:
            return instance
        anime_item = Items(**item)

        try:
            session.add(anime_item)
            session.commit()
        except:
            session.rollback()
            raise
        finally:
            session.close()

        return item
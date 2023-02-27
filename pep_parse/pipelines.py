import csv
import datetime as dt
from collections import defaultdict

from pep_parse.settings import BASE_DIR, DATETIME_FORMAT


class PepParsePipeline:
    def open_spider(self, spider):
        self.count_status = defaultdict(int)


    def process_item(self, item, spider):
        if 'status' in item:
            self.count_status[item['status']] += 1
        return item

    def close_spider(self, spider):
        results_dir = BASE_DIR / 'results'
        now = dt.datetime.now()
        now_formatted = now.strftime(DATETIME_FORMAT)
        file_name = f'status_summary_{now_formatted}.csv'

        with open(results_dir / file_name, mode='w', encoding='utf-8') as f:
            csv.writer(
                f, dialect=csv.unix_dialect, quoting=csv.QUOTE_NONE
            ).writerows([
                ['Статус', 'Количество'],
                *sorted(self.count_status.items()),
                ['Total', sum(self.count_status.values())]
            ])



"""BakeryTableSeeder Seeder."""

from masoniteorm.seeds import Seeder
from app.Bakery import Bakery

class BakeryTableSeeder(Seeder):
    def run(self):
        Bakery.create({"name": "Perospero Cake", "details": "Lollipop gum flavored cake"})
        Bakery.create({"name": "Zeus Cake", "details": "Creamy puffy vanilla flavored cake"})
        Bakery.create({"name": "Prometheus", "details": "Bright Yellow orange flavored cake with strawberry filling"})

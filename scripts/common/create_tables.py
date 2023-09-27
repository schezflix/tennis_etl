from base import Base, engine
# from tables import Player, Match, Tournament, Country, Surface, Currency, Round
from tables_staging import Player, Match, Tournament, Country, Surface, Currency, Round

if __name__ == "__main__":
    Base.metadata.create_all(engine)


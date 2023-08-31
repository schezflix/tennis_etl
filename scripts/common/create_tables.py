from base import Base, engine
from tables import Player, Match, Tournament, Country


if __name__ == "__main__":
    Base.metadata.create_all(engine)
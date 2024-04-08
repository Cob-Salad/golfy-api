import uuid

from fastapi import FastAPI

from models.course import Course
from models.player import Player, PlayerResponse


app = FastAPI()


players: dict[uuid.UUID, Player] = {}
courses: dict[uuid.UUID, Course] = {}



@app.get("/players")
async def get_players() -> list[Player]:
    return players.values()

@app.post("/players")
async def create_player(player: Player) -> PlayerResponse:
    player_id = uuid.uuid4()
    player = Player(name=player.name, handicap=player.handicap)
    players[player.id] = player
    return PlayerResponse(id=player_id)

@app.put("/players/{player_id}")
async def update_player(player_id: uuid.UUID, updated_player: Player) -> PlayerResponse:
    players[player_id] = updated_player
    return PlayerResponse(id=player_id)


@app.delete("/players/{playuer_id}")
async def delete_player(player_id: uuid.UUID) -> None:
    players.pop(player_id)

#
#@app.get("/courses")
#async def get_courses() -> list[Course]:
#    pass
#
#@app.post("/courses")
#
#@app.put("/courses/{course_id}")
#
#@app.delete("/courses/{course_id}")
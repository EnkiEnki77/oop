import pytest

hero_params = {
    "name": "superman",
    "power": ["super strength", "laser vision"],
    "health": 1_000_000,
    "speed": 1_000_000
}
@pytest.mark.parametrize("create_hero, name, power, health, speed", [(hero_params, "superman", ["super strength", "laser vision"], 1_000_000, 1_000_000)], indirect=["create_hero"])
def test_hero_attributes(create_hero, name, power, health, speed):
    # print(f"This bitch {dir(create_hero)}")
    assert create_hero.power == power
    assert create_hero.name == name
    assert create_hero.speed == speed
    assert create_hero.health == health
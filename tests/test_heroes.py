import pytest
import sys
from heroes import Hero

hero_params = {
    "name": "Superman",
    "power": ["super strength", "laser vision"],
    "health": 1_000_000,
    "speed": 1_000_000
}

class TestHero:

    def setup_method(self, method):
        """Instantiates new object for each test in the class"""

        print(f"Setting up {method}")
        self.hero = Hero(hero_params['name'], hero_params['power'], hero_params['health'], hero_params['speed'])


    def teardown_method(self, method):
        """Tears down instantiated object when test is finished"""

        print(f"Tearing down {method}")
        del self.hero


    @pytest.mark.parametrize("power, expected", [("super strength", "Superman used the super strength power"), ("laser vision", "Superman used the laser vision power")])
    def test_use_power(self, capfd, power, expected):
        """Tests that use_power method prints proper statement when a power the hero has is passed as argument"""
        self.hero.use_power(power)
        out, err = capfd.readouterr()
        out = out.replace("\n", "")
        assert out == expected

    @pytest.mark.parametrize("power, expected", [("super flexibility", "Superman doesn't have the super flexibility power")])
    def test_use_power_with_unobtained_power(self, capfd, power, expected):
        """Tests that use_power method prints proper statement when a power the hero doesn't have is passed as argument"""
        self.hero.use_power(power)
        out, err = capfd.readouterr()
        out = out.replace("\n", "")
        assert out == expected

    @pytest.mark.parametrize("power, expected", [("laser vision", "Superman is dead, he can't use powers")])
    def test_use_power_with_zero_health(self, capfd, power, expected):
        """Tests that use_power method prints proper statement when a hero has zero health"""
        self.hero.take_damage(2_000_000)
        self.hero.use_power(power)
        out, err = capfd.readouterr()
        out = out.replace("\n", "")
        out = out.replace("Superman is now dead!", "")
        assert out == expected











# @pytest.mark.parametrize("create_hero, name, power, health, speed", [(hero_params, "superman", ["super strength", "laser vision"], 1_000_000, 1_000_000)], indirect=["create_hero"])
# def test_hero_attributes(create_hero, name, power, health, speed):
#     """Tests that fixture can be parametrized with multiple arguments"""
#     # print(f"This bitch {dir(create_hero)}")
#     assert create_hero.power == power
#     assert create_hero.name == name
#     assert create_hero.speed == speed
#     assert create_hero.health == health
#
#
# @pytest.mark.parametrize("create_hero, power", [(hero_params, "super strength"), (hero_params, "laser vision")], indirect=["create_hero"])
# def test_use_power(create_hero, power):
#     """Tests that use_power method prints proper statement when a power the hero has is passed as argument"""

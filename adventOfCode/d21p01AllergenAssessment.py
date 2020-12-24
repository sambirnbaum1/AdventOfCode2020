import re
from functools import reduce
from operator import or_
from dataclasses import dataclass
from typing import Tuple, FrozenSet, Iterable, Mapping

from adventOfCode.aocUtils import solver

RECIPE_PATTERN = re.compile(r'([\w ]+) \(contains ([\w, ]+)\)')
FILENAME = 'inputs/allergen_assessment.txt'

@dataclass
class Recipe:
    ingredients: FrozenSet[str]
    allergens: FrozenSet[str]


def parse_recipe(recipe_str: str) -> Recipe:
    ingredients, allergens = RECIPE_PATTERN.fullmatch(recipe_str).groups()
    return Recipe(frozenset(ingredients.split(' ')), frozenset(allergens.split(', ')))


def get_allergen_map(recipes: Iterable[Recipe]) -> Mapping[str, FrozenSet[str]]:
    allergen_map = dict()
    for recipe in recipes:
        for allergen in recipe.allergens:
            allergen_map[allergen] = allergen_map.get(allergen, recipe.ingredients) & recipe.ingredients
    return allergen_map


@solver(FILENAME, parse_recipe, tuple)
def solve(recipes: Tuple[Recipe]) -> int:
    allergen_map = get_allergen_map(recipes)
    allergen_ingredients = frozenset(reduce(or_, allergen_map.values()))
    return sum(len(recipe.ingredients - allergen_ingredients) for recipe in recipes)

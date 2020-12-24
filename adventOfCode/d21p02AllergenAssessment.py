from typing import Tuple, FrozenSet, Mapping
from .aocUtils import solver
from .d21p01AllergenAssessment import FILENAME, Recipe, parse_recipe, get_allergen_map


@solver(FILENAME, parse_recipe, tuple)
def solve(recipes: Tuple[Recipe]) -> str:
    allergen_map = get_allergen_map(recipes)
    matching = match_allergens(allergen_map)
    return ','.join(sorted(matching.keys(), key=matching.__getitem__))


def match_allergens(allergen_map: Mapping[str, FrozenSet[str]]) -> Mapping[str, str]:

    def recurse(match: Mapping[str, str], allergen_traversal: Tuple[str, ...]):
        if not allergen_traversal:
            return match
        allergen = allergen_traversal[0]
        ingredients = allergen_map[allergen] - frozenset(match.keys())
        for ingredient in ingredients:
            full_match = recurse({**match, **{ingredient: allergen}}, allergen_traversal[1:])
            if full_match:
                return full_match
        return None

    return recurse(dict(), tuple(sorted(allergen_map.keys(), key=lambda a: len(allergen_map[a]))))

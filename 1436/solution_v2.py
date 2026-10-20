class Solution:
    def destCity(self, paths: list[list[str]]) -> str:
        next_city = {}

        for source, destination in paths:
            next_city[source] = destination

        city = paths[0][0]

        while city in next_city:
            city = next_city[city]

        return city
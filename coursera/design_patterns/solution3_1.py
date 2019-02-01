class MappingAdapter:
    def __init__(self, adapter):
        self.adapter = adapter

    def _get_objects_by_grid(self, descriptor, grid):
        result = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == descriptor:
                    result.append((j, i))
        return result

    def lighten(self, grid):
        dim = (len(grid[0]), len(grid))
        self.adapter.set_dim(dim)
        lights = self._get_objects_by_grid(1, grid)
        obstacles = self._get_objects_by_grid(-1, grid)
        self.adapter.set_lights(lights)
        self.adapter.set_obstacles(obstacles)
        return self.adapter.generate_lights()
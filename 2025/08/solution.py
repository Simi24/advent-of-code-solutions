from collections import defaultdict
from heapq import merge
import math
junction_boxes: list[tuple[int, int, int]] = []

def parseInput(file_name: str = "input"):
    with open(file_name + ".txt") as file:
        lines = file.readlines()
        for line in lines:
            junction_boxes.append(tuple(int(x) for x in line.strip().split(",")))

def get_linear_distance(jb1: tuple[int, int, int], jb2: tuple[int, int, int]) -> int:
   return math.sqrt(math.pow((jb1[0] - jb2[0]), 2) + math.pow((jb1[1] - jb2[1]), 2) + math.pow((jb1[2] - jb2[2]), 2))

def get_all_distances(junction_boxes: list[tuple[int, int, int]]) -> dict[tuple[int, int], int]:
    distances = defaultdict(int)
    for x in range(len(junction_boxes) - 1):
        for j in range(x+1, len(junction_boxes)):
            distance = get_linear_distance(junction_boxes[x], junction_boxes[j])
            distances[(x, j)] = distance 
    distances = {k: v for k, v in sorted(distances.items(), key=lambda item: item[1])}
    return distances
            
def solve_part1(junction_boxes: list[tuple[int, int, int]]):
    sorted_distances = get_all_distances(junction_boxes)
    print(sorted_distances)
    merged_boxes = []
    for i in range(1000):
        box1_idx, box2_idx = list(sorted_distances.keys())[i]
        box1 = junction_boxes[box1_idx]
        box2 = junction_boxes[box2_idx]
        print(f"Box 1: {box1}, Box 2: {box2}, Distance: {sorted_distances[(box1_idx, box2_idx)]}")
        #TODO: we must merge boxes if after merging they are now connected to other boxes
        merged = False
        for box in merged_boxes:
            if box1 in box or box2 in box:
                print(f"Merging boxes in box :{box}")
                box.add(box1)
                box.add(box2)
                print(merged_boxes)
                print("-----")
                merged = True
                break
        else:
            print("Creating new merged box")
            merged_boxes.append({box1, box2})
            print(merged_boxes)
            print("-----")
        while True:
            did_merge = False
            for i in range(len(merged_boxes)):
                for j in range(i + 1, len(merged_boxes)):
                    if merged_boxes[i].intersection(merged_boxes[j]):
                        print(f"Merging boxes: {merged_boxes[i]} and {merged_boxes[j]}")
                        merged_boxes[i].update(merged_boxes[j])
                        del merged_boxes[j]
                        did_merge = True
                        break
                if did_merge:
                    break
            if not did_merge:
                break 
    merged_boxes.sort(key=lambda x: len(x), reverse=True)
    print(merged_boxes)
    ret = 1
    for box in merged_boxes[:3]:
        ret *= len(box)
    print(ret)

class UnionFind:
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.num_components = n

    def find(self, i: int) -> int:
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i: int, j: int) -> bool:
        root_i = self.find(i)
        root_j = self.find(j)
        if root_i != root_j:
            self.parent[root_i] = root_j
            self.num_components -= 1
            return True
        return False

def solve_part2(junction_boxes: list[tuple[int, int, int]]):
    sorted_distances = get_all_distances(junction_boxes)
    uf = UnionFind(len(junction_boxes))
    
    for (idx1, idx2), dist in sorted_distances.items():
        if uf.union(idx1, idx2):
            if uf.num_components == 1:
                box1 = junction_boxes[idx1]
                box2 = junction_boxes[idx2]
                print(f"Last connection: {box1} and {box2} with distance {dist}")
                result = box1[0] * box2[0]
                print(f"Result Part 2: {result}")
                return result

if __name__ == "__main__":
    parseInput("input")
    solve_part1(junction_boxes)
    solve_part2(junction_boxes)
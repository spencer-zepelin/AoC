ENERGY = {"a": 1, "b": 10, "c": 100, "d": 1000}
HALLS = ["l2", "l1", "ml", "mm", "mr", "r1", "r2"]
BASES1 = ["a1", "a2", "b1", "b2", "c1", "c2", "d1", "d2"]
BASES2 = [
    "a1",
    "a2",
    "a3",
    "a4",
    "b1",
    "b2",
    "b3",
    "b4",
    "c1",
    "c2",
    "c3",
    "c4",
    "d1",
    "d2",
    "d3",
    "d4",
]

POSITIONS1 = HALLS + BASES1
POSITIONS2 = HALLS + BASES2

DIST_MAP = {
    "l2-a4": (6, ["l2", "l1", "a1", "a2", "a3", "a4"]),
    "l2-a3": (5, ["l2", "l1", "a1", "a2", "a3"]),
    "l2-a2": (4, ["l2", "l1", "a1", "a2"]),
    "l2-a1": (3, ["l2", "l1", "a1"]),
    "l2-b4": (8, ["l2", "l1", "ml", "b1", "b2", "b3", "b4"]),
    "l2-b3": (7, ["l2", "l1", "ml", "b1", "b2", "b3"]),
    "l2-b2": (6, ["l2", "l1", "ml", "b1", "b2"]),
    "l2-b1": (5, ["l2", "l1", "ml", "b1"]),
    "l2-c4": (10, ["l2", "l1", "ml", "mm", "c1", "c2", "c3", "c4"]),
    "l2-c3": (9, ["l2", "l1", "ml", "mm", "c1", "c2", "c3"]),
    "l2-c2": (8, ["l2", "l1", "ml", "mm", "c1", "c2"]),
    "l2-c1": (7, ["l2", "l1", "ml", "mm", "c1"]),
    "l2-d4": (12, ["l2", "l1", "ml", "mm", "mr", "d1", "d2", "d3", "d4"]),
    "l2-d3": (11, ["l2", "l1", "ml", "mm", "mr", "d1", "d2", "d3"]),
    "l2-d2": (10, ["l2", "l1", "ml", "mm", "mr", "d1", "d2"]),
    "l2-d1": (9, ["l2", "l1", "ml", "mm", "mr", "d1"]),
    "l1-a4": (5, ["l1", "a1", "a2", "a3", "a4"]),
    "l1-a3": (4, ["l1", "a1", "a2", "a3"]),
    "l1-a2": (3, ["l1", "a1", "a2"]),
    "l1-a1": (2, ["l1", "a1"]),
    "l1-b4": (7, ["l1", "ml", "b1", "b2", "b3", "b4"]),
    "l1-b3": (6, ["l1", "ml", "b1", "b2", "b3"]),
    "l1-b2": (5, ["l1", "ml", "b1", "b2"]),
    "l1-b1": (4, ["l1", "ml", "b1"]),
    "l1-c4": (9, ["l1", "ml", "mm", "c1", "c2", "c3", "c4"]),
    "l1-c3": (8, ["l1", "ml", "mm", "c1", "c2", "c3"]),
    "l1-c2": (7, ["l1", "ml", "mm", "c1", "c2"]),
    "l1-c1": (6, ["l1", "ml", "mm", "c1"]),
    "l1-d4": (11, ["l1", "ml", "mm", "mr", "d1", "d2", "d3", "d4"]),
    "l1-d3": (10, ["l1", "ml", "mm", "mr", "d1", "d2", "d3"]),
    "l1-d2": (9, ["l1", "ml", "mm", "mr", "d1", "d2"]),
    "l1-d1": (8, ["l1", "ml", "mm", "mr", "d1"]),
    "ml-a4": (5, ["ml", "a1", "a2", "a3", "a4"]),
    "ml-a3": (4, ["ml", "a1", "a2", "a3"]),
    "ml-a2": (3, ["ml", "a1", "a2"]),
    "ml-a1": (2, ["ml", "a1"]),
    "ml-b4": (5, ["ml", "b1", "b2", "b3", "b4"]),
    "ml-b3": (4, ["ml", "b1", "b2", "b3"]),
    "ml-b2": (3, ["ml", "b1", "b2"]),
    "ml-b1": (2, ["ml", "b1"]),
    "ml-c4": (7, ["ml", "mm", "c1", "c2", "c3", "c4"]),
    "ml-c3": (6, ["ml", "mm", "c1", "c2", "c3"]),
    "ml-c2": (5, ["ml", "mm", "c1", "c2"]),
    "ml-c1": (4, ["ml", "mm", "c1"]),
    "ml-d4": (9, ["ml", "mm", "mr", "d1", "d2", "d3", "d4"]),
    "ml-d3": (8, ["ml", "mm", "mr", "d1", "d2", "d3"]),
    "ml-d2": (7, ["ml", "mm", "mr", "d1", "d2"]),
    "ml-d1": (6, ["ml", "mm", "mr", "d1"]),
    "mm-a4": (7, ["mm", "ml", "a1", "a2", "a3", "a4"]),
    "mm-a3": (6, ["mm", "ml", "a1", "a2", "a3"]),
    "mm-a2": (5, ["mm", "ml", "a1", "a2"]),
    "mm-a1": (4, ["mm", "ml", "a1"]),
    "mm-b4": (5, ["mm", "b1", "b2", "b3", "b4"]),
    "mm-b3": (4, ["mm", "b1", "b2", "b3"]),
    "mm-b2": (3, ["mm", "b1", "b2"]),
    "mm-b1": (2, ["mm", "b1"]),
    "mm-c4": (5, ["mm", "c1", "c2", "c3", "c4"]),
    "mm-c3": (4, ["mm", "c1", "c2", "c3"]),
    "mm-c2": (3, ["mm", "c1", "c2"]),
    "mm-c1": (2, ["mm", "c1"]),
    "mm-d4": (7, ["mm", "mr", "d1", "d2", "d3", "d4"]),
    "mm-d3": (6, ["mm", "mr", "d1", "d2", "d3"]),
    "mm-d2": (5, ["mm", "mr", "d1", "d2"]),
    "mm-d1": (4, ["mm", "mr", "d1"]),
    "mr-a4": (9, ["mr", "mm", "ml", "a1", "a2", "a3", "a4"]),
    "mr-a3": (8, ["mr", "mm", "ml", "a1", "a2", "a3"]),
    "mr-a2": (7, ["mr", "mm", "ml", "a1", "a2"]),
    "mr-a1": (6, ["mr", "mm", "ml", "a1"]),
    "mr-b4": (7, ["mr", "mm", "b1", "b2", "b3", "b4"]),
    "mr-b3": (6, ["mr", "mm", "b1", "b2", "b3"]),
    "mr-b2": (5, ["mr", "mm", "b1", "b2"]),
    "mr-b1": (4, ["mr", "mm", "b1"]),
    "mr-c4": (5, ["mr", "c1", "c2", "c3", "c4"]),
    "mr-c3": (4, ["mr", "c1", "c2", "c3"]),
    "mr-c2": (3, ["mr", "c1", "c2"]),
    "mr-c1": (2, ["mr", "c1"]),
    "mr-d4": (5, ["mr", "d1", "d2", "d3", "d4"]),
    "mr-d3": (4, ["mr", "d1", "d2", "d3"]),
    "mr-d2": (3, ["mr", "d1", "d2"]),
    "mr-d1": (2, ["mr", "d1"]),
    "r1-a4": (11, ["r1", "mr", "mm", "ml", "a1", "a2", "a3", "a4"]),
    "r1-a3": (10, ["r1", "mr", "mm", "ml", "a1", "a2", "a3"]),
    "r1-a2": (9, ["r1", "mr", "mm", "ml", "a1", "a2"]),
    "r1-a1": (8, ["r1", "mr", "mm", "ml", "a1"]),
    "r1-b4": (9, ["r1", "mr", "mm", "b1", "b2", "b3", "b4"]),
    "r1-b3": (8, ["r1", "mr", "mm", "b1", "b2", "b3"]),
    "r1-b2": (7, ["r1", "mr", "mm", "b1", "b2"]),
    "r1-b1": (6, ["r1", "mr", "mm", "b1"]),
    "r1-c4": (7, ["r1", "mr", "c1", "c2", "c3", "c4"]),
    "r1-c3": (6, ["r1", "mr", "c1", "c2", "c3"]),
    "r1-c2": (5, ["r1", "mr", "c1", "c2"]),
    "r1-c1": (4, ["r1", "mr", "c1"]),
    "r1-d4": (5, ["r1", "d1", "d2", "d3", "d4"]),
    "r1-d3": (4, ["r1", "d1", "d2", "d3"]),
    "r1-d2": (3, ["r1", "d1", "d2"]),
    "r1-d1": (2, ["r1", "d1"]),
    "r2-a4": (12, ["r2", "r1", "mr", "mm", "ml", "a1", "a2", "a3", "a4"]),
    "r2-a3": (11, ["r2", "r1", "mr", "mm", "ml", "a1", "a2", "a3"]),
    "r2-a2": (10, ["r2", "r1", "mr", "mm", "ml", "a1", "a2"]),
    "r2-a1": (9, ["r2", "r1", "mr", "mm", "ml", "a1"]),
    "r2-b4": (10, ["r2", "r1", "mr", "mm", "b1", "b2", "b3", "b4"]),
    "r2-b3": (9, ["r2", "r1", "mr", "mm", "b1", "b2", "b3"]),
    "r2-b2": (8, ["r2", "r1", "mr", "mm", "b1", "b2"]),
    "r2-b1": (7, ["r2", "r1", "mr", "mm", "b1"]),
    "r2-c4": (8, ["r2", "r1", "mr", "c1", "c2", "c3", "c4"]),
    "r2-c3": (7, ["r2", "r1", "mr", "c1", "c2", "c3"]),
    "r2-c2": (6, ["r2", "r1", "mr", "c1", "c2"]),
    "r2-c1": (5, ["r2", "r1", "mr", "c1"]),
    "r2-d4": (6, ["r2", "r1", "d1", "d2", "d3", "d4"]),
    "r2-d3": (5, ["r2", "r1", "d1", "d2", "d3"]),
    "r2-d2": (4, ["r2", "r1", "d1", "d2"]),
    "r2-d1": (3, ["r2", "r1", "d1"]),
}
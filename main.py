class TreeStore:
    ROOT_NODE = "root"

    def __init__(self, items: dict):
        self._init_items = items
        self._items_wrapped = {
            item["id"]: {"item": item, "children": []} for item in items
        }

        self._load_children()

    def _load_children(self):
        for item_id, value in self._items_wrapped.items():
            parent_id = value["item"]["parent"]
            if parent_id != self.ROOT_NODE:
                self._items_wrapped[parent_id]["children"].append(item_id)

    def getAll(self) -> dict:
        return self._init_items

    def getItem(self, item_id: int) -> dict:
        return self._items_wrapped[item_id]["item"]

    def getChildren(self, item_id: int) -> list:
        return [
            self._items_wrapped[id_]["item"] for id_ in self._items_wrapped[item_id]["children"]
        ]

    def getAllParents(self, item_id: int) -> list:
        parents = []
        current_node_id = self._items_wrapped[item_id]["item"]["parent"]
        while current_node_id != self.ROOT_NODE:
            parents.append(self._items_wrapped[current_node_id]["item"])
            current_node_id = self._items_wrapped[current_node_id]["item"]["parent"]

        return parents


items = [
    {"id": 1, "parent": "root"},
    {"id": 2, "parent": 1, "type": "test"},
    {"id": 3, "parent": 1, "type": "test"},
    {"id": 4, "parent": 2, "type": "test"},
    {"id": 5, "parent": 2, "type": "test"},
    {"id": 6, "parent": 2, "type": "test"},
    {"id": 7, "parent": 4, "type": None},
    {"id": 8, "parent": 4, "type": None}
]

ts = TreeStore(items)

print(ts.getAll())
print(ts.getItem(7))
print(ts.getChildren(4))
print(ts.getChildren(5))
print(ts.getAllParents(7))

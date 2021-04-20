from itertools import islice


class PaginationHelper:

    # The constructor takes in an array of items and a integer indicating
    # how many items fit within a single page
    def __init__(self, collection, items_per_page):
        self.collection = collection
        self.items_per_page = items_per_page

    # returns the number of items within the entire collection
    def item_count(self):
        return len(self.collection)

    # returns the number of pages
    def page_count(self):
        # pages = zip_longest(*[iter(self.collection)] * self.items_per_page)
        # pages = list(pages)
        it = iter(self.collection)
        pages = iter(lambda: tuple(islice(it, self.items_per_page)), ())
        pages = list(pages)
        return len(pages)

    # returns th?!?jedi=0, e number of items on the current page. page_index?!? (*_*function: Callable[[], _T]*_*, sentinel: Any) ?!?jedi?!? is zero based
    # this metho?!?jedi=0, d should return -1 for page_index values that are out of ran?!? (*_*function: Callable[[], Optional[_T]]*_*, sentinel: None) ?!?jedi?!?ge
    def page_ite?!?jedi=0, m_count(self, page_index):?!? (*_*iterable: Iterable[_T]*_*) ?!?jedi?!?
        it = iter(self.collection)
        pages = iter(lambda: tuple(islice(it, self.items_per_page)), ())
        pages = list(pages)
        try:
            return len(pages[page_index])
        except IndexError:
            return -1

    # determines what page an item is on. Zero based indexes.
    # this method should return -1 for item_index values that are out of range
    def page_index(self, item_index):
        if self.item_count() == 0:
            return -1
        elif item_index < 0:
            return -1
        elif item_index < self.items_per_page:
            return 0
        elif item_index >= self.item_count():
            return -1
        else:
            return item_index // self.items_per_page


if __name__ == "__main__":
    helper = PaginationHelper(['a', 'b', 'c', 'd', 'e', 'f'], 4)
    assert helper.page_count() == 2
    assert helper.item_count() == 6
    assert helper.page_item_count(0) == 4
    assert helper.page_item_count(1) == 2
    assert helper.page_item_count(2) == -1

    # page_index takes an item index and returns the page that it belongs on
    assert helper.page_index(5) == 1
    assert helper.page_index(2) == 0
    assert helper.page_index(20) == -1
    assert helper.page_index(-10) == -1

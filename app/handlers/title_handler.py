from fastapi import HTTPException

from app.dependencies.data_store import get_title_data


def _filter_titles(titles: list, filter_key: str, filter_value: str):
    """
    Filter the list of titles to include only those which have the key value pair specified.

    :param titles: The list of JSON titles to filter.
    :param filter_key: The key on which the filter.
    :param filter_value: The value on which to filter.
    :return: A subset of the titles list containing only those that match the key value pair.
    """
    return [title for title in titles if title[filter_key] == filter_value]


def _sort_titles(titles: list, sort: str, order: str):
    """
    Sort in place for the provided list of titles based on a chosen key and order.

    The list is sorted by the primarily by the first "sort" key and then any ties are broken by the second "sort"
    key if provided.

    The number of "sort" keys must match the number of "order" values.

    :param titles: A list of JSON titles.
    :param sort: A comma separated list of keys to sort by. Valid values: 'id' and 'title_number'.
    :param order: A comma separated list of orders to sort by. Valid values: 'asc' and 'desc'.
    """
    sort_split = sort.split(",")
    order_split = order.split(",")

    sort_split.reverse()
    order_split.reverse()

    if len(sort_split) != len(order_split):
        raise HTTPException(status_code=400, detail="Number of sort and order values must match")

    for index, sort in enumerate(sort_split):
        is_reverse = order_split[index] == "desc"
        if sort == "id":
            titles.sort(key=lambda title: int(title["id"]), reverse=is_reverse)
        elif sort == "title_number":
            titles.sort(key=lambda title: title["title_number"], reverse=is_reverse)
        else:
            raise HTTPException(status_code=400, detail="Sort type must be 'id' or 'title_number'")


def list_titles(page: int, limit: int, sort: str, order: str, title_class: str = None):
    """
    Return a paged subset of titles.

    If a title_class filter is provided only titles of that class will be returned.

    Operations on results are performed in the following order: title_class filter, ordering, paging.

    :param page: The number of the page to return
    :param limit: The size of the pages
    :param sort: A comma delimited list of properties to sort by
    :param order: A comma delimited list, corresponding to the sort list, of the order each sort is applied
    :param title_class: An optional filter on the title_class of the returned titles
    :return: A list of titles in JSON format
    """
    title_data = get_title_data()

    # If a title class filter has been provided, filter the data
    if title_class:
        title_data = _filter_titles(title_data, "title_class", title_class)

    _sort_titles(title_data, sort, order)

    # Get a sub list of titles based on the provided paging information
    start = (page - 1) * limit
    end = start + limit
    paged_titles = title_data[start:end]

    for title in paged_titles:
        del title["content"]

    # Return the requested, paged titles and a count of all available titles which match the filter
    return paged_titles, len(title_data)


def get_title_by_id(title_id: str):
    """
    Return a single title based on the title ID.
    :param title_id: The string ID of the title.
    :return: A JSON representation of the title.
    """
    title_data = get_title_data()

    for title in title_data:
        if title['id'] == title_id:
            return title

    raise HTTPException(status_code=404, detail=f"Title with ID {title_id} not found")

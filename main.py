from typing import Dict


class SomeTaggableObject:
    """
    A placeholder class that can be tagged
    """

    def __init__(self, **kwargs: any):
        self._tags: Dict[str, str] = kwargs
    
    @property
    def tags(self) -> Dict[str, str]:
        return self._tags


def read_tags_count_from_user() -> int:
    """
    Read and return number of tags from user
    """

    while True:
        try:
            num_params = int(input("Number of tags (1-5): "))
            if 1 <= num_params <= 5:
                return num_params
        except ValueError:
            pass


def read_tags_from_user(num_params: int) -> Dict[str, str]:
    """
    Read and return tag keys and values from user
    """

    tags: Dict[str, str] = {}
    
    while len(tags) < num_params:
        tag_key = input(f"Key #{len(tags)}: ")
        
        if tag_key not in tags:
            tag_value = input("Value: ")
            tags[tag_key] = tag_value
    
    return tags


if __name__ == "__main__":
    num_params = read_tags_count_from_user()
    tags = read_tags_from_user(num_params)
    
    tagged_obj = SomeTaggableObject(**tags)
    print(tagged_obj.tags)

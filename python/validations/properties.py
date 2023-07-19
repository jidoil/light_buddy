import weakref
import re
import gazu.project


class ValidateURL:
    url_pattern = r"^https?:\/\/(?:www\.)?[-a-zA-Z0-9@:%._\+~#=]" \
                  r"{1,256}\.[a-zA-Z0-9()]{1,6}\b(?:[-a-zA-Z0-9()@:%_\+.~#?&\/=]*)$"

    _min_length = 5
    _max_length = 64000
    data = {}

    def __set_name__(self, owner, name: str):
        self.property_name = name

    def __set__(self, instance, value: str):
        if not isinstance(value, str):
            raise ValueError(f'{self.property_name} must be string type')
        try:
            self.url_length_inspect(value)
            self.url_pattern_inspect(value)
        except ValueError as ex:
            print(f'{repr(ex)}')
        self.data[id(instance)] = (weakref.ref(instance, self._finalize_instance), value)

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return self.data.get(id(instance))[1]

    def _finalize_instance(self, weakref):
        reverse_lookup = [key for key, value in self.data.items() if value[0] is weakref]
        if reverse_lookup:
            del self.data[reverse_lookup[0]]

    def url_length_inspect(self, url: str) -> None :
        if len(url) > self._max_length:
            raise ValueError(f'{self.property_name} is longer than max_length: {self._max_length}')
        elif len(url) < self._min_length:
            raise ValueError(f'{self.property_name} is longer than max_length: {self._max_length}')
        else:
            print(f'{self.property_name}: valid url length')

    def url_pattern_inspect(self, url: str) -> None :
        match = re.match(self.url_pattern, url)
        if match:
            print("url is ok")
        else:
            raise ValueError(f'{self.property_name} is not valid url.')


class ValidateID:
    email_pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    _min_length = 5
    _max_length = 255
    data = {}

    def __set_name__(self, owner, name):
        self.property_name = name

    def __set__(self, instance, value):
        if not isinstance(value, str):
            raise ValueError(f'{self.property_name} must be string type')
        try:
            self.url_length_inspect(value)
            self.url_pattern_inspect(value)
        except ValueError as ex:
            print(f'{repr(ex)}')
        self.data[id(instance)] = (weakref.ref(instance, self._finalize_instance), value)

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return self.data.get(id(instance))[1]

    def _finalize_instance(self, weakref):
        reverse_lookup = [key for key, value in self.data.items() if value[0] is weakref]
        if reverse_lookup:
            del self.data[reverse_lookup[0]]

    def url_length_inspect(self, url):
        if len(url) > self._max_length:
            raise ValueError(f'{self.property_name} is longer than max_length: {self._max_length}')
        elif len(url) < self._min_length:
            raise ValueError(f'{self.property_name} is longer than max_length: {self._max_length}')
        else:
            print(f'{self.property_name}: valid ID length')

    def url_pattern_inspect(self, url):
        match = re.match(self.email_pattern, url)
        if match:
            print("ID is ok")
        else:
            raise ValueError(f'{self.property_name} is not valid ID.')


class ValidateProject:
    _min_length = 1
    _max_length = 255
    data = {}

    def __set_name__(self, owner, name: str):
        self.property_name = name

    def __set__(self, instance, value: str):
        if not isinstance(value, str):
            raise ValueError(f'{self.property_name} must be string type')
        try:
            self.url_length_inspect(value)
        except ValueError as ex:
            print(f'{repr(ex)}')
        project = gazu.project.get_project_by_name(value)
        print(f'project = {project}')
        if project:
            self.data[id(instance)] = (weakref.ref(instance, self._finalize_instance), project)
        else:
            raise ValueError("해당 프로젝트가 존재하지 않습니다.")

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return self.data.get(id(instance))[1]

    def _finalize_instance(self, weakref):
        reverse_lookup = [key for key, value in self.data.items() if value[0] is weakref]
        if reverse_lookup:
            del self.data[reverse_lookup[0]]

    def url_length_inspect(self, url: str) -> None :
        if len(url) > self._max_length:
            raise ValueError(f'{self.property_name} is longer than max_length: {self._max_length}')
        elif len(url) < self._min_length:
            raise ValueError(f'{self.property_name} is longer than max_length: {self._max_length}')
        else:
            print(f'{self.property_name}: valid url length')

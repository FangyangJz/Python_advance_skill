# !/usr/bin/env python3
# -*- coding:utf-8 -*-
'''
created by Fangyang on Time:2018/9/15
'''
import numbers

__author__ = 'Fangyang'

class Field:
    pass

class IntField(Field):
    '''数据描述符, 用于数据检查'''
    def __init__(self, db_column, min_value=None, max_value=None):

        self._value = None
        self.db_column = db_column
        self.min_value = min_value
        self.max_value = max_value

        if min_value is not None:
            if not isinstance(min_value, numbers.Integral):
                raise ValueError('min_value must be int')
            elif min_value < 0:
                raise ValueError('min_value must be positive')

        if max_value is not None:
            if not isinstance(max_value, numbers.Integral):
                raise ValueError('max_value must be int')
            elif max_value < 0:
                raise ValueError('max_value must be positive')

        if min_value is not None and max_value is not None:
            if min_value > max_value:
                raise ValueError('min_value must be smaller than max_value')

    def __get__(self, instance, owner):
        return self.value

    def __set__(self, instance, value):
        if not isinstance(value, numbers.Integral):
            raise ValueError('int value need')
        if value < self.min_value and value > self.max_value:
            raise ValueError('value must between min_value and max_value')
        self.value = value


class CharField(Field):
    '''数据描述符, 用于数据检查'''
    def __init__(self, db_column, max_length=None):
        self._value = None
        self.db_column = db_column
        self.max_length = max_length

        if max_length is None:
            raise ValueError('you must spcify max_length for charfield')

    def __get__(self, instance, owner):
        return self.value

    def __set__(self, instance, value):
        if not isinstance(value, str):
            raise ValueError('string value need')
        if len(value) > self.max_length:
            raise ValueError('value length excess max length')
        self.value = value


# 有了以上属性描述符做属性检查, 接下来定义我们的元类 metaclass
class ModelMetaClass(type):
    def __new__(cls, name, base, attrs, **kwargs):
        if name == 'BaseModel':
            return super().__new__(cls, name, base, attrs, **kwargs)


        fields = {}
        for key, value in attrs.items():
            if isinstance(value, Field):
                fields[key] = value

        attrs_meta = attrs.get("Meta", None)
        _meta = {}
        db_table = name.lower()
        if attrs_meta is not None:
            table = getattr(attrs_meta, 'db_table', None)
            if table is not None:
                db_table = table

        _meta['db_table'] = db_table
        attrs['_meta'] = _meta
        attrs['fields'] = fields
        del attrs['Meta']
        return super().__new__(cls, name, base, attrs, **kwargs)


class BaseModel(metaclass=ModelMetaClass):
    def __init__(self, *args, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
        return super().__init__()

    def save(self):
        fields = []
        values = []
        for key, value in self.fields.items():
            db_column = value.db_column
            if db_column is None:
                db_column = key.lower()
            fields.append(db_column)
            value = getattr(self, key)
            values.append(str(value))
        sql = "insert {db_table}({fields}) value({values})".format(db_table=self._meta["db_table"],
                                                                   fields=','.join(fields),
                                                                   values=','.join(values))
        pass

class User(BaseModel):
    name = CharField(db_column='', max_length=10)
    age = IntField(db_column='', min_value=0, max_value=100)

    # def __init__(self):  # 把init这部分写到BaseModel里去
    #     pass

    class Meta:
        db_table = 'user'


if __name__ == '__main__':
    user = User()
    user.name = 'bb'   # 传入值的类型检查, 由属性描述符实现
    user.age = 28
    user.save()
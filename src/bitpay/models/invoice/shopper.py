"""
Shopper
"""
from typing import Optional

from ...utils.key_utils import change_camel_case_to_snake_case
from ...utils.model_util import ModelUtil


class Shopper:
    """
    shopper
    """

    __user = None

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            try:
                getattr(self, "set_%s" % change_camel_case_to_snake_case(key))(value)
            except AttributeError:
                pass

    def get_user(self) -> Optional[str]:
        """
        Get method for to user
        :return: user
        """
        return self.__user

    def set_user(self, user: Optional[str]):
        """
        Set method for to user
        :param user: user
        """
        self.__user = user

    def to_json(self):
        """
        :return: data in json
        """
        return ModelUtil.to_json(self)

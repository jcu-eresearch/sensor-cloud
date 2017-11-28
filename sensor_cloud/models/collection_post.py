# coding: utf-8

"""
    Sensor Data API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: 2.20
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class CollectionPost(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'name': 'str',
        'organisationid': 'str',
        'groupids': 'list[str]',
        'public': 'bool'
    }

    attribute_map = {
        'name': 'name',
        'organisationid': 'organisationid',
        'groupids': 'groupids',
        'public': 'public'
    }

    def __init__(self, name=None, organisationid=None, groupids=None, public=None):
        """
        CollectionPost - a model defined in Swagger
        """

        self._name = None
        self._organisationid = None
        self._groupids = None
        self._public = None

        self.name = name
        self.organisationid = organisationid
        if groupids is not None:
          self.groupids = groupids
        if public is not None:
          self.public = public

    @property
    def name(self):
        """
        Gets the name of this CollectionPost.

        :return: The name of this CollectionPost.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this CollectionPost.

        :param name: The name of this CollectionPost.
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")

        self._name = name

    @property
    def organisationid(self):
        """
        Gets the organisationid of this CollectionPost.

        :return: The organisationid of this CollectionPost.
        :rtype: str
        """
        return self._organisationid

    @organisationid.setter
    def organisationid(self, organisationid):
        """
        Sets the organisationid of this CollectionPost.

        :param organisationid: The organisationid of this CollectionPost.
        :type: str
        """
        if organisationid is None:
            raise ValueError("Invalid value for `organisationid`, must not be `None`")

        self._organisationid = organisationid

    @property
    def groupids(self):
        """
        Gets the groupids of this CollectionPost.
        A list of group identifiers for which this stream will be a member.

        :return: The groupids of this CollectionPost.
        :rtype: list[str]
        """
        return self._groupids

    @groupids.setter
    def groupids(self, groupids):
        """
        Sets the groupids of this CollectionPost.
        A list of group identifiers for which this stream will be a member.

        :param groupids: The groupids of this CollectionPost.
        :type: list[str]
        """

        self._groupids = groupids

    @property
    def public(self):
        """
        Gets the public of this CollectionPost.

        :return: The public of this CollectionPost.
        :rtype: bool
        """
        return self._public

    @public.setter
    def public(self, public):
        """
        Sets the public of this CollectionPost.

        :param public: The public of this CollectionPost.
        :type: bool
        """

        self._public = public

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, CollectionPost):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
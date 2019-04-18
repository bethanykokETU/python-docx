# encoding: utf-8

from __future__ import absolute_import, division, print_function

from .constants import MIME_TYPE
from .exceptions import InvalidImageStreamError
from .helpers import BIG_ENDIAN, StreamReader
from .image import BaseImageHeader


class Svg(BaseImageHeader):
    """
    Image header parser for SVG images
    """
    @property
    def content_type(self):
        """
        MIME content type for this image
        """
        return MIME_TYPE.SVG

    @property
    def default_ext(self):
        """
        Default filename extension, always 'svg' for SVG images.
        """
        return 'svg'

    @classmethod
    def from_stream(cls, stream):
        """
        Return a |Svg| instance having header properties parsed from image in
        *stream*.
        """
        

        return cls()

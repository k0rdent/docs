"""Mkdocs plugin for disabling the sitemap"""
import logging
from mkdocs.plugins import BasePlugin


LOGGER = logging.getLogger(__name__)


class NoSitemapPlugin(BasePlugin):
    def __init__(self):
        pass

    def on_config(self, config, **kwargs):
        config['theme'].static_templates.remove('sitemap.xml')
        return config

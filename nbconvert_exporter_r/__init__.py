import os
import os.path

from traitlets.config import Config
from nbconvert.exporters.templateexporter import TemplateExporter

# -----------------------------------------------------------------------------
# Classes
# -----------------------------------------------------------------------------


class RExporter(TemplateExporter):
    """
    Custom exporter for R language
    """

    # If this custom exporter should add an entry to the
    # "File -> Download as" menu in the notebook, give it a name here in the
    # `export_from_notebook` class member
    export_from_notebook = "R format"

    def _file_extension_default(self):
        """
        The new file extension is `.R`
        """
        return '.R'

    @property
    def template_path(self):
        """
        Like Python template, template should be under 
        `./templates/` so append it to the search path. (see next section)
        """
        return super().template_path + [os.path.join(os.path.dirname(__file__), "templates")]

    def _template_file_default(self):
        """
        We want to use the new template we ship with our library.
        """
        return 'r.tpl'  # full


class RNotebookExporter(TemplateExporter):
    """
    Custom exporter for R Notebook
    """

    # If this custom exporter should add an entry to the
    # "File -> Download as" menu in the notebook, give it a name here in the
    # `export_from_notebook` class member
    export_from_notebook = "Notebook format"

    def _file_extension_default(self):
        """
        The new file extension is `.Rmd`
        """
        return '.Rmd'

    @property
    def template_path(self):
        """
        Like Python template, template should be under 
        `./templates/` so append it to the search path. (see next section)
        """
        return super().template_path + [os.path.join(os.path.dirname(__file__), "templates")]

    def _template_file_default(self):
        """
        We want to use the new template we ship with our library.
        """
        return 'rnotebook.tpl'  # full

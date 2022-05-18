from nbconvert.preprocessors import ClearOutputPreprocessor


class CustomClearOutputPreprocessor(ClearOutputPreprocessor):
    """
    Removes the output from all code cells in a notebook,
    except the first one if its source is empty.
    """

    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)
        self.skip = True

    def preprocess_cell(self, cell, resources, cell_index):
        """
        Apply a transformation on each cell. See base.py for details.
        """
        if cell.cell_type == "code":
            if not self.skip or cell.source != "":
                cell.outputs = []
                cell.execution_count = None
                # Remove metadata associated with output
                if "metadata" in cell:
                    for field in self.remove_metadata_fields:
                        cell.metadata.pop(field, None)
            self.skip = False
        return cell, resources
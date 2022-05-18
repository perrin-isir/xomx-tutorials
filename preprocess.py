from nbconvert.preprocessors import ClearOutputPreprocessor


class CustomClearOutputPreprocessor(ClearOutputPreprocessor):
    """
    Removes the output from all code cells in a notebook,
    except if their source is empty.
    """

    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)

    def preprocess_cell(self, cell, resources, cell_index):
        """
        Apply a transformation on each cell. See base.py for details.
        """
        if cell.cell_type == "code":
            if cell.source == "":
                print("Code cell skipped")
            else:
                cell.outputs = []
                cell.execution_count = None
                # Remove metadata associated with output
                if "metadata" in cell:
                    for field in self.remove_metadata_fields:
                        cell.metadata.pop(field, None)
        return cell, resources

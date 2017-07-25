from IPython.core.display import HTML

import uuid

# Jupyter Extension points
def _jupyter_nbextension_paths():
    return [dict(
        section="notebook",
        # the path is relative to the `my_fancy_module` directory
        src="static",
        # directory in the `nbextension/` namespace
        dest="egal",
        # _also_ in the `nbextension/` namespace
        require="egal/main")]


def edit_svg(filename, height="400"):
    svg_id = str(uuid.uuid1())

    # load the file
    # populate svg element on page
    # javascript code that edits svg
    # trigger that stores current svg element in original file
    html = """
    <div id='""" + svg_id + """'>
    <script>
        require(['nbextensions/egal/snap.svg','nbextensions/egal/egal'], function(snap, egal) {
            console.log("Egal Loaded in edit_svg");
            drupyter = new egal.Egal('#""" + svg_id + """','""" + filename + """',{ width: '100%', height: '""" + height + """'});
        });
    </script>
    """
    return HTML(html)

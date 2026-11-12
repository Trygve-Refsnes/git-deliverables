"""Execute this deliverable's plain Python cells and export all content to PDF."""

import contextlib
import io
import json
import textwrap
from pathlib import Path
from xml.sax.saxutils import escape

from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph, Preformatted, Spacer


def main():
    path = Path(__file__).with_name("deliverable3_notebook.ipynb")
    notebook = json.loads(path.read_text(encoding="utf-8"))
    namespace = {"__name__": "__main__"}
    count = 0
    styles = getSampleStyleSheet()
    styles["Code"].fontSize = 8
    styles["Code"].leading = 10
    styles["Code"].backColor = colors.whitesmoke
    story = []
    for cell in notebook["cells"]:
        source = "".join(cell["source"])
        if cell["cell_type"] == "markdown":
            for block in source.split("\n\n"):
                if not block.strip():
                    continue
                heading = len(block) - len(block.lstrip("#"))
                style = styles["Heading1" if heading == 1 else "Heading2"] if heading else styles["BodyText"]
                story.append(Paragraph(escape(block.lstrip("# ") if heading else block), style))
        elif cell["cell_type"] == "code":
            count += 1
            output = io.StringIO()
            with contextlib.redirect_stdout(output):
                exec(compile(source, f"cell {count}", "exec"), namespace)
            cell["execution_count"] = count
            cell["outputs"] = ([{"name": "stdout", "output_type": "stream",
                                 "text": output.getvalue().splitlines(keepends=True)}]
                               if output.getvalue() else [])
            story.append(Paragraph(f"In [{count}]", styles["BodyText"]))
            for content in (source, output.getvalue()):
                if content:
                    wrapped = "\n".join(textwrap.fill(line, width=95, replace_whitespace=False,
                                                       drop_whitespace=False) if line else ""
                                        for line in content.splitlines())
                    story.append(Preformatted(wrapped, styles["Code"]))
        story.append(Spacer(1, 10))
    SimpleDocTemplate(str(path.with_suffix(".pdf")), title="INF201 Deliverable 3").build(story)
    path.write_text(json.dumps(notebook, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Executed {count} code cells and exported {path.with_suffix('.pdf').name}")


if __name__ == "__main__":
    main()

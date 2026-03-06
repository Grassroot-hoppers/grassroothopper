#!/usr/bin/env python3
import importlib.util
import tempfile
from pathlib import Path


def load_module():
    script_path = Path(__file__).with_name("build-hackathon.py")
    spec = importlib.util.spec_from_file_location("build_hackathon", script_path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


def write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def main() -> None:
    module = load_module()

    with tempfile.TemporaryDirectory() as tmpdir:
        root = Path(tmpdir)
        devlog_dir = root / "docs" / "devlog"
        output_dir = root / "website" / "hackathon"
        template_dir = root / "scripts" / "templates"

        write(
            template_dir / "index.html",
            "<html><body>{{timeline}}|{{latest_card}}|{{retrospective_link}}</body></html>",
        )
        write(
            template_dir / "day.html",
            "<html><body>{{title}}|{{prev_link}}|{{next_link}}|{{dots}}</body></html>",
        )
        write(
            template_dir / "retrospective.html",
            "<html><body>{{status_label}}|{{content}}</body></html>",
        )
        write(
            template_dir / "preview.html",
            "<html><body>Hackathon Preview</body></html>",
        )

        write(
            devlog_dir / "day-1.md",
            """---
title: "Public Day"
date: 2026-03-10
day: 1
status: done
shipped: ["One"]
---

Published.
""",
        )
        write(
            devlog_dir / "day-2.md",
            """---
title: "Draft Day"
date: 2026-03-11
day: 2
status: draft
shipped: []
---

Draft.
""",
        )
        write(
            devlog_dir / "retrospective.md",
            """---
title: "Retrospective"
date: 2026-03-14
status: draft
---

Later.
""",
        )

        module.DEVLOG_DIR = devlog_dir
        module.OUTPUT_DIR = output_dir
        module.ENTRY_PAGE = root / "website" / "hackathon.html"
        module.TEMPLATE_DIR = template_dir

        module.main()

        index_html = (output_dir / "index.html").read_text(encoding="utf-8")
        day_1_html = (output_dir / "day-1.html").read_text(encoding="utf-8")
        entry_html = (root / "website" / "hackathon.html").read_text(encoding="utf-8")

        assert (output_dir / "day-1.html").exists(), "public day should be generated"
        assert (output_dir / "index.html").exists(), "index should exist when public content exists"
        assert 'url=hackathon/index.html' in entry_html, "entry page should redirect when public content exists"
        assert not (output_dir / "day-2.html").exists(), "draft day should not be generated"
        assert 'href="day-1.html"' in index_html, "public day should be linked"
        assert 'href="day-2.html"' not in index_html, "draft day should not be linked from index"
        assert "day-2.html" not in day_1_html, "draft day should not appear in day navigation"
        assert not (output_dir / "retrospective.html").exists(), "draft retrospective should not be generated"

    with tempfile.TemporaryDirectory() as tmpdir:
        root = Path(tmpdir)
        devlog_dir = root / "docs" / "devlog"
        output_dir = root / "website" / "hackathon"
        template_dir = root / "scripts" / "templates"

        write(
            template_dir / "index.html",
            "<html><body>{{timeline}}|{{latest_card}}|{{retrospective_link}}</body></html>",
        )
        write(
            template_dir / "day.html",
            "<html><body>{{title}}|{{prev_link}}|{{next_link}}|{{dots}}</body></html>",
        )
        write(
            template_dir / "retrospective.html",
            "<html><body>{{status_label}}|{{content}}</body></html>",
        )
        write(
            template_dir / "preview.html",
            "<html><body>Hackathon Preview</body></html>",
        )
        write(
            devlog_dir / "day-1.md",
            """---
title: "Draft Day"
date: 2026-03-10
day: 1
status: draft
---

Draft.
""",
        )

        module.DEVLOG_DIR = devlog_dir
        module.OUTPUT_DIR = output_dir
        module.ENTRY_PAGE = root / "website" / "hackathon.html"
        module.TEMPLATE_DIR = template_dir

        module.main()

        entry_html = (root / "website" / "hackathon.html").read_text(encoding="utf-8")
        assert not (output_dir / "day-1.html").exists(), "draft-only day should not be generated"
        assert not (output_dir / "index.html").exists(), "index should not exist with only draft content"
        assert "Hackathon Preview" in entry_html, "draft-only state should keep the preview page"

    with tempfile.TemporaryDirectory() as tmpdir:
        root = Path(tmpdir)
        devlog_dir = root / "docs" / "devlog"
        output_dir = root / "website" / "hackathon"
        template_dir = root / "scripts" / "templates"

        write(template_dir / "index.html", "<html></html>")
        write(template_dir / "day.html", "<html></html>")
        write(template_dir / "retrospective.html", "<html></html>")
        write(template_dir / "preview.html", "<html><body>Hackathon Preview</body></html>")
        write(
            devlog_dir / "day-1.md",
            """---
title: "Live Day One"
date: 2026-03-10
day: 1
status: live
---

Live.
""",
        )
        write(
            devlog_dir / "day-2.md",
            """---
title: "Live Day Two"
date: 2026-03-11
day: 2
status: live
---

Also live.
""",
        )

        module.DEVLOG_DIR = devlog_dir
        module.OUTPUT_DIR = output_dir
        module.ENTRY_PAGE = root / "website" / "hackathon.html"
        module.TEMPLATE_DIR = template_dir

        try:
            module.main()
        except SystemExit as exc:
            assert "only one entry can be marked live" in str(exc), "multiple live entries should fail clearly"
        else:
            raise AssertionError("multiple live entries should abort the build")


if __name__ == "__main__":
    main()

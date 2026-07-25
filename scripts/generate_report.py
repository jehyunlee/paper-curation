#!/usr/bin/env python3
"""Public entrypoint for the reusable Markdown policy-report generator.

Examples:
    python scripts/generate_report.py reports/source/report.md
    python scripts/generate_report.py reports/source/report.md --keep-html
    python scripts/generate_report.py report.md --css reports/styles/policy-report.css \
        --pdf reports/output/report.pdf

The implementation lives in ``md_report_to_pdf.py`` so existing commands remain compatible.
"""
from md_report_to_pdf import main


if __name__ == "__main__":
    raise SystemExit(main())

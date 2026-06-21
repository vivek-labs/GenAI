# Streamlit page import error

## Problem
`languageTutor/app.py` raised `AttributeError: module 'pages.grammar_fun' has no attribute 'app'` when the app tried to render the selected page.

## Cause
`pages` was missing an `__init__.py` file, so Python treated it as a namespace package and the import resolution was not reliable.

## Solution
Add `languageTutor/pages/__init__.py` so `pages` is a regular package and `from pages import grammar_fun, home` resolves to the local page modules consistently.

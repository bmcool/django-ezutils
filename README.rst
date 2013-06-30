==============
django-ezutils
==============


Overview
--------

Django-ezutils consists of the following things:

    - Common base abstract models for inherit.

    - Common fields, forms, functions for use.

Installation
------------

- Add ``django_ezutils`` to your Django settings ``INSTALLED_APPS``::

    INSTALLED_APPS = [
        # ...
        "django_ezutils",
    ]

======
Fields
======

Date picker field
-----------------

- Add ``DatePickerField`` to your ``forms.py``::

    from django import forms
    from django_ezutils.fields import DatePickerField
    
    class YourForm(forms.Form):
        ...
        date = DatePickerField()

=========
Changelog
=========

0.0.1
---

    - First commit.

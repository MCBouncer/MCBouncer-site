#!/usr/bin/env python
# -*- coding: utf8 -*-
"""
Starts a local mcbouncer instance for debugging & developing.
"""
from mcbouncer import start

if __name__ == '__main__':
    app = start(debug=True)
    app.run()

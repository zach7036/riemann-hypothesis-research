#!/usr/bin/env python3
"""Compatibility entry point for the exact low-multiplicity certificate.

The complete standard-library rational interval implementation is in
`certify_low_multiplicity.py`.  This entry point is retained because the
manuscript and verification notes refer to the exact-certificate command.
"""
from certify_low_multiplicity import main

if __name__ == "__main__":
    main()

#!/bin/bash
# Get the byte size of the HTTP response header for a given URL.
curl -s -w %{size_download}"\n" "$1" -o /dev/null

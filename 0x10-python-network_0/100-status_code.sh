#!/bin/bash
# bash Script
curl -s -o /dev/null "$1" -w %{http_code}

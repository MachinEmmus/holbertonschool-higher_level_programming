#!/bin/bash
# HTTP methods allow
curl -sI "$1" | grep Allow | cut -c 8-

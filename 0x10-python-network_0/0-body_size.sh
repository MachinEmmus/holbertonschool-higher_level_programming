#!/bin/bash
# Script that count the content in URL espicify
curl -s "$1" | wc -c

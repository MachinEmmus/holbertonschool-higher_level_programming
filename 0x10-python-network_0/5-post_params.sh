#!/bin/bash
# POST request to pass URL
curl -s -X POST -d "email=hr@holbertonschool.com&subject=I will always be here for PLD" "$1"

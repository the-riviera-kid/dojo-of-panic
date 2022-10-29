#!/usr/bin/bash
. venv/bin/activate
for F in ./exemplars/input*
do
    echo "$F"
    NUMBER="${F//[^0-9]/}"
    EXEMPLAR="./exemplars/exemplar-output-$NUMBER.txt"
    OUTPUT="./word-grid-output-$NUMBER.txt"
    python word-grid.py < "$F" > "$OUTPUT"
    if cmp -s "$EXEMPLAR" "$OUTPUT"; then
        echo "SUCCESS!"
    else
        echo "FAIL FAIL FAIL FAIL FAIL FAIL"
    fi
done

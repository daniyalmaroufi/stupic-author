# a tester for checking the app
# Usage: ./test_app.sh

python cli.py < input.txt > output.txt

diff output.txt expected_output.txt
if [ $? -eq 0 ]; then
    echo "Output Test passed"
else
    echo "Output Test failed"
fi
rm output.txt

diff o.txt expected_o.txt
if [ $? -eq 0 ]; then
    echo "Story Analysis Test passed"
else
    echo "Story Analysis Test failed"
fi
rm o.txt

diff o.csv expected_o.csv
if [ $? -eq 0 ]; then
    echo "CSV Test passed"
else
    echo "CSV Test failed"
fi
rm o.csv


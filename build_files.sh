echo "BUILD START"
python3.11.2 -m pip3 install -r requirments.txt
python3.11.2 manage.py collecstatic --noinput --clear
echo "BUILD END"
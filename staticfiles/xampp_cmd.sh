##this cmd gather all static files into a folder called staticfiles in our project root directory.
python manage.py collectstatic
cd staticfiles
rm -r  ../static/*
cp -r  ./* ../static

cd ..
cd ..
sudo chmod 777 -R foodshop
pwd

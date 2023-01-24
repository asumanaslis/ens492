# In this bash script, first line pings all the domains by taking all small files one by one and write the url, status code, and redirected final url in 
# output.txt then it runs selTest.py and gets the contents of the urls.

for i in /home/domains/small_files/*.txt; do     
  cat $i |   parallel -P0 -q curl -o /dev/null --silent --head --write-out '%{url_effective} %{http_code} %{redirect_url}\n' > output.txt 
 
  wait

  sudo python3 selTest.py

  wait
 
  rm $i

done

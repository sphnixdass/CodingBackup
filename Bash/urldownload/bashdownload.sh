wget -O - "http://index-of.co.uk/Programming/" | grep -io '<a href=['"'"'"][^"'"'"']*['"'"'"]' | grep -i "pdf" | sed -e 's/^<a href=["'"'"']/http:\/\/index-of.co.uk\/Programming\/\//i' -e 's/["'"'"']$//i' >output.txt && wget -i output.txt


#wget -O - "https://theswissbay.ch/pdf/Gentoomen%20Library/Programming/C%2B%2B/" | grep -io '<a href=['"'"'"][^"'"'"']*['"'"'"]' | grep -i "pdf" | sed -e 's/^<a href=["'"'"']//i' -e 's/["'"'"']$//i' >output.txt



# Ens492
# Phishing Detection and Finding Technologies

In this project, we download daily created domains list from whoisds.com using getDomains.py file, and then we run splitFiles.py file to split the domains list into smaller files.
Then we run deneme.sh to get the status codes, redirected final urls and contents of the domains. We store the datas in MongoDB Atlas localhost.

phishingdetection.py is the script where we build our training dataset, apply preprocessing steps, extract features, analyze statistics, build machine learning model and test the accuracy on test set. Script should be run lastly.

Webtech-master file is needed for the technology finding script.

PhishingDetectionFlow.drawio.pdf shows the flow of the scripts.

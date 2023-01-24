# Ens492
# Phishing Detection and Finding Technologies

You can run the phishingdetection.ipynb using the link below this way will be easier.
https://drive.google.com/drive/folders/14W5qP6CWJ4IuepO2P1MukERCO89Qfn0L?usp=share_link


In this project, we download daily created domains list from whoisds.com using getDomains.py file, and then we run splitFiles.py file to split the domains list into smaller files.
Then we run deneme.sh to get the status codes, redirected final urls and contents of the domains. We store the datas in MongoDB Atlas localhost.

phishingdetection.py is the script where we build our training dataset, apply preprocessing steps, extract features, analyze statistics, build machine learning model and test the accuracy on test set. Script should be run before webtech. We advise you to run the script in Google Colaboratory, the link to the colab project is in the script. 

Webtech-master file is needed for the technology finding script.

PhishingDetectionFlow.drawio.pdf shows the flow of the scripts.

Virustotal1.py , Virustotal2.py , Virustotal3.py , Virustotal4.py can run simultaneously on the different tabs. After we run these files, in the technologies.py we for a one dataframe using their output and than get the technologies as technologies.py's output.

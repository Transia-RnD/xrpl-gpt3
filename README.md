
### Configure Google Cloud account:
```
gcloud config configurations create metaxrplorer
gcloud config set account dangell@transia.co
gcloud config set project metaxrplorer
```

`gcloud config configurations list`

`gcloud config configurations activate metaxrplorer`



gcloud beta run deploy xrpl-gpt3 \
--image=gcr.io/metaxrplorer/xrpl-gpt3:latest \
--platform=managed \
--region=us-central1 \
--project=metaxrplorer \
--service-account=firebase-devsdk@metaxrplorer.iam.gserviceaccount.com
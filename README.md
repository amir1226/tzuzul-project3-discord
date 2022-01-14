# Discord for student 

**App deployed:** https://final-project-django-tzuzul.ue.r.appspot.com/ <br/>
**Technologies:** Django, Django Rest Framework, PostgreSQL, Docker, AWS S3 and GCP

## Local Development Environment
1. Create an S3 service instance on AWS (you may change the config to store the images on local environment and remove all environment variables related to AWS). [Permissions for the S3 bucket](https://docs.aws.amazon.com/config/latest/developerguide/s3-bucket-policy.html)
2. Add .env file in root folder (proyecto3_discord) with at least this variables:
* SECRET_KEY={Django secret key}
* DJANGO_DEBUG = {True or False. Settings default value is False, so this variable is optional)
* DATABASE_URL={postgres://{postgres user}:{postgres password}@{postgres host}:{database port}/{database name}}
* POSTGRES_USER={postgres user}
* POSTGRES_PASSWORD={postgres password}
* AWS_ACCESS_KEY_ID={Aws access key id}
* AWS_SECRET_ACCESS_KEY={Aws secret access key}
* AWS_STORAGE_BUCKET_NAME={Aws bucket name}
3. Check docker-compose.yml that should have same db port as `DATABASE_URL` variable.
4. Run the command `docker-compose up` on terminal and start working with the project in the defined port (currently port 8001)

## GCP Deployment
You can review the basic config in the [google_cloud_deploy](https://github.com/amir1226/tzuzul-project3-discord/tree/google_cloud_deploy) branch.
1. Create a new GCP project with Cloud Storage (static files) and Cloud SQL (PostgreSQL) services instaces.
2. Based on `app-example.yml` add your environment variables and rename as `app.yml` (DON'T PUSH THIS FILE WITH YOUR CREDENTIALS TO GITHUB).
3. Install Google Cloud SDK and run `gcloud init` to select your project.
4. Sync Django static files with the Cloud Storage instance through command `python manage.py collectstatic` (generate a folder with all your static files as js, css, images and so on). Rename generated folder as static (if you use that folder name in the app.yml variable`static_dir`, else use the name that you defined) and run commands: `gsutil defacl set public-read gs://«your bucket»` and `gsutil -m cp -R «your source directory ("static" in my case)» gs://«your bucket»`
5. Run `gcloud app deploy` and wait. When it completes it will output a link to your live project.

If you need more orientation about GCP deployment, you can use [this useful article](https://codeburst.io/beginners-guide-to-deploying-a-django-postgresql-project-on-google-cloud-s-flexible-app-engine-e3357b601b91)
